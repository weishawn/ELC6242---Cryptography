first_string = "FORMATIVE ASSESSMENT CAN BE VIEWED AS A MEAN TO ENHANCE THE LEARNING PROCESS BASED ON THE RESULTS OF SUCH ASSESSMENTS STUDENTS WILL BE ABLE TO ASSESS THEIR KNOWLEDGE AND IDENTIFY STRENGTHS AND WEAKNESSES THE TEACHER WILL ALSO HAVE INDICATION ON HOW WELL THE STUDENTS ARE GRASPING THE FUNDAMENTAL FACTS AND WHETHER HE NEEDS TO ALTER THEIR TEACHING TO EMPHASIS SOME IMPORTANT CONCEPTS"
second_string = "Xmjpnhtfy niiyiipyoh uno ey ftydyz ni n pyno hm yovnouy hvy qynjotow ljmuyii. Eniyz mo hvy jyigqhi mx iguv niiyiipyohi, ihgzyohi dtqq ey neqy hm niiyii hvytj romdqyzwy noz tzyohtxb ihjyowhvi noz dynroyiiyi. Hvy hynuvyj dtqq nqim vnfy toztunhtmo mo vmd dyqq hvy ihgzyohi njy wjniltow hvy xgoznpyohnq xnuhi noz dvyhvyj vy oyyzi hm nqhyj hvytj hynuvtow hm yplvniti impy tplmjhnoh umouylhi."

first_string = ''.join(e for e in first_string if e.isalnum())
first_string = first_string.lower()

second_string = ''.join(e for e in second_string if e.isalnum())
second_string = second_string.lower()

keys = list(second_string)
values = list(first_string)
output_dict = (dict(zip(keys, values)))
output_dict = sorted(output_dict.items())
print(output_dict)