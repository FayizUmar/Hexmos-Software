def load_fps(path):
    with open(path, 'r') as file:
        file_content = file.read()
        lines=file_content.split('\n')[1:]
        questions = []
        for line in lines:
            question, options, votes, tags = map(str.strip, line.split('::'))
            option_list = [option.strip() for option in options.split('|')]
            vote_list = [int(vote.strip()) for vote in votes.split('|')]
            tag_list = [tag.strip() for tag in tags.split('|')]
            
            # print(question)
            question_dict = {
            'Question': question,
            'OptionVote': {option: vote for option, vote in zip(option_list, vote_list)},
            'Tags': tag_list
            }
            questions.append(question_dict)
    return questions
def filter_by_tags(polls_data, list_of_tags):
    filtered_tag=[]
    for tag in list_of_tags:
        for data in polls_data:
            if tag in data['Tags']:
                filtered_tag.append(data)
    return filtered_tag
def view_poll(polls_data, pollNumber):
    print(polls_data[pollNumber-1]['Question'])
    for op in polls_data[pollNumber-1]['OptionVote']:
        print('*',op,polls_data[pollNumber-1]['OptionVote'][op])
    print('')
    print('Tags:',end='')
    for tag in polls_data[pollNumber-1]['Tags']:
        if tag!=polls_data[pollNumber-1]['Tags'][-1]:
            print(tag,end=',')
    print(tag)
polldata_path="C:/Users/HP/Desktop/Heximos/week2/polldata.fps"
polls_data=load_fps(polldata_path)
# print(polls_data)
filtered_data=filter_by_tags(polls_data, ["cricket","phones","health"])
#print(filtered_data)
poll_view=view_poll(polls_data,4)