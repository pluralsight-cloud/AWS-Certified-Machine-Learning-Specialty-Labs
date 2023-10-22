# This code is the you will add to the Jupyter Notebook to complete the analysis

success_rate = dataset.groupby('questionId')['isCorrect'].mean()

plt.bar(success_rate.index, success_rate.values)

for i, rate in enumerate(success_rate):
    plt.text(i, rate, f'{rate:.0%}', ha='center', va='bottom')


plt.xlabel('Question ID')
plt.ylabel('Success Rate')
plt.title('Question Success Rate')

plt.xticks(rotation=90)

plt.show()