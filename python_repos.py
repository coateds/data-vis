import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store the API reponse in a variable.
response_dict = r.json()
print("Total repositories:" , response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
# print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
# repo_dict = repo_dicts[0]

# Look at fields/keys available
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    # print('Name:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    # print('Stars:', repo_dict['stargazers_count'])
    # print('Repoisitory:', repo_dict['html_url'])
    # print('Created:', repo_dict['created_at'])
    # print('Updated:', repo_dict['updated_at'])
    # print('Description', repo_dict['description'])
    # print('\n')

    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])

    # Get the project description, if one is available.
    description = repo_dict['description']
    if not description:
        description = "No description provided"
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# Make visualization
my_style = LS('336699', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config)
chart.title = 'Most-starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
