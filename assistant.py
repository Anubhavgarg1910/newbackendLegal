import re


def legal_assistant(query):
    patterns = {
    
        r"(copyright|intellectual property)": "Copyright law protects original works of authorship.",
        r"(trademark|brand)": "A trademark is a symbol, word, or words legally registered or established by use as representing a company or product.",
        r"(contract)": "A contract is a legally binding agreement between two or more parties.",
        r"(criminal law|crime)": "Criminal law deals with offenses against the state, and is concerned with punishment for unlawful acts.",
        r"(civil law|lawsuit)": "Civil law deals with disputes between individuals or organizations, often seeking compensation or resolution through the courts.",
        r"(murder|killing|homicide|manslaughter)": "Murder, killing, and manslaughter are illegal acts punishable by law.",
        r"(stealing|theft|robbery)": "Stealing is taking someone else's property without permission unlawfully.Stealing, theft, and robbery are illegal acts punishable by law.",
        r"(contract)": "A contract is a legally binding agreement between two or more parties.",
        r"(criminal law)": "Criminal law deals with offenses against the state, and is concerned with punishment for unlawful acts.",
        r"(crime)": "Criminal law deals with offenses against the state, and is concerned with punishment for unlawful acts.",
        r"(civil law)": "Civil law deals with disputes between individuals or organizations, often seeking compensation or resolution through the courts.",
        r"(lawsuit)": "Civil law deals with disputes between individuals or organizations, often seeking compensation or resolution through the courts.",
        r"(fair use)":"Fair use allows limited use of copyrighted material without permission for purposes such as criticism, comment, news reporting, teaching, scholarship, or research.",
        r"(trademark application)":"The process for filing a trademark application involves submitting an application to the appropriate government agency, along with the required fees and supporting documentation.",
        r"(slogan)": "A slogan can be trademarked if it is used to identify and distinguish the goods or services of one seller from those of others, and if it is capable of functioning as a source identifier.",
        r"(licensing agreement)": "A licensing agreement is a contract between the owner of intellectual property and another party that outlines the terms and conditions under which the licensee can use the intellectual property.",
        r"(statute of frauds)": "The statute of frauds is a legal doctrine that requires certain types of contracts to be in writing in order to be enforceable.",
        r"(elements of a crime)": "The elements of a crime typically include an actus reus (a wrongful act), a mens rea (a guilty mind), concurrence (the act and the mental state must occur together), causation (the wrongful act must cause harm), and harm (the wrongful act must result in harm to the victim).",
        r"(felony)": "A felony is a serious crime that is punishable by imprisonment for more than one year, or by death.",
        r"(misdemeanor)": "A misdemeanor is a less serious crime that is punishable by imprisonment for one year or less, or by a fine.",
        r"(warrant)":"A warrant is a legal document issued by a judge or magistrate that authorizes law enforcement officers to take certain actions, such as searching a person's property or arresting a suspect.",
        r"(arraignment)": "Arraignment is a court proceeding during which a defendant is formally charged with a crime and enters a plea.",
        r"(defense attorney)": "A defense attorney is a lawyer who represents a defendant in a criminal case.",
        r"(prosecutor)": "A prosecutor is a lawyer who represents the government in criminal cases and is responsible for presenting evidence against the defendant.",
        r"(mediation)":"Mediation is a voluntary and confidential process in which a neutral third party helps disputing parties to reach a mutually acceptable agreement.",
        r"(arbitration)": "Arbitration is a process in which a neutral third party, called an arbitrator, hears evidence and arguments from both sides and makes a decision to resolve the dispute.",
        r"(discovery)": "Discovery is the process by which parties in a lawsuit obtain information from each other and from third parties relevant to the case.",
        r"(punitive damages)": "Punitive damages are damages awarded in addition to compensatory damages to punish the defendant for egregious conduct and to deter others from engaging in similar conduct.",
        r"(appealing a court decision)": "An appeal is a request for a higher court to review and possibly change the decision of a lower court.",
        r"(punitive damages)": "Punitive damages are damages awarded in addition to compensatory damages to punish the defendant for egregious conduct and to deter others from engaging in similar conduct.",
        r"(appealing a court decision)": "An appeal is a request for a higher court to review and possibly change the decision of a lower court.",
        r"(actus reus)": "Actus reus is a Latin term that refers to the physical act or conduct that constitutes a criminal offense.",
        r"(mens rea)": "Mens rea is a Latin term that refers to the mental state or intent necessary to commit a crime.",
        r"(concurrence)": "Concurrence is a legal principle that requires the actus reus and mens rea to occur together in order for a crime to be committed.",
        r"(causation)":"Causation is a legal principle that requires the actus reus to cause the harm or result that is prohibited by law.",
        r"(harm)": "Harm is a legal term that refers to the injury, loss, or damage caused by the defendant's wrongful conduct.",
        r"(Miranda rights)": "Miranda rights are constitutional rights that must be read to a suspect before custodial interrogation.",
        r"(contract law)": "Contract law is a branch of civil law that deals with agreements between parties that create legally enforceable obligations.",
        r"(breach of contract|breaks a conract)":"Breach of contract occurs when one party fails to perform its obligations under a contract without a valid legal excuse.",
        r"(statute of limitations)": "The statute of limitations is a legal time limit within which a lawsuit must be filed.",
        r"(hii|hello|hey|heyy|hi)":"Hello, nice to see you!!. Let's get ahead with a legal query",
        r"(child abuse|child labour)":"Child Abuse is meant by  physical, sexual, emotional and/or psychological maltreatment or neglect of a child, especially by a parent or a caregiver.If the child is between 12 and 16 years old, the abuser can be sentenced to up to seven years in prison. Anyone who beats or abuses a child more than 16 years old can be sentenced to 10 years in prison.",
        r"(sexual assault|rape)":"Sexual assault or rape is an act in which one intentionally sexually touches another person without that person's consent, or coerces or physically forces a person to engage in a sexual act against their will.The punishment is rigorous imprisonment of 7 years to life and the person will also be liable to pay a fine. ",
        r"(hit|accident)":"If someone hits your vehicle, check for damage, exchange information, take photos, report to insurance, seek medical attention if needed, and consider legal options if necessary.",
        r"(IPC)":"The Indian Penal Code (IPC) was the official criminal code in the Republic of India, inherited from British India after independence, until it was replaced by Bharatiya Nyaya Sanhita in December 2023. It was a comprehensive code intended to cover all substantive aspects of criminal law.",
        r"(liability|liabilities)":"Liabilities are debts or obligations a person or company owes to someone else. For example, a liability can be as simple as an I.O.U. to a friend or as big as a multibillion dollar loan to purchase a tech company.",
        r"(defendant)":" Individual or entity accused or sued in a legal case.",
    }


   
    for pattern, response in patterns.items():
        if re.search(pattern, query, re.IGNORECASE):
            return response

    return "I'm sorry, I'm not sure how to answer that legal question.I am still learning. Maybe, we can try with another Question :)"

# if __name__ == "__main__":
#     print("Legal Assistant: Hello! I'm a legal assistant. What legal term do you want to know about?")
#     while True:
#         user_query = input("You: ")
#         if user_query.lower() == "exit":
#             print("Legal Assistant: Goodbye! Have a great day!")
#             break
#         response = legal_assistant(user_query)
#         print("Legal Assistant:", response)