# README

## Setup Instructions

### Install Requirements

```
pip install -r requirements.txt
```

### Basic Configurations

In `run.sh` you can edit the configuration of the project. An example of configuration:

```
CLIENT_ID="your_client_id"
CLIENT_SECRET="your_client_secret"
USER_AGENT="health_research_bot"
USERNAME="your_reddit_username"
PASSWORD="your_password"
TIMEFRAME="year"
MAXPOSTS=10
KEYWORDS="clinical trial healthcare"

```

Note that it's OK not to edit anything, the script will run under default settings.

### Run the Script

To continue, run `run.sh` in your terminal:

```
bash run.sh
```

### Output

All the data collection + sentiment analysis + message generation results are saved to `reddit_health_posts.txt`.

## Methodology and Challenges

### Data Collection

The `praw` package provides an access to the Reddit API. Through setting topics and time filters we can easily direct to the posts we are interested in.

I choose "clinical trials", "drug trials", "experimental treatments","chronic illness", "cancer trials", "mental health trials" and "rare diseases" as the default topics. I believe these topics include most information of clinical trials and users who are intended to look for clinical trials.

### Sentiment Analysis

In this part I choose the `Vader` package for sentiment analysis in posts. `Vader` is specially designed for light-weighted unformal text scenarios, which I believe is a good fit for the Reddit posts.

Besides, to have a better grasp of the whole information, I add the title of the posts and it's contents as an integrity to perform the analysis.

### Personalized Message Generation

The 'gpt-3.5-turbo-instruct' model is utilized here for message generation. Making use of the users post contents and the sentiment analyses, I make a strategy targeting different kind of users:

* For positive attitude users, the message would focus on highlighting the benefits and importance of participating in the upcoming trial.
* For neutral attitude users, the message provides information about the benefits of the trial and encourages them to participate, explaining how it could improve their health outcomes.
* For negative attitude users, the message emphasizes that the upcoming trial avoids the issues they mentioned.

I believe the strategy would make messages suitable for different groups of potential customers.

### Challenges

Most of the challenges in present comes from access limits of openai api. For now I just limit the length and number of inquiry tokens to address the problem.

Another concern I might have is that sentiment analysis might not be sufficiently appropriate for judging the attitude of a user. Given that a person who shows a strong negative feeling towards undergoing clinical trials may also in desperate need of new ones. So I designed the strategy targeting different group of people, which may ease the problem. But this is just a trial in limited time, I believe there will definitely be space for optimization.

## Examples of the process

Here I would like to post two examples of the whole process, coming from a positive and a negative post:

The positive attitude user:

```
Title: Any good app to stay up to date with clinical trials?
Text: The recent surge of data is driving me crazy. Every day there’s a new trial popping up. Any recommendations on apps to stay upto date with those?

Sentiment Score: {'neg': 0.056, 'neu': 0.867, 'pos': 0.076, 'compound': 0.2168}

Personalized Message: Hello! I see your frustration with trying to stay up to date with all the clinical trials popping up. As someone who is interested in clinical trials, I wanted to personally invite you to participate in our upcoming trial. Not only will you have access to the most current data and findings, but you will also have the opportunity to make a significant impact on the future of healthcare. Our app will keep you notified of any updates and provide detailed information about the trial. We would love to have you join our community and be a part of groundbreaking research. Thank you for your interest!

While this clinical trial avoids many of the issues you mentioned, we still recommend considering any potential risks. Feel free to ask more questions to ensure you fully understand the trial.

This message is generated based on your feedback about clinical trials. We value your input and have considered it in our recommendations.

```

The negative attitude user:

```
Title: Insurance denied wifes pacemaker as experimental treatment
Text: Wife had a pacemaker implanted last year.  The dr used a micro pacemaker and called insurance to precertify. Ins said it wasnt required.  We didnt receive a bill for 9 months after the procedure from hospital.  Insurance denied appeal since it was past 6 months.  Now the hospital has sent it to Paragon collections after they told me they would wait on a OPM appeal.  Do I have any options?  Bill is $16k.

Sentiment Score: {'neg': 0.069, 'neu': 0.931, 'pos': 0.0, 'compound': -0.7003}

Personalized Message: Dear [User],

I understand your skepticism about clinical trials, especially after your experience with your wife's pacemaker and insurance denial. However, I want to assure you that the upcoming trial I am inviting you to participate in addresses the issues you mentioned.

Firstly, our trial does not involve any experimental treatments. It is carefully designed and follows all regulations to ensure the safety and effectiveness of the treatment being tested.

Secondly, our trial does not require any upfront payments or insurance approvals. We cover all costs related to the trial, including procedures, medications and follow-up visits.

Lastly, we have a strict timeline in place for billing and appeals. We understand the importance of timely communication and will work with you to avoid any confusion or delays in processing billing. Our team is also available to help with any appeals and address any concerns you may have.

We value your time and your trust in our trial. Please let me know if you have any further questions or concerns. We are committed to providing you with the best care possible and will do everything in our power to make this a positive and successful experience for you and your wife.

Sincerely, 
[Your Name]

While this clinical trial avoids many of the issues you mentioned, we still recommend considering any potential risks. Feel free to ask more questions to ensure you fully understand the trial.

This message is generated based on your feedback about clinical trials. We value your input and have considered it in our recommendations.


```

I believe these two examples give a good reflection of the effectiveness of the project.

## Ethical Considerations

It is always an inevitable and important concern in the medical field whether data collection and trial advertising obey ethical rules. Here I've provide two approaches for the two parts respectively.

### Data Collection Ethical Concerns

To better protect user privacy, the script didn't track usernames or gender or address of the users. Also, not taking these information into account avoids gender/regional bias when composing the message.

### Trial Advertising

It is important for the advertising messages to avoid misguiding users to sign up for trials. Given that it will be difficult to regular the message generation to completely get rid of exaggeration, I choose to add some reminders after the message to make sure the target users would be aware of their freedom to choose and reject as well as our protection of their privacy.
