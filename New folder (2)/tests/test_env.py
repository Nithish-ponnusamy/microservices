import unittest
from rl_agent.env import MicroserviceDeploymentEnv

class TestMicroserviceDeploymentEnv(unittest.TestCase):
    def test_reset(self):
        env = MicroserviceDeploymentEnv()
        state, _ = env.reset()
        self.assertEqual(len(state), 10)

    def test_step(self):
        env = MicroserviceDeploymentEnv()
        env.reset()
        state, reward, terminated, truncated, info = env.step(0)
        self.assertEqual(len(state), 10)

if __name__ == '__main__':
    unittest.main()
