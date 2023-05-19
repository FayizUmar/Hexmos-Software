f = open('polldata.fps', 'r')
file_contents = f.read()

lines=file_contents.split('\n')[1:]
questions =[]

for line in lines:
    print(line)

for line in lines:
    qn,opt,vote,tag=map(str.strip,line.split("::"))
    opt_list=[opt.strip() for opt in opt.split("|")]
    vote_list=[vote.strip() for vote in vote.split('|')]
    tag_list=[tag.strip() for tag in tag.split('|')]
    
    #print(opt_list)
    #print(vote_list)
    #print(tag_list) 
    
    question_dict={
        'Question':qn,
        'Vote':{opt: vote for opt ,vote in zip(opt_list,vote_list)},
        'tag':tag_list
    }
    questions.append(question_dict)
    
    for qn in questions:
        print(qn)