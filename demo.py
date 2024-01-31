import minerl
import gym

env = gym.make('MineRLBasaltFindCave-v0')
done = False
obs = env.reset()

while not done:
    # Take a random action
    action = env.action_space.sample()
    # In BASALT environments, sending ESC action will end the episode
    # Lets not do that
    action["ESC"] = 0
    obs, reward, done, _ = env.step(action)
    env.render()
