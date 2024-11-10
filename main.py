import os
import graphviz

file_hash = r''
repo_path = r''
prog_path = r''
commits = dict()
def init(path):
    try:
        with open(path) as f:
            prog_path = f.readline().split()[1].replace('\\', '\\\\')
            repo_path = f.readline().split()[1].replace('\\', '\\\\')
            file_hash = f.readline().split()[1]
            os.chdir(repo_path)
            return (prog_path, repo_path, file_hash)
    except: # файл не найден
        return ("", "", "")

def get_commits():
    output = os.popen('git log --all --pretty=format:"%H %P %s%d"').read().split("\n") # получим список всех коммитов в нужном нам формате
    for commit in output:
        commit = commit.split()
        if len(commit) == 2: # если только хэш коммита и подпись, то это начальный коммит
            commits[commit[0]] = ["", commit[1]]
            continue

        commits[commit[0]] = [commit[1],] # в словаре по хэшу коммита храним список, который начинается с хэша родителя
        for i in range(2, len(commit)): # пройдёмся по оставшимся словам в информации о коммите
            if (not commit[i].startswith('(')): # ненужную информацию убираем
                commits[commit[0]].append(commit[i])
            else:
                break
    return commits

true_commits = dict()
def check_dirs(commit, hash1): # я не понимаю, как идентифицировать файл, если в каждом коммите у него разный хэш?
    output = os.popen(f'git cat-file -p {hash1}').read().split('\n')
    for str in output:
        if len(str) == 0:
            continue
        name = str.split()[1]
        hash = str.split()[2]
        if name == 'blob':
            if hash == file_hash or hash.startswith(file_hash):  # если его хэш совпадает с хэшом искомого файла, то добавляем этот коммит
                true_commits[commit] = commits[commit]
                break
        elif name == 'tree':
            check_dirs(commit, hash)

def select_commits():
    for commit in commits:
        output = os.popen(f'git cat-file -p {commit}').read().split('\n') # исследуем коммит по его хэшу
        obj = output[0].split()[0] # сохраним название объекта в коммите
        hash = output[0].split()[1] # сохраним хэш объекта

        if obj == 'blob':   # если в коммите только один файл, без каталогов
            if hash == file_hash or hash.startswith(file_hash): # и если его хэш совпадает с хэшом искомого файла, то добавляем этот коммит
                true_commits[commit] = commits[commit]
                continue

        check_dirs(commit, hash) # пройдёмся по объектам коммита. проверим все файлы на совпадение
    return true_commits

def build_graph():
    dot = []
    dot.append('digraph {')
    for commit1 in true_commits: # проходимся по словарю
        for commit2 in true_commits:
            if true_commits[commit2][0] == commit1: # если хэш родителя какого-то коммита равен хэшу другого коммита, то они связаны
                dot.append(f'"{commit1}" -> "{commit2}" [label="{' '.join(true_commits[commit2][1:])}"]')
    dot.append('}')
    return '\n'.join(dot)

def show_graph(dot_graph):
    # Создаем объект графа
    graph = graphviz.Source(dot_graph)
    # Рендерим граф в виде изображения
    graph.format = 'png'
    graph.render(filename='dependencies', cleanup=True)
    # Открываем изображение
    graph.view()


if __name__ == "__main__":
    (prog_path, repo_path, file_hash) = init('config.yaml')
    get_commits()
    select_commits()
    graphv = build_graph()
    os.chdir(prog_path)
    show_graph(graphv)