from text_rewrite import TextRewrite


sentences = ['My machine is so bad and dramatic', 'I have one dog and two cars', 'This season is so weak.', 'my home is so sucky','Exasperating farrago of distortions, misrepresentations outright lies being broadcast by an unprincipled showman masquerading as a journalist']
for sentence in sentences:
    new_sentence = TextRewrite(sentence).work() 
    print(sentence + " -> " + new_sentence)
