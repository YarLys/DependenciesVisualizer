import unittest
from main import init, get_commits, select_commits, build_graph

class TestVisualizer(unittest.TestCase):
    def test_init_file(self):
        self.assertEqual(init('asdf'), ("", "", ""))

    def test_get_commits(self):
        init('config.yaml')
        commits = {'c1f473a418a06a5d1f3f6ea4dfcde0414e1abeb1': ['aa0905d5fb63ace52ff6c6727c8f56461a8a3577', 'added', 'new', 'file'], 'aa0905d5fb63ace52ff6c6727c8f56461a8a3577': ['ad732046e62d9b037e13939d874e2e9c455fe42d', 'work', 'on', 'master', 'again'], '0f5db7484ead253ca379fd253c34dff84c1fe5be': ['c05563118dbc7e71c2953dc1d826dddbda23b921', 'some', 'bugs', 'fixed,', 'del', 'files'], 'c05563118dbc7e71c2953dc1d826dddbda23b921': ['5e8ae805fd0330ee7c02e683be6603b1fbff3b47', 'second', 'branch', 'commit'], '5e8ae805fd0330ee7c02e683be6603b1fbff3b47': ['ad732046e62d9b037e13939d874e2e9c455fe42d', 'branch', 'commit'], 'ad732046e62d9b037e13939d874e2e9c455fe42d': ['9d598dfc942ff06ab7abf44fbeef59a269b8db29', 'create', 'file', 'again'], '9d598dfc942ff06ab7abf44fbeef59a269b8db29': ['ffcf03c3aa6ce920aaab447c0cc8eb97c2cd8c27', 'del', 'file'], 'ffcf03c3aa6ce920aaab447c0cc8eb97c2cd8c27': ['e80bcf8e0c18641fdaab0e4bda9e1a0e524159cb', 'some', 'changes'], 'e80bcf8e0c18641fdaab0e4bda9e1a0e524159cb': ['', 'init']}
        self.assertEqual(get_commits(), commits)

    def test_select_commits(self):
        init('config.yaml')
        get_commits()
        true_commits = {'c1f473a418a06a5d1f3f6ea4dfcde0414e1abeb1': ['aa0905d5fb63ace52ff6c6727c8f56461a8a3577', 'added', 'new', 'file'], 'aa0905d5fb63ace52ff6c6727c8f56461a8a3577': ['ad732046e62d9b037e13939d874e2e9c455fe42d', 'work', 'on', 'master', 'again'], '0f5db7484ead253ca379fd253c34dff84c1fe5be': ['c05563118dbc7e71c2953dc1d826dddbda23b921', 'some', 'bugs', 'fixed,', 'del', 'files'], 'c05563118dbc7e71c2953dc1d826dddbda23b921': ['5e8ae805fd0330ee7c02e683be6603b1fbff3b47', 'second', 'branch', 'commit'], '5e8ae805fd0330ee7c02e683be6603b1fbff3b47': ['ad732046e62d9b037e13939d874e2e9c455fe42d', 'branch', 'commit'], 'ad732046e62d9b037e13939d874e2e9c455fe42d': ['9d598dfc942ff06ab7abf44fbeef59a269b8db29', 'create', 'file', 'again'], '9d598dfc942ff06ab7abf44fbeef59a269b8db29': ['ffcf03c3aa6ce920aaab447c0cc8eb97c2cd8c27', 'del', 'file'], 'ffcf03c3aa6ce920aaab447c0cc8eb97c2cd8c27': ['e80bcf8e0c18641fdaab0e4bda9e1a0e524159cb', 'some', 'changes'], 'e80bcf8e0c18641fdaab0e4bda9e1a0e524159cb': ['', 'init']}
        self.assertEqual(select_commits(), true_commits)

if __name__ == '__main__':
    unittest.main()