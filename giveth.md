---
slug: futureOfGiving2017
title: What is the Future of Giving?
author: Kris
author_image_url: /img/krisAuthor.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


An Overview of the Giveth Donation Application
==============================================

_Edit: for the current status of the development, more recent updates_ [_here_](https://medium.com/giveth/tagged/dappening)

If you ever talked to a Giveth [Unicorn](https://medium.com/giveth/giveth-introduces-decentralized-altruistic-communities-dacs-d1155a79bdc4) chances are high we did not let you go before you understood what Giveth is all about — we’re a passionate bunch. If you haven’t met people like [Griff Green](https://medium.com/@thegrifft), [Jordi Baylina](https://github.com/jbaylina), [Grace Torrellas](https://twitter.com/GraceTorrellas), [Vojtech Simetka](https://github.com/vojtechsimetka) and the [many other great faces](https://wiki.giveth.io/dac/team-organisation/) contributing to the Giveth Platform you might wonder **what it is exactly we’re building and why.**

To put it plain and simple: we want to make the **process of giving to causes you believe in effective and transparent**, and we are using blockchain technology to do so. In [October 2016](https://medium.com/giveth/the-minime-token-open-sourced-by-giveth-2710c0210787) the team started developing the DApp (Donation Application) and is now [coming closer](https://wiki.giveth.io/dapp) to the release of its Minimum Viable Product (MVP). In the build-up to this, we would like to take a moment to explain why we are creating the platform and give you a sneak peak of the user flow.

**Wait, but why?**

If you have ever donated to non-profits or charitable organizations chances are high your experience was similar to this one: on your way to the metro you got stopped by a convincing youth who got your name, mailing address and signature for a fixed monthly donation to a specific cause. Since that moment, a few times per year — if you’re lucky — you receive an old-school newsletter which you throw away without reading. **You are left entirely in the dark about where your donation went,** and the non-profit receives a monthly amount until you decide to cancel.


Giveth changes all this. As all donations are recorded on the Ethereum blockchain you can follow, in real-time, who gets your donations and why at a very granular level.

The Giveth platform has a simple result-based incentive structure: when funds are collected they are stored in our [Vault](https://medium.com/giveth/the-vault-contract-open-sourced-by-giveth-fe2261f7b91b) and only after Milestones are completed, can the funds be withdrawn. The Giver’s funds are under their control until their donations are locked for a specific purpose.

This basic structure gives them a clear view on the various people involved in the process and the possibility to contact everyone directly. And if they don’t like what their funds are intended to be used for, they have time to block its use.

We are building the **Future of Giving by cutting out the bureaucracy** so that funds can be spent more efficiently and everyone can collaborate in making the world a better place.

**Talk the Talk**

We are re-engineering how donations are made, and with it, we had to reinvent the [language](http://wiki.giveth.io/dapp/product-definition) to talk about it. The 3 key building blocks of the Giveth system are Communities (DACs), Campaigns and Milestones. A **DAC** — short for Decentralized Altruistic Community — is the group of people united around a cause they want to support. This DAC will fund and steer multiple **Campaigns**, which can in their turn also be supported by more than one DAC. A Campaign translates the dreams of a DAC into a more specific agenda to which action points are linked: we call these the **Milestones**. Milestones are the smallest entity within the Giveth system and are the last step in our donation flow. Once completed, the funds are released into the wild to reimburse and reward good people for their good work.

<img alt="Building Blocks of Giveth" src={useBaseUrl('img/blog/buildingBlocksGiveth.png')} />

##### The 3 key building blocks of Giveth are Communities (DACs), Campaigns and Milestones.

We focus on the technology so people can focus entirely on uniting around causes. In order to do so, we need to define **some of the basic roles** in our system.

A **Giver** can donate directly to a Campaign they believe in, or can decide to pledge funds to a DAC that will allocate these funds to appropriate Campaigns in the Giver’s name — we call this process [Liquid pledging](https://medium.com/giveth/liquid-democracy-what-that-bd3c63e8df52). By donating, the Giver automatically becomes part of the DAC and is connected with the rest of the community.

The **Delegates** are registered DAC members that take on the task of allocating funds sent to their DAC to one or more Campaigns.

The **Makers** are all the people within these campaigns making the change the DACs want to see in the world. There are a few specific roles the Makers have to fulfill.

*   The **Campaign Managers** are the Makers that create Campaigns, assign funds to specific Milestones and make sure their specific Campaign is a success.
*   The **Milestone Managers** are the Makers in charge of specific Milestones and need to assure these very specific actions are achieved as described.
*   The **Recipients** are the Makers that receive the funds when a Milestone is successfully completed.

<img alt="Giveth Roles" src={useBaseUrl('img/blog/givingBlogRoles1.png')} />

##### Main roles within the Giveth Platform: Giver, Delegate, Campaign Manager, Milestone Manager, Recipient.

Two additional roles have been created to **guarantee the correct usage of funds**.

*   The **Campaign Reviewer** can reject completion of any Milestone and can, as a strong security measure, even cancel a whole Campaign if it appears to be fraudulent.
*   The **Milestone Reviewer**’s role is to confirm the Milestone Manager really achieved the proposed goal or action described in the Milestone.

This brings us to the **true power** of the Giveth platform: at all times the Giver knows exactly what is happening to the donated funds, how these are being spent and is in full control through a **transparent network of accountabilities**. If a Milestone is canceled, the funds are returned to the Campaign. If a Campaign is canceled, the funds are automatically returned to the Delegates that supported it. If a Delegate quits, the funds are returned to the Giver. On top of this, one of the most revolutionary aspects of this system is that at any point up until the moment funds are locked into a Campaign, the Giver can decide to withdraw them.

<img alt="Giveth Additonal Roles" src={useBaseUrl('img/blog/givingBlogRoles2.png')} />

##### Two extra roles guarantee the correct usage of funds: Campaign Reviewer and Milestone Reviewer.

You can discover more about these roles and responsibilities by reading on in [the product definition](https://wiki.giveth.io/dapp/product-definition/) on our wiki.

**Walk the Walk**

The Giveth Donation Application is [now in beta stage on testnet](https://wiki.giveth.io/dapp), with all of the roles described above integrated, and currently undergoing testing with a select team of volunteers.

<iframe width="560" height="315" src="https://www.youtube.com/embed/gPXoEzuNQzc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

##### Giveth co-founder Griff Green explains what the Giveth Donation Application is about.

We always have opportunities for skilled developers to contribute to our project, and you can [donate](https://wiki.giveth.io/dac/finances/) to \`revolution.eth\` to reward and incentivize the devs that are making the Giveth platform a reality. Please join our [Slack](http://slack.giveth.io) and find out how you can contribute.

In the meantime, we will keep on building the platform and will share in the coming weeks and months how the different components work. Stay tuned for more!

Warm regards,

[Giveth](https://giveth.io/)

*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [Github](http://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🤲🏼 [Donate directly](http://donate.giveth.io/) 🤲🏼 or buy a Ledger with our [affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663). ⏎
---
slug: liquidDemocracy
title: Liquid Democracy…What That?!?
author: Yalor
author_image_url: /img/yalorAuthor.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

<img alt="Liquid Democracy" src={useBaseUrl('img/blog/liquidDemocracy.jpeg')} />

Welcome to the future of voting.

Or as some would say the Land of Possibilities :-)

### So what IS liquid democracy?

In addition to being simply a system of tokenized voting you can think of it as a hybrid between representative and direct democracy.

Instead of one person casting one vote, the system can become fractional. One vote can now be split in any number of ways between multiple delegates or sent entirely to your chosen delegate, and your delegate can delegate to someone else. Much delegation, so democracy.

As an example take a busy college student who just doesn’t have time to vote, she could delegate ½ her vote to her mom and ½ her vote to her professor. If either of them wanted they could allocate a portion of the vote or all of it to a popular politically active persona that acts as a representative for the local community and controls an influential % of the total vote.


Giveth is a perfect playground for implementing liquid democracy
================================================================

Of course, the reason we’re explaining liquid democracy is because it is one of the core technologies that inspired Giveth’s [Liquid Pledging](https://github.com/Giveth/liquidpledging) system, and we see it as an important building block for the governance of [DACs](https://medium.com/giveth/giveth-introduces-decentralized-altruistic-communities-dacs-d1155a79bdc4).

While there is no voting inherent in Giveth’s base layer, there is an opportunity to use a governance system like liquid democracy in the various roles that are filled currently by people such as [Delegates or Reviewers](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4). This would mean that that a delegate, instead of being one person, would become a smart contract that has liquid democracy built in so that the donors can elect several delegates to decide which projects get funded (we will likely use a “liquid plutocracy” model, the more you donate the more votes you get).

But wait there’s more, with liquid democracy + blockchain you have the ability to actually codify your vote.

Yes, I know, code what?

Codifying your vote could allow you to tag different delegates to represent you based on the subject matter for the initiative. This means that if one initiative has an economic tag your vote for that initiative would be automatically allocated to the delegate you want to represent you on the economic issues, if another initiative carries the environmental tag your vote would be automatically allocated to your environmental delegate. Very diverse, much effective.

Say an important issue comes up that you feel very strongly about. You can push a button and take your voting back and vote yourself, then push a button and put your delegation settings back the way they were.

You set the term limits, you can delegate for 20 seconds or 20 years!

Liquid democracy gives everybody the ability to delegate their vote accordingly or even to overstep the position of their representative keeping them accountable for their actions on a day to day spectrum instead of year to year.

No one knows exactly what the future of voting looks like, but with Giveth we can start experimenting with this incredible model while making the world a better place at the same time! Much vast, many possibility, sooo future!

[Democracy 3.0 For The Transparent World](https://medium.com/decentfund/democracy-3-0-for-the-transparent-world-5a9f1ffad1ad)
-----------------------------------------------------------------------------------------------------------------------------

(Updated 11/20 ) Excellent article by [Igor Line](https://medium.com/u/bc1f295769e2?source=post_page-----bd3c63e8df52--------------------------------) on the varied benefits of Liquid Democracy.

To find out more about liquid democracy and how you can experiment within Giveth:

*   Join us on [Riot or Slack](http://join.giveth.io)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [Github](http://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)
---
slug: decentralizedGiving
title: How Decentralized Giving could have helped (and will help) increase Transparency and avoid Cases like Oxfam’s Scandal
author: Lanski
author_image_url: /img/Lanski.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


Oxfam, consistently rated [one of the best NGOs in the world](https://www.oxfam.org.uk/blogs/2012/01/oxfam-number-three-in-top-100-best-ngos) and a household name in most western countries, is mired in a scandal over allegedly [abusing of both people and funds](http://nationalpost.com/news/world/a-full-on-caligula-orgy-oxfam-charity-accused-of-exploiting-haiti-disaster-victims-for-sex) in Haiti during the aid mission deployed after the hurricane Harvey. Not only this, but it is also accused of its employees exchanging aid for sexual favours, plain and simple sexual abuse. The case has opened the door for a cry of the nonprofit sector to uncover and denounce these practises, which seem to be [more common than one would think](https://www.theguardian.com/global-development/audio/2018/feb/14/oxfam-allegations-are-tip-of-iceberg-sexual-harassment-and-aid-workers-podcast).

Transparency and accountability in charitable donations have been put in check after the scandal broke out, with the International Development Secretary of the UK announcing a big audit of the organizations funded by public money, under [threat of cutting the funding](https://www.independent.co.uk/news/uk/home-news/oxfam-sexual-abuse-aid-workers-haiti-prostitutes-scandal-national-crime-agency-mordaunt-latest-a8211211.html) if their standards are not met. Presumably, such an audit will be expensive and will not bring much to light, as the system is fundamentally opaque, spending more taxpayers’ money that could be dedicated to social impact projects.

Despite some challenges, I genuinely believe that almost every person working in the development sector is in it to help other people and that they do the best they can. Until now, we didn’t have tools that allowed for a different governance and management of large amounts of aid funds… but now we do.

Campaign-based giving
=====================

Nowadays, one gives money to an organization and must trust them to use it properly. The money is given a priori, being a grant from the government, from a granting organization or from individuals. Once the money is in their bank account, it’s -by design of how the banking system works- opaque to external people: we must trust them again to have proper procedures in place to avoid mismanagement of such funds i.e. [“Caligula orgy with prostitutes in Oxfam T-shirts”](https://www.thetimes.co.uk/article/oxfam-in-haiti-it-was-like-a-caligula-orgy-with-prostitutes-in-oxfam-t-shirts-p32wlk0rp).

With [Giveth](http://giveth.io/) you will be able to see how the project is laid out, [Milestone by Milestone](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4), and how much money is required for each and every part. If a Milestone is not achieved, or the Milestone Reviewers (more on this category of validators shortly) perceive misconduct, 1) this Milestone will not be approved and paid out and 2) the Reviewer can decide to send all of the unspent funds back to the original Givers to be donated to other projects.

The most common issue raised here is: what happens if the Milestone Reviewer(s) is/are ‘greased’ by the Milestone Manager to approve an underachieved Milestone or to turn a blind eye on inappropriate behaviour? I see this as an excellent opportunity to bring together agents that have no special interest in colluding: a grassroots organization, the local community leadership, the government and an independent observer. One could decide that all of these need to agree on the validation and submit proof, similar to the videos used in Giveth’s [RewardDAO](https://medium.com/giveth/how-rewarddao-works-aka-what-are-points-7388f70269a). Technically, since the figure of the Reviewer is just an Ethereum address, it can be a contract, it could be a multisig wallet held by these relevant stakeholders. Another, if slightly more complex, setup is that a percentage of all Givers to a Campaign need to approve the Milestone after reviewing proof. Using a [Liquid Democracy](https://medium.com/giveth/liquid-democracy-what-that-bd3c63e8df52) governance system here would naturally concentrate voting power in people that are reputable and are perceived to be neutral in this particular Campaign or even Milestone.

I see this as a side benefit of Giveth’s Campaigns: the need to be in constant communication with Milestone Reviewers and Campaign Managers creates — apart from transparency — a true Community where problems are openly discussed and input comes from all sides, because everyone has stake in the game.

Communities solving problems
============================

Thinking of the bigger picture, how can we really shake the giving ‘industry’ awake? Without questioning the expertise and indubitable economies of scale and know-how transfer of the big International NGOs, Giveth enables another sort of organization: The DAC, the [Decentralized Altruistic Community](https://medium.com/giveth/giveth-introduces-decentralized-altruistic-communities-dacs-d1155a79bdc4). Can we do better than just trust Oxfam (or any equivalent INGO) to drop out of the air and deploy their tactics? The Giveth platform can be used for validation of Campaigns and Milestones, but … maybe we could go a step further.

Imagine the creation of a true DAC in Haiti, conformed by Givers, people on the ground (the ‘Makers’) and even representation of the INGOs, all communicating with each other and through an agreed form of governance that works to pledge resources the right way. This way we can make sure that Oxfam’s expertise is allocated where it can impact the most, in constant communication with other stakeholders and with fully transparent decision making.

You get some decision power, you get some more, and you get some too!
=====================================================================

Does it sound complicated? After all, you are not an expert in Haiti… maybe you’ve never even been there! How are you supposed to choose where to pledge funds or to know which Campaigns are going to be the most impactful? Giveth has got you covered. With Liquid Pledging, a concept derived from [liquid democracy](https://medium.com/giveth/liquid-democracy-what-that-bd3c63e8df52), you can delegate the choice of your donations to Communities you perceive as experts: this can be an influential development group — Oxfam if you really must!- but also your former roommate’s social impact group, which was really into this ‘making a better world’ thing. You delegate to a DAC, and it can send your donation to its chosen Campaign, a lot like how charity is supposed to work nowadays, but with much more oversight. You will be able to track your donation, veto any decisions the delegates make and get connected to the people/communities running the Campaigns you will be funding.

Once you start down the rabbit hole, the possibilities are endless: You can delegate half of your pledged funds to a DAC specializing in disaster relief, which in turn will fund some trusted Campaigns for smaller specific problems. The other half you can delegate to your favourite Campaign focusing on improving education in your hometown or even to another DAC that brings together all education projects in your area. Be as local or global as you want!

<img alt="Liquid pledging at work" src={useBaseUrl('img/blog/liquidPledging.png')} />

##### Liquid pledging at work

Help us solve the challenges
============================

The future is near. But not quite here yet, as this is not happening now. The main challenges are

*   Scalablity of the crypto ecosystem. Let’s face it, maybe we are not quite there yet. And I am not even speaking of unpredictable transaction fees raising the cost of donating and transactions not going through: Liquid Pledging is a complicated system that requires a lot of gas. Luckily [Giveth has a good stop-gap solution](https://medium.com/giveth/tackling-ethereum-scalability-issues-29bd700b5060).

> _If you are a Dev and/or working on scalability solutions, have a look at what ScalingNOW is doing_ [_here_](https://medium.com/giveth/scalingnow-bridge-chains-parity-8c359aca2b01) _and join us in building the future of Ethereum!_

*   Liquid pledging would benefit greatly from some sort of identity on the blockchain, integrated with [governance tools like AragonOS](https://blog.aragon.one/announcing-aragon-labs-a679693429ae). The UI/UX for most of these applications remains outside of the control of most individuals, let alone organizations in the humanitarian sector who shouldn’t have to focus on the technical side and should be able to interface seamlessly with the platform(s).

> _Our Social Coding circle pushes Open Source projects like BrightID for Proof-of-Identity and other great projects. Read more about them_ [_here_](https://steemit.com/blockchain4humanity/@giveth/what-is-the-social-coding-circle)_!_

*   Bridge Crypto — Fiat. How do you deal with international crypto transfers and especially the conversion of ETH (or whatever cryptocurrency Campaigns receive as donations) to fiat in order to pay for the expenses of the Campaigns?

> _If you are working on projects that are building solutions for the last mile, please get in touch!_

*   There are also many unanswered questions around taxation for the organizations deploying the Campaigns. They are receiving donations in crypto currencies and how this is to be treated is not well defined for taxation in most jurisdictions right now.

> _If you are a lawyer and/or have good resources on the regulatory aspect, please hit me up or leave them in the comments!_

[Join our community](http://join.giveth.io/): by tackling interesting problems like this one you can help us positively impact charitable giving forever!

*   Find us on [Riot](https://riot.im/app/#/group/+giveth:matrix.org) or [Slack](http://slack.giveth.io/)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [Github](http://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🤲🏼 [Donate directly](http://donate.giveth.io/) 🤲🏼 or buy a Ledger with our [affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663) ⏎

Written by [Pol,](https://steemit.com/@pol-lanski) lovingly edited by [Griff](http://twitter.com/thegrifft) and [Kris](http://twitter.com/krrisis)
---
slug: masterpieceManifesto
title: Giveth Masterpiece Manifesto
author: Yalor
author_image_url: /img/yalorAuthor.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

We [asked](https://medium.com/giveth/giveth-make-it-so-manifesto-80c7e3576e16) you (our community) to dig deep into your hearts and minds, to give us your best version of the Giveth Manifesto. The results did not disappoint.

The value of **community**, of the people, stands out in virtually every submission. A case to that point is the enthusiasm and passionate co-creation we witnessed in and by our own tight-knit Giveth Community, which honestly floored, wawed and awed us. To celebrate this, we are not only giving away eth to our top 3 winners (excluding jury members), [we will also dish out (comm) Points](https://medium.com/giveth/how-rewarddao-works-aka-what-are-points-7388f70269a) to each and **every submission**.

We are so proud and honored to present every one of the entries here for all to see, but first things first a 🎊MAJOR CONGRATULATIONS🎊 to our winners!

Choosing the winners was not an easy process due to the fact that **every entry had gems of wisdom, sparks of insight and heartfelt candor.**

These contributions are the germination of a longer process in the coming weeks. As you might already know, transparency, accountability and especially **open-source** are key words in our vocabulary. So, practising what we preach **we will take the very best from each of these entries and use it to create a crowd-sourced manifesto**. And now _without further ado:_

**🌌 Galactic award goes to:**
------------------------------

> We are a **Community**
>
> What we are doing is not about the technology. Most of us are very, very tech-minded and geeky people, and we love tech, but that is not what it is about or why we are here. It is about the people, the human connection…[**continue reading**](#30fb)



**~**[**Kris Decoodt**](https://medium.com/u/f56581bbe1a7?source=post_page-----19649c57c6aa--------------------------------)

**🚀 Solar System award goes to:**
----------------------------------

> Giveth is a community focused on using blockchain technology to make the world a better place.
>
> Making the world a better place is a very broad mission, narrowing the scope would be a requirement for a normal organization but Giveth is not an organization it is a COMMUNITY. As long as the group of people that are working on a project that they believe can use blockchain to make the world a better place, they are a part of Giveth, if they choose to be…[**continue reading**](#f102)



**~**[**Griff Green**](https://medium.com/u/a2b8809e4b0f?source=post_page-----19649c57c6aa--------------------------------)

**💫 Star award + 1 ETH goes to:**
----------------------------------

> At some point in our lives, almost every one of us experiences an earnest desire to make a real difference in the world. Some of us dream of traveling to far off places and delivering cold, clean drinking water to those who are thirsty. Some imagine providing housing for the ever-growing homeless and refugee populations worldwide. Others picture themselves developing a small plot of land for inner-city children to learn about gardening. Whether global or local, big or small, many of us truly want to help others…[**continue reading**](#00d9)



**~**[**Joshua Du Chene**](https://medium.com/u/b60aa9f7ce4d?source=post_page-----19649c57c6aa--------------------------------)

**🌚 Moon award + 0.4 ETH goes to:**
------------------------------------

> The life of the Giveth Unicorn  
> Giveth Unicorns may come and go. But the role of a Unicorn remains the same.
>
> Each Unicorn cares about at least some aspects of Giveth and strives to help Giveth and its communities achieve and maintain their goals and values.
>
> An altruistic Unicorn does their work in the spirit of collaboration, bringing their skills to bear on the worthwhile goals of Giveth and it’s communities, often without the expectation of reward…[**continue reading**](#961f)


**~**[**Matt Stabeler**](https://medium.com/u/822110fc7bba?source=post_page-----19649c57c6aa--------------------------------)

**☄️ Asteroid award + 0.2 ETH goes to:**
----------------------------------------

> The Giveth Manifesto is a statement of **principles**, of **purpose** and of **determination**.
>
> We are **determined** to accomplish our **purpose** to make a better world through **decentralization, technology and the power of communities**.
>
> We believe communities are evolving organizations (call them flocks, swarms, galaxies or as you may) that are flexible, stronger than the individual and built by such individuals in order to accomplish a purpose…[**continue reading**](#2b3f)


**~**[**Pol Bordas**](https://medium.com/u/dccbc9c48740?source=post_page-----19649c57c6aa--------------------------------)


Time to celebrate, collect your ETH and do a little dance 🕺🏽 because all of you are DAC super heroes for giving your time, words and unique perspectives. For reasons of objectivity our benevolent Giveth judges agreed collectively to not accept any prizes for their entries, so the ETH awards have simply moved down to the next highest voted entry.

**Below are all 21 amazing entries as promised:**
-------------------------------------------------

*   [**Galactic award**](#30fb)**~**[**Kris Decoodt**](https://medium.com/u/f56581bbe1a7?source=post_page-----19649c57c6aa--------------------------------) **🦄**
*   [**Solar System award**](#f102)**~**[**Griff Green**](https://medium.com/u/a2b8809e4b0f?source=post_page-----19649c57c6aa--------------------------------) **🦖**
*   [**Star award**](#00d9)**~**[**Joshua Du Chene**](https://medium.com/u/b60aa9f7ce4d?source=post_page-----19649c57c6aa--------------------------------) **🔮**
*   [**Moon award**](#961f)**~**[**Matt Stabeler**](https://medium.com/u/822110fc7bba?source=post_page-----19649c57c6aa--------------------------------) **👾**
*   [**Asteroid award**](#2b3f)**~**[**Pol Bordas**](https://medium.com/u/dccbc9c48740?source=post_page-----19649c57c6aa--------------------------------) **🐼**
*   [**~GeleeRoyale**](#111b) **🦉**
*   [**~Cleo**](#d524) **🚀**
*   [**~Vojtěch Šimetka**](#bb8f) **🏃🏻‍**
*   [**~Meefs**](#175f) **🎩**
*   [**~DAppLion**](#0f91) **🎧**
*   [**~Ron Mat**](#884d) **⛵️**
*   [**~jen Giveth**](#1bf9) **🚌**
*   [**~Xilef**](#7ac7) **👽**
*   [**~Parker Williams**](#fd75) **🏗**
*   [**~Zak Perna**](#579d) **👨🏼‍🎨**
*   [**~Yalor Tackson**](#ef2e) **🌚🌝**
*   [**~Alan Borger**](#fcfb) **🕴🏻**
*   [**~Bowen Sanders**](#e878) **🦇**
*   [**~LinzeeLouu**](#9e74) **🦋**
*   [**~Andreas Papazidis**](#3fb8) **👨🏻‍💼**
*   [**~Mandala Kitten**](#a843) **👩🏼‍🎤**

**_What does Giveth stand for? What are some of the crazy things we believe in? After working with the team for +7 months now (which is years in blockchain time) these are some of the thoughts that come to mind…_**

We are a Community
------------------

> What we are doing is not about the technology. Most of us are very, very tech-minded and geeky people, and we love tech, but that is not what it is about or why we are here. It is about the people, the human connection.
>
> We live in a world that has never been more connected, but never have we felt more isolated, never have our individualistic traits and our ego been more nurtured (think social media, for one) than today. But has it made us happier? Definitely not. Even worse, it has made us retreat into ourselves, giving less, both emotionally as well as financially. Giveth wants to turn the tide, bring back the connection by building/buidling and making the World a Better Place.
>
> We are not an organization, not a DAO, we strive to be more, we are a Decentralized Altruistic Community (a DAC). Communities are based on shared values and this is what corporations and organizations lack. They do pretend to have core values, but these are outward facing, top-down and are used for branding purposes. Our values are bottom-up, crowdsourced and are the higher good that connects us.
>
> We are a community of individuals and we celebrate and respect each and everyone’s uniqueness.

We dare to be Vulnerable
------------------------

> Our main value, our essence lies in vulnerability. Most of the people at Giveth, and even in the wider ‘Maker’ blockchain space (=the opposite of daytrader land) are here because they know what ego and image brings to the world. They are professionals who have lived the corporate life and knew something was ‘off’. Hierarchy and image boosting bring pain, misunderstanding and most of all a huge waste of time and loads of inefficiency.
>
> When you dare to be vulnerable - even fragile, open and true - you can make lasting changes, because it’s the only way to truly connect with another human being. And together, when you connect, you always achieve more.
>
> Another crucial reason to open up is because ‘the system’ has trained us to be numb by providing us with all possible tools (binge-watching, medication, social media, shopping, … the list is endless). We have been trained to care less, to be less conscious of suffering and injustice, during a time where we are actually hyper-connected and thus can be hyper-informed. Knowledge brings power: sharing your thoughts, ideas and feelings can change the world. We just have to express our **outrage** and team up, because right now, as individuals, together, we actually have a bigger impact than ever before in the history of mankind.

(Please watch [THIS](https://www.youtube.com/watch?v=rGIY5Vyj4YM) if you never have before)

We are Inclusive
----------------

> Everyone is welcome, we are huggers. We believe everyone has talents, has skills and can contribute to Making the World a Better Place. If you see a need in our community you should come over and get it done (see ‘We are Makers’). But even if you just want to lurk around, you should, even just you being there inspires us and we hope to inspire you.
>
> We believe in equal rights, even more, this is a given, this is no topic of discussion. No matter what gender, race, religion or political philosophy you adhere to: you are welcome, and you will be loved. Because giveth is all about community.

We advocate Abundance
---------------------

> When there is abundance people shine. Abundance is the opposite of fear and scarcity, the things that make people become protective and close-minded. We want to give people the chance to develop themselves. We want to be a spark of light, a pulsing star in this galaxy, an inspiration to others, an energy that rubs off.
>
> Only if we harness this internal energy we will be able to make real and lasting change in this world. When there is abundance people thrive and are able to not only show off their skills but their talents. The difference between skills and talents is that you no longer only do what you are good at, you do what brings happiness into your life and you bring this into the lives of others.

We are striving to be fully Decentralized
-----------------------------------------

> Money is not evil. Neither are people. But centralized power is. We are all equal with our differences. Blockchain technology, which is by its nature decentralized, is a driving force that builds and inspires our language. Language brings Culture and Culture will bring lasting change, an entirely different way to approach tensions, a new angle to think about ‘issues’.
>
> We are about the people. But we are not about just one person or a few stars, we are a Galaxy and all of us should burn brightly.

We are Humble
-------------

> You cannot be decentralized and part of a Community if you do not let go of your ego. We don’t boast. We are not interested in your words but in what you do. We let our work speak for itself and will celebrate the individuals, but most of all the community that makes dreams a reality.
>
> We like to have fun but we celebrate balance and modesty. When it comes to spending, we are transparent and accountable because it makes things easier and just, well… more honest.

We are Transparent
------------------

> Sharing is caring. We have nothing to hide. We are fully transparent, we practise what we preach, we are open-source.
>
> We communicate as much as possible, also between us, we do not hold back. We convey our tensions and our desired outcomes, but always try to do this in a very respectful way.

We are Makers
-------------

> When we see something needs to be done, we do it. As Swarm City [would say](https://press.swarm.city/niks-moet-2fd1b7682bb8), “the person who spots a problem is likely the most suited to solve it, because it is their brain that is attuned to seeing the gap between what is now, and what might be.” We don’t endlessly discuss things, this is just negative energy.
>
> Do not underestimate us. Our values might sound ‘out there’, idealistic or naive. But we are not. We underpromise and overdeliver. We are professionals, with lots of experience. We are engineers, developers, professional marketeers, business owners, … and we are here to stay.


> ~[Kris Decoodt](https://medium.com/u/f56581bbe1a7?source=post_page-----19649c57c6aa--------------------------------)

🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄🦄

**Giveth is constantly evolving and so should this document, in no way should we expect any document to totally encompass what it is to be a part of the Giveth community. The purpose of this document is to give people some understanding of the values shared by the members of the Giveth community, but if this document in some way limits the imagination of Giveth Community Members, it should be thrown away!**

> Giveth is a community focused on using blockchain technology to make the world a better place.
>
> Making the world a better place is a very broad mission, narrowing the scope would be a requirement for a normal organization but Giveth is not an organization it is a COMMUNITY. As long as the group of people that are working on a project that they believe can use blockchain to make the world a better place, they are a part of Giveth, if they choose to be.
>
> Giveth is radically inclusive and trusts each individual and group to practice self-reliance and self-management leaning towards collaboration whenever possible.
>
> Giveth supports human connection within its community even when classically certain actions/conversations maybe “unprofessional.” Especially in the name of FUN! Authenticity, vulnerability, candor, wholeness, and silliness are encouraged as long as they are building trust and stronger relationships.
>
> Giveth believes altruistic people can be rewarded for their good work and strives to find ways to make that feel easy and natural. People are more important than profits.
>
> **Blockchain technology:**

*   Aligns incentives around a collaborative consensus and shared values
*   Is radically inclusive
*   Rewards radical participation, “Do-ocracy” and innovation
*   Maintains a global perspective
*   Is at its best when decentralized
*   Can not be used coercively
*   Spreads via network effect
*   Balances Privacy with Transparency

> Giveth aspires to model itself after these incredible attributes of Blockchain tech.
>
> Givethers have the right to their pseudonymity but everything done under Giveth’s name is as transparent as possible, as replicable as possible, as accountable as possible and invitingly open source.
>
> Every Givether is a hero, a role model, living in service, while still embracing their own wants and needs. We courageously and humbly lead by example, knowing we have a lot to learn.
>
> Giveth is about experimentation and innovation. There is no right or wrong way to solve the issues in our world, we know this, and ask for help and advise, while still pushing a NOW! attitude with integrity and gratitude for the opportunity to change the world.


> **_~_**[**_Griff Green_**](https://medium.com/u/a2b8809e4b0f?source=post_page-----19649c57c6aa--------------------------------)

🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖🦖

> “At some point in our lives, almost every one of us experiences an earnest desire to make a real difference in the world. Some of us dream of traveling to far off places and delivering cold, clean drinking water to those who are thirsty. Some imagine providing housing for the ever-growing homeless and refugee populations worldwide. Others picture themselves developing a small plot of land for inner-city children to learn about gardening. Whether global or local, big or small, many of us truly want to help others.
>
> But how do we actually help? How do we go about making a real impact?
>
> If we have money available to donate to people in need, we soon discover the seemingly infinite layers of vampiric bureaucracy between our donations and the intended recipients, massively decreasing our intended impact.
>
> If we have plentiful time to donate through traditional volunteer opportunities, we’re soon disillusioned by the major inefficiencies, lack of training and organization, misallocation of resources, and other issues that exist within hierarchically managed systems.
>
> If we have willpower and like-minded individuals and we decide to initiate our own causes, we quickly encounter regulatory roadblocks and resistance from archaic systems of centralized power, diverting our focus away from doing good and toward filling out paperwork and paying fees, if we’re allowed to proceed at all.
>
> We exhaust ourselves trying to do good through traditional channels, and the question still remains: how do we actually help? How do we go about making a real impact?
>
> When the systems available to us are inherently flawed, we stop relying upon those systems to achieve our goals. With tools and technologies hitherto nonexistent, we instead build a new platform for giving for the future.
>
> The desire to make the world a better place hasn’t changed, but the tools available to do so have. At the intersection of this drive to do good and the opportunities opened up to us through blockchain technology and decentralized governance, you’ll find a group of individuals known as Unicorns. These Unicorns are all a part of a growing, global community dedicated to changing the way we give. This decentralized altruistic community is known as Giveth.
>
> Like the Unicorns who make up Giveth, Giveth is diverse and ever-growing.

*   Giveth is both a culture and a manifestation of intent.
*   Giveth is an expression of love and the result of action and hard work.
*   Giveth is a transparent proof of decentralized governance in action.
*   Giveth is an amalgamation of altruism and the adjacent possible.
*   Giveth is a global community and a gift to the world.
*   Giveth is open, welcoming, and ready to support you in making the world a better place.

> If you have money available to donate to people in need, you can watch its transmittance across the world on an open ledger to assure it actually gets to those who need it. With the tools and technologies available to us, there’s no more bureaucracy to siphon off funds along the way to the recipients. Giveth doesn’t even take a cut — it doesn’t need to — it’s funded through the same process as the project you just donated to.
>
> If you have plentiful time to donate through traditional volunteer opportunities, you’ll find the Giveth platform maximizes the efficiency and impact of the work you do with clearly defined milestones and the minimal number of actors needed to accomplish the goal. Transparency and accountability are built in, so your work is both noticed and supported by your fellow Unicorns as well as the donors themselves.
>
> If you have willpower and like-minded individuals and you decide to initiate your own causes, you’ll discover an easy-to-use toolset that enables you to create a project with the same ease as creating a blog post. You’ll immediately be able to start receiving donations and create clear steps to achieving your ultimate outcome with no red-tape or fees of any kind.
>
> The best part about Giveth is that anybody can join the community and contribute to making the world a better place. If you’re a human being living on planet Earth and you want to do good, we are your people, and this is your opportunity to make a real impact. Make your mark and add your name to the growing community of Unicorns from around the world by joining us on this magnificent journey to building the future of giving!
>
> **With A Love That Echoes Throughout The Galaxy**


> **_~_**[**_Joshua Du Chene_**](https://medium.com/u/b60aa9f7ce4d?source=post_page-----19649c57c6aa--------------------------------)

🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮🔮

The life of the Giveth Unicorn
==============================

> Giveth Unicorns may come and go. But the role of a Unicorn remains the same.
>
> Each Unicorn cares about at least some aspects of Giveth and strives to help Giveth and it’s communities achieve and maintain their goals and values.
>
> An altruistic Unicorn does their work in the spirit of collaboration, bringing their skills to bear on the worthwhile goals of Giveth and it’s communities, often without the expectation of reward.
>
> Unicorns may be rewarded in many ways, and fairly depending upon their contribution.
>
> Giveth Values  
> Giveth does not knowingly do any harm.
>
> Nobody owns Giveth, it is an entity born out of the spirit of kindness into the world of technology through the hard work of Giveth Unicorns, for the benefit of those who need it.
>
> Giveth is here to make the world a better place.  
> Giveth enables charities and charitable organisations to do good work better.  
> We collaborate to make the goals of Giveth happen, and to uphold the Giveth values.  
> Giveth values transparency, and does not hide from the world.  
> Giveth evolves to achieve it’s goals and maintain it’s values.  
> Giveth favors altruism over profit.
>
> **Why are we here?**  
> Giveth uses the power of technology, to help bad things be be less bad, strives for good things to happen and enables good people to do good things.
>
> Giveth people want to make positive changes to this world, in a transparent way, so that everyone can benefit, and anyone can make sure things have been done right.


> ~ [Matt Stabeler](https://medium.com/u/822110fc7bba?source=post_page-----19649c57c6aa--------------------------------)

👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

The Giveth Manifesto is a statement of principles, of purpose and of determination.
===================================================================================

> We are **determined** to accomplish our **purpose** to make a better world through **decentralization, technology and the power of communities**.
>
> We believe communities are evolving organizations (call them flocks, swarms, galaxies or as you may) that are flexible, stronger than the individual and built by such individuals in order to accomplish a purpose.
>
> We believe the Giveth Unicorns, the members of the Giveth Galaxy, are people and not cogs in a machine, that find resonance between Giveth’s purpose and their own purpose. Our Galaxy is universal and radically inclusive and able to accommodate everyone that wants to contribute to its goal. We experiment with Governance to unleash everyone’s potential and ability to play a part.
>
> We believe in **openness, transparency and accountability**: we apply these concepts internally and work towards facilitating other communities externally thanks to our outputs by the [DApp Development Circle](https://medium.com/giveth/tagged/dappening), as well as contributing to other projects guided by the same principles through our [Social Coding Circle](https://medium.com/giveth/tagged/socialcoding).
>
> We believe blockchain technology is a powerful tool to design systems that incentivize the creation of communities that transcend the chain -or Decentralized Altruistic Communities- where all stakeholders, including but not limited to Makers, Donors and recipients, can be upfront about their needs and expectations in an environment of trust and collaboration. We believe we can help build these systems and transform how the non-profit sector has traditionally worked.
>
> We want to make **a better future by building the tools** for any community to push their vision of a better, decentralized world.
>
> We are determined to succeed. We are the Giveth Unicorns. We and you. A better future for all.


> ~[Pol Bordas](https://medium.com/u/dccbc9c48740?source=post_page-----19649c57c6aa--------------------------------)

🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼

> We, the people of Giveth,  
> regard human dignity as inviolable and personal freedom as the highest value in human society,  
> decide through rough consensus and running code,  
> work on software solutions that empower the individual through decentralized validation,  
> play through daring experiments,  
> apply original thinking,  
> open our hearts to share love as a human experience.


> **_~_**[**_KRASSVS_**](https://medium.com/u/6da453cac63a?source=post_page-----19649c57c6aa--------------------------------)

🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉

Humanity vs. The Problems of the World
======================================

> **Why do we have the problems we do,** like global warming, homelessness, and environmental destruction?
>
> **It’s not because we lack the capacity to fix it**. For any problem, there’s an array of experts who have a plan of action to tackle it.
>
> **It’s not because we lack the capital**. There’s more money in the world than ever before.
>
> **What we lack is an effective system for organizing and incentivizing people to tackle the problems that are not profitable to solve.**
>
> [Giveth](https://giveth.io/) is that system — a platform for unleashing the human spirit to conquer the problems of our world. Giveth enables those who want to do good in the world to trustlessly collaborate with those who want to fund that work. Funds are paid only when the work happens. All actions are transparently recorded on the Ethereum blockchain. Giveth is the lightest possible framework for allowing strangers to effect change together.
>
> The Giveth Unicorns are the group of people building Giveth. We have different backgrounds, skill sets, and countries of residence; but we’re united by a shared vision:
>
> We believe that every human being should be able to get funding to make the world a better place.
>
> We believe that every human being should be able to transparently see their funds create good in the world.
>
> We believe that our problems are too large for any individual to solve, and so we need the power of communities.
>
> We believe that transparency is the key to staying focused on the work at hand.
>
> We believe a better world is possible if we effectively unite the minds, funds, and time of everyone who cares about the same issues.
>
> Are you one of those magical creatures — a _Unicorn_ — who believes our problems are solvable through collaboration, aligned incentives, and a little ETH? Giveth will be better with your contributions. [Come create Giveth with us.](https://giveth.io/join/)


> **_~_**[**_Cleo_**](https://medium.com/u/8ddbad602c52?source=post_page-----19649c57c6aa--------------------------------)

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀

**Giveth is a decentralized community of collaborators around the cause of making the world a better place. We are the Giveth Galaxy that empowers communities to achieve their mission. Giveth’s actions are guided by following principles:**

Radical Openness and Transparency:
==================================

> Any project, git repository, presentation or document that has been made within Giveth shall be publicly accessible and usable. We pledge to share these transparently in an organized fashion and provide all necessary guidance. In this sense we identify ourselves with the GNU principles.

Inclusiveness
-------------

> To Giveth there is only one race -the human race-, no sex, no religion, no disability nor political affiliation. Everyone is welcome and we encourage you to share your view and enrich our community.

Independence
------------

> We are financed through unconditional donations that will be used to build, support, evolve and maintain our products, contributors and community. As a group of individuals we pledge to be neutral and any affiliation or promotion of other projects, political parties or movements shall be discussed and agreed by the majority of our community through our internal governance organs. Any such decision shall be publicly shared and be accessible as long as Giveth exists. You can not buy Giveth.

Accountability
--------------

> We see Giveth as a gift to humanity. As such we are accountable to our donors, contributors and the whole of humanity that we will do our best to build Giveth with the resources given and according to our abilities. We assume the responsibility of accounting for our actions as a movement.

Voice of change
---------------

> We are not blind nor silent. When we witness acts of violence, bullying or oppression we may speak out publicly as individuals or as a group. Any such action is not welcome in our own community and will be dealt with.


> **~**[**Vojtěch Šimetka**](https://medium.com/u/cc037be155df?source=post_page-----19649c57c6aa--------------------------------)

🏃🏻‍🏃🏻🏃🏻🏃🏻‍🏃🏻🏃🏻‍🏃🏻‍🏃🏻🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻🏃🏻‍🏃🏻🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻🏃🏻‍🏃🏻‍🏃🏻‍🏃🏻‍

What Giveth.io Means to Me
==========================

> Giveth is a very special altruistic offering of distributed software and grouping of rare unicorns. At its core Giveth enables communities to form around the causes that matter to them the most. On a personal level Giveth is the reason I shifted my vision from only seeing fungible stores of value loosely referred to as ‘crypto’ and decided to dedicate my corporeal energy to enabling trust within this space. A bit about me is in order first however.
>
> I came to ‘crypto’ not as a newbie but someone who was well versed in utilizing cryptographic hashes and technology within daily operations. My first introduction to personal computers came in 1986 when my family moved to Houston TX, and I would play games like ‘Wheel of Fortune’ , ‘Ninja Gaiden’, and ‘SpiderMan’ on our IBM 8086. My first tech job came at the age of 17 where I taught children QBASIC, html, and audio processing at the ‘American Computer Experience’ summer camps. Fast forward to 2009 and my technolust was immediately sparked by this thing I caught wind of called Bitcoin. I had no position in the market other than watching the price of BTC go from near nothing to over $10 USD/BTC.
>
> In August of 2017 life dealt me two perspective altering situations within a week: Hurricane Harvey and losing my job as a Corporate Security Analyst of 5 years. The loss of my position was heartbreaking but being surrounded by constant destruction brought on by an “800 year flood” kept me sane and sober. By December life had begun to return back to normal for most of us Houstonian’s, however something incredible was taking place with the price of Bitcoin: it was over $10,000/BTC!
>
> The dramatic increase of volume plus pricing momentum within Bitcoin caused me to study value theory and seriously contemplate just wtf was going on. Whether it was serendipity, fate, or just plain dumb luck I discovered Giveth via a [youtube presentation](https://www.youtube.com/watch?v=iShzx6iqwus&index=15&list=PLIR2KLUqBsWnbhDZKi0S43Q5PnxFGdiEo) from Griff Green at the Ethereum Community Conference 2018. At this point all of my attention shifted studying pricing and volatility to determining how to best distribute trust.
>
> Giveth will play a key role in enabling communities to distribute trust via decentralized governance. At a high level, Giveth can be viewed as software that enables communities to form causes and promote those causes via group determined milestones. Individuals who are part of a given community can spawn their own milestones, and via pledging of ETH to those milestones prioritize what is and is not important for that community with 100% transparency. Additionally those who give within this structure can be notified when their milestone is reached as well as delegate authority of their contribution to others within their community.
>
> Giveth is not an ICO, a corporation, or a monolithic organization that promises to render aid while capturing the majority of users contributions in times of need (most charities). Giveth is an opportunity to do better by humanity via distributed trust within systems of decentralized governance that \*anyone\* can run.


> **_~_**[**_Meefs_**](https://medium.com/u/40f75102c422?source=post_page-----19649c57c6aa--------------------------------)

🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩🎩

> ~DAppLion

🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧🎧

**Why Giveth?**

> We believe in the power of communities to solve problems.
>
> We believe in decentralized technology to unleash the creativity and energy of altruistic communities.
>
> Giving is a humanitarian act of solidarity and empathy — we believe in the fundamental rights and dignity of every human being.
>
> We are doing nothing less than reinventing giving!

**What?**

> We build a platform for trust and transparency in giving.
>
> Decentralized altruistic communities promote social innovation and create opportunities for people.
>
> This platform is in strong contrast to the systems currently in place: bureaucratic, inflexible, centralized, with a lot of overhead

**How?**

> We are enthusiastic and passionate — we do a hell of a lot of amazing stuff.
>
> We are a community — open, transparent, cooperative, companionable and focused to deliver.
>
> We are an active part of the Ethereum eco-system and contribute to the development of Ethereum.



> **_~Ron Mat_**

⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️⛵️

> **“You can’t go around building a better world for people. Only people can build a better world. Otherwise it’s just a cage.” — Terry Pratchett**

> If you want to understand what Giveth values are and what it means to be a Unicorn and to be part of the Giveth community, you has to understand that the simple goal of all Unicorns in the Giveth galaxy, all around the world is, to make the world a better place.
>
> This starts with the fact that Giveth trusts in people, real, actual people.
>
> Let me explain why this is an amazing, outstanding fact in 2018. We spend the last years and maybe generation with the trust in the big systems and cooperations. The (centralized) banking system, centralized political systems with so called “representatives of the people” who rule countries and do not even know any longer what is going on in a country, the idea that the fact that we are allowed to go to vote every 4 (or 5 years) is all it needs for a democracy to work. We trusted in this centralized systems to rule the world and sort out our human problems. What we end up with was a banking crisis, plastic rubbish all over the planet, a so called refugee crisis and more and more the distrust in systems. We trust in charity organizations all over the world to sort out what we humans fucked up in the past and wonder in the end that we do not know what happened with the donations that we made. We trusted in system for a long time, until we realized that this systems are not working out the way we wanted. We realized that no one will sort out all the rubbish in the oceans and at the beaches if we do not start doing it ourselves, more and more people realize that we need to take our power as citizens back to actually have a say in a democracy, we start to realize that it makes sense to have a reliable person we can trust instead of a bank. We start to realize that centralized systems do not work out the way we though. Decentralization and the trust in people, actually people are two of the main values of Giveth. All these people, all over the world, who contribute their love and time, their work and ideas into Giveth are Unicorns. People with ideas who want to be part of the movement to change the world and make it a better place are Unicorns.
>
> Giveth wants to give power back to people while decentralizing systems. One of Giveths goals and values is to make a donation system transparent, complete and absolute. We want to make donations transparent, direct and reliable. And even if Giveth is a charity organization, we are not just talking about donations. We are talking about the structure of governance within the organization, about reliable, accountable people within the Giveth galaxy, about the fact that everyone and anyone can actively participate in the platform, the organization and the idea of Giveth. The future of giving is not just giving ether to a cause that needs support. Giving can of course be monetary but can also be work force, bodys, love, time, minds and ideas for the greater good.
>
> A lot of people already volunteer for a good cause, give time and love to a project or an idea. Giveth is on the way to build a platform that allows any one of us to make a real change in our community, our neighborhood. I will be able to put up a cause that is important in my direct neighborhood and will make a change and a direct impact in my community — and you can too. Because, you not what? No one knows better what’s going on in your neighborhood than you. Why should anyone donate money to a big, intransparent organization that pays CEO’s instead of directly to your cause? Your community wants to teach kids how to code, you want to feed the homeless people, you want to gather a couple of people and pick up all the rubbish at your local beach/town/park? Cool, put up a cause on the Giveth platform and start to do so. Giveth believes and trusts in people and in you. This is the highest value any organization can have: the trust in people.
>
> Shaping the future needs more than just a couple of people, it needs all of us, the human community. So we are calling everyone, to become a Unicorn and join us in the movement to #maketheworldabtterplace.



> **_~_** [**_jen Giveth_**](https://medium.com/u/7d328be176a3?source=post_page-----19649c57c6aa--------------------------------)

🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌🚌

> _“It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven,_ [_we were all going direct the other way”_](https://en.wikipedia.org/wiki/A_Tale_of_Two_Cities)

**_–_ in short the Unicorns were getting easier and easier to spot as they were coming together to reinvent the most fundamental thing there is.**

> **Giveth is reinventing what it means to be human.**
>
> Humans are not the only life form which create but we have made it our ultimate evolutionary skill. To create is to give and vice versa. Giving is the most primal expression of creating, the most basic level. To voluntarily give something that is yours ( mind, body, property…) by leaving your ownership it becomes something for somebody else. In other words : something changed, transformed, got created.
>
> So giving, What’s so special about that? Everybody does it in one way or another. But the giving the Unicorns are talking about is voluntarily or coercion-free! This means no one can force you in any way. Nor are there gatekeepers who have the power to interfere in the process of you giving. The Giveth Unicorns credo is very clear :
>
> • Donating can be simple, fun and effective.
>
> • Transparency and accountability can be the default.
>
> • Every idea has the potential to make a positive impact, and it can be heard and funded in a decentralized fashion.
>
> • Every Donor can have the ultimate say over how their donation is used.
>
> • People that want to do good work for their cause can be rewarded for their actions.
>
> • Real change and innovation comes about when communities join together to make the world a better place.
>
> Unicorns have always been elusive creatures but now the stars in the Giveth Galaxy have aligned and they are popping up everywhere. Everywhere people are noticing what is being built, being reinvented and want to contribute. The moment you give your time, your energy, your love to this community and project, and help in some way in its existence, a new Unicorn is born.
>
> Permissionless creation will make us unstoppable. It gives hope for the future and the confidence that there will always be people who act for the good of others and that they will succeed.


> **_~Xilef_**

👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽👽

> There are restrictive walls that contain possibility. Inside these walls passion and motivation are strangled by bureaucracy, limitations, and unrelated political tethers. Giveth breaks down these walls and exposes possibility to the wide open expanse contained only by the one natural restriction, capacity. Giveth is where possibility meets capacity, where, passion and motivation are free to flourish and where only nature itself can restrain us.
>
> Those with the passion to change the world sit on one side of a vast and long continent, on the other side are those who want to help them and have the resources to make their vision possible. Giveth is a canal right through the middle of that continent, removing the need to go all the way around and convincing more and more people on both sides to make the journey from the world we live in to the world we believe in.

*   Giveth is a decentralized platform that facilitates better giving and better receiving, contributing to creating a better world
*   Giveth creates increased transparency and allows results based giving for individual donors, in turn inspiring creation of more and more givers and more and more change makers
*   Giveth believes in connecting change makers with those who want to support their mission, allowing them to avoid the mission creep that comes with chasing semi-related funding
*   Giveth believes in decentralized, democratic, liquid control of donor funds
*   Giveth believes in maximizing each gifts potential, utilizing blockchain technology to decrease administrative cost requirements
*   Giveth believes in giving change makers the funds and trust they need to make the change they want to see a reality



> ~[Parker Williams](https://medium.com/u/5d71f4e010d?source=post_page-----19649c57c6aa--------------------------------)

🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗🏗

> Unicorns, previously thought of as being as elusive as they are mysterious and wondrous are in actuality easier to see than one would think and you even possess what it takes to be one. With transparency at the height of their values, however, they are just as easily looked past as they are open with their ability to share and positively impact their world. Hiding in the plain sight of the blockchain forests, these Unicorns believe in a simplicity that allow the moving parts of the world they believe in to glide seamlessly together without the need of a centralized force to guide them. They hope to give the power over sharing and donation out to the very people participating in order to stimulate a positive change of attitude and integrity for the **Decentralized Altruistic Communities** that they are a part of. By using this value system based on participation, innovation, transparency, and accountability the Giveth Unicorns hope to use smart contracts to put donors in charge of how their funds are used, they hope to allow that direct relationship to create a rewarding system for all who are involved so that positivity is felt at the very core of each donation. Giveth Unicorns know that sharing should feel good and that goodness has the ability to shift attitudes of the world for the better, for a more common force toward one another acting accountable and responsible for what they are putting out into the place we’re all a part of.



> **_~Zak Perna_**

👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨👨🏼‍🎨

> Dear Galaxy,
>
> If you’re reading this we’ve done it, all the work the Unicorn troopers fought for was not in vain.
>
> **The mission we set out to accomplish was clear:**
>
> _Create a trustless system of self governing bodies, capable of uniting around causes they choose to support._
>
> _Build a platform that fosters experimentation, collaboration and open source initiatives._
>
> _Awaken the Giver within all the citizen of this Galaxy and beyond, by showing them how and where their contributions make a difference._
>
> The Centralization forces were determined to keep the Galaxy under their control, well we couldn’t let that happen, not for our sake and the sake of generations to come.
>
> To accomplish our mission we had to do something greater than simply unseating the unjust forces.
>
> We had to show them a better way!
>
> **The way of the Unicorn.**
>
> We started a battle that will never end, the fight for truth, justice and transparency between citizens and powers is one that must live on forever.
>
> It’s up to you to keep this fight alive all throughout your Galaxy, to inspire, incite and expose the truth for all to see.
>
> This was the cause we chose to fight for, the one we believed mattered most to our generation.
>
> Now it’s your turn to decide, what will you fight for?
>
> We’ve given you the tools to sculpt your future, to build your community and free yourselves.
>
> Use them wisely and never, EVER…… **Forget!**
>
> **The way of the** [**Unicorn**](https://twitter.com/YalorMewn/status/992864729407291392) ( ͡o ͜ʖ ͡o)



> **_~_**[**_Yalor Tackson_**](https://medium.com/u/33144025168f?source=post_page-----19649c57c6aa--------------------------------)

🌕🌖🌗🌘🌚🌑🌒🌓🌔🌕🌖🌗🌘🌚🌑🌒🌓🌔🌕🌖🌗🌘🌚🌑🌒🌓🌔🌕🌖🌗

> Giveth is a global community focused on improving the world through blockchain technology.
>
> Trustless systems like a distributed ledger allow us to eliminate the middle man, cut down costs and provide transparency and accountability. Our mission at Giveth is to bring this new reality to the world of charitable giving.
>
> Although we recognize the important work performed by NGOs and philantropic institutions around the world, we believe that with blockchain technology we can improve and streamline this process by finally connecting the donor directly to the recipient through on-chain transactions.
>
> This allows for a new level of engagement between givers and makers, between communities and sponsors between the developed and developing worlds.
>
> Giveth is a community of communities. We are building a platform that provides the tools for individuals to get together, organize and fund their own projects.
>
> We value honesty, transparency, freedom and accountability. We believe in the power of people to self-govern for the interest of the community.
>
> Giveth is open to all individuals and communities who wish to build a better future together. Will you join us?



> **_~_**[**_Alan Borger_**](https://medium.com/u/bcecf6e269af?source=post_page-----19649c57c6aa--------------------------------)

🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻🕴🏻

> To help facilitate a greater understanding of emergent technologies
>
> To show the world the power of blockchain and smart contracts to make huge improvements in more than just charitable donations
>
> To help foster new coders into this new ecosystem
>
> To demonstrate the importance of transparency in giving by using our own technology to drive the creation and improvement of our own systems
>
> To remain ever vigilant for problems or threats to the system (both Giveth and the greater Ethereum community), vis-a-vis scammers, bugs or ongoing hacks
>
> Something something Batman costume?


> **_~_**[**_Bowen Sanders_**](https://medium.com/u/64d9a5dda0f8?source=post_page-----19649c57c6aa--------------------------------)

🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇🦇

**Urban dictionary explains a unicorn as: The rare creature who is able to give you the thing you always wanted but thought you you could never have.**

> I feel that is at of the heart of Giveth. So many people from all over the globe are coming together to build a tool that will change the future in ways we thought we could never could; creating impact that was impossible not long ago.
>
> We see past borders, languages and currencies and are building a new way of helping each other without any of these traditional obstacles.
>
> Giveth is for the do-er, the dreamer who desires to see their dream as reality, the heroes, and everyone out there who has a different expression of love.


> **_~LinzeeLouu_**

🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋

> From an aid perspective:
>
> Transparency: A completely transparent process!
>
> \-The ability to influence where your donations get spent!
>
> A great way to utilize new technologies.
>
> A platform that has immense possibilities…
>
> The motto in my head keeps revolving around GivEth — Give ETH — Ethical Giving
>
> For GRACEaid the GivEth ideology aligns with our ethos and look forward to moving together.
>
> Supporting and promoting the ethos of GivEth as well as putting on the forefront of our work important issues like Refugees and destitute people.


> **~**[Andreas Papazidis](https://medium.com/u/91016de0eb58?source=post_page-----19649c57c6aa--------------------------------)

👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼👨🏻‍💼

> Decentralized community where everyone is encouraged to get involved in decision making.
>
> Dissolving the blurred gap between the giver and the receiver.
>
> Our transparency causes everyone in the community to have good working relationships and a higher level of engagement.
>
> Offering coders of any skillset & level to contribute.
>
> Advancing the power and utilization of blockchain through open source code.


> **~Mandala Kitten**

👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤👩🏼‍🎤

There you have it 21 beautiful, thoughtful and truly inspiring visions of Giveth. If you want to find out more or you want to contribute 👇🏼


[**Join our community**](http://join.giveth.io/)**: by tackling interesting issues you can help us positively impact charitable giving forever!**

*   **Join us on** [**Riot or Slack**](http://join.giveth.io/)
*   **Discover our** [**Site**](http://giveth.io/) **and** [**Wiki**](https://wiki.giveth.io/)
*   **Fork our code on** [**Github**](http://github.com/Giveth/)
*   **Follow us on** [**Medium**](http://medium.com/giveth/)**,** [**Facebook**](https://www.facebook.com/givethio)**,** [**Twitter**](http://twitter.com/givethio) **and** [**Reddit**](https://www.reddit.com/r/giveth/)

**Help us Build the Future of Giving: 🚀** [**Donate directly**](http://donate.giveth.io/) **🚀 or** [**buy a Ledger with our affiliate link**](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: futureOfWork
title: "The Future of Work: Distributed Teams & Decentralized Workspaces"
author: Agent Smith
author_image_url: /img/agentSmithAuthor.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

<img alt="Connections" src={useBaseUrl('img/blog/futureOfWork.png')} />

The world is changing at a rapid pace. Gone are the days where you could work 30 years at a company, then get a fancy watch and a golden handshake into retirement. The industrial revolution of the early 1800’s brought more people out of the country and into factories and workshops, attracted by better pay.

And while offices were growing in number back then, it wasn’t until the 20th century that office culture became a mainstream phenomenon. Now with the arrival of the internet and, more recently, blockchain we are seeing another shift in the way people work.

At [**The Bounties Network**](https://medium.com/bounties-network) and [**Giveth Social Coding**](https://riot.im/app/#/room/#giveth-social-coding:matrix.org) we decided to collaborate on this topic. So we recently posed and posted a question about The Future of Work:

> _“If you love your employees let them go, to Thailand, to school, to a sabbatical where ever they might choose. The constraints placed on us today in the working economy are unreasonable and completely unconducive to personal growth, truth, happiness and workplace fulfilment.”_

Today we’re going to integrate some of the responses from [**that post**](https://explorer.bounties.network/bounty/1641) to get a better idea of how the future of work may look like.

Location, Location, Location
============================

The company of the future is no longer bound by company walls or even country borders for that matter. Employers are starting to understand that sourcing the best talent at the right price is more important than where they are located. Poster **Jose Aguinaga** highlights this about his international company:

> _In our company, we are roughly 15+ employees/designers all over the world. We have people from Mexico City to New Zealand, in Vancouver and Sofia. We started in Switzerland, and have embraced a decentralized workspace from day 1._


Many jobs these days only require a laptop and a good internet connection

The internet ushered in the digital economy and a huge percentage of job postings these days are looking for digital skills. The obvious benefit of this is that you can work remotely just about anywhere you have a computer and a decent internet connection.

Jose goes on to explain, however, that remote working is not for everybody. It requires discipline, flexibility, and a sense of responsibility that may not suit everyone’s personality. Some workers are just not cut out for that kind of independence. To be clear, many jobs still require us to be in the same space. But in the future, we will be able to solve many of the problems that come with trying to cram so many people into big cities.

Working in Tune with Your Own Rhythms
=====================================

Let’s expand on that a bit. As many of you will know, working a 9–5 job in a major city can be a real headache. With worldwide populations continuing to grow, it’s not unheard of to hear people spend 2–3 hours every day commuting to work. But now many companies are starting to wake up to the fact that many tasks are not time-specific. Do you really need to be in the office at 9 to respond to client emails for an hour?

In addition, employees are not robots (most anyway) and do not function with on/off switches. Every worker is unique and possesses strengths and weaknesses. People produce their best work at various times of the day. User **Brad** highlighted this in his post with the following words:

> _It has been repeatedly shown that creative and intelligent minds are more likely to be night owls, and unlikely to stay tied down to one place for long periods of time._

Now whether or not that fits your profile is irrelevant. Some people love the early morning hours and take the afternoon off. Some work perfectly in the 9–5 structure. Others, as Brad suggests, work well into the night when the peace and quiet provide plenty of opportunities to get work done.

To add to that, most workers would agree that one of the most important aspects of a job is a healthy working environment. Happy employees are productive workers. Poster **Bount\_Hunter** highlights this well in his/her post:

> _If the person you want to do X job for you is happier to be doing it a 8pm -4 am in Malaysia vs 9–5 in chicago their work will always be better. We’ve all worked jobs we HATE (i’m currently doing that now) and you don’t get the best work from people who are working jobs they don’t like._

Decentralized Autonomous Organizations
======================================

It should come as no surprise then that decentralized organizations are springing up everywhere. And blockchain is pioneering this effort with projects dedicated to making that kind of a future a reality. Take [**Aragon**](https://aragon.org/) for example, a project aimed at breaking down traditional borders and intermediaries.

In the modern world, much of the existing business value is captured by those at the top of the pyramid. It’s a little sad then that many of the people creating that value don’t actually get rewarded for doing so. The workplace of tomorrow will flatten these management structures and allow the value to be distributed more evenly.

Take this very article for example. It was crowd-sourced and funded from contributors around the world using a decentralized application. What could be more empowering than allowing employees to have an active stake and say in the company and process from the get-go?

Closing Thoughts: The Future of Work
====================================

It’s sometimes hard to see a change in the future of work since we’ve been following a centralized hierarchical office model for many years now. The only thing we can be certain of is change. Those that embrace it are usually the ones who reap the most rewards in the new economy.

Finally, to highlight the real-life change we are facing as work evolves, let me tell you a little about my own history. I am a South African who is dating a German who lives in the Netherlands. My mother is Italian and I work part-time for an American company. Borders are completely artificial constructions of man. The human spirit doesn’t want to be tied down by the rules of a few men sitting in an office somewhere. The future of work is exciting. The future of work is decentralized.

Are you ready to join us in the distributed work space? Head on over to [**The Bounties Network**](https://explorer.bounties.network/) and say hello. Or even better, take on a bounty for yourself. We’re not just looking for programmers and computer scientists. We need communication people, project managers, writers, graphic designers, cheerleaders and more!

Dig the concept of crowdsourcing content and/or decentralizing All The Things? Join us in the [**Social Coding chat**](https://riot.im/app/#/room/#giveth-social-coding:matrix.org))  or discover more about the Giveth Galaxy right [here](http://giveth.io)!

*   Join Giveth on [Riot or Slack](http://join.giveth.io)
*   Discover our [site](http://giveth.io/) and [wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: unicornDACexperiment
title: The Unicorn DAC, a Non-hierarchical Decentralized Governance Experiment
author: Lanski
author_image_url: /img/Lanski.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


_Why are bosses necessary? They aren’t. Self-managed organizations exist all over the world, but there is no template for how a decentralized self-managed organization should work. Let us try to change that._

Self-managed organizations (those without a management middlemen layer and hierarchy) have to overcome a lot of hurdles when it comes to governance. For example, on one side, the direction of the organization cannot be dictated top-down by management and on the other side nobody can push responsibility up and “just do what they are told”.

These hurdles, Frederic Laloux, author of “[Reinventing Organizations](http://www.reinventingorganizations.com/)” suggests, exist mainly because traditional management practices and traditionally managed organizations are so prevalent that we have a lack of examples to follow. In other words, we might have never seen better! Moreover, there have been years and years of organizational research and practice on hierarchical structures (think both about an old-age tribe with a clear, visible head and also a large corporation with a twitter rant-prone CEO).

On top of that, we have new models of governance arising within blockchain structures or enabled by blockchain solutions ([here’s](https://medium.com/@leo_pold_b/blockchain-governance-takeaways-from-nine-projects-8a80ad214d15) a pretty good article that touches on some of the key points), although there is not so much literature on specifically non-hierarchical, egalitarian structures.

While there are great companies pushing the envelope in both blockchain governance and self-management, it’s time for us to investigate, explore and document different forms of non-hierarchical governance for organizations. Giveth’s Governance Circle, and particularly [Loie](https://twitter.com/Loie_Low), whose goal is to foster governance experiments, is launching the Unicorn DAC on that regard. Lorelei devoted countless hours to ideate, iterate and bring to life this project with the rest of the Unicorns… and this is the result.

Stepping up the game
--------------------

Operationally, Giveth works much like a swarm. Around a strong core of main contributors, collaborators that are aligned with the purpose of Giveth come and go and offer their time, ideas and work. Some of these collaborators do one assignment and leave and others stay collaborating on the periphery but for the longest time. They are rewarded through a mechanism called [RewardDAO](https://medium.com/giveth/how-rewarddao-works-aka-what-are-points-7388f70269a), with which everyone can get points that then can be exchanged for ether if they upload a video on our [Wall of Fame](https://fame.giveth.io/) or to the [DApp itself](https://beta.giveth.io/campaigns/5b3d9746329bc64ae74d1424).

But these points are awarded somewhat arbitrarily and there’s a limited amount of monthly ether that goes to fund these rewards. Hence, the amount that collaborators receive in ether can vary depending on other people’s contributions and points. We think it’s a great introductory system for getting into the Giveth Galaxy, but might not be ideal as a fully decentralized non-hierarchical governance model. In fact, it’s not really a complete governance model, as it doesn’t necessarily steer Giveth’s big decisions, but our experience tells us that it does motivate people to take initiative, talk to the most committed contributors and suggest new projects and initiatives.

**Put your money where your purpose is**
----------------------------------------

To be clear, governance in self-managed organizations boils down to who decides — and how it is decided — what the organization dedicates its resources to?

So in the case of Giveth, the question was: How could we empower everyone that is fully committed to Giveth to decide what actions and what strategic direction should the organization take? And even further, could we do that in a way that we leverage our own products, i.e. the Giveth DApp? -we do like our #dogfooding!

Well, the Giveth DApp allows Makers to create [DACs, Campaigns and Milestones](https://wiki.giveth.io/dapp/product-definition/), and Givers to fund whatever change they want to see realized in the world. Could we not create a DAC that Unicorns can use to propose projects through Milestones, and other Unicorns can fund them if they think they are aligned with Giveth’s purpose? We would distribute money to our Unicorns — this group of core contributors — and they could fund any Milestone they wanted.

> **What better way to steer an organization than by democratizing both the access to resources and the power to propose actions and then let everyone actually put resources where the Giveth purpose lies the strongest?**

Sometimes Unicorns will decide to fund already existing Milestones, and sometimes they will create a new bounty. This gives everyone the power to suggest a project, give it a price tag, and if the funding target gets reached, empower and pay this person to make it happen. If it doesn’t get funded, it would mean that the project was possibly not so aligned with the general feeling and purpose anyway.

**Examples of funded proposals:**

a) Lorelei is often frustrated by the lack of sharing info in the Ethereum community. Everybody seems to be having the same conversations but no one is hearing each other. When she hears about Tennagraph, the community signaling aggregator to answer just this need, she becomes very passionate about it and decides to use her Unicorn DAC delegation allowance to fund Deam to go to Web3 Summit and raise awareness and adoption for Tennagraph!


b) Lanski has identified a feature for our [DApp](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4) that a bunch of Makers would like to have in the platform. It might not seem it’s a priority from a technical point of view, but as a matter of fact, all the feedback that he is receiving from the users mentions that particular need. He assesses the cost with the DApp team and creates a Milestone where they (the DApp team) are the beneficiary. The work, though, is too expensive and he cannot pay it on his own, but Lorelei realizes how important the feature is and funds the Milestone too so the DApp team can go ahead and build it to claim the Milestone.

**Example of an unsuccessful proposal:**

Lanski wants to make stickers of Giveth’s logo to stick all over the world — for marketing purposes. Everyone has got some stickers left from the last batch, but not enough to cover half of the world with them, so he wants to make MORE. But the general consensus is that we are publicizing well and doing the right outreach in the circles that we want to attract at this stage, so nobody actually funds the Milestone. Sorry Lanski, maybe later when we decide to do a publicity campaign for the general public!

**Ins and outs of the Unicorn DAC**
-----------------------------------

This Governance experiment is precisely that, an experiment. And the initial parameters are sort of arbitrarily defined and will be polished as we go along.

1.  We’ve been a community gathered around shared principles and purpose for a while now, but never had an official onboarding process because there’s no clear entity to be onboarded to. Now, we have the opportunity to come together around these agreements and create a membrane that gathers and recognizes the most committed of us as we join the Unicorn DAC. You can read about our Onboarding Process [here](https://wiki.giveth.io/governance/unicorn-dac/unicorn-onboarding/), which ensures commitment to Giveth’s purpose and alignment with our principles in order to opt to be part of the DAC.
2.  The resource allowance per head will be the equivalent in ether to 600 USD every week. In order for people not to fund only their own Milestones, we have capped the amount people can put into their own Milestones at 150 USD, so 450 will be used to decide on other people’s initiatives. Unicorns don’t have to use the full 600 USD every week if they feel that there are no interesting projects to fund, or the ones that are truly interesting are already fully funded.
3.  Needless to say, people can choose NOT to fund any of their own Milestones. The reason why we allow people to self-fund their Milestones for a certain amount is to facilitate the funding of menial or uninteresting jobs that have to be done, but they would waste people’s time and resources if they had to be reviewed and funded by other unicorns.
4.  We cannot expect people to feel connected to a purpose by only chipping money into Milestones. Hence, in order to keep purpose alive, we have a once a month Unicorn Meeting! Here, we discuss which projects we delegated to and why it is aligned to Giveth.
5.  As a rule of thumb, Milestones will be created by those who hold roles related to the matter at hand. That’s not to say that people can’t have great ideas outside of their roles, but they should follow the [advice process](https://wiki.giveth.io/governance/advice-process/) and certainly consult with those who hold relevant roles before taking action, even if it is merely for keeping information flows going. Roles are evaluated on how well they have been fulfilled in a peer review system every month.

**MVPing our way through it**
-----------------------------

We are ready to try the Unicorn DAC and carve our own way in decentralized governance practices. As the experiment that it is, we do expect some issues to come up, and we have already identified a few:

1.  [Dogfooding](https://en.wikipedia.org/wiki/Eating_your_own_dog_food) is our motto because we believe the Giveth DApp is a great tool. Nevertheless, it does not yet have the advanced functionalities of a compounded delegation system that would allow you to allocate only up to a percentage of funds into your own Milestones and the rest to others. We will track donations manually at this point while we look for a solution, be it homemade or leveraging [Aragon](https://aragon.org/).
2.  Foreign influence. Our DAC will always be public, transparent and held to the highest standards, but the fact that it’s an open way to fund the projects that Giveth undertakes, it could be exposed to an admittedly unlikely vector of attack where a powerful party decides to fund specific Milestones or projects that are on the periphery of the purpose and this acts in detriment of the best direction to take. This would be a similar attack to sovereignty to the [IMF dictating policies to countries](https://www.sciencedirect.com/science/article/pii/S0161893815001003) in exchange for bailouts or access to concessional loans.
3.  That said, we have funds to support this initiative for a limited period of time, and since Giveth is a non-profit blockchain entity that accepts donations, if you are a donor and **want to support Blockchain4Good projects PLUS a decentralized non-hierarchical governance experiment like the Unicorn DAC**, we are all ears (and eyes!): hit us up on [Riot](https://riot.im/app/#/group/+giveth:matrix.org) or [Twitter](https://twitter.com/Givethio) or fund us [directly](https://giveth.io/donate/)!

**Already winning**
-------------------

The Unicorn DAC was presented during DevCon4 at the [Aragon Dream DAO contest](https://blog.aragon.org/devcon4-recap/)… and it won the runner-up prize! 250 ANT + 250 DAI for making it a reality! Aragon and Giveth (and the Unicorn DAC in particular) share the basic principles of decentralization and non-hierarchicality. We see Aragon as the perfect tool to facilitate and enable this governance experiment.

Have a look at Lorelei pitching at minute 58:15 below!

<iframe width="560" height="315" src="https://www.youtube.com/embed/ewL9ZvFeaHU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

#winning

**But… why?**
-------------

It is worth reproducing a conversation I had with Lorelei on the reason to spend money and effort trying to devise and implement untested ways of governance:

> “Is it appropriate to answer this question with a meme?

<img alt="Santa Gives Unicorns" src={useBaseUrl("img/blog/santaMemeUnicornDAC.jpeg")} />

> Ha, but in all seriousness, the Unicorn DAC takes these decentralization experiments within. Any good mission reaches as far out into the world as it does into its creator, which in this case is us, the Ethereum community. We can yab about decentralization of power all day while at home we still have one or a privileged few making the influential calls on how money is spent, and this DAC offers a solution to that.”

We are launching this experiment to change how the world looks at self-management. We believe there are more human ways to interact and organize than the rigid, sometimes alienating structures of today.

Come join our dialog in our [Riot](http://join.giveth.io/) or share your ideas below — they will be read and discussed! Participate and join us in the revolution of management!

Enter the Unicorn DAC.
======================

*   Join us on [Riot or Slack](http://join.giveth.io/)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

_The Giveth DAC — the community working on the_ [_DApp_](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4) _and many other projects — is funded through our Donation Application._ **_We ourselves depend on you, on Givers_**_: the people out there who believe a tool like this should be a reality, individuals who want to help us to make the World a Better Place. If you want to_ **_be one of our favorite Unicorns, go to_** [**_donate.giveth.io_**](http://donate.giveth.io/) **_and claim your space on our leaderboard_**_, donate directly in the DApp (right_ [_here_](https://beta.giveth.io/dacs/5b37da13a239ac21b383d4da)_) or come talk to_ [_Griff or Kris on Riot_](https://giveth.io/join/)_, and tell us how you’d like to contribute._ ❤
---
slug: realigningIncentives
title: The Future of Giving is Realigning Incentives
author: Kris
author_image_url: /img/krisAuthor.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

<img alt="All hands on for Giveth" src={useBaseUrl('img/blog/givethHands.png')} />

> A Trade leaves things as they were, with no external Surplus. A Gift creates a Surplus as it spreads. _~ Seth Godin_

Giveth is exploring new territories and expanding its horizons: we are embarking on an exciting mission to enrich the Giveth Donation Application by **making the core part of it, the donations, more sustainable**. From enabling Givers to donate to the causes they believe in and providing a layer of [transparency and accountability](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4) through our [DApp](https://wiki.giveth.io/dapp), we will now be tackling the sustainability of the donation process itself. **We want to create continuous streams of funding through the creation of economies around causes**, by building a system of [token bonding curves](https://blog.goodaudience.com/rewriting-the-story-of-human-collaboration-c33a8a4cd5b8) feeding cause-focused DAOs (with a unique governance model) on top of the Giveth DApp, in a collaboration with [BlockScience](https://block.science/).

_Edit May 2019: for more on the Commons Stack initiative, read_ [_this most recent update_](https://medium.com/commonsstack/the-commons-stack-scaling-the-commons-to-re-prioritize-people-and-the-planet-e1293123831d) _by_ [_Jeff Emmett_](https://medium.com/u/ae6d20c4931e?source=post_page-----ac265e3010b8--------------------------------)_, for a technical deepdive by_ [_Abbey Titcomb_](https://medium.com/u/5967a5d3b611?source=post_page-----ac265e3010b8--------------------------------) _go_ [_here_](https://medium.com/commonsstack/deep-dive-augmented-bonding-curves-b5ca4fad4436)_._

**_From centralized Donations to sustainable Collaborations_**
--------------------------------------------------------------

If you have been following Giveth closely, you will know by now that we are not your regular organization and are constantly changing our own collaboration models through many experiments, and that we are involved in [many](https://medium.com/giveth/giveth-partners-with-alibre-io-for-last-mile-solution-in-mexico-50c5155dfcd5), [many](https://medium.com/giveth/the-unicorndac-a-non-hierarchical-decentralized-governance-experiment-8dfbe6e98d19) [initiatives](https://medium.com/aragon-dac/aragon-dac-a-new-community-effort-to-foster-aragons-development-led-by-giveth-2228dcc17b63), seemingly not moving in just one specific direction, but actually, we are! **We are a Decentralized Altruistic Community (DAC) focused on making the World a Better Place** through the use of blockchain technology, and yes, this is a wide and ambitious [mission](https://wiki.giveth.io/dac/mission/). But we have a path we are on, well, actually we have several, and we are doing this on purpose, to make us more resilient, even antifragile. The Ethereum community and the blockchain space as a whole is in constant flux, so we are working on and supporting a wide array of different initiatives (we call it the [Giveth Galaxy](https://giveth.io/#galaxy)) that we believe are bringing lasting value to the wider community.

During this cryptowinter, we ourselves, as a non-profit blockchain-based entity, have been struggling quite a bit to keep financially afloat and have only been able to do this through a generous donation by [an anonymous donor](https://medium.com/giveth/surprise-285-eth-anonymous-donation-given-to-giveth-9167266a5085), but mostly through a constant stream of [personal donations by our co-founder Griff Green](https://beta.giveth.io/dacs/5b37da13a239ac21b383d4da), for which we are eternally grateful. This scarcity however got us to discuss our own sustainability quite a bit, and the importance of good, objective governance that will benefit our individual and collective interests, our ‘Commons’. **Depending on pure goodwill, even if it happens in a transparent and accountable way, is not sustainable**, not for us nor for any other altruistic community: it puts you in a scarcity mindset and is a heavy distraction from the cause(s) that unite you. This concern made us see more clearly than ever that we have to invest time in bringing Giving to the next level, and change the way humans collaborate.

**_1–2–3 — Infinity._**
-----------------------

First things first, we are very happy and proud to say that **our flagship project, the Giveth DApp,** [**currently in beta**](https://wiki.giveth.io/dapp/)**, is now** [feature-complete](https://medium.com/giveth/whats-dappening-0x5-ultra-configurable-milestones-27ff92383de2)**,** bringing us very close to what we could call ‘Giveth 1.0’. This of course does not mean that we will stop working on the DApp, on the contrary, much more is coming, such as deploying our DApp on the [xDAI chain](https://medium.com/poa-network/poa-network-partners-with-makerdao-on-xdai-chain-the-first-ever-usd-stable-blockchain-65a078c41e6a), introducing governance solutions through [Aragon](http://aragon.org), a complete UX overhaul and so much more. This is all in the making but in order to continue with this, we are currently focusing very hard on the funding part of the puzzle**.** We want to help forward the ecosystem itself through an ambitious token-engineering experiment, in collaboration with [BlockScience](https://block.science/). **The target of this experiment is to transform communities around altruistic causes into entire economies and to build this on top of the Giveth DApp.** In the coming months, we will be working hard on this initiative that will bring us at some point to what we like to call ‘Giveth 2.0’.

Now that we have traceable donations working in the DApp, we can start to experiment with new models to support both the organization as well as the funding of communities. Your support stays very, very welcome ([all tokens accepted](http://giveth.io/donate) 🙏) but in the long run, we want to incentivize you so that you are no longer just a Giver, but have a real stake in the success of the community you will be supporting: **we want to align the very human behavior of profit-seeking with socially beneficial behavior: to us this is the real Future of Giving**.

We built the foundational layer of our Giveth DApp on the Ethereum blockchain and not on a centralized server to bring **true accountability and transparency to decentralized governance experiments**: there is an immutable piece of evidence of what happened with your funds. The true magic however, that will allow us to create sustainable streams of funding, lies hidden within the existing dynamics of blockchain technology. **Every blockchain network in existence has aligned incentives around supporting the network itself: every ‘actor’ in the system, when acting in their own best interest, actually benefits the system.** Miners earn inflation for supporting the network, developers hold the token hoping their efforts will raise its value, and users buy the token creating demand and pay transaction fees: it is a very simple and well-balanced ecosystem: **helping yourself, helps the system to thrive, and very often it doesn’t even matter whether that system is useful or not.**

We are building the Future Of Giving and are fascinated by these mechanisms, we want to use these self-sustaining models for actual good. **The ‘Commons’** can be [defined](https://en.wikipedia.org/wiki/Commons) as “\[…\] resources that groups of people (communities, user groups) manage **for individual and collective benefit**.” We, and many communities like ours, that are organized around social impact causes, are suffering from scarcity, because **we think about the collective benefit and ignore the individual,** who needs to survive as well; this is unsustainable. By default, people will actually do the opposite and take their individual interest over that of the common good, which is often called the [tragedy of the commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons). In **both cases**, there is a major incentive alignment issue: either the individual gains but the collective suffers or the other way around. Witnessing for a while now these emerging, more sustainable systems, we believe it is time for the next step. By modeling the success of existing blockchain ecosystems (through the implementation of new cryptoeconomic primitives) we want **to create abundance to support the Commons**, thinking about both the collective as well as the individual interests.

Now, our goal at Giveth is to use token engineering, more specifically, Curation Markets, to bring this from a purely digital realm, into the real world. We will build it on top of our Dapp, and **build it in such a way that it supports projects that benefit our common interest**, or in other words, that will enable us to sustainably crowdfund the Commons. The initial work was to enable transparent and accountable donations on the blockchain, the next step is to move away from ‘donating’ altogether and to create a sustainable system: **gifted funds become backed by a token of value in a circular economy.** As [Abbey Titcomb](https://medium.com/@abbey_titcomb/crowdfunding-the-commons-d590238d8c3c) says:

> “We believe the answer to the underfunding of social goods and underserved community contribution is to reframe social goods as self-governing and continuously funded commons.”

**Wait but How?**
-----------------

Through building the augmented bonding curve model created by [BlockScience](https://block.science/) on top of our DApp we want to create continuously funded organizations. How does this work? We first learned about them through [a post](https://blog.goodaudience.com/rewriting-the-story-of-human-collaboration-c33a8a4cd5b8) by [Jeff Emmett](https://twitter.com/jeffemmett), a Giveth collaborator, who explains the basic building blocks — a highly recommended read to learn more on how token bonding curves could enable a project to bootstrap funding and token value along with project success and popularity. You can find more references in Abbey Titcomb’s report on [what we built at ETHDenver](https://medium.com/@abbey_titcomb/crowdfunding-the-commons-d590238d8c3c), and for all [technical definitions](https://medium.com/@michaelzargham/jargon-party-e3616cd16a9) and [more theory](https://medium.com/block-science/on-the-practice-of-token-engineering-part-i-c2cc2434e727), we refer you to [Michael Zargham](https://medium.com/@michaelzargham).


However, we would like to illustrate the theory now through a real life example of how this could work, imagining a future in which Giveth has already built this model into its DApp (also available [in video format, narrated by Griff Green](https://youtu.be/WJ23oQpooG0?t=694)):

So imagine you live by the beach, and you have the habit of picking up trash regularly, but you see this is just not having the impact you desire: it doesn’t scale. For more impact you are also regularly donating to a nonprofit promising exactly this, large-scale impact but … all you see is a lot of marketing and a continuous request for more funds. This is all very frustrating.

At this point in time, you run into Jonathan, an activist who you often saw on the beach doing exactly what you do: cleaning up. He tells you about a new kid on the block: the ‘TrashHeroes’ and they are offering you something else. They invite you to not just give money but to actually help them steer the organization. In return for an amount you choose you will receive tokens, tokens that allow you to make decisions for the common good of the organization. On top of this, if you do a good job and the organization runs smoothly one day those tokens could be worth more than what you donated. This sounds too good to be true, but hey, you were donating funds anyways and with this one you get a say in the decisions!

So you give 10 xDAI ([a representation of DAI token](https://medium.com/poa-network/poa-network-partners-with-makerdao-on-xdai-chain-the-first-ever-usd-stable-blockchain-65a078c41e6a)) and receive TrashHero Tokens, which you hear actually have value, in the real world. **The value however, is not determined by an open market, but by a smart contract**, which is actually the token bonding curve. So how does this work you ask? The price, the value of the TrashHero Token, is determined by the total supply of the token in general: if more people mint the token in return for xDAI, the price of the TrashHero Token goes up. If the supply goes down — when people burn their tokens and take money out of the contract the price of the token goes down. **The big difference however with existing curve models, and which makes this one sustainable is two-fold.** First, there is **the curve itself** which disincentivizes people who get in late to burn their tokens quickly, they need to keep these for a while if they want to make a profit. The second element is that people who get in early should be the people who are in it for the long haul, because they are the believers in the cause, they will most often be the experts. This is stimulated by preventing our pioneers from burning their tokens immediately: **their tokens are locked until specific goals** (which we call Milestones in our DApp) have been reached. In this way the collective interests you are fighting for are protected by default, the Commons needs those funds and outweigh your short-term self-interest, and you are incentivized to reach the set goals, the Milestones. **This innovative system where everyone acts in their own self-interest, propels the Commons forward and pushes it to reach its set goals.**


Back to our TrashHeroes that have invited you to be part of this initial group of experts who together have raised quite some xDAI to initialize the curve and the TrashHero Commons. One half, 50% of this xDAI, is locked in the smart contract, 50% of this xDAI is given to a DAO controlled by the TrashHero token holders to execute on their common interest, now baptized the TrashHero Commons. **This Commons that supports the cause of cleaning up the beaches will now need to come up with good proposals to actually support this cause. As the Commons spends money, the tokens that were given to the group that initialized the curve will become unlocked periodically.** This spending goes through Milestones you help create in the Giveth DApp: xDAI will be released once the initiative takers (the ‘Milestone Managers’) prove they have actually reached the goals they set that support the Commons’ cause (i.e. cleaning up beaches) — this is where the power of Giveth kicks in: **you only get rewarded when you are being accountable**.

The effective working of the TrashHero Commons is steered through a novel type of curation market governance system that allows you to use your TrashHero Tokens to signal priorities of tasks (Milestones) to be executed for the Commons to reach its goals. When a target that supports the goals of the Commons is proposed — for example, you get 15 friends together and make a Milestone for doing a side-by-side, step-by-step cleaning of 5 km of coast — and if it is supported by the TrashHero Token holders, it will receive funding from the Commons: xDAI will be sent to the Giveth Milestone. Then once the task has been completed, by documenting in pictures and videos the gathering of 3 tons of plastic and waste, the xDAI will be sent to the token bonding curve and you will be minted TrashHero Tokens, which you can then decide to burn immediately (without a need to speculate if you don’t want to) to receive your xDAI. When you or anyone else decides to burn your tokens, there is a fee that goes back into the Commons, which is the lever that will support more social good. **To us, this is the Future of Giving**: your socially beneficial behavior creates a surplus!

<iframe width="560" height="315" src="https://www.youtube.com/embed/WJ23oQpooG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

##### _Griff Green’s talk at EthCC Paris on the evolutionary movement of human collaboration through blockchain (TrashHero Commons example starts at_ [_10:55_](https://youtu.be/WJ23oQpooG0?t=655)_)_

**Generosity generates Income**
-------------------------------

Doing good _feels_ good, and we hope our alternative economic system will attract more people who want to do good by not just giving but by staying involved. **Instead of just simply donating, they get the opportunity to participate in a circular economy that supports the underlying cause**. As more people will be encouraged to join the Commons, it incentivizes the people who initialized the curve to do even better, as the initial token holder’s funds will only be unlocked as the community actually does good, and spends the money. **By being generous and by participating in good governance they can generate an actual financial return, an income — they create abundance.**

Next to this, speculators will get involved, because that is what happens with tokens, and actually, its great! Secondary markets and the trading volume will hopefully create an extra flow of funds that isn’t normally part of a charitable community. **After the initialization of the curve, the new donations create tokens that have no locking period, and 100% of those funds go straight into the bonding curve.** When later participants burn their tokens they however always pay a fee, and this fee goes back into the Commons, which further support its goals. Every participant — whether it is an initial crowdfunder, a regular Giver or a speculator — should and will act in their own self-interest, which is steering the Commons to become a success, with everyone’s incentives aligned.


**One more important note: this is a giant experiment and it may not work.** However because of the use of the Giveth DApp the projects that are looking to clean up beaches, help the homeless or do research to cure Alzheimer are insulated from the governance experiment’s failure. **The benefit is that these initiatives will exist on our Giveth DApp, so there are multiple ways to fund them.** If a token holder really wants a specific Giveth Milestone to be supported but the governance of the Commons breaks down for one reason or another, they can burn their token (again helping the economy through a small fee), receive xDAI, and send it directly to the specific Milestone on the DApp they wanted to support. The Commons is one actor in an open system. What we will have done is create an extra way to fund projects on our DApp and most probably generate quite some buzz around that specific economy, a buzz supported both by the community as well as by speculators. Whatever happens, more people will know that this cause needs to be supported.

**We started Building this Future of Giving Yesterday**
-------------------------------------------------------

With every statement we make, new questions come up (for example [this dialogue in our chat](https://riot.im/app/#/room/!vwFGsktMNkdorFWJRi:matrix.org/$1552247327760014NjKKA:matrix.org?via=matrix.org&via=giveth.io&via=status.im)), and we do not have all the answers just yet. The models we use are however based on years of research by BlockScience, and are being refined and further documented by the team led by [Michael Zargham](https://twitter.com/mzargham) with whom we are in a constant dialogue. To put this theory to the test, we wanted to build this yesterday, so that’s what we are doing. With the very limited funds we have available, **we have decided to kickstart this project by addressing the wisdom and skills of the very core for whom we are building this: the Crowd, the Commons, You.** We will build and hack this together with you, and we have already started doing this successfully. At ETHDenver we supported the Pactful Team, where we won the Impact Track [by building a proof-of-concept user interface](https://medium.com/@abbey_titcomb/crowdfunding-the-commons-d590238d8c3c) for our idea. We continued at [EthParis](https://twitter.com/Givethio/status/1101583428506583040) and are **now ramping up to build various components that will all tie into a working whole during** [**Odyssey**](https://www.odyssey.org/) in the Netherlands, the biggest AI & Blockchain Hackathon in the world. We are the largest group participating and have been accepted with five teams, working on four of the hackathon’s tracks gathering a multi-talented team of 30+ people. We are uniting developers from many different projects in the Ethereum space to form a Commons and help us build this Future of Giving, together.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GymkCSdm778" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

##### Abbey Titcomb with the Pactful Team, who won the Impact Track at ETHDenver

More is coming very soon but in the meantime you can **catch up** by watching Griff Green’s [EthCC talk](https://www.youtube.com/watch?v=WJ23oQpooG0&feature=youtu.be&t=20), read Abbey Titcomb’s [ETHDenver update](https://medium.com/@abbey_titcomb/crowdfunding-the-commons-d590238d8c3c), scrutinize the [models at BlockScience](https://medium.com/block-science/on-the-practice-of-token-engineering-part-i-c2cc2434e727), and keep yourself up-to-date by following us on [Twitter](http://twitter.com/givethio). Next to this we are actively looking for **more developers** to help us build at future hackathons (such as [ETHCapeTown](https://ethcapetown.com)) and beyond, so please come join our community via [the Social Coding chat](https://riot.im/app/#/room/!kUeYRcrXObgGoJlFjn:matrix.org?via=matrix.org&via=giveth.io&via=status.im) and signal your interest.

We hope you will join us on an adventure that has already started and is expanding our Giveth Galaxy, and [**invite you**](https://riot.im/app/#/room/!kUeYRcrXObgGoJlFjn:matrix.org?via=matrix.org&via=giveth.io&via=status.im) **to be an active participant in this primordial Ethereum and Giveth-powered Commons that is Building The Future Of Giving**. [Join us Today](https://riot.im/app/#/room/!kUeYRcrXObgGoJlFjn:matrix.org?via=matrix.org&via=giveth.io&via=status.im).

Warm regards,

[Giveth](http://giveth.io)

*   Join us on [Riot or Slack](http://join.giveth.io)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: howToDocs    
title: How to contribute to documentation
author: geleeroyale
author_title: Giveth
author_url: https://github.com/geleeroyale
author_image_url: https://avatars1.githubusercontent.com/u/317685?s=460&u=cad937f322db29d6ade49956c8d7d289a583fa9c&v=4
tags: [how-to, documentation]
---

import useBaseUrl from '@docusaurus/useBaseUrl'

Hello dear contributor!

It is very easy to contribute to our new Giveth documentation website. We use [docusaurus v2](https://v2.docusaurus.io), so you can also refer to their documentation, especially for advanced changes.

However - here are the simple ways to contribute:

## Change something in a page

<img
  alt="Editing a page"
  src={useBaseUrl('img/content/screenshot-edit-page.png')}
/>;

`Click` on the *Edit page* link at the bottom of any entry.

## Add an image

If your content needs an image, you should place it in this folder: `static/img/content`

For relative links you should also import the `useBaseUrl` hook from @docusaurus/useBaseUrl - place it immediately after your *front matter*.

```js
import useBaseUrl from '@docusaurus/useBaseUrl'
```

Then you can import the image - i.e. the image I used above to demonstrate the look of the edit link:

```js
<img
  alt="Editing a page"
  src={useBaseUrl('img/content/screenshot-edit-page.png')}
/>;
```

## Make a new page

In order for this to work nicely, please fork and clone from our main repository on github and make a pull request after you have made your changes.

Docusaurus will automatically create new pages from any added markdown (`.md`) files with the correct frontmatter (look at current pages to get an example).

So to create a new page, you should create a new markdown document, depending on the type of content.

- User guides should be created in the `guides` folder
- Developer documentation should be created in the `docs` folder
- Updates, content that does not easily fit other categories, as well as longer entries should go into the `blog` folder

If you want the entry to show up in the respective sidebar you will need to add the title to the existing array:

- `sidebars.js` for the docs section
- `sidebarsGuides.js` for the guides section
 No newline at end of file
---
slug: futureofGiving
title: The Future of Giving is Here
author: Lauren
author_title: Blockchain DAbbler and Heart-Centered Jack of All Trades
author_image_url: /img/laurenAuthor.png
image: /img/blog/futureofGivingimg1.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

<iframe width="720" height="405" src="https://www.youtube.com/embed/ASv420Vf3F8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

We are very excited to announce the launch of Giveth at [giveth.io](https://giveth.io/) — a free, open-source donation application for community philanthropy featuring an all-new UI/UX.


<img alt=""  src={useBaseUrl('img/blog/futureofGivingimg1.png')} width="575" height="auto" />

###### Photo by [Giveth](https://giveth.io/)

Giveth is known for being radically transparent, community-owned and community-driven. Our flagship DApp (live for 3 years at beta.giveth.io) is now being rebranded as “Giveth TRACE”. Giveth TRACE offers a platform for peer-to-peer donations on the blockchain with detailed traceability for “Givers” and mutual aid projects. However, it does require some knowledge of Ethereum and wallet management.

**_With the new Giveth, project owners anywhere in the world can publish an online profile and start accepting donations within minutes._**

<img alt=""  src={useBaseUrl('img/blog/futureofGivingmeme1.jpeg')} width="500" height="auto" />

###### Image Credit: Grandma Finds the Internet via [imgflip](https://imgflip.com/)

<img alt="" class="leftfloat"  src={useBaseUrl('img/blog/futureofGivingSignIn.png')} width="375" height="auto"  />

###### Screenshot taken from [Giveth](https://giveth.io/)

Both Torus and MetaMask wallets are fully integrated into the DApp, meaning that a blockchain newbie can create a wallet with Torus by signing in via social media as easily as the crypto-savvy can sign in with their MetaMask browser extension. Torus integration also means that Giveth is compatible with mobile and a wide range of desktop browsers.

Once logged in, a “Maker” can follow the highly intuitive step-by-step project creation flow and begin raising funds in crypto right away with zero fees added by Giveth.

**_100% of every donation goes directly to the project. This way, together, we can make the world a better place._**

<img alt=""  src={useBaseUrl('img/blog/futureofGivingmeme2.jpeg')} width="500" height="auto" />

###### Image Credit: Imagination Spongebob via [imgflip](https://imgflip.com/)

We have really made it easy for you to give to the regenerative projects you love! Anyone can become a Giver simply by clicking donate and connecting to their preferred wallet.  New to crypto? No worries! Torus integration makes it possible for you to top-up your crypto wallet easily with fiat.

For all Givers, to save and track your donations you need only to sign in with Torus or MetaMask and all that you give will be visible in your account. Your generosity shall be forever immortalized transparently on the Ethereum blockchain!

<img alt=""  src={useBaseUrl('img/blog/futureofGivingGiver.png')} width="auto" height="auto" />

###### Screenshot taken from [Giveth](https://giveth.io/)

**_At Giveth we are committed to building the future of giving based on feedback from you, our community._**

In the next months as we continue to hone the user experience and squash any bugs we encounter while on-boarding new projects, we want to hear what we can do better to make Giveth the best user-friendly DApp for peer-to-peer donations.

So head over to [giveth.io](http://giveth.io), try it out for yourself, and let us know what you think!

## Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: flavorsOfGiveth
title: Two Flavors of Giveth.. Which One to Choose?
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/twoFlavoursBanner.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

<img alt=""  src={useBaseUrl('img/blog/givethsSIDEbySIDE.png')} width="700" height="auto" />

###### Giveth TRACE and Giveth.io landing pages

A new DApp for Giveth has launched! WOW! Much Excite! The pre-existing Giveth henceforth will be known as Giveth TRACE. The [new Giveth.io Donation Application](https://giveth.io/) is an important continuation of our mission to build the future of giving. Both iterations will continue to exist and do contain different features. In this article we’ll be diving into the nitty gritty to help you decide which version of Giveth will aid you the most on your philanthropic venture.

<a href="#summary">TL;DR</a> ←
----------------

Three key distinguishers of the Giveths are: **_Trust_**, **_User Experience,_** and **_Scope_**. Let’s dive in.

**_Trust_**
===========

First up let’s talk about Trust. Giveth TRACE (Originally Giveth Beta) was launched in 2017. Following [the great DAO hack](https://www.gemini.com/cryptopedia/the-dao-hack-makerdao) from the previous year, the burning question at the time was: how do we make these new decentralized innovations resilient and trustworthy? Giveth itself was on the frontlines of these events and set out to solve these issues.

Giveth TRACE employs smart contracts to handle various transparency-oriented functions of the platform. These interactions happen on the blockchain, including traceable donations, escrow, and dispersal of funds. It uses Milestones for specific projects or goals that can have conditions outlined for funds to be released. An example would be to prove work was done on a project or that money was spent to acquire something specific. The milestone contract is employed to act as an escrow. A milestone creator can designate a recipient other than themselves and also a reviewer. The reviewer of a milestone is responsible to assure that any stated expectations were completed before authorizing the smart contract to release the funds to the recipient.

The new Giveth DApp does not use smart contracts to facilitate donations but instead provides a true peer-to-peer experience where funds go directly from donor to receiver. The resulting transaction is eternally scribed onto the blockchain. There are no escrow or reviewer functions on the Giveth.io DApp so while donations are much more direct, you are encouraged to do your due diligence before donating.

**_User Experience_**
=====================

Following the rise of ‘cryptokitties’ and the mooning of the price of ETH in 2018, the Rinkeby test network was implemented on Giveth TRACE to resolve absurd gas fees and scalability issues. This allows users to interact with smart contracts on the Dapp for no actual fees, using only gas on Rinkeby to execute the majority of contract transactions. In fact, Giveth actually pays the fees to send your donations to mainnet.

<img alt="" class="leftfloat"  src={useBaseUrl('img/blog/cryptokitties.png')} width="450" height="auto" />

**_“The Rise and Fall of Ethereum circa 2018 AD”_**
###### Image Source: medium.com

Profile creation on Giveth TRACE is facilitated by smart contract interactions on Rinkeby and is reasonably straightforward, however is currently limited to MetaMask. Giveth TRACE currently allows donations in ETH, DAI, PAN, WBTC and USDC.

Giveth.io has expanded giving capabilities by allowing donations in ETH and any ERC-20 Token on Mainnet and [**xDai network**](https://www.xdaichain.com/)! The [Giveth.io DApp](https://giveth.io/) uses Onboard.js to permit virtually any Ethereum wallet to be used for donations. Project creation has been streamlined, so creators can sign-in, make a project and start collecting funds literally in minutes. For creating a profile you may choose between standard MetaMask login or Torus Wallet. Torus Wallet also provides a crypto on-ramping feature so you can convert your cold-hard cash into cryptocurrency very easily and get to donating in the digital age. [More Info on Torus wallet can be found here.](https://docs.tor.us/)

**_Scope_**
===========

Scope  is the last, but perhaps coolest, distinction I want to mention. Giveth TRACE has **huge** scope: its donation hierarchy is broken down into Communities (formerly known as DACs), Campaigns, and Milestones. Donations made to Communities and Campaigns are stored in a ‘pledge’ vault. The Community or Campaign manager can then delegate your pledge into the Campaign or Milestone, respectively, of their choosing. This system created by Giveth has coined the term ‘Liquid Pledging’ and in effect allows for curated donor funds. This means would-be donors can make non-custodial contributions to causes that they care about and funds can find their way to the right place at the right time. Once your funds have been delegated you’re able to track where they went on Giveth TRACE.

Giveth.io Dapp aims to provide a simpler experience. While not achieving the same scope of Giveth TRACE it is much easier to navigate. Donations made on Giveth.io go straight A → B and the project owners themselves dictate the scope by the projects they choose to create.

<span id="summary">**_To Summarize:_**</span>
===================

_Giveth TRACE_
--------------

*   Allows for donations on macro and micro levels via Communities, Campaigns, and Milestones
*   Has a system of oversight to prevent misuse or fraud
*   Donations accepted in ETH, DAI, PAN, WBTC, and USDC
*   Curated Donor Funds via ‘Liquid Pledging’
*   Giveth doesn’t charge any fees, in fact we pay the fees to send funds to the recipient
*   Works with MetaMask

Giveth.io
---------

*   Streamlined project creation accessible for all
*   Multi-wallet functionality
*   Peer-to-peer transactions
*   Giveth doesn’t charge any fees
*   Fiat donations via Torus On-ramping
*   ETH and ERC-20 token donations
*   Donate on **xDai** and save on gas

The new Giveth is straightforward if you’re looking to make simple donations peer to peer without any added complexity but with more connectivity. Giveth TRACE allows you to define how broad or narrow your donations are while maintaining a high standard of transparency and checks on fund flow. Each has specific advantages in terms of collecting donations. Check out both and decide which flavor suits your taste; [Giveth TRACE](https://beta.giveth.io/) or [Giveth.io](https://giveth.io/).

## Want to get more involved?


*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: whatDappened1
title: "What DAppened: March 17–31"
author: Lauren
author_title: Blockchain DAbbler and Heart-Centered Jack of All Trades
author_image_url: /img/laurenAuthor.png
image: img/blog/whatsDappening1Meme.gif
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


_Hello friends and fans of Giveth! This is one part of a series of short transparency posts where we keep you in the loop with updates on what’s in development for_ [_giveth.io_](http://giveth.io)_._

Our new DApp [went live](2021-03-24-futureofGiving.md) at [giveth.io](https://giveth.io/) on March 24, 2021, and since then we got some great feedback from our testers and community, and we’ve been hard at work fixing bugs and adding new features.

First, we addressed the issue of gas fees not being calculated correctly, added an informative banner, and enabled users to login directly on xDai chain. We disabled the ability of a project creator to use a contract address for their project so that donations to all projects can be done either on Mainnet or xDai. We also added more tokens to our list in order to allow the Giver to donate with even more flexibility!

We onboarded a new member into our dev team and thanks to him we now have functional automated testing that allows us to make changes to the DApp in development and then push to our testing site with greater confidence.

Next we tackled a bigger fish: the development and implementation of a quality score, sorting/filtering method, and search function to add greater flow and organization to the projects page.

<img alt="Magic Sorting" class="leftfloat" src={useBaseUrl('img/blog/whatsDappening1Meme.gif')} width="375" height="auto" />

Now the projects are sorted by default using a “quality score” — a combination of number of likes, number of donations and quality of project description. We have also added the ability for the user to filter projects by category, and to change the sorting method from the default to “number of likes” or “amount raised”.


Lastly, you are now able to use the search bar to quickly and easily find the exact project you want to view or Give to!

<img alt="Filter and Sort on Giveth.io" src={useBaseUrl('img/blog/whatsDappening1img1.png')} width="800" height="auto" />

###### “Filter by Category”, “Sort By” and “Search Projects” Features on [Giveth.io](https://giveth.io/)

Another exciting update is that we’re now using [Segment](https://segment.com/) analytics and [Autopilot](https://www.autopilothq.com/) to track activity on the DApp and send appropriate corresponding notifications. We also worked on some internal organization in our [Discord server](https://discord.com/invite/JftjK8Un3z) that enables us to receive notifications so we can monitor site actions (such as new project creation, new donation, etc.) in-house.

In the next sprint we’re excited to continue with QA by getting email notifications working smoothly and ensuring that the donation amount (at time of donation) is being calculated and added to the database correctly. We also plan to add rich text formatting to the project creation flow, and enable the Maker to add videos and/or images to their project description. Furthermore, we are now developing systems for project verification to increase the quality of projects on the DApp.

In the coming weeks we will be investigating fiat integration for on-ramping and off-ramping solutions, and continuing to work on creating a white-label option.

As always, we are committed to building the future of giving based on feedback from you, our community! Let us know what you’d like to see us work on in future sprints by [trying out the DApp](http://giveth.io) and sharing your thoughts in our [Discord](https://discord.com/invite/JftjK8Un3z).

<img alt="Darth Vaders Wants you on Giveth!" class="center" src={useBaseUrl('img/blog/whatsDappening1Meme2.jpeg')} />

Thanks for reading and we’ll see you at the end of the next sprint for more dev updates ;)

_Many thanks to our amazing team for making all this possible: James Farrell, Mateo Daza, Kay, Merlin Egalite, Danielle Gennety, Willy Ogorzaly, Griff Green, Mark Prljic, Mitch, Ashley Wagner, and Lauren Bajin!_

## Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: changeMakers
title: Calling All Change-Makers!
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/change-makersMeme1.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

**Are you passionate about changing the world for the better?** We want to hear how you’re taking action to improve upon a social or environmental issue that speaks to you. Tell us how you’re making a difference. **Share your story.**

This is a call to action for all projects that are making a positive impact in the world! We would like to feature your stories on the Giveth social network and bring you into the Giveth ecosystem to help you achieve your goals. We believe in supporting each other to bring about global change as a collective. That’s why we are hard at work building the Future of Giving, connecting Givers to impact projects with a passion for global evolution.

<img alt="Cat Donating on a Computer" class="leftfloat" id="gifborder"  src={useBaseUrl('img/blog/catTypingMeme.gif')} width="300" height="auto" />

In March of 2021 we launched the new [Giveth Donation Application](https://giveth.io/) for fostering and facilitating donations to philanthropic projects on the Ethereum blockchain. It’s a free open-source platform for transparent peer-to-peer donations that aims to support innovators by building communities of donors around vital causes.

The goal of this campaign is to provide a space for altruistic developers and change-makers to talk about their passion projects, find guidance, and gain credibility and support with our dApp. So we want to hear from you! Share your perspective and tell us how you are creating change or helping to solve a problem.

### **Your Task?**

1.  **Go to** [**Giveth.io**](https://giveth.io/) **and add your project**
2.  **Tell your story\***
3.  **Share your project and story on** [**Twitter**](https://twitter.com/Givethio) **or** [**Reddit**](https://www.reddit.com/r/giveth/) **using the hashtag #Giveth4Change\*\***

\*Describe the problem you’re working on, the difference you want to make, and why this matters. Your impact story can be told as a tweet thread, a short video, a blog post/article, a photo journal — feel free to get creative! Be sure to include the message you wish to share with others.

\*\*Submissions must be made either on Twitter (tagging [@giveth.io](https://twitter.com/Givethio) and #Giveth4Change) or under our subreddit ([r/giveth](https://www.reddit.com/r/giveth/) with #Giveth4Change). Your submission must include your story and a link to your project on [giveth.io](https://giveth.io/).

<img alt="Great Gatsby calling all change-makers" src={useBaseUrl('img/blog/change-makersMeme1.jpeg')} />

We will be shining the spotlight on submitted projects by sharing them in Medium blog posts, via Twitter, Discord, and blasting off your praises throughout our network. Don’t miss this opportunity to get involved and get noticed with #Giveth4Change.

## Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/), [Docs](https://docs.giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: whatDappened2
title: "What DAppened: March 31 — April 14"
author: Lauren
author_title: Blockchain DAbbler and Heart-Centered Jack of All Trades
author_image_url: /img/laurenAuthor.png
image: img/blog/whatsDappening2Gif.gif
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

_We’re back with another development update from our recent sprint cycle! Read on to stay in-the-know on what’s dAppening at_ [_giveth.io_](https://giveth.io/)

In this past sprint, we discovered in our testing a wee little bug in our “sort” feature that was causing only the pre-loaded projects to be sorted. Rest assured, we squashed that bug and now the sort/filter/search functionality is working smoothly. We have documented how to obtain a project with a high “quality score” in our [Giveth docs](https://docs.giveth.io/guides/qualityscore/). Makers can now ensure that they’re doing everything they can to see their projects rise to the top!

We’ve upgraded the projects page as well with “infinite scroll”, allowing the user to scroll down the page as new projects load automatically.

<img alt="Infinite Scroll is fun" class="center" src={useBaseUrl('img/blog/whatsDappening2Gif.gif')} />

To further improve upon the quality of projects on our dApp, our team has been working on the new project verification method. We are developing a process in which Makers can submit their projects for review by our team and potentially achieve “verified” status. In the future, verified projects will be eligible for some exciting benefits 😉

<img alt="Bob Ross for Giveth4Change" class="leftfloat" width="475" height="auto" src={useBaseUrl('img/blog/whatsDappening2Meme1.jpg')} />

If you haven’t heard yet, we launched the “[Change Maker Campaign](https://medium.com/giveth/calling-all-change-makers-7fa964684c2b)” with [#giveth4change](https://twitter.com/hashtag/Giveth4Change?src=hashtag_click), encouraging Makers to creatively share their stories on how they are making a positive impact in the world we live in. Our favourite projects are going to be highlighted across the Giveth social network, helping them gain cred and support!

It runs until May 12, 2021, so it’s not too late to submit your projects!

---

Coming with our next sprint, we’ll be putting the finishing touches on rich text formatting for project descriptions so Makers can add photos, embed videos, create lists, format texts, and customize the presentation of their project information.

We’re also continuing to improve email notifications so that our users get appropriate and useful emails in accordance with their interactions on Giveth.

Further adding to the dApp, we’ll be integrating an embedded support chat so that users on giveth.io can ask questions directly to our team while using the platform.

Still in the works is the implementation of efficient methods of fiat on-ramping and off-ramping, and we now have more of our team members focusing efforts on resolving this long standing issue.

---

As always, we are committed to building the future of giving based on feedback from you, our community! Let us know what you’d like to see us work on in future sprints by [trying out the DApp](http://giveth.io/) and sharing your thoughts in our [Discord](https://discord.com/invite/JftjK8Un3z).

Thanks for reading and we’ll see you at the end of the next sprint for more dev updates 😘

_Many thanks to our amazing team for making all this possible: James, Mateo, Kay, Merlin, Danibelle, Willy, Griff, Marko, Mitch, Ashley, and Lauren!_

## Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/), [Docs](https://docs.giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: changeMakersRoundup1
title: The First Change-Maker Submission Roundup is In!
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/changeMakersRoundup1Meme1.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

_We asked our community to add their projects to_ [_giveth.io_](https://giveth.io/) _and_ [_share their stories_](2021-04-15-change-makers.md) _about how they are changing the world for the better using #giveth4change. Read on to discover our first round of submissions, or_ [_submit your story_](2021-04-15-change-makers.md) _via_ [_twitter_](https://twitter.com/Givethio) _or_ [_reddit_](https://www.reddit.com/r/giveth/) _to be featured in our next summary._

<img alt="Purrfect Project on Giveth" class="leftfloat" src={useBaseUrl('img/blog/changeMakersRoundup1Meme1.png')} width="370" height="auto" />

Wow 2 weeks already into the change-maker campaign! It’s been an exciting couple of months for Giveth. We’ve come hot off the heels from the Giveth.io launch right into this opportunity to hear about projects making a difference across the globe. We’ve received **six outstanding submissions** that we would like to highlight in our first roundup. Without further ado here they are!

---


## **Sage to Saddle**

aims to focus Native American youth on healthy lifestyle alternatives, rising above the poverty and substance abuse that they often live with. Nate Bressler realized while on photo-assignment shooting Native American horse racing teams for Outside Magazine, that a winter horse riding facility would greatly benefit the community of Pine Ridge, South Dakota. He teamed up with Lakota Native, Stan Brewer, the driving force behind Pine Ridge’s horse community and Angela Smith, who grew up in Utah and has been involved in nonprofits her whole life. Together, they created lofty but attainable goals that will bring structure, education, celebration, along with the opportunity for these Native youth to lift their chins with pride.

This project hopes to provide an after-school program for kids 8–18 focused on equine relationships in an indoor horse riding arena. Students of the program will be granted the opportunity to learn and grow while carrying on a traditional relationship with the very animal that made their ancestors’ survival possible. [Check out Sage to Saddle on Giveth here!](https://giveth.io/project/sage-to-saddle/)

## **Conscious Medicine Collective**

dreams to create a one-of-a-kind psychedelic consciousness center. Manex Ibar and Victoria Ibar, partners and founders, intend to create powerful experiences to bring together creativity, music, art, and high-end healing. The intention is to gather medical practitioners and influencers together into a club that fosters innovation, problem solving, and creative solutions through the use of plant medicines, psychedelics, and consciousness programs. They seek funding to establish their center on 12 acres of land they already have purchased in the picturesque Basque Pyrenées. Conscious Medicine Collective aims to bring magic, nature and wonder into an experiential club center that provides elevation of consciousness. [Venture over to their Giveth project page.](https://giveth.io/project/conscious-medicine-collective/)

## **Trust Graphic Novel**

is a transmedia project by Blockchain Philanthropy Champion Anne Connelly and accomplished artist and storyteller Chief Nyamweya. Both a graphic novel and motion comic, it is set in a future African nation that tells the story of Moraa, a young woman who learns about blockchain and uses it to protect her homeland from cultural and ecological destruction. By using storytelling to educate readers about blockchain technology, they hope to inspire African youth to see a bright future and link them to the training to create it. Currently Anne and her team are partnered with groups in Ghana, Kenya, Rwanda and South Africa. The book will cover the basics of blockchains and cryptocurrency, and provide resources and links to their African-based educational partners. [You can find their Giveth project here.](https://giveth.io/project/trust-graphic-novel-and-motion-comic/)

## **Bloom Network**

represents an international community of people and projects working toward regenerative cultures. Local Bloom hubs around the world grow participation in practices such as food security, local economies, celebrations of diversity, and art as cultural transformation. There are tens of thousands of initiatives solving major social and environmental problems, who are excluded from mainstream media and institutional finance because the way they work is naturally collaborative and polycentric. Three big picture goals the Bloom Network hopes to achieve are:

*   Inspire a billion acts of regeneration.
*   Build capacity and relationships across regenerative culture initiatives.
*   Transfer power and resources to decentralized networks.

Contributions made to their project will go towards “Regenerative Actions Ticker” on their homepage, DAO templates that local Bloom chapters can use to fund the coordination labor of actions and launch the “Call to Bloom” that will help 100+ local Blooms get started as centers of regenerative action in their cities. [Donate to Bloom Network on Giveth.io!](https://giveth.io/project/bloom-network/)

## **Must Have Crypto**

is a Cryptocurrency project based out of Kenya led by Mutinda Kisio. The Project is about teaching the masses about Crypto while enabling them to earn a daily basic income. They have minted their own token and plan to use it to teach low income individuals and families about how to use cryptocurrency by providing a steady stream of airdrops up to a maximum of a 1000 addresses. Mutinda is seeking funding to back the value of the token and provide real value to the tokens that are being airdropped. [Make a Contribution to Must Have Crypto on their Giveth project page.](https://giveth.io/project/musthavecrypto/)

## **Diamante Bridge Collective**

is a group of land stewards in the Diamante Valley, Costa Rica working together to create collective foundational agreements and a local regenerative economy that includes digital currencies for the transparent and accountable recordkeeping of their exchanges. They are building bridges between communities and organizations, local and global cultures, property owners and skilled service providers who are committed to working together long term to care for their bio-region, their neighbors, and the community at large. The Diamante Bridge Collective functions as a hub of many physical nodes, connected via global networks of shared vision and missions with the goal of restoring, preserving and consciously stewarding surrounding lands and watersheds while living harmoniously within them in alignment with planetary values. Donations will help develop infrastructure systems to support growing communities. [Head over to their project on giveth.io to make a donation!](https://giveth.io/project/diamante-bridge-collective)

Six change-making projects live on Giveth and inspiring change! There are a couple more weeks left to make submissions so if you or someone you know is working on a great cause then now is the time to get on board! [You can check out our original medium post here for more details!](2021-04-15-change-makers.md)

<img alt="Koolaid Man" width="350" height="auto" class="leftfloat" src={useBaseUrl('img/blog/changeMakersRoundup1Meme2.jpg')} />

## Want to get more involved?


*   Try out [Giveth.io](https://giveth.io/project/giveth/) or [Giveth TRACE](https://beta.giveth.io/dac/giveth-dac)
*   Discover our [Docs](https://docs.giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: whatDappened3
title: "What DAppened: April 21— May 5"
author: Lauren
author_title: Blockchain DAbbler and Heart-Centered Jack of All Trades
author_image_url: /img/laurenAuthor.png
image: img/blog/whatsDappening3img1.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

_Upholding our values of Transparency and Accountability by sharing recent development updates from this past sprint._

In this past sprint, we worked out the kinks on our **rich text editor**, allowing Makers to add photos, videos, numbered lists, font styles, headers and more to project descriptions and updates! This should be ready to go on [giveth.io](https://giveth.io/) this week. If you’re a project owner, be sure to log-on and update your description to get potential Givers even more excited about what you’ve been up to.

<img alt="Rich Text Editor Embedded in Create-a-Project" class="center" src={useBaseUrl('img/blog/whatsDappening3img1.png')} />

###### Rich Text Editor Embedded in Create-a-Project

We also spent some time optimizing the presentation of our Dapp for Mobile, fixing some visual inconsistencies and improving overall usability. We improved upon our email notifications, ensuring that Givers and Makers receive confirmation when a donation is made.

We developed and implemented automated testing for the create-a-project flow and updated the [testing guidelines](https://docs.giveth.io/docs/testing-guidelines/) in our documentation — two measures to ensure that new features work as intended.

We also addressed a few bugs: ensured that cancelled projects don’t show up in the projects list, fixed pricing, and rerouted external links for xDai donations to blockscout.

One of our all-star developers also surprised us this past sprint with a proof of concept: building Giveth.io using Next.js and Vercel instead of Gatsby and Netlify. Once we make sure all our functionality is bug-free, this change will drastically improve the UX. We’re talking faster site build, fewer issues on loading and updating, and an overall snappier site experience.

In the future, we’re going to be enhancing the UI so Makers will be able to upload photos via Unsplash when editing or creating a project. We are in the process of updating our Join, About, Contact and Support sections to the most recent info. We are also still working on the integration of an embedded chat bridged directly to our team, and project/profile verification using 3box or other.

Finally, the most exciting update to share is that we are working on giving the site a little makeover. We won’t give too much away, but here’s a little sneak peak of the new design:

<img alt="Working on a New Look for Giveth.io" class="center" src={useBaseUrl('img/blog/whatsDappening3img2.jpg')} />

###### Working on a New Look for Giveth.io

We want to extend a huge thank you to our community for all your support so far! Since launching in March, [Giveth.io](https://giveth.io/) has seen the following metrics:

<img alt="Working on a New Look for Giveth.io" class="center" src={useBaseUrl('img/blog/whatsDappening3stats.png')} />

###### Site Metrics from Giveth.io

As always, we are committed to building the future of giving based on feedback from you, our community! Let us know what you’d like to see us work on in future sprints by [trying out the DApp](http://giveth.io/) and sharing your thoughts in our [Discord](https://discord.com/invite/JftjK8Un3z).

Thanks for reading and we’ll see you at the end of the next sprint for more dev updates 😘

_Many thanks to our amazing team for making all this possible: James, Mateo, Kay, Merlin, Danibelle, Willy, Griff, Marko, Mitch, Ashley, and Lauren!_

## Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/), [Docs](https://docs.giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: changeMakersRoundup2
title: "Change-Maker Submissions — Round Up #2!"
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/changeMakersRoundup1Meme1.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

<img alt="Cowboy Rounding up Submissions" class="leftfloat" src={useBaseUrl('img/blog/changeMakersRoundup2img1.jpg')} width="450" height="auto" />

We asked our community to add their projects to [giveth.io](https://giveth.io/) and [share their stories](2021-04-15-change-makers.md) about how they are changing the world for the better using #giveth4change. Keep reading for our second round of submissions, or [submit your story](2021-04-15-change-makers.md) via [twitter](https://twitter.com/Givethio) or [reddit](https://www.reddit.com/r/giveth/) to be featured in our next round up.

It’s an absolute pleasure to have the opportunity to highlight another batch of great projects shaking things up out in the world! We have **four** awesome submissions for this period that we would like to share. Let’s check them out:

***

<img alt="Diamante Luz Center for Regenerative Living" src={useBaseUrl('img/blog/dluz.png')}  />

## **Diamante Luz Center for Regenerative Living**

is gathering passionate individuals who care about land stewardship and building conscious, intentional communities. They are catalyzing action to restore lands and protect water resources. Based in the Diamante Valley, Costa Rica, their goal is to strengthen connections to local culture and lands by building an integrated village designed to support human development and regenerate local ecosystems. They are nurturing holistic ways of living in order to live in harmony with humanity and Mother Earth. [Make a donation to the Diamante Luz Center on Giveth.io](https://giveth.io/project/diamante-luz-center-for-regenerative-living/)!

<img alt="The Commons Simulator" src={useBaseUrl('img/blog/commonsSimulator.png')}  />

## **The Commons Simulator**

is a gamified computation tool powered by a cadCAD backend that blends art and simulation into a choose-your-own-adventure sci-fi storyline. In the game, you travel back in time to use cadCAD as a tool to help a community design a regenerative Commons with the potential to save the world from total planetary and economic destruction. The first level is live and you can play it right now on [https://sim.commonsstack.org](https://sim.commonsstack.org).

Developed by the Commons Stack Dev community, the Commons Simulator illustrates one of the core missions of the Commons Stack: Empowering communities to design their own economies using open source simulation tools. Donations to this project on Giveth will go towards expanding the game by adding another level with a new story and new mechanics, such as the [Augmented Bonding Curve](https://medium.com/giveth/deep-dive-augmented-bonding-curves-3f1f7c1fa751). [Help the Commons Simulator ‘Level Up’ by making a donation on Giveth!](https://giveth.io/project/the-commons-simulator/)

<img alt="AmwFund" src={useBaseUrl('img/blog/amwFund.png')}  />

## **AmwFund**

is a registered 501(c)(3) non-profit managed by Craig Anderson. It is a digital asset fundraising ecosystem that is the primary fundraising entity for the AM Winn Community Public School based in Sacramento, California. It’s parent entity, the AM Winn Community Guild, serves primarily low-income and otherwise disadvantaged communities. They facilitate several projects relating to public education funding utilizing the potential of digital assets, NFTs and DeFi protocols. [Find out more info and make a donation to AmwFund on Giveth](https://giveth.io/project/amwfund/)!

<img alt="Njombe Beyond" src={useBaseUrl('img/blog/njombeBeyond.png')}  />

## **Njombe Beyond**


aims to tackle waste management challenges in Njombe, a town of 40,000 in southwest Tanzania. A common challenge in Tanzania is solid waste management, including in Njombe. Mettodo, the project’s creator states:

> ‘ 35 tons of solid waste is generated daily by the town: 28 tons are taken to a dumpsite, where the waste is usually burned . . . 10 % of the solid waste is plastic waste: 3,500 kg of per day, which is equal to 1000 tons of plastic waste every year.’

Njombe Beyond is working hard to reduce the plastic wasted in Njombe town. Their three specific objectives are:

*   Establish a small scale value chain for recycling plastics within the local community.
*   Collaborate with stakeholders of the program and ensure fair working conditions.
*   Involve schools and local communities in Njombe Beyond to bring awareness to the problems and opportunities of plastic waste.

[Check out Njombe Beyond’s project on Giveth!](https://giveth.io/project/njombe-beyond)

When we first set out on the change-maker campaign we had decided to wrap things up on the 12th of May, but after some discussion we have decided to **extend the change-maker campaign** indefinitely. It’s an amazing opportunity to engage with our community and celebrate the amazing projects happening on [Giveth.io](http://giveth.io). If you’d like to learn how to participate [check out the original medium post](2021-04-15-change-makers.md) for more details on getting your project featured in our submission round-ups!

<img alt="Heman wants you to make a submission!" class="center" src={useBaseUrl('img/blog/changeMakersRoundup2Meme2.png')} width="500" height="auto" />

## Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Site](http://giveth.io/), [Docs](https://docs.giveth.io/) and [Wiki](https://wiki.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio) and [Reddit](https://www.reddit.com/r/giveth/)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: changeMakersFinal
title: "Change-Makers: Final Round-up!"
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/changeMakersFinalCover.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'



Giveth has been buzzing with action! While we’ve been hard at work behind-the-scenes building for our community, Giveth change-makers have been hard at work creating positive impact on the ground. We are excited to share with you one final round-up of projects in the Change-Maker Campaign.

<img alt="Change Makers Going out to pasture" src={useBaseUrl('/img/blog/changeMakersFinalCover.jpeg')}  />

Our [Calling All Change-Makers Campaign](/blog/changeMakers) launched in April 2021 as a way to highlight the unique stories of for-good projects on Giveth and bring extra attention to the work that they are doing to change the world for the better. Read on to discover the final submissions!

<img alt="Perfect Village Communities (PVC) in Burundi" src={useBaseUrl('/img/blog/changeMakersFinal1.png')}  />

Perfect Village Communities (PVC) in Burundi
============================================

Is an organization that aims to improve the living conditions in rural communities across the central African country of Burundi. The project’s creator, Mugisha, states that in rural Burundi up to **58% of children suffer from malnutrition** and communities often have no access to medical services. Agriculture and livestock can represent up to 95% of a village’s commercial activities, yet families still struggle to get enough food to sustain themselves.

PVC Burundi began in 2015 and is teaching rural communities how to implement regenerative systems for improving education, agriculture and healthcare. Activities focus on soil regeneration, organic waste recycling, tree planting, and of course, growing food. PVC Burundi provides healthcare access to communities in exchange for tree-planting services, incentivizing a healthy environment in tandem with healthy humans.

Food sold in markets via Village Communities are used to fund PVC’s healthcare and education initiatives. Every year they launch “Community Reconciliation” where they expose new communities to different regenerative techniques, begin tree planting campaigns and bring food to market. Currently, one of their main goals is to extend their healthcare facilities in Burundi.

[Check out Perfect Villages in Burundi](https://giveth.io/project/CREATING-THE-PERFECT-VILLAGES-IN-BURUNDI) and help spread the regenerative movement in Africa!

<img alt="Bridging Digital Communities" src={useBaseUrl('/img/blog/changeMakersFinal2.png')}  />

Bridging Digital Communities
============================

Is run by a Digital Wizard by the name of Kay. He creates online bridges that allow communities to stay connected. In the decentralized world of Blockchain, communities can spring up seemingly out of nowhere, forming around causes, concepts, technologies or protocols. In this rapidly growing part of the world wide web, communities thrive off of the collective innovation and synergy of ideas, exponentiated greatly by the digital bridges that Kay creates. He has been creating and maintaining bridge servers for applications such as Discord, Telegram or Riot and has never charged anyone to make these connections. He bridges quite a few notable Ethereum projects such as: Matic, Gitcoin, 1hive, Conensys, Aragon and even Giveth (Thanks Kay! 😉)

Kay has a project on Giveth — the proceeds of which go into funding the work he does building bridges and keeping digital communities connected. [Check out his project on Giveth here!](https://giveth.io/project/Bridging-Digital-Communities-1)

<img alt="Vegan Africa Fund" src={useBaseUrl('/img/blog/changeMakersFinal3.png')}  />

Vegan Africa Fund
=================

Is a Social Enterprise focused on creating a vegan economy in Africa. They actively support African ventures in education, regenerative agriculture, renewable-energy cryptocurrency mining, vegan leather and clothing, reforestation and making delicious vegan food! They have minted their own digital $VAF impact-tokens which are accepted by all of their affiliate businesses for any products, services and experiences they might offer. Vegan Africa Fund hopes to kick-start their green economy with initial funding to back their $VAF token.

Help Vegan Africa Fund pave the way for a plant-based Africa by making a donation to [their project on Giveth.](https://giveth.io/project/vegan-africa-fund)

<img alt="Spread the Love Commission" src={useBaseUrl('/img/blog/changeMakersFinal4.png')}  />

Spread the Love Commission
==========================

Bridges the divide in the US between those experiencing homelessness and the inspired individuals who want to lend a hand. Wren Fialka, the founder, started it all by asking a man experiencing homelessness one question: “If there was a bag of items that I could bring you tomorrow to make your day-to-day life easier, what would be in the bag?”. Based on their simple approach focused on “Connection, Compassion and Vital Supplies” they have been serving communities across the US for the last 6 years.

On the Spread the Love project page they state that anywhere between 600,000 to 1.5 million people experience homelessness across the country, and with Covid-19 financial support ending soon, that number is likely to rise. With only one employee, Spread the Love Commission needs to grow in order to meet these rising challenges. So far they have served over 30 communities and with Giver support they hope to serve many more.

Spread the Love Commission aims to remove the stigma of homelessness and connect those stuck in a vicious cycle with support from those who are ready to offer it. With sustainability, compassion and persistence they hope to end the homelessness crisis once and for all.

[Visit the Spread the Love Commission Giveth project page](https://giveth.io/project/spread-the-love-commission) to find out more and help them fund their critical mission!

And that’s a wrap! Thank you to all the Givers that provide support to projects that are making a difference, and to all the change-makers that are finding a way to make positive global impact. It has been amazing to have the opportunity to learn from and highlight so many projects that are daring to be different, working hard to connect humans and improving the world we live in!

While the Change-Maker campaign has ended you can still get some **_Giveth love_** by sharing your project with us on [Reddit](https://www.reddit.com/r/giveth/) or [Twitter](https://twitter.com/Givethio) for a shout out or a repost on our social media channels. We always appreciate outstanding Giveth projects and are planning to keep highlighting Makers going the extra mile on the Giveth.io. Thank you to all of our participants!

Want to get more involved?
--------------------------

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: traceLaunch
title: "Giveth TRACE is Live 🚀"
author: Lauren
author_image_url: /img/laurenAuthor.png
image: /img/blog/traceLiveBanner.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


**_We are pleased to announce the official full release of_** [**_Giveth TRACE_**](http://trace.giveth.io/?utm_source=medium&utm_medium=article&utm_campaign=traceLaunch) **_— a platform for traceable, accountable, effective donations powered by blockchain technology._**


<img alt="Giveth TRACE homepage"  src={useBaseUrl('/img/blog/traceLaunchCover.png')}  />


In the [early stages](/blog/futureOfGiving2017) of Giveth, we set out to demystify philanthropic contributions to nonprofits by empowering Givers with the ability to see where and how their donations are being used. We released our MVP DApp in 2018 to be beta tested by the Giveth Galaxy, but faced huge obstacles. Scope creep, maintenance of a complex system, and an overly complicated user experience prevented a quick release, and then we simply ran out of funding. We were close to “calling it quits” on our original DApp in favour of a simpler, [user-friendly version](https://giveth.io/) that we would design from scratch.

Fortunately for Givers everywhere, our all-star devs refused to give up. We assembled a team around the DApp and worked tirelessly for months on stabilization and beautification. With our hearts full of joy and our hats in our hands, we are proud to finally come out of beta and release TRACE to the world.

**Giveth TRACE is no longer a wistful dream of something that could have been — it’s a reality!**
-------------------------------------------------------------------------------------------------

Allow us to proudly present a platform that lifts the veil between Givers and their donations in action. A platform that empowers projects to create highly customizable online representations to attract real supporters. A platform that emphasizes the development of trust between all parties — the Givers, the projects and the greater community. We proudly present: [Giveth TRACE](http://trace.giveth.io/?utm_source=medium&utm_medium=article&utm_campaign=traceLaunch).

<img  alt="Memery - Traceable Donations" src={useBaseUrl('/img/blog/traceLaunchMeme1.jpeg')}  />


Project Verification
====================

<img class="leftfloat" width="250" height="auto" alt="Verified Project Badge" src={useBaseUrl('/img/blog/traceLaunchPhoto1.png')}  />


Givers using TRACE know that their donations are going to top-quality legitimate projects thanks to our project verification system. In order to add a project as a Campaign on Giveth TRACE, a Maker must first add their project to [giveth.io](http://giveth.io) and apply to become verified. Currently this process is informal, but soon it will be integrated into the project flow. For now, if you want to verify your project, fill [out this typeform](https://hlfkiwoiwhi.typeform.com/to/pXxk0HO5) and reach out in the #project-onboarding channel on our [Discord](https://discord.giveth.io).

Accountability
==============

Campaigns represent the big picture for each project — projects use Campaigns to collect traceable donations and manage them transparently. Under each Campaign there can be multiple “[Traces](/dapps/leavingTraces)”, i.e. payments, bounties, or expenses. Traces specify how the project is using their donations to achieve the goals of the overarching Campaigns. When a Giver donates to a Campaign they can follow the flow of their donations. Whenever donations are moved from a Campaign to a Trace, the Giver is notified and can see exactly how their donations are used.

Traces are the only way for donations to leave Giveth TRACE. Every project on the platform will have to explain how they are using the donations before collecting them.

**This way, the Campaigns are held accountable to the Givers and the Givers can see their donations in action!**
----------------------------------------------------------------------------------------------------------------
<img  alt="TRACE campaign page" src={useBaseUrl('/img/blog/traceLaunchPhoto2.png')}  />


###### Campaigns Live on [Giveth TRACE](https://www.trace.giveth.io/)

Donor Empowerment
=================

Not sure which Campaign to donate to? Giveth TRACE also offers “Communities”, which represent people and projects united by common goals and initiatives. When you donate to a Community, you are donating to a cause that you believe in! [Communities can delegate donations to Campaigns or to specific Traces](/dapps/entitiesAndRoles), and each time donations are delegated, the Giver can choose to veto the movement.

In this way, Giveth TRACE builds on blockchain technology with an added layer of donor empowerment that has never before been possible. **Givers don’t have to trust that their donations are flowing to projects they believe in, they can actively ensure it.**

### But wait — there’s more…


Free Gas for Giveth TRACE Projects
==================================

<img  alt="Memery - Free gas, gas station" src={useBaseUrl('/img/blog/traceLaunchMeme3.jpeg')}  />


On Giveth TRACE, Giveth pays the gas fees so projects don’t have to!
--------------------------------------------------------------------

Giveth TRACE makes use of two networks in order to address security and scalability issues. Our use of Rinkeby testnet [makes it free to perform basic site interactions](https://medium.com/giveth/tackling-ethereum-scalability-issues-29bd700b5060), such as creating a Trace, managing donations, or updating a profile. However, in order to collect or disburse donations from a Trace, [Ethereum gas fees must still be paid](/dapps/bridgeSecurity/) to get the donations to the final recipient on mainnet. We are excited to financially support each project on Giveth TRACE while also protecting them from the difficult user experience and the complications of the Ethereum network, so we cover their gas costs!

You can see the total gas Giveth paid for each Campaign, Trace or Individual on TRACE — and can even share it with your friends.

<img  alt="Memery - Traceable Donations" src={useBaseUrl('/img/blog/traceLaunchPhoto4.png')}  />


###### Total Gas Paid for the [Commons Stack Community Campaign](https://www.trace.giveth.io/campaign/commons-stack-community-iteration-0) on Giveth TRACE  

Our mission at Giveth is to bridge the non-profit and blockchain worlds, connecting people, ideas and resources with free, open source decentralized applications. The launch of Giveth TRACE and its ability to offer unique transparency, traceability, customization, empowerment and accountability is a major milestone in Building the Future of Giving!

So what are you waiting for?  Head over to [Giveth TRACE](http://trace.giveth.io/?utm_source=medium&utm_medium=article&utm_campaign=traceLaunch), try it out for yourself and let us know what you think!

**Want to get more involved?**

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: communitySpotlight1
title: "Community Project Spotlight #1"
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/communitySpotlight1Cover.jpeg
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


<img alt="Watching for those doing good" src={useBaseUrl('/img/blog/communitySpotlight1Cover.jpeg')}  />

We’re back with a silver platter of community curated projects to celebrate and highlight! Our Giveth contributors went through the list and chose their top picks. We’ve found six great projects that are [live on Giveth now](https://giveth.io/projects) and looking for funding to meet their goals. Read on to discover some of our favourite projects from a diverse range of causes using our DApps.

<img alt="Colorado Multiversity" src={useBaseUrl('/img/blog/communitySpotlight1.png')}  />

Colorado Multiversity
=====================

Is a partnership of local and international organizations based in the Northern Caribbean side of Costa Rica. They provide resources for disaster relief workers and environmental conservationists. The biodiversity contained in Costa Rica cannot be understated and the preservation of the plethora of unique flora and fauna in this region is paramount to the Multiversity’s mission. They currently steward a land area of 1235 acres located within the Barra del Colorado National Refuge which has been designated by UNESCO as one of most important places for natural conservation.

Currently, Colorado Multiversity operates out of a biological station called “El Zota”, which is one of the Multiversity’s partners. El Zota carries out research and training for those who are passionate about conservation and biodiversity. There is also The Refuge Project, another one of the Multiversity’s organizations, that utilizes the facility as a safe space for disaster relief workers worldwide to meet, rest, teach and learn.

The Colorado Multiversity has been recognized by some notable organizations for potential funding, including the SDG Impact Fund, Gaia Gives and the Spanish Cooperation. They are seeking initial funding to kick-start their mission and meet the funding criteria outlined by these organizations. They have a wide range of projects being launched including decarbonization initiatives, international volunteering programs, agricultural development research and plastic recycling. Check out their introduction video below and [visit their project on Giveth](https://giveth.io/project/colorado-multiversity) to learn more and donate!

<img alt="Feed the Hungry in Chilliwack, BC, Canada" src={useBaseUrl('/img/blog/communitySpotlight2.jpeg')}  />

Feed the Hungry in Chilliwack, BC, Canada
=========================================

Is a local effort led by a man named David to make a contribution to the homeless population prevalent in the local community of Chilliwack, a city near Vancouver, British Columbia. In Vancouver the homeless population is ever-present and expanding. The temperate climate of southern BC has allowed this region to become a year-round hub for the Canadian demographic experiencing homelessness. The problem in Chilliwack is exacerbated as the city of Vancouver rounds up the homeless on one-way buses to Chilliwack, dropping them off in the town with no return.

Feeding the hungry is a simple and powerful gesture. David’s trusty team, consisting of him and his daughter, plans to create food packages to hand out to the population experiencing homelessness in Chilliwack. David is seeking funding to purchase ingredients for the food packages, cover gas costs and pay for lodging expenses. At the time of writing this article, David’s team is gearing up and getting ready to execute their plan in the coming weeks. Funds contributed to this project will allow them to scale their mission and feed more people. [Find their project on Giveth.io](https://giveth.io/project/Feed-the-Hungry-in-Chilliwack-BC-Canada), make a donation and stay tuned for updates in the near future!

<img alt="Women of Crypto Art (WOCA)" src={useBaseUrl('/img/blog/communitySpotlight3.png')}  />

Women of Crypto Art (WOCA)
==============================

Have launched an inclusive community to celebrate, support and connect the women in the crypto art space. The voices of women are extremely important and often underrepresented so WOCA is championing the presence of women in the crypto sphere. They share ideas and information and promote each other’s work across all realms of cryptocurrency. In 6 short months their community has quickly grown to over 400 members.

WOCA has kept pace with their rapid growth, improving their organization in many ways. They’ve built a website to showcase their community talent, they launched a Colony DAO to manage their thriving tribe and have formed great relationships with entities such as Panvala and Cryptovoxels. WOCA is seeking funding to reach their next milestones, including building a permanent gallery, onboarding members to the DAO and promoting all of the incredible work done by women artists. Check out WOCA and make a donation to their [project on Giveth](https://giveth.io/project/women-of-crypto-art-(woca)).

<img alt="Vukani" src={useBaseUrl('/img/blog/communitySpotlight4.jpeg')}  />

Vukani
==========

Translates to “Wake Up” in the regional isiZulu tongue, and is the motto of this project based in rural Zimbabwe. The entire country faces extreme food security challenges, driven by political and environmental factors. This project is dedicated to finding food security solutions for one of the most important, yet vulnerable groups in society: the children. The project’s owner, Tim Olsson, believes that satisfying the nutritional needs of children allows them to focus on their education and development. Children will create the future of tomorrow and providing them with the means to succeed will help them overcome the challenges we still face today.

Vukani’s immediate goal is to grow food to nourish the local school children. Research is needed to find an agricultural system that works in the unique conditions of Zimbabwe. Once an effective system is found by the initial pilot project, their aim is to scale up and one day serve the entire country. Progress has been made for finding a water source but more infrastructure needs to be acquired to effectively distribute it for irrigation. Funds to this project will help make purchases for water pumps and solar-powered irrigation systems. Head over to [Vukani’s project on Giveth](https://giveth.io/project/vukani) to read more and make a donation!

<img alt="MyCrypto" src={useBaseUrl('/img/blog/communitySpotlight5.jpeg')}  />

MyCrypto
============

Is making wallet management a breeze in the Ethereum ecosystem. MyCrypto is a hub for creating and connecting your Ethereum wallets. It boasts a great UI that can consolidate and keep track of all your tokens and their values on Mainnet and several Ethereum sidechains. MyCrypto also allows you to deploy and carry out direct interactions with Ethereum smart contracts! Neato! Apart from those wonderful tools, it can also facilitate sending, requesting, swapping and buying crypto as well as tracking eligible airdrops. They also have a desktop app for offline wallet management, useful for managing private keys and seed phrases.

MyCrypto is open-source and has developed many free tools for Ethereum user security, such as a [database for tracking known crypto scams](https://cryptoscamdb.org/), [a web extension for preventing phishing attempts](https://chrome.google.com/webstore/detail/etheraddresslookup/pdknmigbbbhmllnmgdfalmedcmcefdfn) and an [application for finding lost Ethereum addresses](https://findeth.io/). Donations to their project will help secure funding to keep their platforms alive and maintained. Experience their DApp on [https://app.mycrypto.com](https://app.mycrypto.com) and [visit their project on Giveth](https://giveth.io/project/mycrypto) to make a contribution.

<img alt="Free the Food" src={useBaseUrl('/img/blog/communitySpotlight6.jpeg')}  />

Free the Food
=================

Believes in creating regenerative food sources using the vacant areas along the sides of roads. Harnessing the knowledge of Syntropic Farming they have launched their project along the lush rural roads of Costa Rica. According to Devin & Arthur, Free the Food’s co-founders, Syntropic Farming is the gateway to restoring ecological diversity, creating wildlife habitats and holistically super-charging the generation of delicious and healthy food.

They have already begun with three streetside syntropic plantations to grow food, with more sites on the way. Their grand vision is to create a network of streetside syntropics and to engineer a grants system allowing new communities to spring up, acquiring the knowledge to begin propagating these regenerative food sources. They are seeking funding now to develop their website and purchase irrigation tools, water tanks, seeds, tools, as well as to provide a monthly budget for 1 employee. [Find their project on Giveth](https://giveth.io/project/free-the-food) and learn more about Free the Food!

There you have it! Six spicy projects running the gambit from art, crypto, nature and all the goodness in between. Don’t see your project on the list? Don’t sweat! We’ll be regularly highlighting more ventures on our blog and social media channels, and you can catch our eye by tweeting about your project and tagging us [@givethio](https://twitter.com/Givethio).

If you have a for-good project looking for funding, get on [Giveth.io](https://giveth.io/) to give the world easy access to donate cryptocurrency to your cause. If you want to spread the love as a donor, check out both our DApps, [Giveth.io](https://giveth.io/) and [Giveth TRACE](https://trace.giveth.io/) for more ways to give!

**Want to get more involved?**
------------------------------

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Facebook](https://www.facebook.com/givethio), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: communitySpotlight2
title: "Community Project Spotlight #2"
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/communitySpotlight2Cover.gif
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

We’re back with another fresh batch of amazing projects on Giveth.io. We have six projects from a wide range of causes that we are featuring in this project spotlight. This is also an extra special spotlight because Giveth.io itself is currently active and accepting donations on the latest round of [**Gitcoin Grants**](https://gitcoin.co/grants/) **(GR11)**. If you feel inspired by the Giveth mission after reading this article then consider making a contribution via our [Grants listing](https://gitcoin.co/grants/795/givethio-panvala-league) and learn about the magic of _Quadratic Funding_! More on that later…

<img alt="GR11 Magic" src={useBaseUrl('/img/blog/communitySpotlight2Cover.gif')}  />  

Without further ado let’s dive in and highlight these projects that are making our DApp great!  

---

<img alt="ETHOS" src={useBaseUrl('/img/blog/communitySpotlight2-1.png')}  />  

**ETHOS**
=========

**Emergency Transitional Housing Offering Services (ETHOS)** is designing funding solutions for the homelessness crisis in Olympia, Washington State. ETHOS has been championed by ‘Art Is Solidarity’ which is a local non-profit combining blockchain technology and art mediums to find solutions and funding opportunities for pressing social issues. At the heart of this project is the city’s first initiative: to combat homelessness. From ETHOS’s project description:

> “In 2018, the City of Olympia sanctioned a tent city adjacent to the transit center downtown dubbed the “Mitigation Site” for those struggling on the streets to have somewhere to rest and seek shelter. In late 2020, two-and-a-half winters and many tents later, a next step in creating a path to housing for downtowners was conceived when the City of Olympia contracted a local design and build firm to create 60 ‘micro-houses’ to replace tents and offer more security and safety for those trying to get on their feet.“

Following the successful construction and installation of these micro-houses, Art Is Solidarity will use additional funds raised to improve upon the amenities inside the Mitigation Site in a unique way. They are engaging the help of local artists to beautify the micro-houses into works of art and mint the art pieces into NFTs to be auctioned off digitally. Proceeds of these auctions will go towards outfitting the house with furniture, heaters and more!

Art Is Solidarity also intends to educate the shelter’s inhabitants and local artists about the vast opportunities that NFTs and cryptocurrencies can offer for alternative forms of income, and provide them with the tools to get involved. Check out their [project on Giveth.io](https://giveth.io/project/ETHOS-Emergency-Transitional-Housing-Offering-Services-1) and donate to help the build and beautification of micro-housing, and the educational opportunities being created for the homeless in Olympia.

<img alt="Finca Morpho" src={useBaseUrl('/img/blog/communitySpotlight2-2.png')}  />  

Finca Morpho
================

Nestled in the Osa Peninsula, Costa Rica, there is a community of thriving nomads building ecological harmony at Finca Morpho. This 5-acre beachfront paradise is where humans create strong ties with each other and the land while learning a wide range of skills for a harmonized lifestyle. These skills include permaculture, bamboo building, recycling techniques, holistic medicine, renewable energy, and healthy cooking techniques.

Founded in 2014 Finca Morpho is a place for curious travelers to spend time in nature and to fully immerse themselves in communal living. They also host events and retreats to further share the important knowledge they have cultivated on the farm. They have created closed-loop recycling systems from the ground up, having found ways to completely repurpose all of their waste. From a simple sandy beach they have nurtured a thriving permaculture system complete with aquaponics, soil sanctuaries and carbon sequestration techniques. They have come a long way from their humble beginnings.

There are 7 pillars that comprise the core physical and conceptual foundations of the farm: **The Kitchen, The Resource Center, Permaculture, Hospitality, Infrastructure, Project Management and Relationships**. Finca Morpho is seeking funding to upgrade a few of these pillars which need a bit of love in order to maintain and improve their functions. The four pillars needing improvements are:

*   **Kitchen** — To keep feeding hungry mouths and processing the bounty of the land. Buying new equipment such as blenders and stoves.
*   **Resource Center** — To fulfill their mission of recycling or repurposing everything they use. Purchasing a 3d printer, plastic shredder, extruder, microscope and expanding the area of the center.
*   **Infrastructure** — The cabins, water storage system and solar grid they maintain are in need of love. Buying new solar batteries, renovating cabins and installing a new water storage system.
*   **Permaculture** — Every season comes with new challenges and needs. Purchasing seeds, plants and trees.

Check out [Finca Morpho’s project on Giveth.io](https://giveth.io/project/Finca-Morpho) and make a donation to keep this community thriving and capable of spreading its message to those who seek it, and learn more about how they do it on their [website](https://www.fincamorpho.com/).

<img alt="Solidity Development Course in Farsi" src={useBaseUrl('/img/blog/communitySpotlight2-3.png')}  />  

Solidity Development Course in Farsi
========================================

The language and gender barriers created by the english-dominated blockchain industry severely hamper opportunities of up-and-coming demographics to fully participate in the revolutionary technology that Blockchain produces. Shayan Eskandari, the project’s creator summarizes the opportunity to provide support:

> “Farsi is spoken by an estimated 110 million speakers mostly in Iran, Tajikistan, Uzbekistan, Iraq, Russia, Azerbaijan and Afghanistan . . . In contrast to the West where computer engineers are predominantly men, Iran’s STEM (Science, Technology, Engineering, Mathematics) graduates are about 70% women.”

CoinIran, the project’s host organization, has built opportunities to overcome these barriers by creating unique programs for Farsi speakers, notably their latest project, “Women in Blockchain’’. This program is putting Iranian women through the ConsenSys Academy Blockchain Developer bootcamp while providing technical and linguistic support, giving them the knowledge and skills to acquire jobs as Ethereum developers. Their initial cycle put 7 women through the course, who all passed, receiving developer certifications from ConsenSys.

**Making Blockchain and Cryptocurrency more accessible will only help to ensure its growth and adoption.** The project is seeking funding to cover the expenses of putting the women through the course and for the costs of building the course tailored for Farsi speakers with comprehensive media, translations and syllabuses. Further funds raised will allow more women to go through the program. Read the [full article on CoinIran](https://coiniran.com/empowering-iranian-women-with-blockchain/) and visit their [project on Giveth.io](https://giveth.io/project/solidity-development-course-in-farsi-by-women-in-blockchain-iran) to make a donation!

<img alt="Oika" src={useBaseUrl('/img/blog/communitySpotlight2-4.png')}  />  

Oika
========

Can be defined as _“The feeling of ecological wellbeing and belonging to nature. It is the intelligence of nature as expressed through human thought and action.”_. The word is derived from the Greek word **_Oikos_**, meaning “home”. The project, Oika, is reconnecting humans with nature and raising awareness of climate change through NFT technology. Dr. Rich Blundell, the project’s creator, has gathered a team of scientists, artists and storytellers to cultivate _Ecological Intelligence_. They are combining the realms of academic ecological analysis with different artistic techniques to produce images and videos that are minted as NFTs. You can check out their creations on the [Oika Media page](https://oika.com/oika-media-projects).

Oika also maintains an off-grid homestead and marine research vessel for inspired researchers to collaborate, incubating new ideas and generating knowledge. There are a wide variety of subjects that Oika advocates research on, such as:

*   Ecological Survey & Monitoring
*   Invasive Species Response
*   Pelagic/Neritic, Plastics Clean-up
*   Fishing Debris Location & Removal
*   Wildlife Reporting & Monitoring
*   Aquaculture Research
*   Phenology (study of climate change effects)
*   Citizen Science
*   Sci-Art Collaboration
*   Public Interpretation/Communication
*   Conservation Journalism/Documentary

Oika also offers courses for teaching the concepts of Ecological Intelligence. They seek funding to continue operating their off-grid research center and to pay artists and scientists for their contributions and collaborations involved in crafting the NFTs. Visit the [Oika website](https://oika.com/) to learn more and check out their [project on Giveth.io](https://giveth.io/project/Oika-in-the-Blockchain-1) to make a donation!

<img alt="Grassroots Economics" src={useBaseUrl('/img/blog/communitySpotlight2-5.png')}  />  

Grassroots Economics
========================

The ability for local economies to spring up, create their own money and give it value is one of the most revolutionary concepts created by cryptocurrency. Grassroots Economics is proving this concept by building open-source economies in communities throughout Kenya. Their base token. known as Community Inclusion Currency (CIC). is to be used across all their participating communities in order to quantify and redistribute the abundance of goods they produce.

Their vision is to create healthy and decentralized ecosystems by empowering locals to design their own economies. They also believe heavily in syntropic agroforestry as the main technique to provide agricultural abundance and economic value production.

They seek funding in order to build the open-source software they need in order to achieve their goals. Development currently takes place on their [public repository on Gitlab](https://gitlab.com/grassrootseconomics). Check out their [project on Giveth.io](https://giveth.io/project/grassroots-economics-community-currency) and make a donation to allow Kenyan communities to build new economies using Blockchain!

<img alt="Rainbow Crystal Land" src={useBaseUrl('/img/blog/communitySpotlight2-6.png')}  />  

Rainbow Crystal Land
========================

Among the Andes mountains in San Agustin, Colombia, there is a community of free-spirits liberating mother nature and creating communal living spaces. Rainbow Crystal Land (RCL), established in 2014, strives to create a global network of leaderless, horizontally structured communities that live in harmony with each other and the Earth. Currently they operate out of their main hub in San Agustin but are seeking to build a global community that shares their philosophy. They are mostly donation based but also sell the food they grow on the land to the local markets. All of these funds go into their “Magic Hat” which is used to buy necessary food and pay overhead costs to continue their existence.

They have written a [comprehensive handbook](https://rainbowcrystal.land/document/handbook/) detailing many aspects of their organization, including their declaration of Common Intention as well as their Mission, Vision and Values. On the land they maintain several houses for families and dormitories for their human inhabitants. They operate a solar grid for closed-loop electricity provision and also a permaculture farm on their 14 hectare plot of land.

RCL is seeking funding to improve much of their existing infrastructure. They are hoping to purchase treated bamboo and other wood to finish building their housing projects. Tools and plant supplies need to be bought to begin putting to use their recently acquired land. Funding also is always needed to feed their citizens, namely, those who are working hard to build their utopian vision. Check out their [project on Giveth.io](https://giveth.io/project/rainbow-crystal-land-colombia) to learn more and make a donation!

**That’s a wrap for this community project spotlight!** Six diverse projects that are making a positive change across the globe, check them out and consider making a donation to keep these important causes alive and thriving! Stay tuned for more featured projects in the future!

Also, if you love Giveth.io and the work we do to provide free and open-source funding platforms for philanthropic causes, consider making a donation to our [Gitcoin Grant](https://gitcoin.co/grants/795/givethio-panvala-league). We also have **our other DApp,** [**Giveth TRACE**](http://trace.giveth.io), for more complex projects that want to offer traceable donations. You can make a donation to Giveth TRACE on its [Gitcoin Grants listing](https://gitcoin.co/grants/2154/givethtrace) as well. Every unique donor to our listings increases the amount of matching funds we receive via [_Quadratic Funding_](https://wtfisqf.com/?grant=&grant=&grant=&grant=&match=1000), so the more the merrier!

Want to get more involved?
--------------------------

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: communitySpotlight3
title: "Community Project Spotlight #3"
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/givethComeWithMeBanner.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


It’s time for another batch of great projects from Giveth.io, hand-picked by our contributors. We have six amazing projects to feature in this edition of the community spotlight.

<img alt="Project spotlight Time!" src={useBaseUrl('img/blog/projectSpotlight3meme1.gif')} />

There’s an exciting array of projects waiting below — everything from indigenous culture, to black art, to even the arcane realm of memery. Discover some of the magic on [Giveth.io](https://giveth.io/) with these projects that are making waves in our physical and digital worlds. Let’s dive in!

<img alt="Futuro Nativo" src={useBaseUrl('img/blog/futuroNativo.png')} />


## FUTURO NATIVO

is celebrating and spreading indigenous cultures and practices found in the western Brazilian region of Acre. They are creating donation pathways to empower several native tribes, and are propagating holistic practices to restore our connection with the Earth. They currently support four tribal villages in the region:

*   **Yawanawa — Shukuvena** (“Toucan” in the local language) — Praised for fostering strong female leaders, this tribe is focused on agroforestry, food sovereignty, natural medicines and spiritual practices.
*   **Huni Kui — Pinuya** (“Hummingbird” in the local language) — Residing in the northern zone of Acre, the village of Pinuya is making huge leaps in reforestation efforts and crop laying. They are focused on yielding saplings and food surpluses with the intention to move away from tourism and find alternative income sources.
*   **Huni Kui — Caucho** — Dwelling in the basins of the rivers Juruà and Purus, the village of Caucho strives to reclaim their culture from the shocks of colonial industrialization. The Amazon Rubber Boom eroded much of their ancestral culture. They believe in sowing their culture through music, dance and art.
*   **Kuntanawa** or “Coconut People” — Believe that plants are the way to connect with the spirits of the forest. They have mastered how to cure their people with traditional medicines and plan to cure the world by creating alliances of communities committed to restore the balance of nature.

Each tribe boasts dozens of families living on their ancestral land, which collectively is spread out over hundreds of thousands of hectares of Amazonian rainforest. These peoples steward their land, implementing traditional agroforestry techniques, as well as ply their artisanal craft-making skills. The tribes affiliated with Futuro Nativo also host visitors and workshops to teach their culture to the curious and passionate.

Futuro Nativo has very well defined funding goals which complement each tribe’s unique needs and offerings. Visiting [their website](https://www.futuronativo.org/projects), you can see projects range from tree nurseries, educational events, to even creating online stores to distribute their artisanal crafts. Check out [their project on Giveth.io](https://giveth.io/project/FUTURO-NATIVO-1) to learn more about the projects of each tribe and to make a donation!

<img alt="HNS Fund" src={useBaseUrl('img/blog/HNSfund.png')} />


## Handshake Development Fund

carries the banner for open-source software and the free decentralized web. The Handshake Development (HNS) Fund is the community funding the Handshake protocol and affiliated systems. HNS at its core is a system for distributing internet domain names using cryptocurrency technology. The HNS protocol website hits home the need for better domain name distribution framework:

> _“Names on the internet (top level domains, social networking handles, etc.) ultimately rely upon centralized actors with full control over a system which are relied upon to be honest, as they are vulnerable to hacking, censorship, and corruption. . . . Services on the internet have become more centralized beginning in the 1990s, but do not fulfill the original decentralized vision of the internet. . . . Centralization exists because there is a need to manage spam, griefing, and sockpuppet/sybil attacks. Previous decentralized systems largely stopped working due to spam. If it were more costly to grief on the internet using decentralized systems, the need for trusted centralized corporations to manage these risks decrease.”_

HNS uses a token (aptly named HNS) to register domain names. Using these cryptographic tokens, participants can transfer and update their registered names. By creating a decentralized and accountable system, HNS (by way of its users) can inhibit a centralized actor from scooping up all the domain names. The HNS Fund seeks out donations to keep afloat their open-source tools, such as DNS records, domain registries, and educational content. [Find their project on Giveth.io](https://giveth.io/project/handshake-development-fund) and make a donation to support HNS public goods!

<img alt="Njome Innovation Academy" src={useBaseUrl('img/blog/NjombeIA.png')} />

## Njombe Innovation Academy

is creating the next generation of African entrepreneurs in Njombe, Tanzania. Njombe Innovation Academy (NIA) is importing the Social Innovation Academy (SINA) educational model which began in Uganda. The premise of SINA is to invite members of marginalized african demographics with passion and ideas to a co-living experience to gain the entrepreneurial skills to make their dreams a reality. SINA has proven to be extremely successful, tackling prevailing African issues around failing education systems and corresponding unemployment rates. Njombe Innovation Academy profoundly lays out their **Theory for Change**:

> _“The desired impact (of NIA) is an increased number of social challenges tackled in Njombe by youth-led enterprises with locally available resources. . . . we will bootstrap a self-organised community of youth in Njombe who commonly owns(sic) and manages(sic) resources (material, knowledge, financial, social) to create social enterprises out of challenges . . . “_

SINA communities have been spreading around the continent and Uganda is ready, more than ever, for it’s own local SINA node. NIA identifies that local youth unemployment hovers around 10% with more than 40% never completing secondary school. Crippling rates of malnutrition and HIV hamper the societal and economic growth of Njombe.

Njombe Innovation Academy has outlined a clear plan for kick-starting the local SINA community. The first step is to send 3 local youth from Njombe to Uganda to gain insight from the original SINA. Then, with supporting members and facilities, these successful graduates begin to train subsequent cohorts of entrepreneurs. In 2 years they are targeting to put over 50 youth through the local Njombe SINA program and generate nearly a dozen new enterprises as a result. 50% of these participants will be women and a further 15% will be people with disabilities. All participants will come from poverty based backgrounds.

To learn more of NIA milestones, their funding targets and to make a donation, visit [their project on Giveth.io](https://giveth.io/project/Njombe-Innovation-Academy-1). NIA is also partnered with Giveth in Panvala’s Regenerative Commons Coalition, you can view [their Panvala listing here](https://panvala.com/njombe-innovation-academy).

<img alt="Meme Manifesto" src={useBaseUrl('img/blog/memeManifesto.png')} />

Meme Manifesto
==============

The 21st century cultural phenomenon of memes has embedded itself firmly in the history of humankind. Meme Manifesto goes deep… deep, down the rabbit hole of memes as an ideological force and as a new medium of communicating complex, nuanced concepts. The project conveys itself as an amorphous transmedia project that will take various forms at various points of its evolution. The Manifesto itself expresses powerful reflections on meme culture:

> _“. . . we believe memes to be the latest iteration of the one true power that defines us as a species: the faculty to understand, interpret and alter our reality through linguistic and symbolic patterns of meaning. To understand this power means to hold the keys to control the uncertain grounds on which our common social world is constructed.”_

<img alt="Meme Manifesto" src={useBaseUrl('img/blog/memeManifesto2.png')} />

###### A snapshot of what to expect among the depths of the “meme iceberg”

On the [Meme Manifesto we bsite](https://mememanifesto.space/) you can embark on a journey through the meme-sphere beginning from the nascent forms of memery, into the depths of niche cultural references and intricate memeified expressions. Prepare yourself, it’s a long way to the bottom. Donations made to this project will go to the artists who wrote and assembled the meme manifesto and its current representations. Check out [Meme Manifesto’s project on Giveth.io](https://giveth.io/project/meme-manifesto) to learn more of their philosophy and to make a donation.

<img alt="Black Love Mural Festival" src={useBaseUrl('img/blog/blackLoveFestival.png')} />

## Black Love Mural Festival

Held in downtown Denver, Colorado, The Black Love Mural Festival (BLMF) highlights prevailing issues in black society and the cultural anecdotes held within. It is also a celebration of the artistic talent of local black artists in Denver.

The festival itself was created from the momentum generated by the George Floyd protests with the first one taking place in 2020. In a collaboration between Rob The Art Museum and IRL Art, two local entities that organize community events and art exhibitions, they hosted 93 artists who painted murals all over the city, including around the state capital buildings.

<img alt="Black Love Mural Festival" src={useBaseUrl('img/blog/blackLoveFestival2.png')} />

###### _Photo credits:_ [_The Denverite_](https://denverite.com/2020/06/12/black-love-mural-festival-will-showcase-art-by-black-denver-artists-at-civic-center-park/) _and_ [_Black Love Mural Festival_](https://www.blacklovemuralfestival.com/)

Now their mission is to prepare for future BLMFs and transfer these works into the digital realm. In 2021, largely resulting from the circumstances of the pandemic, new portals are being created to bring the festival to the blockchain. Several dozen artists have had their works minted as NFTs, to be preserved digitally. BLMF strongly believes that blockchain holds the solutions to empower minority groups and artists with the tools for a better future.

Funding received on the BLMF project will go to the volunteer team who not only pay gas in Ethereum to mint NFTs for artists but also continue to educate the BLMF artist community on using blockchain and the Ethereum network. Check out [their project on Giveth.io](https://giveth.io/project/Black-Love-Mural-Festival) and make a donation to support black art in Denver!

<img alt="Black Love Mural Festival" src={useBaseUrl('img/blog/permacultureActionNetwork.png')} />

## Permaculture Action Network

is a North American collective that orchestrates action on environmentally regenerative programs. Utilizing music, culture, and art they have mobilized hands to create and maintain localized nodes of permaculture in over 65 cities for the last 5 years. In more concrete terms, this is executed via **Permaculture Action Days;** an event which organizes various activities including workshops and discussion panels, often in partnership with local music festivals or cultural events. During the event, participants are channeled to aid in the construction of permaculture infrastructure, such as community gardens, rainwater catchment systems and greenhouses.

The heart of activity during the event is the **Permaculture Action Hub**. This is the physical place which brings in curious festival attendees to learn a wide variety of subjects, ranging from alternative economies to mushroom cultivation.

Also featured during Action Days are **Permaculture Action Courses**. These  are free, hands-on classes that teach regenerative ecological techniques and socio-economic structures for individuals and communities.

Adapting to the pandemic, the Permaculture Action Network has begun building their next interactive tool: the Just Transition Map. This map will show locations of community spaces and projects that are creating better alternatives to the current extractive economy. This will be a tool for the global environmental justice movement to coordinate and create action. Donations to Permaculture Action Network will help them build the Just Transition Map and to allow the network’s programs to persist through the pandemic. Check out [their project on Giveth.io](https://giveth.io/project/permaculture-action-network) and make a donation to support permaculture education and environmentally regenerative tools.

That’s a wrap on this edition of the community project spotlight: Six unique projects bringing new dimensions of insight and change into the world! Want to get more eyes on your project? Coming soon on Giveth, we’ll be launching a rewards system for donors who contribute to verified projects. [Learn more](https://www.youtube.com/watch?v=9ZiGlIm2vBs) or [apply to get verified today.](https://hlfkiwoiwhi.typeform.com/to/pXxk0HO5) Stay tuned to the Giveth Medium for more project spotlights and updates on what we’re cooking up at the Future of Giving.

<img alt="Come with me if you want to give" src={useBaseUrl('img/blog/givethComeWithMeBanner.png')} />

### Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: communitySpotlight4
title: "Community Project Spotlight #4"
author: Mitch
author_image_url: /img/mitchAuthor.jpeg
image: /img/blog/projectSpotlight4banner.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'



Wow, what an exciting month it’s been since our last update. The crypto market is hitting all-time highs across the board, there’s no better time to spread the joy and make some donations to projects that are working hard to make positive changes.

<img id="resize50" alt="Project spotlight Time!" src={useBaseUrl('img/blog/projectSpotlight4meme.jpeg')} />  

We’ve got another fresh batch of five projects that we’re featuring in this fourth edition of the Community Project Spotlight. But first, we’ve got some big news! 1Hive let the cat out of the bag and gave a sneak peek of the GIVeconomy launch. Tune-in to get the insider scoop on some of the details and the UI.

<iframe width="560" height="315" src="https://www.youtube.com/embed/mIhfmmGjT8g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  

Expect to hear more about the GIVeconomy in the coming weeks ;) Now let’s dive into some awesome projects that are live [giveth.io](https://giveth.io)!

<img alt="UPF coin" src={useBaseUrl('img/blog/UPFcoin.png')} />  

## UPF Coin

We all know plastic is a problem, its impact on the environment cannot be overstated. Untangling our relationship, as humans, with plastic will be one of the great challenges of our time. UPF Coin is a project by Unplastify which, as the name implies, is on a mission to put the brakes on our consumption of plastic. Unplastify is based out of Argentina and the USA, and provides a wide range of educational and practical activities promoting unplastification.

Their primary area of interest is the crippling effects of plastic waste in our oceans. To that end in 2018 they embarked on an epic oceanic adventure where the team took off on a sailboat named “Fanky” across the Atlantic and back, collecting plastic samples and researching impacts and alternatives to plastic. Their voyage took them from the ports of New York City all the way to Corsica and back across the pond to Buenos Aires, Argentina. You can check out more of the work unplastify does on [their website](https://www.unplastify.com/).

The UPF Coin project introduces the powerful realities of blockchain and tokenization to their noble cause. At the heart of this lies a proprietary UPF blockchain which operates on a “proof of unplastify work” to distribute UPF coins. Every coin minted represents one tonne of avoided plastic consumption. Unplastification work done will be human validated by the UPF team. They plan to have a working blockchain and 25 UPF coins emitted by the end of this quarter! That’s 25 tonnes of plastic mitigated. Donations to their project will help them research and fund the deployment of the UPF token economy. [Check out UPF Coin on giveth.io](https://giveth.io/project/upf-coin) and make a donation!

<img alt="Positive Blockchain" src={useBaseUrl('img/blog/positiveBlockchain.png')} />

## Positive Blockchain

With an ever-increasing emergence of ‘blockchain-for-good’ projects, how can anyone keep up with all these amazing high vibes? Positive Blockchain is building the data-driven solution, having created the database for the blockchain-for-good universe. They maintain an impressive library of philanthropic blockchain project profiles that allow anyone to find projects working on causes they care about.

Positive Blockchain keeps track of the status of each project, whether they are in conception, began development or have already launched. From their [Impact Dashboard](https://pb.chainist.de/) you can make a wide range of queries and see statistics of what projects are working on. They use the [UN’s 17 Sustainable Development Goals](https://sdgs.un.org/goals) as part of the base metrics for querying projects. From the Social Impact Map you can see the distribution of blockchain-for-good projects worldwide.

They are asking for donations to expand their network of partners, maintain their databases and source out professional assistance in their tasks. If an excessive amount of funds are raised they will put them to expanding their network of projects in Africa. Visit the [Positive Blockchain website](https://positiveblockchain.io/) and check out [their project on giveth.io](https://giveth.io/project/positiveblockchain.io) to make a donation!

<img alt="CineFi Network" src={useBaseUrl('img/blog/cineFiNetwork.png')} />

## CineFi Network

_Coming soon to a blockchain near you! …_

The decentralization of the film industry stands to be a great boon for artists, producers, actors and viewers alike. The game-changing dynamics of blockchain are pervasive across an expansive list of modern industries. CineFi is introducing a platform to revolutionize funding and revenue streams from film-making.

The CineFi Network begins with artists submitting proposals for films they’re inspired to create. A CineFi token (CINE) will be the medium through which users can interact with proposals and films. Platform users can decide whether or not to invest funds (CINE) into bringing the film proposals into fruition. If the film reaches its funding goal a fractilized NFT is generated which represents proportional rights to creators and investors of the film, guaranteeing a cut of the revenues generated. The platform also allows users to stream or purchase these decentrally financed films with the same CINE tokens.

By this novel system, CineFi effectively allows for real-time community signalling for what films they want to see made. Thanks to Blockchain technology, creators and artists can more transparently navigate the terms on which they share revenues generated from their works. The blockchain becomes the final source of truth for where the fractalized NFTs are distributed, where funding comes from and where revenues go.

According to the [CineFi website](https://cinefi.network/) we can hope to see film proposals rolling in by around mid-2022. Checkout [CineFi Network on giveth.io](https://giveth.io/project/cinefi) to make a donation!

<img alt="Good Work Foundation" src={useBaseUrl('img/blog/goodWorkFoundation.png')} />

## Good Work Foundation

Access to modern education programmes in rural communities has always proved to be challenging; resources, budgeting and infrastructure all play a role. In Africa, these challenges create troubling disparities between populations. The Good Work Foundation (GWF) is focused on closing this gap and raising the bar. They have created a wide range of educational programmes with a focus on digital literacy. The programmes offered go from primary school students all the way to post-secondary specialized training for adults.

On Giveth, GWF is raising funds particularly for their Open Learning Academy programme, which focuses on young students in rural South Africa. On the project page they mention the staggering statistics they’re grappling with:

_“In_ **_rural South Africa_**_, of 100 South African children that start school, approximately 60 will reach and write matric (high-school graduation exam), 37 will pass, and 12 will access university. This crippling problem will be even more exacerbated going into 2022.”_

The programme intends to reach over 9,000 students from grade 4 to 8 in the municipality of Bushbuckridge in South Africa. The Open Learning Academy allows rural schools to outsource coding, robotics and digital literacy programmes to the GWF learning centre. The programme intends to support existing curriculums, rather than diverge from them, allowing participating children to build relevant skills to continue their education. You can learn more about GWF and their other programmes on [their website](https://www.goodworkfoundation.org/). Be sure to check out [their project on giveth.io](https://giveth.io/project/gwf-giving-tuesday-2021) and make a donation to support rural African education!

<img alt="Co-funding the DAOist" src={useBaseUrl('img/blog/cofundingDAOist.gif')} />

## Co-funding the DAOist

The Decentralized Autonomous Organization (DAO), as a concept, is reforging the archaic methods of how we organize and govern as humans. DAOs represent not just a technological blockchain breakthrough, but also a cultural force to be reckoned with. DAOs in effect allow organizations to form organically and continually evolve, leaning on blockchain transparency and computer-aided governance systems. The technology we use to create DAOs is constantly iterating upon itself however we as humans remain as the constant base layer, “**_Layer 0_**”.

The DAOist is a DAO (aptly so) that intends to capture this social phenomenon and to incubate resulting ideas, collaboration and cultural practices. This takes form as live and virtual events held around existing events in the Ethereum community. They host conferences where DAO champions can come and share experience and knowledge and to build partnerships with other value-aligned communities.

Their first event was in [Paris for EthCC4 in July of 2021](https://www.youtube.com/watch?v=hBV5All5yM8). It was a huge success and the people demanded more, so they [hosted a second one in Lisbon](https://www.youtube.com/watch?v=U5aUHWDU7jg), in October, of the same year. Their instant success has only proven that there’s a real desire to open up a space for DAOs to share and learn. To that end, they want to create educational spaces, physical and virtual, to empower DAOs. They are also in the process of defining their DAO structure. The DAOist is seeking funds in order to continue to host events and to create a year-round space for DAO enthusiasts to meet, collaborate and learn. Check out [their project on giveth.io](https://giveth.io/project/cofunding-the-daoist) to make a donation!

That’s a wrap for this one! Five projects shaking things up in our virtual and physical worlds. The digital realms being constructed are only becoming more ground-breaking and people are taking notice. Digital technology, particularly blockchain, is poised to revolutionize a wealth of domains, from education, arts, the environment, to even the fundamentals of how we organize.

Keep your eyes peeled for more details on the next phase of Giveth, it’s going to be BIG! Of course, we’ll have more projects to spotlight soon enough so **_watch this space_**.

### Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: givethDAO
title: "The Giveth DAO: Community GIVernance"
author: Dani
author_image_url: /img/blog/DaniAuthor.jpg
image: /img/blog/givethDAOblog.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'



Giveth has a long [history of experimentation](https://medium.com/giveth/the-unicorndac-a-non-hierarchical-decentralized-governance-experiment-8dfbe6e98d19) in the decentralized governance realms.

Before becoming a [DAO](https://xdai.aragon.blossom.software/#/nrgiv/0x749cccd03c00110cf76f4e009c6eaf59b5f2bd0e/) (with a [DAF](https://www.sdgimpactfund.org/giveth-foundation)), Giveth fund allocation was administered by a [Unicorn DAC](https://trace.giveth.io/community/unicorn-dac) — A Decentralized Altruistic Community — trying out new ways of governing the build and use of our DApp (Donation Application).

<img alt="rGIV Trace Header" src={useBaseUrl('img/blog/rgivDAOtraceHeader.png')} />  

Decisions for how to distribute incoming donations to the Giveth DAC across our platform were made by nominated and approved team members, who met regularly to evaluate Traces (formerly Milestones). From rewarding contributors to funding initiatives that further #blockchain4good, each Unicorn allocated a portion of funds to deserving people and projects every two weeks.

<img alt="Unicorn DAC donations" src={useBaseUrl('img/blog/rgivDAOleaderboard.png')} />  

###### On-chain (Rinkeby) tracking of the original Giveth DAO — [The Unicorn DAC at trace.giveth.io](https://trace.giveth.io/community/unicorn-dac)

Our “GIVernance” has matured significantly in preparation of launching the [GIVeconomy](https://youtu.be/mIhfmmGjT8g). We’ve learned a lot along the way and are excited to share where the Giveth Reputation DAO (rGIV DAO) is now.

## How does Giveth DAO it?

Within Giveth, we strive to demonstrate these principles:

*   To value transparent, holistic governance and work to be a shining example of it.
*   To explore and readily adopt new innovations that support us in embodying these values.
*   To practice the self-organizing power of sociocracy, which we apply in the organization of tasks, participation in the [Proposal and Advice Process](../whatisgiveth/adviceProcess/), and facilitation of our governance meetings.

Our [GIVernance Circle](../whatisgiveth/introGIVernance) Mission Statement reflects this foundational intention:

> We **_are progressively decentralizing the Giveth decision-making process by building a community and a token-based economy around our platform that recognizes contributions, values participation and rewards altruism._**

The Giveth DAO is made up of [people](https://giveth.io/about) who have acquired reputation and trust through perseverance and dedication to the Future of Giving by participating in building the Giveth community and our Donation Applications (DApps).

## nrGIV — The Reputation Token for Stewarding the GIV launch

<img alt="the nrGIV DAO" src={useBaseUrl('img/blog/rgivDAOnrGIVvoting.png')} />  

Minting the new reputation tokens (nrGIV) to replace the old (rGIV) on Aragon.

While most activities take place off-chain in our [publicly accessible forums](https://forum.giveth.io) and [live-streamed meetings](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg), the community has implemented and recently renovated an on-chain solution. Deployed via [1Hive](http://1hive.org) as an Aragon Reputation DAO using the [xDai chain](https://www.xdaichain.com/for-users/getting-started-with-xdai), it is designed to evolve along with the advancements of our own protocols as well as those of Ethereum collaborators and eventually, multi-chain ecosystems.

It has 3 primary stewardship responsibilities:

1.  Stewarding the existing Giveth commons ([Giveth Multisigs](https://docs.google.com/spreadsheets/d/1q_5VFt9C3pX-A5V0UYRSefoNPHfn3GDvEywXGvdj7cw/edit#gid=1931334782), [Giveth.io](http://giveth.io), [Trace.giveth.io](http://trace.giveth.io), and soon to launch GIVeconomy DApps)
2.  Stewarding the GIV token initial distribution.
3.  Stewarding the [Progressive Decentralization](https://a16z.com/2020/01/09/progressive-decentralization-crypto-product-management/) of the GIVeconomy.

## Why participate?

Reputation is earned over time, but rewards are dished early and often to recognize value and encourage participation in the Giveth Community.

We [!praise](../whatisgiveth/introDiscord#praisebot) you for:

*   Attending meetings and speaking up in Discord
*   Testing and using our tools
*   Feedback into development for improvement
*   Maintenance of our living processes
*   Writing and reviewing documentation
*   Talking about us on social media (criticism welcome, just be kind about it!)

Monthly tabulation of [Praise](https://trace.giveth.io/campaign/rewarddao) and [SourceCred](https://sourcecred.io/) results in the disbursement of ETH, DAI, and/or PAN tokens, depending on what’s been donated to Giveth. We give what we’ve got, and the more you give, the more you get!

Over time, new contributors can build reputation in the community and become eligible for nrGIV tokens that are minted on a quarterly basis. **In this way we co-create a community of builders that are self-organized by design, decentralized by technology, and altruistic by nature.**

## Who Qualifies? It Starts with Showing Up!


**Anyone can earn rewards by engaging in the Giveth community**

Praise is our way of saying thanks for being awesome. The first 20 minutes of our [weekly Community Call](https://calendar.google.com/event?action=TEMPLATE&tmeid=MW5zazNraGxzbmZza3EzcDJlYmpnaWd1YjYgZ2l2ZXRoZG90aW9AbQ&tmsrc=givethdotio%40gmail.com) are dedicated to celebrating who did what for the past week. By using the PraiseBot, !praise can be given in any channel on the Giveth Discord server at any time, and we even have a dedicated [#praise channel](https://discord.giveth.io) because there are so many people doing great things.

All those **_thank you_**’s are captured in a spreadsheet and reviewed by the Working Group Stewards every four weeks, to use in combination with SourceCred for allocating a percentage of the available Rewards to contributors. This practice of !praising contributors transparently and distributing rewards was kicked off 4 years ago with the [first PraiseBot built for Giveth](https://github.com/Giveth/giveth-bot) on Matrix and now carried forward by [Commons Stack](http://commonsstack.org) and the [Token Engineering Commons](http://tecommons.org)!

<img alt="Giveth.io join page" src={useBaseUrl('img/blog/rgivDAOjoinPage.png')} />  


**Givething Cred for contributions through Discord, Discourse, & GitHub**

As a global digital community, we recognize that while much of what we do is seen by others — a lot is also just happening organically online and can be quantified to some extent by using data analytics.

When you engage in our community discussions on Discord, participate in the soft governance via our Discourse forums, and create or work on issues in the GitHub repositories, these interactions are recorded and gathered into a [SourceCred dashboard](https://cred.giveth.io/#/explorer).

**Consistency builds Reputation, and earns Trust**

Contributors qualify for nrGIV (Giveth Reputation Tokens) after 3 months of participation as recorded via the Praise and SourceCred calculations reviewed monthly. These tokens are minted quarterly for new and active contributors. Those no longer contributing do not receive more nrGIV — but do retain all of the tokens previously received.

## When did Giveth move to On-chain Governance?

> The original rGIV DAO instance can be seen [here](https://aragon.1hive.org/#/giveth/0x8ce560c4e8ddc2f735044140e677cc936a68dd6a/), where we launched with 1,111 tokens distributed to each of the 8 Giveth Reputation DAO co-founders in January 2021 for the previous year.

<img id="resize50" alt="current contributor spreadsheet" src={useBaseUrl('img/blog/rgivDAOcurrentContributors.png')} />  

2,222 tokens were minted for each qualifying contributor in April for January-March 2021, then [3,333 in July](https://forum.giveth.io/t/passed-rgiv-token-distro-q2-contributors/52) for April-June. As in any good experiment, discoveries arose from these iterations and in October 2021, the rGIV DAO voted to retire the rGIV token in favor of creating a new instance (nrGIV) with several configuration changes, including the move from 1,111 to 1, ditching the extra digits.

**_Also changed in this new rGIV DAO: the distribution of tokens now follows a Fibonacci sequence. This means that the number of tokens minted for each contributor in the latest period is equal to the sum of the two previous two periods._**

As shown, [Dani](https://twitter.com/TheOfficeMystic) has been contributing since day 1. She earned 1 token to vote with the first period (1,111 — which was converted to 1 in the new simplified DAO), 2 tokens for the second period, 3 tokens the third period (because 1 + 2 = 3), and 5 tokens the fourth period (because 2 + 3 = 5). If she stops contributing there, she will retain her total balance of 1 + 2 + 3 + 5 = 11 nrGiv tokens for voting on governance proposals after the 4th period. If she continues consistently contributing to the Giveth Community, she will always have at least 1 token more than any contributors that came in later.

<img alt="the nrGIV DAO token holders" src={useBaseUrl('img/blog/rgivDAOtokenHolders.png')} />  

[James](https://twitter.com/positonic) is a co-founder of the rGIV DAO, and received tokens for periods 1, 2, and 3. He resigned during the 3rd period to focus on [toucan.earth](https://toucan.earth/), and did not contribute during the 4th period, so does not qualify for the minting of 5 tokens. His voting weight remains at 6 tokens, while current contributors weight grows to 11. In this case where a past contributor does not return for 6 months and misses 2 full periods, their voting weight is now lower than a new contributor receiving nrGIV tokens during those two mintings.

So in this example, new contributors in periods 4 and 5 receive 8 tokens (3 + 5) bringing their total to 12 (5 + 8) — double that of James. When James returns, he will come in with his previous token weight and after another 3 months of contributions, qualifies to again receive nrGIV tokens.

In this way new contributors can gain as much influence as someone who has contributed in the prior two time periods, and over time the influence of past contributors is reduced after exiting the community. Behind this design is an assumption that those currently contributing can make the most informed vote about current governance of the organization. For consistent contributors who have been around from the beginning, those joining later will never reach or surpass your voting power, incentivizing retention of talent and wisdom for the community while incrementally fractionalizing the lead.

> Successful decentralized governance has been shown to require a healthy balance of new contributors being valued early, and long-time contributors valued for carrying the vital threads of vision, mission and information on the organization from past experience.

Note: If you are on maternity or paternity leave, you still get the period’s token allocations during leave.

## What is the nrGIV token used for?

**Voting on proposals that build the #FutureofGiving**

Anyone can make a proposal to the rGIV DAO, whether they are an nrGIV token holder or not. But first! Giveth follows a Sociocratic proposal-forming process by soliciting opinions and clarifying questions initially, then making revisions and polling for support via an Advice Process on our forum.

> **Previously hosted on** [**Loomio**](https://www.loomio.com/)**, you can see the proposal process** [**used to initiate the rGIV DAO**](https://www.loomio.org/d/4TKQjvCg/configuring-giveth-dao-rep-token-on-aragon-1hive) **here!**

In 2021 Giveth revised its organizational structure into new Circles and Working Groups while launching a [new proposal management method on Discourse](https://forum.giveth.io/):

<img alt="the giveth forum" src={useBaseUrl('img/blog/rgivDAOforum.png')} />  

## From Off-chain Advice to On-chain Voting

After a proposal has been reviewed, the champion (person writing and advocating for the proposal) can post a new Vote to the rGIV DAO! Once made, nrGIV token holders have 5 days to use their tokens and vote “yes” or “no”. Voting on each proposal in this DAO allocates your fully accrued nrGIV token quantity; and you do not lose them if you vote. In other words, if you have 7 tokens, and you vote “yes,” then 7 nrGIV tokens are added to the total “yes” votes while the tokens remain in your wallet. When you vote on other proposals, you still have 7 nrGIV tokens to vote on those as well.

> **The Giveth Reputation DAO does not use Conviction Voting or require you to “stake” your reputation tokens — you never lose your tokens or have to choose which proposal to use them on; you always have the same number of tokens to vote with for each new proposal.**

In order for a proposal to pass, it must have a majority of yes votes, and reach a “minimum approval” level, which we’ve set at 25%. If a proposal doesn’t have more than 25% of all minted tokens voting yes on it, it automatically does not pass regardless of the distribution of “yes” and “no” votes given. However, the proposal can always be proposed again and voted on again.

The second metric within each vote is the “Support” level. We have set that at 88%. If a vote reaches this level, it has more than the majority by a large margin and is labeled as having strong support. The third metric set by the DAO is “vote duration”; how much time must pass before voting is closed.

Which Decisions Does the Giveth Reputation DAO Need to Vote on?
===============================================================

The rGIV DAO has the responsibility for governing the GIVeconomy launch and our commons. This means that the assets built by the Giveth community and the funding received from donors to support Giveth are owned by the Community itself — the Givers and Makers contributing their skills, time, energy and resources to it. So deciding how to build the DApps, contract with individuals to fill roles on the team, and distribute funds to the Circles for maintaining operations and development of the open source code is a job for nrGIV token holders that collectively make up the rGIV DAO.

The road to decentralized governance has been paved with the bricks of this goodwill, and you can see again in Loomio how the Giveth Unicorn DAC used the Advice Process and voting to decide how to [allocate a 285 ETH gift in 2019](https://www.loomio.org/d/Sbn1FeT7/285-eth-what-am-i-gonna-do-)!

The Giveth Reputation DAO has the opportunity to do this again now as we contemplate allocation of the proceeds from [Rainbow Rolls](https://medium.com/rainbow-rollup/nftps-rainbow-rolls-7a01d5eb1bb2) and the [Optimism Retroactive Public Goods Grant](https://medium.com/ethereum-optimism/retropgf-experiment-1-1-million-dollars-for-public-goods-f7e455cbdca). Balancing the upcoming needs of the Community to sustain itself through launching the GIVeconomy this year, and to reward the contributors who worked tirelessly in past years to earn the respect and the funding, is the responsibility of the current DAO members.

<img alt="rainbow rollup donation" src={useBaseUrl('img/blog/rgivDAOrainbowRoll.png')} />  

If this is a subject that interests you enough to have read this whole post, perhaps you are interested in contributing to the Giveth commons by participating in our off-chain Advice Process on the current decision regarding [how to allocate the funds from Rainbow Rolls](https://forum.giveth.io/t/what-to-do-with-the-eth-from-rainbow-rolls/173)!

We are a donor-focused organization and in order to build what meets the needs of our donors AND project owners, we welcome and encourage your donations AND your suggestions.

<img alt="spice girls - tell me what you want" src={useBaseUrl('img/blog/rgivDAOmeme1.jpeg')} />  

## Giveth DAOs Donations


Giveth is run entirely on donations, which can be given through a variety of routes including the [DAC on TRACE](https://trace.giveth.io/community/giveth-dac), the [Project at Giveth.io](https://giveth.io/project/the-giveth-community-of-makers), [Gitcoin Grants](https://gitcoin.co/grants/795/givethio-panvala-league), and direct contributions to the MultiSig wallet address. Some of these are given by charitable entities with specific intention and others are unconditional gifts — through [trace.giveth.io](https://trace.giveth.io) you can select the exact purpose of your gift yourself.

Stay tuned to our [Discourse Forum and Discord Chats](http://giveth.io/join) as we launch the GIVeconomy, and feel welcome to chime in as we structure the longer-term transition of governing the Giveth commons from the rGIV token holders to the GIV token holders using [the GIVgarden by 1Hive](https://twitter.com/Givethio/status/1466827058793832451)!

> **_Become part of the #FutureofGiving on_** [**_Giveth.io_**](http://giveth.io) **_by donating to any project with a Verified badge, and you can begin your journey as a Giver by qualifying to receive GIV tokens… the Future of the Giveth DAO._**

### Want to get more involved?

*   Join us on [Discord](https://discord.giveth.io) or [Telegram](http://t.me/givethio)
*   Discover our [Docs](https://docs.giveth.io/)
*   Fork our code on [GitHub](https://github.com/Giveth/)
*   Follow us on [Medium](http://medium.com/giveth/), [Twitter](http://twitter.com/givethio), [Reddit](https://www.reddit.com/r/giveth/) and [YouTube](https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ)

Help us Build the Future of Giving: 🦄 [Donate directly](http://donate.giveth.io/) 🦄 or [buy a Ledger with our affiliate link](https://www.ledgerwallet.com/products/ledger-nano-s?utm_source=&utm_medium=affiliate&utm_campaign=d663)
---
slug: welcomeGIVeconomy
title: Welcome to the GIVeconomy
author: Lauren
author_image_url: /img/laurenAuthor.png
image: /img/blog/GIVeconomyBanner.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

_It is our great pleasure to officially introduce the GIVeconomy — an economy that rewards and empowers those who give to projects, to societies, and to the world._

<iframe width="560" height="315" src="https://www.youtube.com/embed/LEw8PaJylNA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

At Giveth, we’ve been Building the Future of Giving [since day one](https://medium.com/giveth/giveth-donation-3-0-the-soft-launch-bf00d3bddca8). We [started in 2016](https://docs.giveth.io/whatisgiveth/history/) by writing the [MiniMe token](https://medium.com/giveth/the-minime-token-open-sourced-by-giveth-2710c0210787) and the [Vault](https://medium.com/giveth/the-vault-contract-open-sourced-by-giveth-fe2261f7b91b) contracts, building open-source infrastructure and using it for our donation applications (DApps). Fast forward to this year, we released [giveth.io](https://giveth.io/) for [streamlined P2P giving](https://medium.com/giveth/the-future-of-giving-is-here-d480388a3338) and [Giveth TRACE](https://www.trace.giveth.io/) for [customizable fund management and traceable donations](https://medium.com/giveth/giveth-trace-is-live-e91b0be1e1f6), both powered by blockchain technology. These are the building blocks that we’ve been developing to realize our vision for the future. A future in which…

> _Giving is effortless and people all around the world are rewarded for creating positive change._

Today, our dreams enter reality as we proudly announce the GIVeconomy: An economy that supports projects that create value for society and encourages on-the-ground change-makers to enter web3. An economy that empowers and rewards donors for giving. And, fundamentally, **an economy that is owned and governed by those who give.**


<img alt='giveconomy banner' src={useBaseUrl('img/blog/GIVeconomyBanner.png')} />

## The GIV Token


GIV is the governance token that fuels and directs the GIVeconomy. GIV holders are empowered to collectively coordinate around shared resources and fund initiatives that shape the Future of Giving.

### Token Info


*   Token Address on Mainnet: 0x900db999074d9277c5da2a43f252d74366230da0
*   Token Address on xDai: 0x4f4F9b8D5B4d0Dc10506e5551B0513B61fD59e75

### Distribution


At inception, the GIVeconomy has an initial circulating supply of 17.05 million GIV which is available to claim by the Giveth “trusted seed” in the GIVdrop. The distribution of all GIV across the GIViverse is as follows:

<img alt='GIVdrop distribution' src={useBaseUrl('img/blog/tokenDistribution.png')} />

Past contributors, crypto donors & Giveth users make up 17.05% of the GIViverse. We’ve allocated 26.95% of GIV to future contributors, the [rGIV DAO treasury](https://medium.com/giveth/the-giveth-dao-community-givernance-84f55fa1ce36) & future roadmap projects (described at the end of this post) as part of our [progressive decentralization](https://a16z.com/2020/01/09/progressive-decentralization-crypto-product-management/). The rest is fueling our GIVeconomy pillars:

*   33% allocated to the [GIVgarden](https://giveth.io/givgarden) common pool to fund proposals governed by GIV holders with [conviction voting](https://forum.giveth.io/t/conviction-voting/154).
*   13% allocated to reward donors to verified projects with GIV from our [GIVbacks](https://giveth.io/givbacks) program.
*   10% allocated to reward liquidity providers and stakers in the [GIVfarm](https://giveth.io/givfarm).

## The GIVdrop


To initialize a DAO led by Givers, we have created the [GIVdrop](https://giveth.io/claim). With the GIVdrop, 17.05% of the initial supply has been distributed to the Giveth trusted seed — crypto philanthropists, Giveth users & contributors, and [Blockchain4good](https://twitter.com/search?q=%23blockchain4good&src=typed_query) heroes. These are value-aligned individuals that have been working, directly or indirectly, to further [Giveth’s mission](https://docs.giveth.io/whatisgiveth/), and now are being brought into an ecosystem of collective support, abundance and value-creation. With no VCs or presales, **the GIVeconomy is kicked off by the donors, of the donors and for the donors.**

To read more about the GIVdrop and eligibility, [check out our documentation](https://docs.giveth.io/giveconomy/givdrop) or [see if you qualify](https://giveth.io/claim).

## The GIVstream


[The GIVstream](https://giveth.io/givstream) provides a continuous flow of GIV to GIVeconomy participants. We call it _the expanding GIViverse_. The GIVeconomy begins humbly but as time passes, the GIViverse expands and GIV is streamed out to our community of GIVers. **In this way, as the GIVeconomy grows & stabilizes, we empower those who support the Giveth ecosystem with increasing governance rights.**

<img alt='GIVstream expansion' src={useBaseUrl('img/blog/GIViverseExpansion.gif')} />

###### h/t [@RodriCastillo](https://twitter.com/_rodricast) for the awesome GIF

Those who receive the GIVdrop also receive a GIVstream. Anyone can increase their GIV/week flowrate by participating in the GIVeconomy through [GIVbacks](https://giveth.io/givbacks), the [GIVgarden](https://giveth.io/givgarden) or the [GIVfarm](https://giveth.io/givfarm). To learn more, [check out our documentation](https://docs.giveth.io/giveconomy/givstream) or [see your GIVstream flowing](https://giveth.io/givstream).

## GIVeconomy Starting Line

We’re launching the GIVeconomy with three key pillars — GIVbacks, the GIVfarm, and the GIVgarden.

### GIVbacks

<img alt='GIVbacks meme' src={useBaseUrl('img/blog/GIVeconomyMeme1.png')} />

###### h/t to [@griff](https://twitter.com/thegrifft) & our #Meme channel in [Discord](https://discord.giveth.io/)

**GIVbacks is a paradigm shift for the donation space. Instead of** [**relying on sacrifice to drive value creation**](https://youtu.be/PFy458wCQ0g?t=504)**, we are _rewarding_ the givers.** With GIVbacks, 1 million GIV is available to give to donors to verified projects on Giveth every 2 weeks!

The GIVbacks program has multiple advantages:

*   It attracts donors — and therefore great projects — to Giveth.
*   It ensures the quality of projects on Giveth using our [Project Verification](https://docs.giveth.io/giveconomy/givbacks#project-verification) system.
*   It “gives back” to donors for supporting on-the-ground teams adding value to society.
*   **It gives donors governance rights so they can direct the Future of Giving.**

Thanks to our verification team and our recent integration with [The Giving Block](https://twitter.com/TheGivingBlock), Givers have over 700 fully-vetted projects to choose from! To learn more about GIVbacks, [check out our documentation](https://docs.giveth.io/giveconomy/givbacks)**.**

### GIVgarden

<img alt='giveconomy banner' src={useBaseUrl('img/blog/GIVeconomyMeme2.png')} />

###### h/t [@mateodaza](https://twitter.com/mateodazab) & our #memes channel in [Discord](https://discord.giveth.io/)

The [GIVgarden](https://giveth.io/givgarden) is the decentralized governance platform for Giveth and the GIVeconomy. [Powered by 1hive](https://gardens.1hive.org/), the GIVgarden is where GIV holders can make and vote on proposals to fund value-aligned initiatives that shape the Future of Giving. It has four main components:

1.  [Conviction Voting](https://medium.com/giveth/conviction-voting-a-novel-continuous-decision-making-alternative-to-governance-aa746cfb9475) for fund management
2.  [Tao Voting](https://forum.giveth.io/t/tao-voting-explained/155) for executing on-chain decisions
3.  [Our Covenant](https://docs.giveth.io/whatisgiveth/covenant/) that outlines standards for on-chain and off-chain community behaviour, and
4.  [Celeste](https://1hive.gitbook.io/celeste/) as a decentralized court to settle disputes.

To learn more about the GIVgarden, [check out our documentation](https://docs.giveth.io/giveconomy/givgarden)**.**

### GIVfarm

<img alt='givfarm homepage' src={useBaseUrl('img/blog/GIVfarm.png')} />
![](https://miro.medium.com/max/1400/0*GHRbTc7_MidaoMI9)

For the GIVeconomy to function, GIV must be easy to acquire. The [GIVfarm](https://giveth.io/givfarm) is the place to grow and harvest rewards while supporting the GIVeconomy by providing liquidity for GIV! We have farming opportunities on Ethereum Mainnet (ETH) and xDai Network (Gnosis chain), and 35 million GIV are allocated to the rewards program for the first 6 months. A further 65 million GIV has been allocated to provide future farming opportunities. Farms are LIVE now and rewards are BOUNTIFUL! 🌾 [Check it out here](https://giveth.io/givfarm) or  [read more in our documentation.](https://docs.giveth.io/giveconomy/givfarm) h/t to our partners at [DAppNode](https://dappnode.io/) and [BrightID](https://www.brightid.org/) for supporting GIVfarm development!

## Future Plans


The launch of GIV and everything above is only the beginning for the GIVeconomy — we’re already crafting the next phase in the Future of Giving. We’re developing systems that completely change the way societies create and reward the creation of public goods.

<img alt='future plans meme' src={useBaseUrl('img/blog/GIVeconomyMeme3.png')} />

###### h/t [@karmaticacid](https://twitter.com/karmaticacid) & our #memes channel in [Discord](https://discord.giveth.io/)

We’ve pre-allocated 80 million GIV to fund the development of the following projects. These ideas are raw, exciting, and beautiful and we are heaven-bent on bringing them to fruition! Here’s a quick breakdown of what we’re planning next.

### GIVcuration


GIVcuration will decentralize GIVbacks! Community members will be able to signal support by staking GIV on projects, and their signal will grow like in [Conviction Voting](https://forum.giveth.io/t/conviction-voting/154). In GIVbacks rounds, donors who give to community-favoured projects will get more GIVbacks, and GIVcurators will earn rewards on their staked GIV.

### GIVmatching


We plan to implement a donation matching system for projects on Giveth using _Causes_. Donors will be able to donate to Cause categories — like environmental regeneration or open-source software — and the funds collected will then be distributed to projects using [quadratic funding](https://wtfisqf.com/?grant=&grant=&grant=&grant=&match=1000), h/t to our friends at [Gitcoin](https://gitcoin.co/).

### GIVfi

The intention with GIVfi is to create a sustainable way of maintaining funds in the GIVgarden common pool. While donations on the DApp are waiting to be disbursed, they will be generating interest that can be used to buy GIV on the open market and send it to the GIVgarden for funding initiatives using Conviction Voting.

### GURVES


This is the real dream! We want projects on Giveth to evolve into their own microeconomies, and for the platform to become a place for crypto impact investment. This is _GURVES_ ([working title](https://www.youtube.com/watch?v=9ZiGlIm2vBs&t=1093s)) — GIV token holders who stake GIV on a project will eventually be able to “opt-in” to initialize a GIV-backed [bonding curve](https://medium.com/commonsstack/the-augmented-bonding-curve-part-1-a-web3-way-to-fund-public-goods-7c9d1a871ae2) for that project.

<img alt='gurves meme' src={useBaseUrl('img/blog/GIVeconomyMeme4.jpg')} />

###### h/t [**@karmaticacid**](https://twitter.com/karmaticacid) **& our #memes channel in** [**Discord**](https://discord.giveth.io/)

With GURVES, the GIVbacks program will transform! Whenever donors donate to a GURVE project, they will get GIVbacks and some of that GIV will go into the GURVE to mint them “project tokens” & in effect, raise the price of the project token. This way, non-profits who advance in the Giveth ecosystem earn **their own economic systems that will turn donors into investors and volunteers into shareholders.**

But wait, there’s more…
-----------------------

The core team at Giveth is committed to executing the above roadmap, but this is a DAO and we aren’t alone in steering the ship! 33% of the token supply has been allocated to the [GIVgarden](https://giveth.io/givgarden) common pool to fund the proposals that the Giveth community believe in.

Giveth has been in the crypto donation scene [since 2016](https://twitter.com/Givethio/status/1454084287184130049). We rescued 210 million dollars from the [Parity multisig attack](https://mashable.com/article/ethereum-stolen-white-hat-group-rescued#ZPTC98wSEPOp), we ran the first [scaling-focused Ethereum conference](https://medium.com/giveth/scalingnow-summit-transcript-ea5373be8523), we created fee-free donation applications, we implemented smooth on-ramps for nonprofits to enter the crypto scene, and that was all solely funded by donations.

The launch of the GIVeconomy is a huge milestone but still just one more step towards building a Future of Giving that we can all be proud of. A future where value-creation for society is rewarded, where altruism becomes profitable, where communities of value-aligned supporters grow and prosper. A future in which we regenerate the earth, we build meaningful connections with each other, we revolutionize economic systems, evolve human coordination and we create societies based on decentralization, freedom, community and **love**.

[**Welcome to the GIVeconomy**](https://giveth.io/)
-------------------------------------------------------
---
slug: evolvingPhilanthropy
title: What if giving gave back? Using web3 to evolve philanthropy.
author: Lauren
author_image_url: /img/laurenAuthor.png
image: /img/blog/GIVbackBanner.png
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


_The Giveth mission is to reward & empower those who give — to projects, to society, and to the world. With GIVbacks, we’re rewarding givers by giving GIV to donors to verified projects on Giveth._

<img alt='what if giving gave back' src={useBaseUrl('img/blog/GIVbackBanner.png')} />


Web3 and, specifically, Ethereum have the potential to revolutionize the philanthropic space. We have the tools to open new funding streams and create economic abundance for everyone who is providing value to society.

Clean air, clear water, bridges, roads, free childcare, public education, taking care of the less fortunate — these are all examples of public goods that, when governments fail to provide them, we look to non-profits to create and care for. For funding, we have been relying on donors to give to these non-profits and receive nothing in return. Society has been depending on and [ultimately exploiting the altruists](https://youtu.be/PFy458wCQ0g?t=504) who are working hard to protect and provide for our collective needs.

**GIVbacks is a paradigm shift for the donation space. For the first time ever, there is an economic upside to donating.**

<img alt='givbacks meme' src={useBaseUrl('img/blog/GIVbacksMeme1.png')} />

GIVbacks is the first step towards a world in which everyone benefits from creating value: **when you give to verified projects, 100% of your donation goes directly to the project, and you get** [**GIV**](https://docs.giveth.io/giveconomy/#about-giv) **from Giveth!**

With over 900 verified projects on Giveth, donors can find projects that speak to their values and get rewarded for giving. Verified projects benefit from the extra traffic on Giveth & can use this program to attract new donors who are willing to support their initiatives.

## The Big Picture


Before we get into the fine details of exactly how the GIVbacks program works, let me walk you through the big picture that is the “why”.

### Projects should feel good about raising funds for their project


Charity has traditionally created a dynamic where projects who do good work to benefit society have to beg for funds to make the world a better place. On the flip side, donors are being asked to sacrifice — to give without expecting anything in return.

<img alt='givbacks meme' src={useBaseUrl('img/blog/GIVbacksMeme2.png')} />


GIVbacks is changing that. Donors have the opportunity to support projects they believe in, get GIV in return, and start or increase their [GIVstream](https://giveth.io/givstream). They can use that GIV to grow their rewards by, for example, staking in the [GIVfarm](https://giveth.io/givfarm). It’s a win/win: Projects benefit from receiving 100% of the donation, and donors benefit by earning GIV and becoming part of the Giveth ecosystem.

### GIVbacks gives governance power to the donors using Giveth

<img alt='givbacks meme' src={useBaseUrl('img/blog/GIVbacksMeme3.png')} />


Giveth is of the donors, by the donors, and for the donors. [Our GIVdrop](https://giveth.io/claim) was sent to the Blockchain4good community — [and particularly crypto donors & Giveth users](https://docs.giveth.io/giveconomy/givdrop/) — because we wanted to kickstart the [GIVeconomy](https://giveth.io/) with value-aligned GIVers. Now, as the economy expands, we want the donors who are using the platform and giving to causes they care about to get proportionally increasing governance power. With GIVbacks, the more you give, the more GIV you get, and that GIV can be used in the [GIVgarden](https://giveth.io/givgarden) to decide which proposals get funded to expand the GIVeconomy.

### GIVbacks are like tax-deductible donations but without governments and borders

<img alt='givbacks meme' src={useBaseUrl('img/blog/GIVbacksMeme4.png')} />


Let’s face it, tax-deductible donations can be a bit of a headache. Nonprofit projects have to cut through miles of red tape and donors have to do accounting each year, saving associated paperwork for some arbitrary number of years.

GIVbacks provides a similar end, but cuts the bureaucracy. If a project can prove they are legitimately adding value to society, they can become a verified project in the GIVbacks program, no matter what their legal or DAO structure is. If a donor is moved by a verified project’s work, they can give and receive GIV in return, no matter where (or if) they pay taxes. No need to save receipts or paperwork for fear of getting audited. Web3 makes it so that we don’t need governments and taxes to make this kind of system. We can transcend borders to connect people with projects anywhere in the world!

### GIVbacks educates community members about web3

<img alt='givbacks meme' src={useBaseUrl('img/blog/GIVbacksMeme5.png')} />


The long-term vision of Giveth is to enable for-good projects to use token engineering and DAO coordination on the ground. GIVbacks is [the first step towards achieving this goal](https://youtu.be/VV7TmNILk6o?t=1640). With GIVbacks, ordinary donors start learning about and getting curious about DAO tools like [token streams](https://docs.giveth.io/giveconomy/givstream), [DeFi](https://docs.giveth.io/giveconomy/givfarm) and [token-weighted voting](https://docs.giveth.io/giveconomy/givgarden). Furthermore, when donors get GIV, they are naturally inclined to donate it! In GIVbacks round 1, 75% of the total value of donations to verified projects on our platform were in GIV.

With the GIVbacks program, both donors and projects receive GIV and start looking into how to grow their earnings, swiftly falling down the web3 rabbit hole via [giveth.io](https://giveth.io/).

### GIVbacks will evolve into a system that transforms successful projects into DAOs and donors into impact investors

<img alt='givbacks meme' src={useBaseUrl('img/blog/GIVbacksMeme6.png')} />

GIVbacks as it is today is the first step on a path to expand Giveth into a place [where nonprofits can become microeconomies](https://youtu.be/VV7TmNILk6o?t=1356). Next, we plan to introduce GIVcuration — a system where users can stake their GIV on projects they care about, signaling support while earning a yield. A successful project in the GIVcuration system will eventually be able to get its own GIV-collateralized [bonding curve](https://medium.com/commonsstack/the-augmented-bonding-curve-part-1-a-web3-way-to-fund-public-goods-7c9d1a871ae2), called a ‘[Gurve](https://www.youtube.com/watch?v=9ZiGlIm2vBs&t=1093s)’.

When donors support a project with a Gurve, their GIVbacks get split: they get some GIV, and [some GIV goes into the Gurve, minting the donor ‘project tokens’](https://youtu.be/VV7TmNILk6o?t=1356), thereby increasing the price of the project tokens.

Before getting a Gurve, a project will need to set up a [rewards system](https://forum.tecommons.org/t/outlining-the-rewards-system-process-v2/646) to distribute their ‘reputation tokens’ to volunteers and on-the-ground supporters. When their Gurve is initialized, those reputation tokens turn into ‘project tokens’, and the project can use token-weighted voting systems to govern their donations.

With Gurves, a successful project on Giveth will be able to become a sustainable DAO, governing its own economy, with its supporters as stakeholders and donors as impact investors!

## The Fine Details


So how exactly does this program work? Well, it makes use of a system for verifying projects on Giveth, and tracks donations to those projects in 2 week “rounds”. Let’s dig into the details.

### Verified Projects

“Verified” is a seal of approval for legitimate projects on Giveth. Many Verified projects came pre-vetted from [The Giving Block](https://twitter.com/TheGivingBlock) API. The Giving Block is an organization that supports and onboards registered 501c3s from the United States into crypto, and with our integration you can donate to their projects from the Giveth UI.

For non-Giving Block projects, project owners need to fill out a [typeform](https://giveth.typeform.com/verification) and answer some questions. Verified Projects need to show that they are doing work to create [non-excludable](https://www.khanacademy.org/economics-finance-domain/microeconomics/market-failure-and-the-role-of-government/externalities-topic/a/public-goods-cnx) value for society and that they have some reputation at stake that would prevent them from gaming or manipulating the GIVbacks program for personal gain.

Our amazing Project Verification Team then reviews these applications, investigates the information provided & informs the project owners about the verdict. Approved projects will have their Verified badges [at the start of the very next GIVbacks round](https://docs.giveth.io/giveconomy/givbacks#project-verification). You can learn more about the project verification process and qualifying/disqualifying factors in our [GIVbacks documentation](https://docs.giveth.io/giveconomy/givbacks/).

<img alt='verified badge' src={useBaseUrl('img/blog/GivethIOdonateButton.png')} />


**Getting your project verified builds a relationship of trust with your donors by demonstrating your project’s legitimacy and showing that the funds are being used to create positive change.**

### GIVbacks Rounds

GIVbacks rounds are 2 week periods wherein all donations to verified projects are tracked and recorded in our database. At the end of a round, our team reviews the donations and [calculates the amount of GIV to send to each donor](https://docs.giveth.io/giveconomy/givbacks#getting-givbacks). Note that recipient addresses of verified projects on Giveth do not get GIVbacks for their donations. This is to prevent recirculating funds and other fraudulent activity**_._**

Once the distribution has been determined, and [any suspicious activity](https://docs.giveth.io/giveconomy/givbacks#disqualifying-factors-for-givbacks-program) has been resolved, [reputation DAO token holders](https://medium.com/giveth/the-giveth-dao-community-givernance-84f55fa1ce36) vote to approve the allocation. You can see the votes to distribute GIVbacks for each round in our forum [here](https://forum.giveth.io/tag/givbacks-distro). When the vote passes, donors are notified via email that their GIVbacks are ready to claim [from the GIVbacks page](https://giveth.io/givbacks).

<img alt='givbacks round example' src={useBaseUrl('img/blog/GIVbacksRoundExample.png')} />

**Every 2 weeks, there is 1 million GIV available to give back to donors!**

Until December 23, 2026 donors who get GIV from GIVbacks are able to claim some part immediately upon distribution, and some part added to their [GIVstream flowrate](https://docs.giveth.io/giveconomy/givstream). With the GIVstream, donors who give to verified projects on Giveth get more GIV continuously [as the GIViverse expands.](https://giveth.io/givstream)

GIVbacks is the next generation of philanthropy where, using the power of web3, we can transform legacy systems that require those who give to sacrifice, into ones where giving actually gives back.

### Join the revolution, [donate to a verified project today](https://giveth.io/projects).
---
id: angelVault
title: The Angel Vault
---
import useBaseUrl from '@docusaurus/useBaseUrl'

The Angel Vault is a strategically managed Univ3 position structured to protect GIV from downward volatility. It is managed by our Angel Vault multisig, a [4/7 multisig of Giveth core team members and two members for ICHI](https://gnosis-safe.io/app/eth:0x2B0ee142dCFE7C2dD150cDbd7B6832F6e9977f51/home). To learn more about Angel Vaults and how they work, please refer to [ICHI’s documentation](https://docs.ichi.org/ichi-docs-v3/ichi-vaults/angel-vaults).
## Contracts
- Angel Vault (ICHI) LM (Unipool): `0xA4b727DF6fD608d1835e3440288c73fB28c4eF16`
- Angel Vault (ICHI) LP: `0xc3151A58d519B94E915f66B044De3E55F77c2dd9`

## oneGIV
oneGIV is a Giveth Branded Dollar (by ICHI) that can be minted using DAI at a 1:1 ratio. This can be done via [ICHI’s website](https://app.ichi.org/vault?poolId=20009&back=vault). To learn more about ICHI’s branded dollar, [please refer to their documentation](https://docs.ichi.org/ichi-docs-v3/branded-dollars/overview).

oneGIV is minted using 100% DAI, and is also over-collateralized by GIV. The contract holds GIV as additional collateral in case there is some issue with the DAI. All mints & burns of oneGIV happen via a contract managed by our Angel Vault multisig.

Over time, the Giveth DAO may vote to change the minting ratio from 100% DAI to a combination of DAI and GIV (e.g. 80% DAI, 20% GIV). However, to keep the peg to the dollar, burning oneGIV to redeem DAI will always result in 100% DAI.

## Providing & Removing Liquidity
Liquidity providers can add liquidity to the Angel Vault using oneGIV via [ICHI’s website](https://app.ichi.org/vault?poolId=20009&back=vault), and then stake their LP tokens in the [GIVfarm](https://giveth.io/givfarm). Because this oneGIV is added to a oneGIV / GIV Univ3 position, when you remove liquidity you will get oneGIV & GIV proportional to the holdings in the Angel Vault.

## Earning Rewards
Rewards are given to liquidity providers in proportion to the liquidity provided. When you stake your LP tokens, you earn rewards in two parts:
1. The 1% Uniswap fee which automatically increase your Angel Vault position ([IRR](https://docs.ichi.org/ichi-docs-v3/resources/faqs#what-does-the-irr-metric-on-the-angel-vault-page-represent)).
2. GIV incentives from within the GIVfarm, which as always, are distributed according to the GIVstream. Check out the [**GIViverse Expansion**](https://giveth.io/givstream) to understand how much your claimable rewards will be.

The APR shown in the GIVfarm oneGIV/GIV staking pool is the sum of these two reward rates.

<img alt="angel vault staking farm staking card" src={useBaseUrl('/img/content/giveconomy/angelVaultCard.png')} />

## Distribution of GIV rewards to Angel Vault LP Stakers
A total of 6 Million GIV has been allocated to run a rewards program for Angel Vault LP stakers for 26 weeks from the start date August 4, 2022. The amount of rewards being sent out throughout each two week period is as follows:

| Week    | GIV Rewarded (within the 2 week period) | % of rewards |
| ------- | --------------------------------------- | ------------ |
| Week 1  | 485,143                                 | 8.09%        |
| Week 3  | 569,143                                 | 9.49%        |
| Week 5  | 140,000                                 | 2.33%        |
| Week 7  | 653,143                                 | 10.89%       |
| Week 9  | 140,000                                 | 2.33%        |
| Week 11 | 737,143                                 | 12.29%       |
| Week 13 | 140,000                                 | 2.33%        |
| Week 15 | 821,143                                 | 13.69%       |
| Week 17 | 140,000                                 | 2.33%        |
| Week 19 | 905,143                                 | 15.09%       |
| Week 21 | 140,000                                 | 2.33%        |
| Week 23 | 989,143                                 | 16.49%       |
| Week 25 | 140,000                                 | 2.32%        |

### Incentives Plan — The Jagged Staircase
When the Angel Vault is initialized, the entirety of its liquidity will be in oneGIV. This is beneficial as the Angel Vault works best when there is a high percentage of oneGIV in the vault, but this percentage does not stay stable over time.
The ratio of GIV goes up when there is sell pressure in the market on the GIV token.
The ratio of oneGIV goes up when new Angel Vault LP positions are created.
The ratio of GIV/oneGIV stays the same when Angel Vault LP positions are removed.
We therefore want to encourage liquidity providers to periodically withdraw liquidity —  removing some % of GIV from the pool — and then re-add liquidity in oneGIV, increasing the total concentration of stables in the Angel Vault. This will help to support the strength of the Angel Vault buy-wall.

<img alt="rewards distribution schedule for jagged staircase" src={useBaseUrl('/img/content/giveconomy/jaggedStaircase.png')} />
---
id: bridgeSecurity
title: Giveth Bridge Security Implementation
slug: dapps/bridgeSecurity
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />

####  A technical overview of the features, roles and theory behind the security of the Giveth Bridge.
*This document assumes that the reader has basic knowledge of smart contracts, multisig contracts and Ethereum testnet chains.*

### What is the Giveth Bridge, exactly?
The bridge has 3 parts: A contract on the Ethereum Mainnet, a contract on the Rinkeby Testnet, and an off-chain service that connects these two contracts. The off-chain service listens for events from these contracts and relays commands from one contract to the other.


<img id="contentimg" alt='Giveth TRACE Bridge Flow' src={useBaseUrl('img/content/trace/givethbridge.png')} />


### How does it work?
The Giveth Bridge contract on mainnet is simply a vault contract with 1 extra security measure and a few modifications to make it function as a bridge. Payments are only paid out under certain conditions. Every bridge payment has a standard 48-hour time lockout before payment can occur.

During this time, the Security Guard has the ability to delay a payment further than the standard 48 hours - up to 30 days. This allows time to determine whether or not a payment needs to be cancelled. No payments can be issued without a check-in from the Security Guard happening XX minutes after the payment was requested. This check-in will happen daily so as not to delay authorized payments.

There is also an `escapeHatch` that can be called by an `escapeHatchCaller` to send the funds in the bridge to the funding multisig during the 48 hour delay, or any additional delay generated by the Security Guard.

This funding multisig will for some time also hold funds to diversify risk between the Bridge contract and the Consensus Multisig contract, when the bridge is holding too much value the funding multisig will `escapeFunds()` out of the bridge and when the bridge is getting low, the funding multisig will manually top it off.

Donations and withdrawals will happen directly out of the bridge. When a donation is made to the bridge, a token is created by the TokenFactory (at 1:1 ETH) and sent to LiquidPledging, where the decisions are made about spending. When a payment is called for, tokens are sent from Liquid Pledging and burned by the ForeignGivethBridge, at which point the command is issued back across the Ghetto Bridge using the Bridge Key to the Giveth Bridge to issue a payment.

In case for some reason the bridge goes down, the listener service will issue alarms to notify of a service interruption. The listener service will also create an alarm if tokens are created without a corresponding donation, or if tokens are not created at the time of a donation.

## Security Roles

### Mainnet Owner
This is the Giveth multisig that can issue control commands to the bridge. They can cancel any payment and can boot the Security Guard or remove the approved spender (bridge key).
### Mainnet Funding and EscapeHatch Destination
This multisig is used to both send funds to the Mainnet Bridge (Vault) and act as the destination for the EscapeHatch Call.
### Security Guard
Keeps watch over all requested payments, checks in each day, and delays suspicious payments.
### Mainnet EscapeHatchCaller
This is a 1 of x multisig that can trigger the vault to dump its funds to a predetermined wallet. We have people that are scattered across the world, multiple points of contacts that can do this.
### Allowed Spenders
These addresses are a whitelist who can issue a payment request to the bridge contract. In the application the bridge key is the only Allowed Spender.
### ForeignGivethBridge Owner
The bridge key.
### Rinkeby DappGod Multisig
This multisig controls updates and has total access to control the ForeignGivethBridge. It also acts as the `escapeHatchDestination` for the ForeignGivethBridge and Liquid Pledging.
### Rinkeby EscapeHatchCaller
This is a 1 of x multisig that can trigger the ForeignGivethBridge and Liquid Pledging contracts to dump their tokens to a predetermined wallet.

## Possible Security Issue Scenarios

**Bridge Key is compromised:**
A hacker could use bridge key to create transactions sending ETH to their own address to force transactions through. The Security Guard can delay these payments long enough for the owner multisig to cancel the payment and remove the compromised key on Mainnet.

They could also create GivETH tokens as the token controller on the rinkeby side. The listener service would catch this though and sound the alarm any time GivETH tokens are generated without a corresponding Ether donation. (also sounds an alarm if the bridge key service decided to take a nap and doesn’t create GivETH tokens when a donation is received.)


**Owner multisig has a bug and is able to be taken over (like the parity hack) or 6 keys out of 11 of the keys are compromised:**
This is highly unlikely but if this happens there will be no loss of funds. This multisig doesn't hold any funds, it only controls the bridge. Tt could reduce the 48 hour delay to 25 hours, the Security Guard can still delay any payments but the Security Guard can be replaced by the owner. Funds could be escaped within the 25 hours in this scenario.

**EscapeHatchCaller keys get compromised:**
In this case the worst thing that can happen is that the flow of the DApp on Rinkeby can be disrupted. This can be repaired however, by removing the compromised key on the EscapeHatch 1 of x multisig, and DAppGod. Once that is done then simply sending the giveth tokens back to the address from which they came, a similar scenario is possible on Mainnet. The EscapeHatch Caller can only move money to an escape destination, and nowhere else. If a key is compromised the worst thing they can do is to remove all owners and themselves from the EscapeHatch multisig, but the owner 6 of 11 multisig on main net can still call the EscapeHatch and can replace the EscapeHatch caller and the 3 of 5 multisig on rinkeby can as well.

**Funding multisig has a bug and is able to be taken over (like the parity hack) or 4 keys out of 7 of the keys are compromised:**
This is extremely unlikely but if this happens there will be a loss of funds. The loss however, would not be catastrophic as funds are split between the bridge and the multisig.

**Bridge on mainnet has a bug that lets someone else take over as owner:**
The 48 hour delay can be only be reduced to 25 hours Security Guard can still delay any payments but the Security Guard can be replaced by the owner. Funds could be escaped within 25 hours in this scenario.

**DAppGod Multisig on the testnet decides to take over:**
If this were to occur, the EscapeHatch from the bridge would prevent any loss of funds, and the testnet set up could be manually redeployed.

**What if the Security Guard’s key and Bridge Key Controller both get compromised (or their holders collude to steal funds)**:
The Owner multisig can cancel payments and extend the time delay to longer than 48 hours. In this scenario though they probably wouldn't have to because the bridge funds can be escaped to the funding multisig. This is the only scenario that could be a serious risk to the funds in the bridge vault. This could be averted within 48 hours of the event starting because of the default delay and that funds can be escaped during that period.

**Finally, what if the Event Listener falls off-line just previous to any of the aforementioned attacks that trigger alarms on compromise?**
The Security Guard should see any suspicious transactions and be able to delay payments until they are dealt with.
---
id: developmentProcess
title: Development Process
slug: dapps/developmentProcess
---
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />

*This section details the Giveth TRACE development process, deployments, and how merging and testing is handled.*

## Development Planning, Sprints and Where to get Involved.
We run on a 2 week sprint cycle with weekly developer meetings to plan sprints and assess progress. You can checkout when the next one is on our [Google Calendar](https://calendar.google.com/calendar/embed?src=givethdotio%40gmail.com) and you can also reach out on the [Giveth Discord](https://discord.giveth.io) to `@moenick` the Giveth TRACE project manager. You can find the current [Giveth TRACE repository on Github](https://github.com/Giveth/giveth-dapp).

## Deployments and Branch Organisation
Giveth TRACE has transitioned from passive to active development for post-beta release coming soon. There are two deployments currently used for the development process.

Name | Blockchain | Branch Deployed | Auto Deploy | Use |
-----|------------|-----------------|-------------|-----|
[beta](https://trace.giveth.io) | Mainnet/Rinkeby | master | no | Bridged deployment; Rinkeby for internal contract interactions, Mainnet for sending and receiving real funds.
[develop](https://develop.giveth.io) | Ropsten Test Network | develop | yes | Development environment for integrating and testing new features. Feature and pull request branches are deployed to this environment.

The two branches below  are being used in the gitflow.

Name | Description |
-----|------------|
master | The master branch tracks released code only. Commits are made to master around the middle of each month so as not to interfere with payment processes happening near the end and beginning of these months.
develop | Deployments made to develop are from local builds and include new features and bug fixes.

## Usage of Zenhub Boards
Currently we use the Zenhub Boards extension for Github to track progress on features and fixes. You can get the [Zenhub extension here](https://www.zenhub.com/extension).

The Current Github issue flow is as follows:

Name | Usage |
-----|------------|
New Issues | Create a new Issue for a new feature request or to report a bug. Tag a developer or `@moenick` to make sure it get's noticed. Use labels to add context to your issue.
Icebox | Features and Ideas to consider for future development, to be assesed by the Giveth Team only when developer bandwidth allows.
Product Backlog | Issues that need to be dealt with or approved new features for development. These will be queued into the next sprint progressively.
Epics | Large tasks which have been broken down into smaller issues.
Needs Clarification | Issues which require more clarification from the issue creator in order to move forward.
Sprint Backlog | Issues being worked on in the current sprint.
Bugs & Ops | Urgent tasks that need to be prioritized. Bandwidth is set aside in the sprint schedule for developers to address any issues here.
In Progress | Issues that have been picked up by a dev for the current sprint.
Code Review | Devs should review code referenced in these issues for quality assurance and fixing potential issues before moving to user testing.
UAT (User Acceptance Testing) | Features or Fixes ready to be user tested.
Done | Issues ready to be merged to `master` according to the commit cycle.


### Making a Pull Request
Before making new Pull Request, make sure that your code does not have any linter issues and can be deployed. Only PRs that successfully deploy and don't have any merge conflicts will be merged. You can also easily check the deploy preview on Github Netlify autodeploy integration.
![Autodeploy Integration](https://d33wubrfki0l68.cloudfront.net/cfa6124f4e0bf556de850f40e97c6b4cc66231f9/d42f0/images/product-development/deploy-preview.png)
**Deployment preview.** Each pull request to the DApp repository has a Netlify deploy preview. You can access it at the bottom of the Conversation tab after clicking **Show all checks** button and **Details**.

## Integration & Testing
Integration of new features is done by the **development team** after a DApp dev meeting where PRs are reviewed. After the PRs are reviewed and fixed, they are merged to the develop branch. Testing of the new features is done in the [`develop`](https://develop.giveth.io) environment to ensure the features do what they say and work well with the rest of the DApp.

## Quality Assurance Testing
After new features are integrated and dev tested in the [`develop`](https://develop.giveth.io) environment, developers will ping testers with requests or updates in the [Giveth TRACE Dev Channel](https://discord.gg/79uUbyVCtE) on Discord. Testing should not be done by developers and is open to anyone who wishes to contribute.

## Production Deployment
Only once all the newly introduced bugs are removed in the `develop` branch it can be merged to master and pushed to production. It is done manually by DApp devteam (by `@aminlatifi` and `@MohammadPCh`).

**To deploy the newest version of feathers-giveth**
```
$ ssh user@feathers.alpha.giveth.io

$ cd /home/deploy/feathers-giveth/
$ sudo -u deploy bash

$ git pull

$ yarn install --pure-lockfile
$ yarn serve
```

Next, check the feathers deploy status
```
$ pm2 logs
```

If the logs are clear, the last step is to deploy the latest master branch commit on [Netlify](http://netlify.com/) and locking the deploy.

## Back-end Webservices Documentation
If you're a new contributor and would like more in depth technical documentation on all the Webservices leveraged from the back-end (feathers-giveth) to the front-end (giveth-dapp), check out our pages on **Swagger** for both Production and Staging deployments:

[feathers-giveth Production](https://feathers.beta.giveth.io/docs/?url=/docs#/)  
[feathers-giveth Staging](https://feathers.develop.giveth.io/docs)


## FAQ

 **What is the definition of a feature?**

A Feature is any non-trivial improvement (less than 10 lines of code). Most features have issue in the corresponding Github Repository.

 **What about fixes?**

 Big non-critical fixes are treated just like any other feature. If a fix is time critical, it is created as new branch with `hotfix/` prefix as a fork from the `master` branch. Such hotfix is tested at minimum by 2 people from dev team before being merged to `master`and `develop` branches.

 **Where do we communicate what needs testing?**

The QA testing is announced in the `Giveth-1 Dev` channel on [Discord](https://discord.giveth.io).

**How do we prioritize when tests fail / bug fixes?**

Bug fixes are done ad-hoc as soon as discovered during the testing process. The bugs can be tackled by the DApp dev team or external contributors can be asked to help. Bug fixing has a priority over new development.

**Who does deployments and how are they deployed?**

The `develop` branch is autodeployed to its environment. The `master` branch is deployed by the dev team (`@aminlatifi`, `@RamRamez` and `@MohammadPCh`) once there are no new known bugs in the `develop` branch. The process is manual and there is a deployment procedure.

**What is the release cycle frequency?**

 There is new release every 2 weeks as depicted in the [product development cycle gant chart](#product-development-testing-fig-release).
---
id: contributors
title: Contributing to Giveth Development
slug: dapps/contributors
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

Giveth currently maintains three products that focus on funding management, peer to peer donations, and DeFi for-good token economics. These are [Giveth TRACE](https://trace.giveth.io), [Giveth.io](https://giveth.io) and the [GIVeconomy](https://giveth.io) respectively

All our products share some common development standards that are paramount to learn before engaging in any development for Giveth. In this document we'll show you how to interact with our open-source repositories, getting in touch with the right people and how to begin creating and picking up issues.


## Github Management
First things first, you'll need to install the [zenhub extension for github](https://chrome.google.com/webstore/detail/zenhub-for-github/ogcgkffhplmphkaahpmffcafajaocjbd) for your web browser that will allow you to see the workspaces and pipelines we use in Github to manage issues.

<img alt='All-Devs Zenhub Board' width='85%' height='auto' src={useBaseUrl('img/content/allDevsZenhub.png')} />

We have transitioned to manage all three DApps(products) under one workspace, **`All-Devs`**.

### Repositories
The [Giveth Github organization](https://github.com/Giveth) has many, many repositories. Here’s a general overview of relevant repositories that relate to our active products:

<table>
  <tr>
   <td><h3>Product</h3>
   </td>
   <td><h3>Repository</h3>
   </td>
   <td><h3>Description</h3>
   </td>
  </tr>
  <tr>
   <td>Giveth.io
   </td>
   <td>impact-graph
   </td>
   <td>Backend of Giveth.io
   </td>
  </tr>
  <tr>
   <td>Giveth.io
   </td>
   <td>giveth-next
   </td>
   <td>Giveth.io current version
   </td>
  </tr>
  <tr>
   <td>Giveth.io
   </td>
   <td>giveth-io-typescript
   </td>
   <td>Givethio typescript version with new design.
   </td>
  </tr>
  <tr>
   <td>GIVEeconomy
   </td>
   <td>GIVeconomy
   </td>
   <td>Usually used for planning and issue tracking
   </td>
  </tr>
  <tr>
   <td>GIVeconomy
   </td>
   <td>giv-token-contracts
   </td>
   <td>Smart contract implementations
   </td>
  </tr>
  <tr>
   <td>GIVeconomy
   </td>
   <td>liquidity-mining-dapp
   </td>
   <td>GIVeconomy Frontend UI
   </td>
  </tr>
  <tr>
   <td>GIVeconomy
   </td>
   <td>giv-token-subgraph
   </td>
   <td>Calculating $GIV data for GIVeconomy Frontend
   </td>
  </tr>
  <tr>
   <td>GIVeconomy
   </td>
   <td>givback-calculation
   </td>
   <td>Calculating GIVbacks
   </td>
  </tr>
  <tr>
   <td>TRACE
   </td>
   <td>giveth-dapp
   </td>
   <td>Frontend and planning of giveth TRACE
   </td>
  </tr>
  <tr>
   <td>TRACE
   </td>
   <td>feathers-giveth
   </td>
   <td>Backend of Giveth TRACE
   </td>
  </tr>
  <tr>
   <td>TRACE
   </td>
   <td>dapp-mailer
   </td>
   <td>Email notification system for TRACE
   </td>
  </tr>
  <tr>
   <td>TRACE
   </td>
   <td>giveth-bridge
   </td>
   <td>Giveth Rinkeby - Mainnet Bridge system
   </td>
  </tr>
  <tr>
   <td>General Services
   </td>
   <td>ui-design-system
   </td>
   <td>npm package for Giveth design assets
   </td>
  </tr>
</table>

### Pipelines on the `All-Devs` Workspace
When you enter a workspace on the Zenhub tab you'll see a line of adjacent columns that are used to identify and manage the statuses of issues currently in the repositories. You can find a short description of each below:

**New Issues** - New bugs and features go here first.

**Epics** - Pipeline for Epic Issues. Larger tasks comprised of several smaller issues.

**Icebox** - Features or Suggestions that have been archived. Issues here are non-priority and might be added into sprints only if Devs have the bandwidth.

**Backlog** - Lower Priority Issues waiting to get pulled into Sprint Planning.

**Sprint Backlog** - These issues have been vetted and are ready to be worked on. They will be added into the next sprint according to priority and Developer bandwidth.

**In Progress** - Picked up and being worked on by the Developers, usually on local builds.

**Code Reviews** - Open Pull Requests waiting for review and eventual merge into the staging server.
:::info
It’s mandatory to have the code reviewed by one of the core team members, usually your mentor or the one which introduces the project to you can review it, pls ask for review before pushing it to any environment.
:::

**UAT Testing/QA** - The feature or bug fix is deployed on the staging server for user testing and Quality Assurance.

**Done** - Bug fix or feature has been completed, and is ready to be deployed on the live server.
:::info
All issues should meet DoD (Definition of Done) criteria to be approved as Done and being in this column:
Success Criteria passed (if it’s  get mentioned in User Story / Task or related issue)
Deployed in Staging
UAT Tested by a tester or PM
Documented
:::

**Closed** - The bug fix or feature has been copied live. It’s recommended that all closed issues get related to a release number in the zenhub and get closed right after the version goes live.

### Creating Issues
Creating Github issues is essential to ensure bug fixes or features are tracked properly and relevant information can be organized, and consolidated. The new issue template is a guide only, feel free to delete any heading that you don't use.

**Labels** will help add context to your issue, please use them so other developers can get a better understanding of issues at a glance and pick them up. Some commonly used labels in `All-Devs` are:

**`fast follow`** - Priority features or improvements following a product launch or version release.

**`documentation`** - Requesting creation or updates of technical documentation.

**`bugs`** - Functionality or feature of a product that is broken or not working as intended

**`feature request`** - Requesting for a new feature or functionality to be added to a product

**`design needed`** - Requesting support from the design team to create assets relevant to this issue

**`question`** - There is a pending question inside this issue that needs a response in order to move forward

**`security`** - Security issue or improvement

**`UI`** - This issue relates to the User Interface of a given product

**`UX`** - This issue relates to the User Experience of a given product

## Ceremonies

We host in the [Giveth Discord](https://discord.giveth.io) many Developer meetings throughout the week including:
- Daily Dev Standups from Tuesday to Thursday at 6:30am GMT-6  
- All-Devs Sync weekly on Mondays at 10:00am GMT-6
- GIVeconomy Sync weekly on Wednesdays at 8:00am GMT-6

These meetings are important places to stay up to date with DApp development and to integrate with the Giveth Team as a Development Contributor.

## Sprint Management

Framework: We’re practicing mostly Scrum, in biweekly iterations (called sprints), sometimes based on project situations we move to KanBan.

### What is Scrum?
In scrum, the sprint is a set period of time where all the work is done. However, before you can leap into action you have to set up the sprint. You need to decide on how long the time box is going to be, the sprint goal, and where you're going to start. The sprint planning session kicks off the sprint by setting the agenda and focus.

- **The What** –  The product owner describes the objective(or goal) of the sprint and what backlog items contribute to that goal. The scrum team decides what can be done in the coming sprint and what they will do during the sprint to make that happen.

- **The How** – The development team plans the work necessary to deliver the sprint goal. Ultimately, the resulting sprint plan is a negotiation between the development team and product owner based on value and effort.

- **The Who** – You cannot do sprint planning without the product owner or the development team. The product owner defines the goal based on the value that they seek. The development team needs to understand how they can or cannot deliver that goal. If either is missing from this event it makes planning the sprint almost impossible.

- **The Inputs** – A great starting point for the sprint plan is the product backlog as it provides a list of ‘stuff’ that could potentially be part of the current sprint. The team should also look at the existing work done in the increment and have a view to capacity.

- **The Outputs** – The most important outcome for the sprint planning meeting is that the team can describe the goal of the sprint and how it will start working toward that goal. This is made visible in the sprint backlog.

<img alt="sprint planning" width='75%' src={useBaseUrl('img/content/sprintInfo.png')} />

Before the iteration starts, you may need to have your expected total contribution hours in [Giveth Resource Planning Spreadsheet](https://docs.google.com/spreadsheets/d/1fJcFTLJof6o0rViKIy4C46sXuisySTud40HFsMGE1e0/edit#gid=311929329), the link usually gets shared in the Discord dev channel before the sprint meeting. You can find the sprint sheet and update the following cells:

<img alt='resource planning spreadsheet' src={useBaseUrl('img/content/resourcePlanningAllDevs.png')} />

It helps the Product Managers (PMs) to plan for the resources better and know if they are able to meet the milestone in each sprint or not. If you couldn’t find time to fill out the spreadsheet, you may be asked to do so during the meeting or whenever you can have an estimate, just DM it to PMs or put it in the dev channel.

The usual sprint planning goes like this:

1. PMs bring the issues (Preferably User Stories to the planning meeting, describe it and make sure it’s clear for the team to start implementing.
2. PM facilitates talks between devs to make it as clear as it can be.
3. PM asks for estimations in Story Points (Story Points are the unit of minimum effort spent on a product which can be delivered asap, like a simple bug fix, for example, could take half of a working day. )
4. PM starts building “Sprint Backlog” with prioritizing the issues and makes sure the total amount of Story Points are proportionate with the total capacity of the teams and contributors.
5. Everyone agrees on the sprint plan and commits to the expected goal.


## Key Contacts

- Development Working Group Steward - Amin
    - Discord Handle: `Amin#2164`
- GIVeconomy Product Manager - Lauren
    - Discord Handle: `karmaticacid#1218`
- Giveth TRACE, Giveth.io Product Manager - MoeNick
    - Discord Handle: `MoeNick#1374`
- Giveth.io Lead Developer - Mateo
    - Discord Handle: `mateodaza#3156`
- DevOps & Security - Kay
    - Discord Handle: `geleeroyale#3228`
- Lead Designer - Marko
    - Discord Handle: `markop#2007`

## Installation Guides for Local Development

- [Giveth.io](./givethioinstallation)
- [Giveth TRACE](./TRACEinstallation)
- [GIVeconomy](./installGIVeconomy)

## Testing Guidelines

- [Giveth.io](./testing-guidelines)
- [GIVeconomy](./testingGIVeconomy)

## Tools we Use

- [Segment](https://segment.com/) (Giveth TRACE, Giveth.io)
- [Sentry](https://sentry.io/welcome/) (Giveth TRACE, Giveth.io)
- [Infura](https://infura.io/) (Giveth TRACE, Giveth.io)
- [Autopilot](https://journeys.autopilotapp.com/features/email-marketing-software) (Giveth.io)
- [Amplitude](https://www.amplitude.com/) (Giveth TRACE, Giveth.io)
- [Docusaurus](https://docusaurus.io/) (Documentation)
- [The Graph](https://thegraph.com/en/) (GIVeconomy)
- [Netlify](https://www.netlify.com/) (Giveth TRACE)
- [Vercel](https://vercel.com/dashboard) (Giveth.io, GIVeconomy)
- [Cryptocompare](https://www.cryptocompare.com/) (Giveth TRACE)
- [Coingecko](https://www.coingecko.com/en/api) (All Products)
- [Github Actions](https://github.com/features/actions) (All Products)
- [MongoDB](https://www.mongodb.com/) (Giveth TRACE)
- [PostgreSQL](https://www.postgresql.org/) (Giveth.io)
- [Redis](https://redis.io/) (Giveth TRACE, Giveth.io)
- [Elastic Search](https://www.elastic.co/elasticsearch/) (Giveth TRACE)
- [Kibana](https://www.elastic.co/kibana/) (Giveth TRACE)
- [Pinata](https://www.pinata.cloud/) (Giveth.io, GIVeconomy)
- [Transak](https://transak.com/) (Giveth.io)
- [AdminBro](https://v2.adminbro.com/index.html) (Giveth.io)
---
id: testing-guidelines
title: Giveth.io Testing Guidelines
slug: dapps/testing-guidelines
---
import useBaseUrl from '@docusaurus/useBaseUrl';

This guide provides a framework for testing the [Giveth.io](https://giveth.io/) DApp.

## Requirements
* User testing should be done on https://staging.giveth.io - **Our staging environment is deployed on both Ropsten (Mainnet) and Gnosis Chain** (formerly xDai Network).
* Please use a modern browser. If you encounter a bug, please try the same thing with another browser. Please make an issue in any case, but tell us if the issue might be browser specific.
* Use issues in [GitHub](https://github.com/Giveth/giveth-next/issues) for reports and feedback.

## Use Cases

The following actions are defined as core functionality. If one of these steps is buggy, that represents a critical error.

### [General](https://github.com/Giveth/giveth-2/issues/800)

This use case will be partially automated but requires user-testing, especially to ensure that all external links function correctly.

### **Home page**

* View Home page, hover all over project cards to see load more, and donate button
* Check all links on the home page
* Check all footer links including social links
* "Liking" projects - successful and "heart count" updates
* Header navbar buttons (`Home`, `Projects`, `GIVeconomy`, etc. ) are functional
* "GIV currently in wallet" (on navbar) shows correctly (token address: `0x4f4F9b8D5B4d0Dc10506e5551B0513B61fD59e75`)
* Project Badges such as `Verified`, `Traceable`, `New` display correctly

<img alt='testingsocialmedia' src={useBaseUrl('img/testingguidelines/testingguideline1.png')} />

* Signup for newsletter
* Subscribe to emails - validation of email, success subscribe
* My wallet drop down menu is functional
* Account name/address shows properly on navbar when logged in
* Report a bug
* Sign in/sign out
* Check that projects appear on the project page (correct format, correct number)
* Links inside https://giveth.io/join are functional
* Content inside https://giveth.io/about displays correctly, including `Mission & Vision`, `History` and `Team` tabs

### **Public Profile Page**

View Public Profile Page - when you click on the project owner

<img alt='testingpublicprofile' src={useBaseUrl('img/testingguidelines/testingguideline2.png')} />

* Surf in all tabs and make sure all data in this profile is accurate
* For example: the number of donations, amount received and donated, and also the number of projects should be accurate
* On the donation tab, test the tx link, sorting by amount, USD value, and date
* Make sure the USD value is accurate
* Test copy address of the user and also test the external link

<img alt='testingadress' src={useBaseUrl('img/testingguidelines/testingguideline3.png')} />

### **Projects Page**

View the projects list, by clicking the projects links in the header

* Make sure badges of verified and trace is working properly
* If signed in view red hearts - remove hearts. If you’re not signed in: you should get asked for sign-in before proceeding

**Test sort by /filter / search**

* Filter by category and make sure filtering works fine
* Sort by Amount raised, newest, oldest, hearts
* In sort by field, we have some items that should act as the filtered items: Accept GIV token (all projects excluding Giving Block projects) - Trace - Verified. all of them should filter the results
* In search, you can easily find results by title, description, impact Location, (project owner is not searchable now but it’s implementing)
* If no result is found, the formatting of no result page should look normal
* Back - in the search box should clear the input and show all projects
* Back in the no result should also do the above

### **Project Public View**

Public view means the view that everyone can see. If you are the owner of this project and you are signed in, you may have another view, called the Project Owner view, which you can see in the following doc.

* Project single page public view -when you click on learn more you can view the details of the project
* About tab should show the project description
* Sidebar: donate button, hover on the button to see the changing color
* The share should work properly
* Like the projects - if not signed in, you should get asked to sign in, if signed in, it should get red after giving heart
* Tags: categories and badges of verified should work properly
* GIVback toast message link `LEARN MORE` should go to docs
* Report issue link should work properly
* Updates have to be shown properly, (to test better as the owner you can post an update, log out and see as public view if it is updated or not)
* Donations Table: Make sure all-time funding received is accurate. Test count, sorting on the date, amount, and USD value, also search in donation

### **Sign-in**

* Signing with Ethereum: select meta-mask, torus, and walletConnect
* Sign-in: you are prompted to connect your wallet and you get asked to sign again for doing some specific actions, for example: liking (“hearting”), viewing your account, viewing the project in owner view, or creating a project
* Social links on sign in should load torus:

<img alt='testingsocialmedialinks' src={useBaseUrl('img/testingguidelines/testingguideline4.png')} />

* Do it with a registered and not registered address
* For specific actions, you may need to sign-in with your wallet

### **Onboarding**

* If you don't have a complete profile, you get asked to complete your profile in a wizard
* Check required fields
* If you are not signed in you should get asked to do it before submitting the data
* Check verification of emails and URLs
* Upload photos, do it with very large and small photos
* Submit your data and the header should load right after you have this information

### **My Account**

* Test it with a newly registered address: you should get asked to complete your profile by a yellow banner up there, and the “Don’t be a stranger” purple banner below the overview
* When clicking on these yellow or purple banners you should get redirected to the onboarding page
* Test if you complete your profile that  you can edit your profile
* Please test all fields and test verification of the correct email. URL and required field
* Delete your profile photo
* Edit your profile photo
* Overview tab checks numbers to be accurate
* Projects Tab - test sorting, links, all provided data including verified and listed projects (you can change the provided amount in admin bro and check it here again to make sure it reflects the latest changes)
* Donations Tab (like public profile)
* Liked Projects tab (like public profile)

### General Purposes Pages

* QAing About Us
* QAing History
* QAing Team
* QAing Terms of Use
* QAing Partners

### Check mobile view and responsiveness

* Resize your browser
* Use different devices: phones, tablets
* Dig into header, menus, all static pages


###  [Project Creator](https://github.com/Giveth/giveth-2/issues/798)

This use case is partially automated to ensure functionality before changes are made. However, user testing is still required.

#### Create Project

* Verification: required fields should be filled and not submitted empty
* Add Project details
* Use rich text formats (bold, italics, quotes, headers, etc.), and ensure they render properly
* In the description please test emojis and report all formatting and bad UX
* In the description, all the formatting should save and work properly
* In the description, embed images, test “update pictures”, resize them and ensure they render properly
* Upload cover photo, delete, upload it again with large and tiny pictures
* Use predefined photos, and change them to see any abnormal behavior
* Embed videos and ensure they render properly
* In address, it should prevent reused ETH addresses, it should be a valid ETH address and not a contract address
* For impact, search locations, cities, areas as well as countries or continents and make sure it’s working properly
* Category select
* Google maps selection
* Preview (save as a draft) means you can reach out to the projects later in your account but it’s not active yet
* Publish. and you have to see the success page and all information and links on the public page should work properly
* Publish directly and publish a preview project to make sure there are no differences.
* Check that projects are all listed in "my projects"
* Check that projects show up on homepage*
* Deactivate/reactivate project


:::info
*Projects created on the DApp have an automatic "unlisted" Status, meaning they will not show up until their status is changed to "listed". Reach out to someone with the `Verification Team` role on the [Giveth Discord](https://discord.giveth.io) who can show you how to list your project on staging in order to continue testing.
:::

#### Edit Project

* Change photo
* Use rich text formats (bold, italics, quotes, headers, etc.), and ensure they render properly
* Embed videos or images, and ensure they render properly
* Change text fields
* Update donation address
* Check that updates are applied

### Update Project

* Add an update to your project
* Use rich text formats (bold, italics, quotes, headers, etc.), and ensure they render properly
* Embed videos or images, and ensure they render properly
* Update is saved and displays properly on the project page

### [Donor](https://github.com/Giveth/giveth-2/issues/799)

This use case does not include any automated testing and must be fully user-tested.

* Donate with different tokens: ETH and ERC-20 tokens on Ropsten (Mainnet) and xDAI, ERC-20 tokens on Gnosis Chain (formerly xDai Network)
* Donate with alternate wallets (other than sign in)
* Check that funds leave wallet
* Check that funds received/tracked by project
* View donations made (correct $ amount, correct currency type)

###  Donation Page

* Before sign-in you should see connect wallet button
* Donate and check the modals look
* Check the links and content on the page to make sure it's working
* Change wallet and change network to check it’s working with your wallet
* Repeat the donation on both ETH(Ropsten) and gnosis Chain networks
* Do it with an insufficient token number
* Do it with too tiny amounts
* Check the project card view beside the donation token
* Search bar for tokens to donate - tokens show up appropriately when searching
* Giving Block - GIV donations should load a Twitter modal about Gemini
* Success Page with eligible and with non-eligible token should differ - on GIVback eligible token donation you may see a banner saying you are eligible for GIVbacks
* Anonymous donations should not show in public profile view

For GIVeconomy testing guidelines, [click here](https://docs.giveth.io/dapps/testingGIVeconomy/).
---
id: styleguide
title: Style Guide
sidebar_label: Style Guide
---

Giveth Design by [@markoprljic](https://twitter.com/markoprljic). 

[Master design file on figma](https://www.figma.com/file/FBqHg0UfeuaIueDEZG0tBS/Giveth-Design?node-id=971%3A43)---
id: donatingmetamask
title: Donating with Metamask
slug: dapps/donatingmetamask
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

We'll walk you through the process of making a crypto donation via Metamask here. If you do not have a Metamask wallet, well, then you should [head on over to the Metamask website, and learn how to get one!](https://metamask.zendesk.com/hc/en-us/articles/360015489531-Getting-Started-With-MetaMask)

### How to Make a Donation

Once you have chosen a project and set an amount to donate, go ahead and click the `DONATE` button. This should bring up a pop-up window confirming the amount to donate.

 <img id="contentimg" alt='Confirm Metamask transaction' src={useBaseUrl('img/content/metamaskDonating.png')} />

 If the amount is right, click on `DONATE`. A pop-up window from Metamask to confirm the transaction details will be shown.

 <img id="contentimg" alt='Confirm Metamask transaction' src={useBaseUrl('img/content/metamaskconfirmTransaction.png')} />

Verify that the amount on the Metamask pop-up corresponds with the amount you specified on the project page. Take note that the gas fee from the Ethereum network or Gnosis Chain will be added on top of the donation amount. Make sure you have enough Ethereum or xDAI in your wallet to cover the gas fees, otherwise the transaction cannot be completed.

 If it looks good, hit `CONFIRM`, and your donation transaction will begin. You should see a pop-up that looks like this:

 <img  id="contentimg" alt='Transaction in Progress' src={useBaseUrl('img/content/metamaskTransactionprogress.png')} />

You can check your transaction in the transaction pop up on your Metamask under the 'Activity' Tab. 

Once the transaction has been confirmed on the blockchain, you'll be taken to the next page confirming your successful donation. Nice work!

 <img id="contentimg" alt='Successful Donation' src={useBaseUrl('img/content/metamaskSuccessfulDonation.png')} />

### To Donate with xDai
If you're tired of paying outrageous gas fees on Mainnet Giveth supports donations on the Gnosis Chain (formerly xDai Network). To get Metamask [setup on the Gnosis Chain go here](https://docs.gnosischain.com/tools/wallets/metamask/). Log in with Gnosis Chain via MetaMask on Giveth.io. You can follow the same process for making donations on Gnosis Chain as on Mainnet.
---
id: entitiesAndRoles
title: Giveth Entities and Roles
slug: dapps/entitiesAndRoles
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


*Content and ideas have been modified from this excellent article [“An Overview of the Giveth Donation Application”](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4) authored by Kris Decoodt in 2017. Many things have been revised and modified since 2017. Here we breakdown the DApp as it is in 2022.*

This document explains how different interactions within the Giveth DApp can be made. The goal is to provide a clear outline of the entities and roles within the Giveth TRACE DApp. This document has been tailored for several audiences and use cases as follows:
* **Developers:** can use this document as part of System Requirements.
* **Testers:** can use this document to understand how the DApp should work in order to determine what behaviour is wrong and should be reported as a bug. This document is not a formal Test Case in SDLC (Software Development Life Cycle) but can still be used for guidance.
* **The Support Team:** can use this document as a refererence to help new users who experience difficulties with the DApp.
* **The End User:** can use this document to gain a greater understanding of how the DApp works. However, foundational knowledge of Blockchain, Ethereum and Giveth is recommended.

## Roles
We have eight roles in Giveth TRACE. In this section we explain in-depth each role, their function, how to become one and the power each role has.
1. <a href="#giver"><strong>Giver</strong></a>
2. <a href="#communityManager"><strong>Community Manager</strong></a>
3. <a href="#campaignManager"><strong>Campaign Manager</strong></a>
4. <a href="#campaignReviewer"><strong>Campaign Reviewer</strong></a>
5. <a href="#traceManager"><strong>Trace Manager</strong></a>
6. <a href="#traceReviewer"><strong>Trace Reviewer</strong></a>
7. <a href="#recipient"><strong>Recipient</strong></a>
8. <a href="#websiteUser"><strong>Website User</strong></a>

### Website User
This refers to any person who visits our website. Without registering as a user on Rinkeby they cannot interact with any Giveth entity nor make donations on Giveth TRACE.
#### How to become a Website User
* Anyone with the address of the Giveth TRACE website can become a User.
#### Power of a Website User
* Browse through Communities, Campaigns and Traces.
* Register a profile.
* Edit their profile.
* View someones else's profile.
* Subscribe to a Community, Campaign or Trace.

***Note:** Most site actions require authentication through an Ethereum web wallet; currently Giveth TRACE only supports MetaMask.*

### <a name="giver">Giver</a>
The term Giver describes anyone who uses our platform to give donations to a Community, Campaign or Trace. Givers can interact with all 3 entities but  are not explicitly part of any unless they choose to join a Community or assume another role as well.
#### How to become a Giver
* Anyone with an Ethereum wallet can donate to a Community, Campaign, or Trace in the DApp and become a Giver.
#### Power of a Giver
* Accept or reject a delayed delegation from a Community or Campaign.

***Note:** Givers can veto or "reject" a proposed Delegation within 3 days of the delegation proposal. This is referred to as a delegation "delay". After 3 days, the delayed delegation will be accepted by the DApp automatically.*

### <a name="communityManager">Community Manager</a> (formerly Delegate)
A Community Manager is the registered user owning a Community. They can delegate the funds donated to their Communities. A delegation is a process, where the donation pledged to a Community is transferred to a Campaign or Trace. Once delegated, the Giver has 3 days to reject (or approve) the delegation. After that time, the money is auto-approved and locked in the Campaign or Trace to which the money was delegated.
#### How to become a Community Manager
* A user can create a Community and become the Community Manager after being whitelisted by a DApp Admin.
#### Power of a Community Manager
* Edit the name, description, image, and link of their Community.
* Give Community funds (via delayed delegation) to Campaigns, and Traces.

***Note:** In order to initiate a delayed delegation, the Community Manager should go to the Traces or Campaign page, and click the `Delegate Funds` button.*

### <a name="campaignManager">Campaign Manager</a>
Campaign Managers are Giveth.io users who have chosen to make their project traceable and have passed the project verification process. The role of the Campaign Manager is to create Traces through which they can fund the work of people and the cost of resources behind the project.

#### How to become a Campaign Manager
* Verify their Giveth.io project and request to become traceable, upgrading to a Campaign on TRACE and becoming the Campaign Manager of said Campaign.
#### Power of a Campaign Manager
* Edit their Campaign.
* Send Campaign funds (via delegation) to Traces within their Campaign.
* Reject or accept proposed Traces to their Campaign.
* Create or edit Traces in their own Campaign.

***Note:** A Trace has to belong to at least one Campaign and needs to be approved by the Campaign Manager.*

### <a name="campaignReviewer">Campaign Reviewer</a>
Because donations to a Campaign are locked, a Campaign Reviewer role is critical to review and track the Campaign's progress. Campaign Reviewers have the responsiblity of checking the legitimacy of a Campaign and its Traces. They also have considerable power within a Campaign.
#### How to become a Campaign Reviewer
* A Campaign Manager can assign a user to become a Campaign Reviewer.
#### Power of a Campaign Reviewer
* Reject or approve Completed Traces.
* Cancel Traces within their Campaign.
* Cancel a Campaign.

### <a name="traceManager">Trace Manager</a> (formerly Milestone Manager)
Traces are the foundation of the Giveth system. Any registered user can propose a Trace to a Campaign. However, a Campaign Manager or Campaign Reviewer must approve the Trace proposed to their Campaign for it to become valid. Traces can represent several types of requests for funding. More info on <a href="#traceTypes">types of Traces</a> are detailed further in this document.
#### How to become a Trace Manager
* A user can propose a Trace to Campaign and become the Trace Manager.
#### Power of a Trace Manager
* Edit their Trace.
* In the case of creating a Bounty or Milestone, a Trace Manager can set a Trace Reviewer.
* Mark a Trace as complete.

***Note**: A Trace can no longer be edited once it has received a delegation or donation.*
### <a name="traceReviewer">Trace Reviewer</a>
* A Trace Reviewer can be assigned by a Trace Manager.
#### Power of a Trace Reviewer
* Reject or approve a completed Trace.
* Cancel a Trace.

***Note:** In the case that a Trace is cancelled, the currency returns to the source, i.e. to the Giver for a donation or to the Community/Campaign for a delegation.*

### <a name="recipient">Recipient</a>
A Recipient is a registered user who will receive payment from their successfully completed Trace. In the majority of cases, the Recipient is also the Trace Manager as they are the one working on the Trace. However, in some cases the recipient is separate, such as for payments to a supplier or a Milestone for a Campaign.
#### How to become a Recipient
* A Recipient can be designated by a Trace Manager; it can be the Trace Manager or another user.
#### Power of a Recipient
* Mark a Trace as complete.
* Request payout of the Trace funds.

***Note:** In the case that the Trace has a Reviewer, collecting funds needs the Reviewer's approval.*
#### Latency
Some actions need to be registered to the Ethereum blockchain network. Adding transactions to the blockchain does not happen immediately, so we observe a latency in some actions. This latency depends on the network conditions, for example traffic on the network.
#### Locality of Roles
All roles have a limited scope and once an entity ceases to exist, so do the connected roles. Every Community contains exactly one Manager. Every Campaign has one Campaign Manager and one Campaign Reviewer. Every Trace has one Trace Manager, one Recipient and potentially one Reviewer. The Giver is not explicitly associated with any entity but may interact with all of them.

<img alt="Relations between Communities, Campaigns and Traces" src={useBaseUrl('img/content/trace/role-locality.svg')} />

### Currency Flow
Giveth TRACE on a technical level is a system for managing currency. Terms referring to the movement of funds within the Giveth system are defined as follows:

* **Donation:** When a Giver sends funds from their wallet to a Trace, Campaign, or Community.
* **Collecting:** When the Recipient sends or "collects" funds from a Trace to their wallet.
* **Disbursing:** When a Trace Manager sends funds from a Trace account to the Recipient's wallet.
* **Delegation:** When a Campaign Manager or Community Manager sends money from the Campaign or Community account to Trace account on behalf of the original Giver. A Giver can reject Delegation within 72 hours, after which the Currency transfer becomes irreversible.
* **Refund:** A Giver who has contributed to a Community can withdraw their funds as long as they are not yet committed to a Campaign or Trace. A Giver contributing to a Campaign can withdraw their funds as long as they are not yet committed to a Trace.

<img alt="Currency Flow on Giveth TRACE" src={useBaseUrl('img/content/trace/currencyFlow.svg')} />

###### Currency Flow on Giveth TRACE

## Entities
Giveth TRACE, on a technical level, is a system for managing currency. The DApp’s entities are accounts to which people can deposit, transfer or withdraw currency. We have three entities on Giveth TRACE, <a href="#communities">**Communities**</a>, <a href="#campaigns">**Campaigns**</a> and <a href="#traces">**Traces**</a>. The relationship between them are defined in the chart below. Each entitity corresponds to one or more smart contracts.

***Note:** In Q1 2021 the Giveth team rebranded the entities **DAC**s (Decentralized Altruistic Communities) to simply **Communities**, and **Milestones** to **Traces**.*

<img alt="Relationship between The DApp's Entities" src={useBaseUrl('img/content/trace/relations.svg')} />

##### Relationship between the DApp's Entities

### <a name="communities">Communities</a>

Communities, **formerly known as DACs**, are the most general entity in the Giveth System. The purpose of a Community is to unite Givers around a cause and provide them with the possibility to give money to a cause without having to do the research involved in finding the exact Campaign to contribute to. Any money donated to a Community can be retrieved by the Giver, however we strongly discourage Givers to do so. The funds remain in the Community until they are delegated to a Campaign or a Trace, or withdrawn by the Giver. **Community Managers** can support any Campaign or Trace by sending currency to the account of the recipient.

<img alt="Community to Campaign delegation state diagram" src={useBaseUrl('img/content/trace/dac-campaign-donation-statediagram.svg')} />

##### **State diagram for Community -> Campaign delegation flow**, showing how donations made to a DAC are delegated to a Campaign.

<img alt="Community to Trace delegation state diagram" src={useBaseUrl('img/content/trace/dac-milestone-donation-statediagram.svg')} />

##### **State diagram for Community -> Trace delegation flow**, showing how donations made to a Community are delegated directly to a Trace.

### <a name="campaigns">Campaigns</a>
Campaigns are in the center of the Giveth donation system. They are effectively tools to steer money towards the smallest entities, Traces. A Campaign can be supported by more than one Community or by no Community at all. Campaign co-owners can only accept or reject proposed Traces. **Campaign Reviewers** can cancel the Campaign if the Campaign is bad or no longer active.

Donations made to a Campaign are locked, and unless the Campaign gets cancelled, the Giver no longer has control over the donation. The reason we lock the donations is to give the people behind the Campaign some level of certainty that they can count on getting the pledged donations and pledge them to one of their Traces.

<img alt="Campaign Donation state diagram" src={useBaseUrl('img/content/trace/campaign-donation-statediagram.svg')} />

##### **State diagram for donations made to Campaign.**


### <a name="traces">Traces</a>
The main building blocks of the DApp are Traces, **formerly known as Milestones**. A Trace is the only way by which funds can exit the Giveth system. Traces must be created inside of a Campaign. Compared to a Community or Campaign, Traces are more complex because more roles can interact with them.

### <a name="traceTypes">Trace Entities</a>
To tailor Traces to meet the specific needs of Communities and Campaigns, there are certain rules that can be applied.

 * **Capped Traces:** The maximum currency which can be given to to the Trace is set. This maximum is called the cap.
* **Trace with Reviewer:** The funds cannot be collected or disbursed from this Trace without confirmation by an assigned Trace Reviewer.
* **Specify Currency Received:** The Trace Creator is able to specify which of the whitelisted cryptocurrencies they would like to receive their funds in.

Based on these rules we can have *four* types of Traces with their own distinct properties: **Milestones, Bounties, Expenses** and **Payments**.


### **Milestones**
**Important goals or events for a Campaign. Any funds collected in Milestones go to the Campaign that it is a part of.**

*The Lifecycle of Milestones in the DApp is as follows:*

<img alt="Lifecycle of Milestones" src={useBaseUrl('img/content/trace/milestone.png')} />

###  **Bounties**
**If a Campaign or Community needs to outsource work to be done, they can use a Bounty to compensate contributors for completing specific tasks.**

*The Lifecycle of Bounties is as follows:*

<img alt="Lifecycle of Bounties" src={useBaseUrl('img/content/trace/Bounty.png')} />


### **Expenses**
**If there are recurring or singular expenses that were paid by a Campaign or Community Member, they can be tracked and reimbursed by this Trace.**

*The Lifecycle of Expenses is as follows:*

<img alt="Lifecycle of Expenses" src={useBaseUrl('img/content/trace/Expense.png')} />

### **Payments**
**Payments are compensation to Campaign members for the work they have done. Payments can be uncapped or capped for the funding they can receive.**

 *The Lifecycle for Payments with NO cap is as follows:*

 <img alt="Lifecycle of Payments without Cap" src={useBaseUrl('img/content/trace/paymentNoCap.png')} />


 *The Lifecycle for Payments with a cap is as follows:*

 <img alt="Lifecycle of Payments with Cap" src={useBaseUrl('img/content/trace/paymentWithCap.png')} />


A breakdown of their functions can be summarized in the table below:


| Trace Type      | Funding is Capped | Specify Currency Received   |  Can Assign Reviewer | Currency Destination |
| --------------- | ------ | --- | ------------- | -------------------- |
| Milestone       | No     |  No   | Yes           | Campaign             |
| Bounty          | No     |  No   | Yes           | Any Address          |
| Expense         | Yes    |  Yes   | No            | Any Address          |
| Payment NO Cap | No     |  Yes   | No            | Any Address          |
| Payment with Cap  | Yes    | Yes    | No            | Any Address          |

### Notes:
* *In coding Entities are called `projects`.*
* *When money goes from a Community to a Trace or Campaign, Giveth then connects the Community with that Campaign or Trace. This means that you will see that Campaign or Trace represented on the Community page.*
* *If a Trace/Campaign/Community is canceled, the funds are returned to the source contributor automatically.*
* *Currency that goes to a Community is a loose commitment: at any point up until the moment funds are locked into a Campaign/Milestone, the Giver can decide to withdraw (refund) them.*
* *Currency that went to a Campaign/Trace is fully committed, because Trace Managers and Campaigns Manager take actions based on these funds.*
---
id: exchangeRates
title: Exchange Rates
slug: dapps/exchangeRates
---
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


When you leave a Trace within [Giveth TRACE](https://beta.giveth.io), you can enter an amount in ether or in fiat. Our system then automatically calculates the conversion rate based on the date of the Trace.

In our Feathers backend we keep a cache of the daily average exchange rate for each date. We use [Crypto Compare](https://min-api.cryptocompare.com/) and [CoinGecko](https://www.coingecko.com/en/api) to fetch these rates.

When you enter a currency amount in a Trace, we fetch the cached conversion rate from Feathers and calculate the result in the UI. When you save the Trace we check that conversion again to make sure all is correct.

Currently we support handling payments in ETH, SAI, DAI, PAN, WBTC, USDC Ethereum Mainnet Tokens. Native currencies whitelisted for trading pair price comparsions are BTC, ETH, AUD, GBP, USD, MXN, CAD, CZK, THB, BRL, CHF.
---
id: givbacks
title: GIVbacks
slug: giveconomy/givbacks
---
import useBaseUrl from '@docusaurus/useBaseUrl';

GIVbacks is a revolutionary concept that rewards donors to verified projects with GIV. When you give to verified projects during a GIVbacks round, you become eligible to receive GIV rewards after the round ends and the GIV is ready to claim. You can see live information --- including round schedule & your claimable GIV --- on the [GIVbacks page](https://giveth.io/givbacks).

## GIVbacks Rounds
GIVbacks rounds last two weeks. For each round, there is 1 million GIV available to be rewarded.

![](https://i.imgur.com/cBBSzJa.png)

Givers who donate to verified projects within an active round are eligible to receive GIVbacks. Note that addresses of verified projects will not receive GIV for donations made to their own project or other verified projects.

![](https://i.imgur.com/aklPnKC.png)


## Project Verification
'Verified' is a seal of approval for legitimate projects on Giveth. Many Verified projects came pre-vetted from [The Giving Block](https://twitter.com/TheGivingBlock) API. The Giving Block is an organization that supports and onboards registered 501c3s from the United States into crypto, and with our integration, you can donate to their projects from the Giveth UI.

For non-Giving Block projects, the verification process requires projects to provide additional information about their project and the intended impact of the organization. Our amazing Project Verification Team then reviews these applications, investigates the information provided and informs the project owners about the verdict.


To learn more about the project verification process check out our [documentation](./projectVerification.md).


## Tokens Eligible for GIVbacks

A donor can donate any ERC-20 token to projects on Giveth.io on Gnosis Chain (formerly xDai Network) or Ethereum Mainnet. However, only donations to verified projects in certain tokens are eligible for GIVbacks. This restriction ensures that we are able to get accurate price data for donations (a requirement for fair distribution of GIVbacks), and prevents bad actors from gaming the GIVbacks program. To see the full list of eligible tokens, visit [this forum post](https://forum.giveth.io/t/givbacks-token-list/253).

## Getting GIVbacks
During each round, all donations to verified projects on the DApp are tracked, and this data is used to calculate the amount of GIVbacks received by each Giver for that period.

Givers are able to claim their GIV after the round ends and a fraud review has been conducted. Donors will receive an email when the rewards are ready to be claimed on the [GIVbacks page](https://giveth.io/givbacks). A portion of the GIV will be liquid immediately, and the rest will increase the flowrate of their [GIVstream](https://giveth.io/givstream). To learn more about the GIVstream and how it works, check out our [documentation](https://docs.giveth.io/giveconomy/givstream/). For the purposes of this documentation, we will refer to the sum of the liquid amount and the amount allocated to the GIVstream from GIVbacks as `cumulative GIVbacks`.

### Rank & Calculation

Note that, even with the GIVbacks program, a donation on Giveth is still a donation. The maximum value of the donor's `cumulative GIVbacks` could be **anywhere from 50% up to 80% of the USD value of their donation**, at the time of donation. The exact amount of GIVbacks they receive will depend on the [project's current GIVpower rank](./GIVpower.md#project-rank). Each verified project that has been boosted with [GIVpower](./GIVpower.md) will have a rank on the platform. The project that has been boosted with the most GIVpower for the previous bi-weekly round will offer the highest GIVbacks factor percentage (80%), while the lowest ranked project and unranked/unboosted projects for the previous round will receive the lowest GIVbacks factor percentage (50%). Each project from the bottom to the top ranked will have an incrementally higher GIVbacks factor percentage, you can learn more in the [GIVpower documentation](./GIVpower.md#project-ranking).

:::info 
GIVbacks sent to donors of verified projects before December 27, 2022 (when project ranking took effect) were calculated using a maximum GIVbacks factor of 75%.
:::

If, at the end of a round, the estimated amount of GIVbacks to distribute exceeds the limit of 1 million GIV per round then donors will receive proportionally less matching relative to the rank of the project they donated to, for each donation. This is calculated as follows:

$$
n = N \frac{g}{G}
$$

where:

- n = Total cumulative amount of GIV tokens earned by the donor for a particular donation
- N = Total number of GIV tokens allocated for distribution in the round (1 million GIV)
- g = The estimated full amount of GIVbacks the donor could receive.
- G = Total estimated amount of GIVbacks for all donors during the given round.

GIV tokens earned through the GIVbacks program can be used throughout the GIVeconomy: for governance within the [GIVgarden](https://giveth.io/givgarden), locking GIV & boosting projects with [GIVpower](https://giveth.io/givpower) or for donating to projects on [Giveth](https://giveth.io/).

:::note
**Referral Program**

Since the launch of the Giveth Referral Program, when making a donation on Giveth using a referral link, part of the GIVbacks generated from that donation will be shared with the person who referred you. As a result, the GIVbacks amount you receive will be lower than if you had made the donation directly without a referral link. Please check our [referral program documentation](./referralprogram.md) for more information about how GIVbacks are calculated for referrals.
:::

## Harvesting GIVbacks

GIVbacks are available to be harvested after the round ends, data has been reviewed and GIV is distributed to eligible donor addresses. Donors will receive an email when GIVbacks rewards are ready to claim - this GIV can be harvested [here](https://giveth.io/givbacks). Please note that when you harvest GIV rewards from any part of the GIVeconomy, our token distro contract sends you all liquid GIV allocated to your address on that network. For example, when you harvest GIV rewards earned from staking LP tokens in the GIVfarm on Gnosis Chain (formerly xDai Network), you also harvest rewards allocated to you from GIVbacks (if any) and the liquid amount from your GIVstream. This is broken down in the harvest popup that you encounter upon claim:

![](https://i.imgur.com/GVpn68a.png)


---
## Disqualifying Factors for the GIVbacks Program

Once a GIVbacks round ends, there is a period of time granted to our team to review flagged projects and donations for the following disqualifying factors before GIV is distributed to donors. A project could have their ‘Verified’ status revoked if any of these factors are found. Donors to projects who are found with any of the following activity may also be denied GIVbacks for that round.

1. **Giving/offering goods or services to donors in exchange for their donation.** A project owner cannot offer goods such as a sponsorship for a conference, Girl Scout cookie purchases or tickets for a dinner, even if the proceeds go to charity. Project owners cannot provide services like acting as a crypto exchange for their donors. They can explain how to use an exchange, but they cannot convert the money for their donors.
2. **Circulating donations raised by other means.** Only “first touch” donations count for GIVbacks. If a project receives funding from a donor and is found to be circulating these donations within the Giveth platform to receive GIVbacks, they will be disqualified. For example, a project should not be sending fiat donations received elsewhere back to their donors and asking them to donate on Giveth with crypto.
3. **The funds are not being used for what is expressed in the project page or submitted verification application.** Verified projects are responsible for keeping their projects up-to-date with information on how the funds are being used. If the project states explicitly that they are, for example, using the funds to develop education programs but are found to be using the funds to employ developers, they may be disqualified from the GIVbacks program.
4. **Unscrupulous or fraudulent activity.** This can be the use of violence, breaking laws, or other behaviour that does not uphold the [values of the Giveth community](https://docs.giveth.io/whatisgiveth/). Projects found to be violating our [Terms and Conditions](https://giveth.io/tos) will not only lose their verification status, but also will be canceled.

The Giveth Project Verification team is responsible for monitoring GIVbacks activity and the Project Verification system, and will ultimately use their discretion to determine whether a project’s actions are unscrupulous and/or disqualifying.

## Sanctions for flagged donations

Verified projects and donations that are flagged for any of the disqualifying factors above will be analyzed and discerned according to the sanctions outlined here:

- A donor whose GIVbacks were revoked because they were found to be recirculating funds or donated to a project that was disqualified for that round will receive an email with a link to the forum post discussing eligible donations for that round. Donations cannot be refunded and GIVbacks cannot be “unrevoked” if the project was disqualified from the round.

Donations are donations and they go directly to the project. The GIVbacks program was created to additionally empower our donors with GIV & therefore governance rights, but you should not make a donation purely out of the expectation of receiving GIV. We appreciate your understanding.

---

**The GIVbacks program is our way of giving back to those who give. It’s our exit to the community - empowering real donors with governance power over the future of Giveth and hence, the Future of Giving. To get GIVbacks, [start donating to verified projects today](https://giveth.io/projects)!**
---
id: givdrop
title: GIVdrop
slug: giveconomy/givdrop
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from '../src/css/custom.css'


The GIVdrop is designed to kickstart the GIVeconomy by distributing GIV tokens to the Giveth trusted seed - crypto philanthropists, Giveth users & builders, Blockchain4Good DAO members, and other ecosystem partners. To check your GIVdrop eligibility or to claim [click here](https://giveth.io/claim). To learn how to claim your GIVdrop, refer to our tutorial below.

All addresses have [until Decemember 24, 2022](https://forum.giveth.io/t/ending-the-givdrop/880) to claim their GIVdrop. After that, any unclaimed tokens will be returned to the Giveth DAO.

## GIVdrop Eligibility

17.05% of the total initial supply (1 billion GIV) has been distributed to our trusted seed. The trusted seed is a group of individuals - previous supporters  10% of these tokens are instantly claimable on Gnosis Chain (formerly xDai Network) as the GIVdrop. The rest initializes and sustains [the GIVstream](https://docs.giveth.io/giveconomy/givstream) - a flow of GIV that becomes claimable gradually and continuously until December 23, 2026.

Eligible recipients of the GIVdrop and the associated GIVstream include:

- Giveth Contributors 5.05%
- Past donors to Giveth directly 4%
- Blockchain4Good heroes 4%
- Past donors to projects on Giveth 2%
- Past users of beta Giveth TRACE 1%
- Past donors to Gitcoin Grants in Rounds 1-7 1%

The Blockchain4Good DAO heroes group includes a list of over 2500 unique addresses, with over 60 different groupings. The majority of addresses belong to people who have been identified as crypto donors, with the rest belonging to value-aligned DAO members that are working, directly or indirectly, to further [Giveth's mission](https://docs.giveth.io/whatisgiveth/). You may have a GIVdrop if you are part of any of these groups (and many others!):

- 1Hive
- ChievMint
- clr.fund
- Commons Stack Trusted Seed
- Crypto Commons Gathering
- Ethereum Foundation
- General Magic
- MetaCartel DAO
- MetaGame
- MetaGammaDelta
- MolochDAO
- STAKEhausDAO
- TEC Hatchers
- TrojanDAO
- Vocdoni
- WeTrust
- WhalerDAO


<span class="importantText">The snapshot for past donors and Giveth users was taken in March 2021.</span> The snapshot for contributors (builders) and Blockchain4Good DAO heroes was taken in September 2021. <span class="importantText">For donors to Gitcoin Grants, GIVdrop eligibility was for those who donated in <i><u>at least two rounds</u></i> from rounds 1-8.</span> Our snapshot was taken at those times because the token development was all public, and we didn't want to give all of the GIV to the airdrop hunters that have proliferated throughout the past year.

:::info
We have made every effort to include all valid addresses in this GIVdrop made at our discretion. Not every person who has ever interacted with Giveth is eligible. If you did not receive GIV, that is because you were not eligible or the wallet that stores the address that was eligible can not be accessed. We will not review past transactions or consider other addresses for inclusion. We appreciate your understanding.

If you did not receive the GIVdrop, check out our [GIVbacks program](https://giveth.io/givbacks) to find out how to get GIV!
:::

**NOTE:** If you received the GIVdrop but no longer have access to the eligible address, it is possible for us to redirect the allocation to another ETH address. However, you need to prove who you are and that you do have tokens allocated to you. If this is you, reach out to our team for support. FYI - if no one in the Giveth team knows you, it probably won't work out.

## Claiming your GIVdrop

The GIVdrop was released on December 24, 2021. In this guide we'll walk you through how to claim your GIV on the GIVdrop claim page.

First thing is to head over to [the GIVdrop claim page](https://giveth.io/claim); you should arrive at this screen:

<img alt='check GIVdrop eligibility' src={useBaseUrl('/img/content/giveconomy/claimConnect1.png')} />

From here you will need to connect your web3 wallet to the DApp to check your eligibility.

After connecting, one of three situations will happen:

1. <a href="#1-givdrop-to-claim">You have a GIVdrop to claim, NICE!</a>
2. <a href="#2-the-address-provided-has-already-claimed-its-givdrop">The address provided has already claimed its GIVdrop, GREAT!</a>
3. <a href="#3-you-missed-the-givdrop-sad-face"> You missed the GIVdrop. :( </a>

Click on any of the above situations to learn how to proceed. To learn more about GIVdrop eligibility, click [here](./givdrop).

---
### 1. GIVdrop to Claim

If you have a GIVdrop ready to claim that's great news! Click the arrow to dive into the GIVdrop claim process.

<img alt='you have giv to claim' src={useBaseUrl('/img/content/giveconomy/claimReady1.png')} />

Go through the flow to learn all the amazing ways to participate in the GIVeconomy. You can see your GIVdrop and GIVstream and visualize the impacts your GIV could make in the GIViverse.

<img alt='how to use your GIV' src={useBaseUrl('/img/content/giveconomy/claimReady2.png')} />


On the final page you can claim your GIVdrop as well as add the GIV token to your MetaMask wallet. When you click `CLAIM` you'll see a summary of all the GIV you're getting.

<img alt='claim your giv now screen' src={useBaseUrl('/img/content/giveconomy/claimReady3.png')} />

In addition to the GIVdrop, you'll also receive a GIVstream which will continuously stream you GIV for a period of up 5 years - learn more about the [GIVstream here](./givstream).

<img alt='harvesting your GIVdrop' src={useBaseUrl('/img/content/giveconomy/claimHarvest1.png')} />


Click `HARVEST` to generate the transaction to claim your GIVdrop to your connected wallet.

You're now equipped and ready to jump into the GIVeconomy - Discover all the great ways you can contribute to a [thriving economy of Giving](https://giveth.io/).


---

### 2. The address provided has already claimed its GIVdrop

You already claimed the GIVdrop for the address you provided. However, you have no shortage of options now at your disposal. Give us a shout out on Twitter, and join our Discord to see the action happening in our Community.

<img alt='you already claimed' src={useBaseUrl('/img/content/giveconomy/claimClaimed1.png')} />

We also have dropped you some gLove tokens on Rinkeby that you can exchange for some awesome Giveth Swag! Check out our [Swag Store](https://swag.giveth.io/) to see all our custom designed apparel and mugs!

Lastly, and most importantly, click `Explore the GIVeconomy` to jump into GIVeconomy and explore all of the wonderful GIVing opportunities available.

---

### 3. You missed the GIVdrop (sad face)

Unfortunately the address provided didn't receive a GIVdrop. Check the wallet address you provided or that you've connected with the correct wallet address.
<img alt='you missed the GIVdrop' src={useBaseUrl('/img/content/giveconomy/claimMissed1.png')} />

If you missed out, don't fret; there are still other ways to get GIV! You can follow the link on the [GIVfarm](https://giveth.io/givfarm) page to take you to your local friendly Decentralized Exchange (on Mainnet or Gnosis Chain [formerly xDai Network]) to swap your crypto for some of that sweet, sweet GIV.

<img alt='buy tokens link from GIVfarm' src={useBaseUrl('/img/content/giveconomy/claimMissed2.png')} />

Or if you want to be a real GIVhero, participate in the GIVbacks program. You can qualify to earn GIV from donating to verified projects on [giveth.io](https://giveth.io/projects/). Learn more about the [GIVbacks program here](./givbacks).

---

### If you get stuck in the GIVdrop claim:
You could find yourself stuck in the GIVdrop Connect page for a variety of reasons including:
- Declining to connect your wallet in MetaMask
- Not connected to Gnosis Chain (formerly xDai Network)

To remedy this, open up your MetaMask extension, and verify your connection:
<img alt='troubleshooting getting stuck' src={useBaseUrl('/img/content/giveconomy/claimStuck1.png')} />

Ensure you're on Gnosis Chain (formerly xDai Network), and connect the wallet you'd like to claim for to the DApp. If the page doesn't update automatically just give it a quick refresh (F5), and you should be good to go!
---
id: giveconomy
title: GIVeconomy
slug: giveconomy/
---
import useBaseUrl from '@docusaurus/useBaseUrl';


Giveth is building a culture of giving that empowers and rewards those who give -- to projects, to society, and to the world. We aim to inspire our community to participate in an ecosystem of collective support, abundance and value-creation. **Welcome to the GIVeconomy.**

## About GIV

GIV is the governance token that fuels and directs the GIVeconomy. GIV holders are empowered to collectively coordinate around shared resources and fund initiatives that shape the Future of Giving.

At launch, our community can participate in the GIVeconomy in the following ways:
- From December 24, 2021 onward, eligible recipients can claim their [**GIVdrop**](./givdrop) on Gnosis Chain (formerly xDai Network).
- Donors to [verified projects](https://giveth.io/projects) on Giveth get rewards from [**GIVbacks**](./givbacks).
- Liquidity providers and stakers can earn rewards in the [**GIVfarm**](./givfarm).
- All GIV holders can create and/or vote on proposals in the [**GIVgarden**](./givgarden).
- Anyone who claims GIV from their participation in the GIVeconomy gets a continuous flow of GIV from the [**GIVstream**](./givstream) until December 23, 2026.

### Token Info

- Token Address on Mainnet: 0x900db999074d9277c5da2a43f252d74366230da0
- Token Address on Gnosis Chain (formerly xDai Network): 0x4f4F9b8D5B4d0Dc10506e5551B0513B61fD59e75

### Distribution

An amount of 1 billion GIV tokens were minted at the onset of the GIVeconomy. 100 million of the GIV tokens are liquid and available for use immediately, and the other 900 million have been allocated to the [GIVstream](./givstream) and are being released continuously throughout the entire "GIViverse" over a period of 5 years (until December 23, 2026). The distribution of the total supply of GIV throughout the GIViverse is outlined in the following graphic:

<img alt='givbacks round 8 sample' src={useBaseUrl('/img/content/giveconomy/giveconomyDistro.jpg')} />

The GIVeconomy has been built thanks to our dedicated community of Givers. Giveth has been growing since 2016 on a foundation of donations, time, skills, sweat, generosity & love! We are proud to launch an economy by and for the donors, with no money gleaned from presales or venture capitalists.

## The GIVeconomy Future

The launch of GIVeconomy with all the features described above is only the beginning - we are already crafting the next phase of the Future of Giving. We're developing systems that will completely change the way societies create and reward the creation of public goods.

Keep reading to learn more about some of the raw, exciting and beautiful ideas that we intend to bring to fruition. If you want to have a hand in shaping the next generation of philanthropy, start to [explore GIVeconomy](https://giveth.io/) and [join our team](https://giveth.io/join)!

### **GIVpower**
GIVpower will, over time, decentralize GIVbacks. Community members will be able to allocate GIVpower to signal support for the favourite projects on Giveth and donors who give to community favoured-projects will get proportionally more GIVbacks. GIVpower users will earn rewards on the GIV they stake & lock for GIVpower, and the rate of reward will be higher if they choose to stake & lock their tokens for a longer period of time.

### **GIVmatching**
Giveth plans to implement donation matching to projects on Giveth using "Causes". Causes will be for-good initiative categories such as environmental regeneration, digital public goods, social causes, etc. Donors will be able to donate to Causes, and these pools of funds will then be distributed to community-favoured projects (as donation matching) using [quadratic funding](https://wtfisqf.com/?grant=&grant=&grant=&grant=&match=1000).

### **GIVfi**
The intention with GIVfi is to create a sustainable way of maintaining funds in the GIVgarden common pool. While donations on the DApp are waiting to be disbursed, they will be generating interest that can be used to send GIV to the GIVgarden for funding initiatives using Conviction Voting.

<img alt="GIVfi diagram" src={useBaseUrl('img/content/giveconomy/GIVfi.jpg')} />

### **GURVES**
Our biggest dream is to support for-good projects on Giveth to become their own microeconomies. The idea is when a donor gives to a verified project on Giveth, they get some GIV from the GIVbacks program. When this happens, some GIV is put into a [bonding curve](https://thegraph.academy/curators/introduction-to-bonding-curves/) that is uniquely generated for the project. The donor then receives freshly minted "project tokens" from the bonding curve. Projects are in effect being gifted their own token economy, opening up endless possibilities for incentives and system design!


<details>
  <summary><h3><i>*Interacting using the Torus Wallet</i></h3></summary>
  <div><p>To interact with the [GIVeconomy](https://giveth.io/) and other dApps using the Torus wallet, you will have to connect your wallet. To connect, click the “Connect Wallet” icon in the upper right corner of the site, then select Torus and verify. The Torus wallet allows users to sign in with accounts from many different web services, so be sure to sign in with the same account you used to set up the wallet.</p>

  <img alt="Signing in with Torus on the GIVeconomy" width="50%" height="auto" class='center' src={useBaseUrl('img/content/giveconomyTorusConnect.png')} />

  <p>If you are using the Brave browser, you will need to turn off Brave’s Shield feature. To do this, click the Brave logo to the right of the search bar, then toggle the Shield to off.</p>

  <img alt="Turning shields off with Brave" class='center'  width="35%" height="auto" src={useBaseUrl("img/content/giveconomyShieldsDown.png")} />
  </div>
</details>


-----

Giveth's mission is to reward and empower those who give. [The GIVeconomy](https://giveth.io/) is a major milestone in the Future of Giving and is enabling our collective of projects, donors, builders, and community members to give in new ways that support projects, society & the world!
---
id: givethioinstallation
title: Installing Giveth.io for Local Development
slug: dapps/givethioinstallation
---

import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

This guide will document the steps to set up and run Giveth.io locally for the purposes of development. The setup process was documented using Ubuntu 20.04 LTS.

#### **You'll need a couple prerequisites to get started.**

 - [Redis](https://redis.io/topics/quickstart)
 - [Postgres](https://www.postgresql.org/download)
 - Node 14+
 - yarn
 - npm
 - Your favourite Code Editor (VScode for linting presets)

#### **Giveth IO leverages notable packages, applications and architectures including:**  
 - Ethereum
 - React
 - NextJS
 - Apollo GraphQL
 - Tor.us
 - theme-ui

### Install the back-end (impact-graph) from GitHub
In order to develop locally you need to clone the back-end server. We are using https://github.com/Giveth/impact-graph for this.

*via SSH on the CLI:*
```bash
    git clone git@github.com:Giveth/impact-graph.git
    cd impact-graph
    npm i
    cp .env.example .env
```


### Create a Database and User in Postgres using psql
Follow this tutorial on PSQL to setup your username and create the database.
https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)

**TL;DR**
```bash
sudo -u postgres psql
postgres=# create database <databaseName>;
postgres=# create user <userName> with encrypted password '<passwordHere>';
postgres=# grant all privileges on database <databaseName> to <userName>;
```
### Clone and Install the Frontend
  Head on over to https://github.com/Giveth/giveth-next, and clone the repo.  

  *via SSH on the CLI:*
  ```bash
  git clone git@github.com:Giveth/giveth-next.git
  cd giveth-next
  yarn install
  ```

### Get the Environment Variables
 In order to run the local build for Giveth.io you'll need to ask for the environment variables. Head on over to our [Contributors Discord](https://discord.giveth.io), say Hi and get in touch with our product manager, @MoeNick or one of the developers.


### Launch the Development Server and Environment
 Start up the `impact-graph` backend server and redis.
  - Run redis by using the command `redis-server`.
  - From the impact-graph repo start with `npm start`.

  :::info
  ### Using the Staging Database for Development
  If you don't need to setup a local database for your development purposes you can use the staging database instead. Set `NEXT_PUBLIC_APOLLO_SERVER` to `https://serve.giveth.io/graphql` (this uses the same database you see on https://next.giveth.io).
  :::


### Run the Migrations to Setup the Database
In a separate terminal `cd` into the `impact-graph`
run this command in the terminal:
```bash
npm run typeorm:cli -- migration:run
```

### Deploy the Front-end
 To take advantage of linting presets, please use **VSCODE**:
 * Select *File -> Open Workspace*.
 * Navigate into the giveth-next directory.
 * Open the workspace file `giveth2-full-stack.code-workspace`.
 * Install recommended extensions (Prettier and StandardJS plugins).
 * Then fire up the front-end locally.

 ```bash
 yarn run dev
 ```

### Start Editing!

Open up the giveth-next repo on your code editor.

Giveth.io is now running locally at `http://localhost:8000`!

<img id="contentimg" alt='Giveth Running Locally' src={useBaseUrl('img/content/givethlocalresized.png')} />

You can also expiremnt with querying your data via GraphQL. You'll find it at this link here: `http://localhost:8000/___graphql`
Learn more about using this tool in the [Gatsby tutorial](https://www.gatsbyjs.org/tutorial/part-five/#introducing-graphiql).

  Save your changes, and the browser will update in real time!

**Current Build Statuses**

[master](https://giveth.io)

[![Netlify Status](https://api.netlify.com/api/v1/badges/f914ac7e-ce27-4909-bd3e-14d749731a52/deploy-status)](https://app.netlify.com/sites/giveth2/deploys)

[staging](https://next.giveth.io)

[![Netlify Status](https://api.netlify.com/api/v1/badges/2f325b5b-e159-443e-bac7-c5e15f3578c0/deploy-status)](https://app.netlify.com/sites/giveth-website-staging/deploys)
<br />
---
id: givethMatchingPool
title: Giveth Matching Pool
---

The [Giveth Matching Pool](https://giveth.io/project/Giveth-Matching-Pool-0) is raising funds to distribute to [verified projects](https://docs.giveth.io/dapps/projectVerification/) on Giveth. It is perfect for donors who want to have a broad impact for public goods while getting rewarded with GIVbacks. 

The Giveth Matching Pool recipient address is a 7/15 multisig at [donation.eth](https://etherscan.io/address/0x6e8873085530406995170da467010565968c7c62) that is managed by core Giveth team members. Donations made to this project, or directly to the donation.eth multisig, on Mainnet or Gnosis Chain are eligible for GIVbacks. 100% of collected funds by this multisig  will be distributed to verified projects on Giveth. Only donations on the [GIVbacks token list](https://forum.giveth.io/t/givbacks-token-list/253) are eligible for GIVbacks. 

We have a raise goal of $500,000, and once it is achieved, we will begin to distribute the funds to verified projects on Giveth at the end of each 2-week donation round. The raise goal ensures we have enough funds to provide significant matching ($10-20k) every 2 weeks for a full year (26 total rounds).

The exact details of how the donations will be distributed are to be determined. Please contribute your feedback and ideas to help us design the system for allocating these matching funds by weighing in on [our forum](https://forum.giveth.io/t/givmatching-idea-generation-on-how-to-distribute-funds/346). We’ll keep you posted with the results in [project updates](https://giveth.io/project/Giveth-Matching-Pool-0)!


---
id: givfarm
title: GIVfarm
slug: giveconomy/givfarm
---

:::caution 
[**On October 29, 2022, the GIVfarm was exploited on ETH Mainnet**](https://twitter.com/Givethio/status/1591431388271677440), all funds in the Mainnet farming contracts were drained and stolen. The Giveth Community voted subsequently to not restart any of the affected farms. Currently **most GIV liqudity farming programs have ended since**, with the exception of [GIVpower Staking :rocket:](./GIVpower.md#givfarm-apr), there are no plans to launch any new GIVfarm programs in the future. However there are still opportunities to **earn liquidity rewards through the [RegenFarm program](./regenfarms.md)**.

 This documentation article will remain for historical reference.
:::

The GIVfarm launched on **December 24, 2021**. 3.5% of the total token supply, 35 Million GIV, has been allocated to the first GIVfarm round of 6 months, 65 million tokens are held in a multisig for future liquidity provision. Farms are available on either **Ethereum Mainnet (ETH)** or **Gnosis Chain** (formerly xDai Network). Any farms you stake tokens into will yield GIV rewards and add to your [GIVstream flowrate](https://docs.giveth.io/giveconomy/givstream) only for that corresponding chain. GIV reward distribution for the 6 pools available is as follows:

| Pool                          | Tokens Allocated |
| ----------------------------- | ---------------- |
|80GIV/20ETH Balancer on Mainnet|2.5 Million GIV|
|GIV Staking on Mainnet|2.5 Million GIV|
|GIV/HNY Honeyswap on Gnosis Chain (formerly xDai Network)|10 Million GIV|
|GIV/WETH Sushiswap on Gnosis Chain (formerly xDai Network)|2.5 Million GIV|
|GIVgardens Staking on Gnosis Chain (formerly xDai Network)|7.5 Million GIV|

:::info
### A Note:  
10 Million GIV was originally allocated as rewards for a GIV/ETH Uniswap V3 pool on Mainnet. However, we detected one actor that was abusing a vulnerability in the system to earn rewards disproportionately and then dump the GIV. The community voted to terminate the Univ3 rewards program ([snapshot](https://snapshot.org/#/giv.eth/proposal/0xfad6aa3baa36d5f2d7acdf135752aafca06201b77a80aee79baf6ff3f5bbaae5)), and they were shut off on March 21st, 2022. You can learn more about it [here](https://twitter.com/Givethio/status/1505981603293585410).
:::

The amount claimable from rewards on the day of launch will be 10% with the other 90% allocated to flow out from the GIVstream. The GIVstream will flow for 5 years, and as time passes, the greater the amount immediately claimable from rewards will be. As you earn rewards in the GIVfarm, you also increase the flow rate of your GIVstream.

### Token Addresses
GIV Mainnet - 0x900db999074d9277c5da2a43f252d74366230da0
GIV Gnosis Chain (formerly xDai Network) - 0x4f4F9b8D5B4d0Dc10506e5551B0513B61fD59e75

### Staking Contract Addresses (Mainnet)
- Balancer v2 80GIV/ETH Pool -0xc0dbDcA66a0636236fAbe1B3C16B1bD4C84bB1E1
- GIV Staking  - 0x3115e5aAa3D6f742d09fbB649150dfE285a9c2A3
### Staking Contract Addresses (Gnosis Chain (formerly xDai Network))
- GIV Staking - 0xD93d3bDBa18ebcB3317a57119ea44ed2Cf41C2F2
- GIV/HNY Honeyswap - 0x4B9EfAE862a1755F7CEcb021856D467E86976755
- GIV/WETH SushiSwap -  0xfB429010C1e9D08B7347F968a7d88f0207807EF0

### LP Token Addresses (Mainnet)
- Balancer v2 - 0x7819f1532c49388106f7762328c51ee70edd134c
### LP Token Addresses (Gnosis Chain (formerly xDai Network))
- GIV/HNY Honeyswap -0x08ea9f608656A4a775EF73f5B187a2F1AE2ae10e
- GIV/WETH SushiSwap -  0x55FF0cef43F0DF88226E9D87D09fA036017F5586

## GIVfarming the GIVgarden
The GIVeconomy implements a unique feature in its GIV Staking pool on Gnosis Chain (formerly xDai Network). When you stake tokens in this farm, you are also wrapping those GIV in the GIVgarden. This means that while collecting rewards from the GIVfarm, you also unlock voting power within the [GIVgarden](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98) as long as you stay staked in this farm. Conversely, while wrapping GIV in the GIVgarden you are also staking tokens into the aforementioned GIV staking pool.

## Weekly Distribution

**Round 1 (26 weeks)** weekly GIV rewards distribution percentages based on GIVfarm liqudity mining supply are as follows:

| Week of Round | % of Rewards | # of GIV tokens |
| ------------- | ------------ | ---------------- |
| Week 1        | 7.75%        | 2,712,500        |
| Week 2        | 7.75%        | 2,712,500        |
| Week 3        | 6.00%        | 2,100,000        |
| Week 4        | 6.00%        | 2,100,000        |
| Week 5        | 4.75%        | 1,662,500        |
| Week 6        | 4.75%        | 1,662,500        |
| Week 7        | 3.75%        | 1,312,500        |
| Week 8        | 3.75%        | 1,312,500        |
| Week 9        | 3.25%        | 1,137,500        |
| Week 10       | 3.25%        | 1,137,500        |
| Week 11       | 3.00%        | 1,050,000        |
| Week 12       | 3.00%        | 1,050,000        |
| Week 13       | 3.00%        | 1,050,000        |
| Week 14       | 3.00%        | 1,050,000        |
| Week 15       | 3.25%        | 1,137,500        |
| Week 16       | 3.25%        | 1,137,500        |
| Week 17       | 3.50%        | 1,225,000        |
| Week 18       | 3.50%        | 1,225,000        |
| Week 19       | 3.75%        | 1,312,500        |
| Week 20       | 3.75%        | 1,312,500        |
| Week 21       | 3.25%        | 1,137,500        |
| Week 22       | 3.25%        | 1,137,500        |
| Week 23       | 2.75%        | 962,500          |
| Week 24       | 2.75%        | 962,500          |
| Week 25       | 2.00%        | 700,000          |
| Week 26       | 2.00%        | 700,000          |


Note that, as a result of the termination of the Univ3 rewards program in week 13 there is approximately 5M GIV, previously earmarked for these rewards, that are no longer part of the GIVfarm allocation.

Further rounds may be launched after this period that could contain new pools and changes in distribution. All rewards from GIVfarm will be affected by the GIVstream. Read up on the [GIVstream documentation](./givstream) for more information.

## GIVfarm Extension (Q2 2022)

The first GIVfarm Extension happened on June 24th, 2022. The farm was extended a further 8 weeks with an additional 4 Million GIV allocated to farming rewards. 

A flat **500,000 GIV** is distributed weekly from June 24th until August 19th 2022

Here is a breakdown of the farms, the percentage allocated to each and the flat amount of GIV distributed weekly:

| Farm | % Allocated | GIV Per Week |
| --- | --- | --- |
| GIV/DAI Uniswap V2 on Mainnet | 23% | 115,000 |
| 80GIV/ETH Balancer on Mainnet | 15% | 75,000 |
| GIV Staking on Mainnet | 5% | 25,000 |
| 50GIV/xDAI Honeyswap on xDai | 25% | 125,000 |
| 50GIV/WETH Sushiswap on xDai | 17% | 85,000 |
| GIVgardens/staking on xDai | 15% | 75,000 |

Here's the contract information:

#### Staking Contract Addresses (Mainnet)
- Balancer v2 80GIV/ETH Pool - 0xc0dbDcA66a0636236fAbe1B3C16B1bD4C84bB1E1
- GIV Staking  - 0x4B9EfAE862a1755F7CEcb021856D467E86976755
- Uniswap v2 GIV/DAI - 0xa4523D703F663615Bd41606B46B58dEb2F926D98
#### Staking Contract Addresses (Gnosis Chain (formerly xDai Network))
- GIV Staking - 0xD93d3bDBa18ebcB3317a57119ea44ed2Cf41C2F2
- GIV/xDAI Honeyswap - 0x24A6067fEd46dc8663794c4d39Ec91b074cf85D4
- GIV/WETH SushiSwap - 0xfB429010C1e9D08B7347F968a7d88f0207807EF0

#### LP Token Addresses (Mainnet)
- Balancer v2 - 0x7819f1532c49388106f7762328c51ee70edd134c
- Uniswap v2 - 0xbeba1666c62c65e58770376de332891b09461eeb
#### LP Token Addresses (Gnosis Chain (formerly xDai Network))
- GIV/xDAI Honeyswap - 0xB7189A7Ea38FA31210A79fe282AEC5736Ad5fA57
- GIV/WETH SushiSwap - 0x55FF0cef43F0DF88226E9D87D09fA036017F5586

## GIVfarm Extension (Q3 2022)

The GIVfarm was extended on August 19th, 2022 with most farms discontinued.

Here's the farms that were included in this extension:


| Farm | Duration in Weeks | GIV Per Week |
| --- | --- | --- |
| 80GIV/ETH Balancer on Mainnet | 12 | 75,000 |
| GIVgardens/staking on xDai | 6.5 | 100,000 |

#### Staking Contract Addresses (Mainnet)
- Balancer v2 80GIV/ETH Pool - 0xc0dbDcA66a0636236fAbe1B3C16B1bD4C84bB1E1

#### LP Token Addresses (Mainnet)
- Balancer v2 - 0x7819f1532c49388106f7762328c51ee70edd134c

#### Staking Contract Addresses (Gnosis Chain (formerly xDai Network))
- GIV Staking - 0xD93d3bDBa18ebcB3317a57119ea44ed2Cf41C2F2

We should also mention the Angel Vault launched on August 4th and will run for 26 weeks, you can find more details in the [Angel Vault documentation article](./angelVault.md).
---
id: givgarden
title: GIVgarden
slug: giveconomy/givgarden
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'


Giveth has chosen the Gardens DAO governance platform developed by [1hive](_https://forum.1hive.org/t/welcome-to-1hive/7) to allow GIV token holders to manage the DAO configurations and allocate funds to projects that are aligned with its [mission, vision and values](/whatisgiveth/). Our unique Giveth Garden has been aptly named “the GIVgarden” and is deployed on Gnosis Chain (formerly xDai Network). The main tools used for governance in the GIVgarden are Conviction Voting and Tao Voting.  

The GIVgarden uses the [Giveth Community Covenant](/whatisgiveth/covenant) as a decentralized social contract that outlines standards for on-chain and off-chain behaviour.   

You can visit the [**GIVgarden** here](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98).  


## Conviction Voting
[**Conviction Voting**](https://forum.giveth.io/t/conviction-voting/154) allows requests for funding from the DAO and to suggest improvements, features or unique actions to Giveth and its platforms. Gardens highlights the fundamental concept of Conviction Voting in their documentation:


> _Conviction voting is the heart of a Garden._ It allows folks to signal their preferences continuously rather than forcing them to “make a decision.” From the perspective of a community member, this is as easy as just showing up and supporting the things you care about.


The unique feature of Conviction Voting is that, instead of voting yes or no on proposals, you stake GIV behind proposals that align with your values. The more GIV you stake and the longer you stake your GIV the more “Conviction” (voting power) you accrue for that proposal.  If the collective Conviction from all proposal participants reaches a certain threshold then the proposal passes.


## Tao Voting

[**Tao Voting**](https://forum.giveth.io/t/tao-voting-explained/155) is a YES/NO decision making tool, with the option of delegation, that is used in the GIVgarden to make important, non-financial decisions for the DAO. Tao Voting is used for proposals on updating DAO parameters, fixing bugs, adding new features to the DAO and/or for emergency situations such as an attack to the DAO treasury.

Tao Voting was named inspired by [the Tao or “the way”](https://en.wikipedia.org/wiki/Tao) which can “be roughly thought of as the flow of the Universe, or as some essence or pattern behind the natural world that keeps the Universe (the Giveth DAO) balanced and ordered”. Tao Voting includes features like [Delegation and Quiet Ending](https://1hive.gitbook.io/gardens/on-chain-governance/garden-framework/decision-voting#delegation) to ensure that votes that pass can reasonably reflect the true opinion of DAO members and are not passed with a lot of contention.

When you delegate your voting power to a “delegate”, you are empowering them to vote on your behalf on decision votes in the GIVgarden with Tao Voting. Delegates have a period of time - the Delegated Voting period - to submit their votes. The Vote Duration is longer than the Delegate Voting power, and within that difference of time you have the opportunity to review and, if desired, change the way your delegate has voted for you. You can delagate your voting power to a delegate in the GIVgarden.




<img alt="delegation UI" src={useBaseUrl('img/content/giveconomy/delegation1.png')} />




<img alt='delegation UI' src={useBaseUrl('img/content/giveconomy/delegation2.png')} />


## Wrapping GIV & Earning Rewards
In order to vote on proposals in the GIVgarden you’ll have to wrap your tokens. This exchanges your GIV tokens for GIVgarden-compatible **gGIV tokens** that can be staked on proposals. You earn rewards for all wrapped GIV, regardless of whether or not you use your wrapped GIV (gGIV) to vote on proposals. You can choose to wrap your GIV and get gGIV [in the GIVgarden](https://1hive.gitbook.io/gardens/actions-for-community-members/getting-started/wrap-your-tokens), or via the GIVfarm by participating in the single-asset GIV staking pool on xDai. When you unwrap your GIV in the GIVgarden or unstake your GIV from the single-asset GIVfarm your gGIV tokens will be burned, removing your voting power, and your GIV tokens will be returned to you.

You can see the APR for wrapped GIV on our [**GIVfarm page**](https://giveth.io/givfarm). The more GIV you stake, the more rewards you get, and the higher your flowrate will be in the GIVstream. Being an active community member is rewarding in more ways than one!



## Proposals

In the GIVgarden, there are three types of proposals that can be made: **Funding, Suggestion,** and **Decision.**



* A **Funding** proposal is a request for funds from the GIVgarden common pool. The more funds being requested, the more Conviction that is required to pass the proposal. Conviction Voting is used to determine the outcome of funding proposals.
* A **Suggestion** proposal is a broad category for any platform feature, or community action you would like to make happen that does not request funds from the treasury. Conviction Voting is used to determine the outcome of Suggestion proposals.
* A **Decision** proposal is used when updating GIVgardenparameters or fundamentally changing the GIVgarden in some way is necessary. These proposals require some degree of community consensus around discrete, binary choice decisions and therefore are expected to be used much less frequently. Tao Voting is used to determine the outcome of Decision proposals.  

To learn more about how the GIVgarden works, visit the Gardens overview in the [1hive documentation](https://1hive.gitbook.io/gardens/).  


## Covenant
In order to participate in the GIVgarden you’ll first need to sign the [Giveth Covenant](/whatisgiveth/covenant). This is our decentralized social contract which outlines standards for on-chain and off-chain community behaviour. In the event that a proposal is challenged, the covenant shall be used as a baseline for what defines acceptable and not acceptable proposals within that GIVgarden.


## Disputability

In order to create or challenge a proposal, you must deposit GIV into the GIVgarden. When you make a proposal, an amount of GIV from here will be used as the [Proposal Deposit](https://1hive.gitbook.io/gardens/actions-for-community-members/proposals/creating-a-new-proposal#what-is-the-proposal-deposit) (aka “Action Deposit”) and will be held as collateral if your proposal is challenged (i.e., accused of not being in agreement with the Covenant). Similarly, if you wish to challenge a proposal, an amount of GIV from the initial deposit will be used as the [Challenge Deposit](https://1hive.gitbook.io/gardens/actions-for-community-members/proposals/challenge-a-proposal#what-is-the-challenge-deposit), i.e., collateral in order to make a challenge.   

When a proposal is challenged in the GIVgarden, the proposal creator has a set amount of time, the [Settlement Period](https://1hive.gitbook.io/gardens/actions-for-community-members/disputes/settle-a-proposal#what-is-the-settlement-period) to dispute the challenge by paying dispute fees and raising the issue to [Celeste](https://1hive.gitbook.io/celeste/), or to resolve the challenge by paying the [Settlement Offer](https://1hive.gitbook.io/gardens/actions-for-community-members/disputes/settle-a-proposal#what-is-the-settlement-offer) and taking down their proposal. If they do not take action before the end of the Settlement Period, the proposal is automatically considered “settled”, is taken down, and the proposer gets back the Proposal Deposit minus the Settlement Offer.

[**Celeste**](https://1hive.gitbook.io/celeste/), also built by 1Hive, is a decentralized court for DAOs which acts as the final backstop in the GIVgarden. Celeste allows for challenged and disputed proposals to be flagged and brought to the consideration of  a randomized group of jurors, ensuring that contentious proposals are not able to be passed without due process.  

## Proposal Lifecycle

If you feel like you have a good grasp on Giveth and [how we work](/whatisgiveth/) and have something great to propose to the community, there are some processes you should respect in order to have the best possible chance of success.



1. **Think of something awesome.** Come up with an idea that you think would be valuable for the Giveth’s Community or Platform. If your idea requires funding, consider how much and how you can justify its costs.
2. **Create a forum post.** Post your idea in the [**Giveth Forum**](https://forum.giveth.io/) in the appropriate category and outline your proposal in detail. This allows the community to review and assess the impacts of your proposal. Proposals created in the GIVgarden must include a link to a Giveth forum post explaining its details.
3. **Use Advice Process.** Following your forum post the community will give you feedback and express any concerns. [The Advice Process](/whatisgiveth/adviceProcess) will allow you to modify your proposal or address any concerns ensuring it is the best version possible and achieves maximum consensus.
4. **Sign the Giveth Covenant. Signing that you agree to the [Giveth Covenant](/whatisgiveth/covenant) in the GIVgardens will permit you to begin using the governance tools it provides.
5. **Deposit GIV to the GIVgarden**. Every proposal requires a Proposal Deposit, i.e., a specified amount of GIV that you post as collateral. This discourages spamming proposals and can also be forfeited in the case of losing or conceding to a challenged proposal.
6. **Submit your Proposal. **Draft and submit your proposal, along with the Proposal Deposit, providing the required information in the GIVgarden.
7. **Remind the Community to Vote!** Now the community will deliberate on your final proposal, choosing whether or not to stake their GIV behind it. If it receives enough support, the proposal will pass.
8. **Celebration and Delivery! **If your proposal passes on the GIVgarden, give yourself a pat on the back - that is no easy feat! Once the proposal has been finalized and executed make sure to deliver on any promised actions you have outlined.

## GIVgarden Parameters (Advanced)  

The current parameters in our GIVgarden are as follow:

### Conviction Voting (Funding Requests and Suggestions)


<table>
  <tr>
   <td><strong>Parameter</strong>
   </td>
   <td><strong>Value</strong>
   </td>
   <td><strong>Metric</strong>
   </td>
  </tr>
  <tr>
   <td>Conviction Growth
   </td>
   <td><p class="rightAlign">
30</p>

   </td>
   <td>days
   </td>
  </tr>
  <tr>
   <td>Spending Limit
   </td>
   <td><p class="rightAlign">
2.50</p>

   </td>
   <td>%
   </td>
  </tr>
  <tr>
   <td>Min Conviction
   </td>
   <td><p class="rightAlign">
5</p>

   </td>
   <td>%
   </td>
  </tr>
  <tr>
   <td>Minimum Active Stake
   </td>
   <td><p class="rightAlign">
2</p>

   </td>
   <td>%
   </td>
  </tr>
</table>


### Tao Voting (Decision Votes)


<table>
  <tr>
   <td><strong>Parameter</strong>
   </td>
   <td><strong>Value</strong>
   </td>
   <td><strong>Metric</strong>
   </td>
  </tr>
  <tr>
   <td>Support Required
   </td>
   <td><p class="rightAlign">
90</p>

   </td>
   <td>%
   </td>
  </tr>
  <tr>
   <td>Min Approval
   </td>
   <td><p class="rightAlign">
10</p>

   </td>
   <td>%
   </td>
  </tr>
  <tr>
   <td>Vote Duration
   </td>
   <td><p class="rightAlign">
1.5</p>

   </td>
   <td>days
   </td>
  </tr>
  <tr>
   <td>Execution delay
   </td>
   <td><p class="rightAlign">
0.5</p>

   </td>
   <td>days
   </td>
  </tr>
  <tr>
   <td>Quiet Ending Period
   </td>
   <td><p class="rightAlign">
0.5</p>

   </td>
   <td>days
   </td>
  </tr>
  <tr>
   <td>Quiet Ending extension
   </td>
   <td><p class="rightAlign">
2</p>

   </td>
   <td>days
   </td>
  </tr>
  <tr>
   <td>Delegated Voting Period
   </td>
   <td><p class="rightAlign">
1</p>

   </td>
   <td>days
   </td>
  </tr>
</table>


### Proposal Settings


<table>
  <tr>
   <td><strong>Parameter</strong>
   </td>
   <td><strong>Value</strong>
   </td>
   <td><strong>Metric</strong>
   </td>
  </tr>
  <tr>
   <td>Action Deposit
   </td>
   <td><p class="rightAlign">
5000</p>

   </td>
   <td>GIV
   </td>
  </tr>
  <tr>
   <td>Challenge Deposit
   </td>
   <td><p class="rightAlign">
10000</p>

   </td>
   <td>GIV
   </td>
  </tr>
  <tr>
   <td>Settlement Period
   </td>
   <td><p class="rightAlign">
7</p>

   </td>
   <td>days
   </td>
  </tr>
</table>
---
id: givpower
title: GIVpower
slug: giveconomy/givpower
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import ReactPlayer from 'react-player'
 

# GIVpower

GIVpower was created to build a win-win relationship between projects & donors. GIV holders get GIVpower and earn a yield when they stake and - if they choose - lock GIV in the GIVfarm. They will eventually be able to use their GIVpower to “boost”:rocket: projects on Giveth and help improve their ranking. Top ranked projects will get benefits on the platform. Initially their donors will get more GIVbacks, and eventually, they will get matching funds and other benefits.

The 1st phase of GIVpower launched on October 4th, 2022 adds a new layer of mechanics for staking GIV on the GIVfarm.

<img alt='givpower staking card' width='30%' heigh='auto' src={useBaseUrl('img/givpowerCard.png')} />


In addition to the APR of GIV rewards and receiving [gGIV for Giveth governance](https://docs.giveth.io/giveconomy/givgarden), users also get **GIVpower**, a non-transferrable ERC-20 token. Staked GIV is matched 1:1 with GIVpower.  
_(i.e. If you stake 100 GIV you will get 100 GIVpower.)_


Users will also be able to "Lock":lock: their staked GIV on the GIVfarm to multiply their rewards APR and their GIVpower.

### Contracts

- GIVpower(POW) Token - [0xD93d3bDBa18ebcB3317a57119ea44ed2Cf41C2F2](https://gnosisscan.io/address/0xD93d3bDBa18ebcB3317a57119ea44ed2Cf41C2F2)
- GIVpower Staking - [0x24F2d06446AF8D6E89fEbC205e7936a602a87b60](https://gnosisscan.io/address/0x24F2d06446AF8D6E89fEbC205e7936a602a87b60)

## Staking & Locking

Users can increase their rewards from staking GIV by locking them up for a period of time. Locking GIV means that it cannot be unstaked for a given amount of time, you can see the date a particular batch of GIV unlocks in the “Locked GIV Details” pop-up.

:::info
GIVpower is only available on Gnosis Chain If you have GIV on Mainnet and wish to earn rewards and participate with GIVpower, you can [bridge your GIV](https://omni.gnosischain.com/bridge) from Mainnet to Gnosis Chain.
:::

GIV can be locked according to bi-weekly segments following the same schedule as GIVbacks, the minimum amount of time is 1 round (2 weeks), and the maximum is 26 rounds (1 year).

The longer you lock your GIV the greater the multiplier will be for that specific amount of GIV locked. A bigger multiplier means you will get more GIV from the GIVfarm rewards (you get a higher APR) and you will also get more GIVpower. The amount of gGIV ([GIVgarden voting](./GIVgarden.md)) you receive will not increase.

<img alt='givpower multiplier' width="80%" heigh='auto' src={useBaseUrl('img/givpowerMultiplier.png')} />

You can lock up multiple batches of GIV tokens for different lengths of time, each batch might have a different APR, depending on how long you locked up your tokens.

<img alt='givpower locked giv details' width="80%" heigh='auto' src={useBaseUrl('img/givpowerLockedDetails.png')} />


After the locking period for your GIV ends your GIV becomes unlocked, meaning it can be unstaked from the GIVfarm. Unstaking your GIV means you will lose any associated GIVpower and gGIV. You can get it back however by staking your GIV again.

### GIVfarm APR

When you lock up your GIV you will see the current estimated APR for that amount of GIV being locked up. The APR may change based on the actual total amount of GIV staked in the farm across all users, and might be different for each batch of tokens locked. You will be able to see your actual APR for each batch by navigating to the "Locked GIV Details'' pop-up on the GIVpower staking card.

<img alt="locked givpower aprs" width="80%" heigh='auto' src={useBaseUrl('img/givpowerLockedapr.png')} />

On the GIVpower staking card the APR shown is the weighted average of all batches of your locked GIV. If you have no GIV locked in GIVpower you will be shown a range of the lowest and highest possible APRs at that moment.

<img alt='givpower staking card apr' width='30%' heigh='auto' src={useBaseUrl('img/givpowerCardapr.png')} />


#### Unlocking

Unlocking only happens at the beginning of a new round, so if you lock your GIV in the middle of a round, the unlock date will be calculated from when the next round begins.


For example:

> _Mohammad locks up his staked GIV for 5 rounds (10 weeks), today is day 5 of round 25. His GIV would remain locked for all of round 25 (9 more days) until round 26 begins, PLUS 5 more rounds, meaning his GIV would finally unlock at the end of round 31._

When the duration of your locking period for each batch ends then that batch of GIV becomes unlocked, thus reducing your APR of that batch to the minimum APR for GIV staking. To increase your APR again you will need to lock up your GIV.

### The Multiplier
The basic formula for calculating the multiplier of GIV APR rewards and GIVpower is:

$$
\sqrt(1 + N)
$$
*N = number of rounds locked*

Let's look at an example to understand how this works:

> _Carlos decides to lock up 100 of his staked GIV for 10 rounds (20 weeks). His multiplier, rounded to 2 decimal places, is **3.32**._
> $$
> \sqrt(1 + 10) = 3.3166247903554
> $$
> _If at the time of locking the minimum GIV staking APR is 35% then his APR at the time of locking will be ~116%. The actual amount will be variable depending, as mentioned, on the total amount of GIV staked into the farm, but that same multiplier of 3.32 would be applied to the current staking APR for the GIV rewards that Carlos earns._
>
>_Carlos also would get a multiplier on his GIVpower. Assuming he had 500 GIV staked and chooses to lockup 100 of that 500 he would then have 732 GIVpower._
>$$
>(100 * 3.32) + 400 = 732
>$$
>
> _After the 10 rounds that Carlos locked his GIV, his GIVpower will no longer have a multiplier, becoming reduced to only 500, matching 1:1 his staked GIV and his APR will go down to the minimum staking APR._


:::success
#### Streamed Rewards
As always, all GIVeconomy rewards are distributed according to the GIVstream. Check out the [**GIViverse Expansion**](https://giveth.io/givstream) to understand how much your claimable rewards will be.
:::


<img alt='GIVpower overview' src={useBaseUrl('img/GIVpowerOverview.png')} />

## Rewards Allocation
7 Million GIV was allocated to the first 6 months of GIVpower Rewards. Near the end of the first 6 months Giveth will assess the program's performance and allocate more rewards accordingly.

## Using your GIVpower

You can use your GIVpower to “boost” verified to projects on the platform. Verified projects are ranked on the platform based on how much GIVpower was allocated to them in the previous round. Projects benefit from a higher ranking by appearing higher on the list of [Giveth projects](https://giveth.io/projects) and also yield more GIVbacks to their donors.



Top-ranked projects will also eventually benefit from matching funds from the [GIVmatching Program](https://forum.giveth.io/t/givmatching-idea-generation-on-how-to-distribute-funds/346/21)(TBD).

### How to Boost

Boosting a project with your GIVpower is very easy. To get started, find the project you want to boost and visit the project's page. Once you're there then click `boost`.

<img alt='boosting on the project page' width="80%" height="auto" src={useBaseUrl('img/content/boostProjectPage.png')} />

:::caution
**You can only boost verified projects**, up to a maximum of 20 unique projects. If a project for any reason becomes unverified (e.g. fails to provide updates, or breaks our [Terms of Service](https://giveth.io/tos)) any of your GIVpower backing that project will become “inactive” (i.e. excluded from the calculations of rank & GIVbacks).  
:::
Select the percentage of your GIVpower you would like to boost with. If it's your first time boosting you will automatically boost with 100% of your GIVpower. Subsequent GIVpower boosts will proportionally reduce your GIVpower on your other boosted projects. More details below in [Managing your GIVpower](#managing-your-givpower).

<img alt='select boosting percentage' width="80%" height="auto" src={useBaseUrl('img/content/boostingProject.png')} />

Click `Confirm' and you should see confirmation that your GIVpower boost was successful! 
<img alt='boostConfirmation' width="80%" height="auto" src={useBaseUrl('img/content/boostConfirmation.png')} />

### Managing your GIVpower

You can manage your GIVpower allocations by navigating to 'My Account' then clicking on the 'My GIVpower' tab.

<img alt='my boosted projects page' src={useBaseUrl('img/content/boostedProjectsPage.png')} />

From this page you can edit your GIVpower allocations to each project you have boosted. To begin click `MODIFY`.

You can edit your percentage of GIVpower allocated to each project, when you modify one allocation all your other allocations will adjust relatively based on what their previous allocation was. If you don't want your allocation to change for a specific project while modifying your GIVpower on other projects you can click the :lock: icon. The sum of percentages allocated to each of your projects must equal 100%, so you can lock all but two of your allocations. 

You cannot have less than 1 project boosted at any given time. If for some reason your boosted project loses its verified status and all your GIVpower becomes inactive, you must boost another verified project before removing the inactive boosting from the unverified project.

Confirm your allocation changes by clicking on `APPLY CHANGES` then `SAVE CHANGES`.

Check out this video to see what modifying your GIVpower looks like in action:

<ReactPlayer playing loop={true} controls url='/video/editingAllocationsConverted.mp4' />




#### GIVpower Balance Changes



Your total GIVpower may change over time depending on 4 typical events that may occur, let’s cover them in detail:

1.**Staking more GIV.** If you stake more GIV on the [GIVpower farm](https://giveth.io/givfarm) you will receive more GIVpower at 1:1 ratio per GIV staked.
2.**Locking staked GIV.** If you lock up more of your staked GIV this will multiply your GIVpower by a factor depending on how long you lock it for. The longer you lock, the greater your multiplier, and the greater your GIVpower.
3.**GIV becomes unlocked.** Once the duration of any of your batches of locked GIV ends, you will lose the multiplier on your GIVpower that was applied from locking up that batch of GIV. Your total GIVpower balance will decrease. 
4. **Unstaking GIV.** If you unstake your GIV from the [GIVpower farm](https://giveth.io/givfarm) you will burn your GIVpower at a 1:1 ratio per GIV unstaked.

After boosting your first project with GIVpower you will always be allocating 100% of it to a project(s). By design, no matter if your total GIVpower goes up or down you will always be using your GIVpower to maximum effect and your allocations to projects will always remain at the relative percentages in which you allocated. 

## Project Rank

All verified projects that have been boosted with GIVpower will receive a GIVpower rank. The project with the most GIVpower will be ranked #1 on the platform. The “current rank” is updated at the start  of each new GIVbacks round, and is taken from the average amount of GIVpower staked behind a project across the previous round (two weeks).


:::note
 The “projected rank” is a projection of what the current rank may be in the next GIVbacks round, based on the GIVpower that is currently on that project. The projected rank gives you an idea of the impact your recent boost might have.
:::

<img alt='project ranking page' src={useBaseUrl('img/content/projectRanking.png')} />


A project's current rank in turn affects the percentage of GIVbacks new donors will receive from donating it. The top ranked project can yield up to 80% GIVbacks matching while a verified project with no rank (i.e. no GIVpower behind it) will yield 50%. To determine the GIVbacks factor for every project between the top and bottom ranks we take the spread, or the difference between the maximum and minimum [GIVbacks factor](./givbacks.md#rank--calculation), and divide that by the number of ranked projects we have at the end of every round, from this we can find the unique GIVbacks factor for every ranked project.

Every project from the bottom to the top rank will receive incrementally more GIVbacks matching. This means that, no matter what a project’s current rank is, boosting it with GIVpower can always make a difference.

 You can read more about [GIVbacks here](./givbacks.md).

<details>
<summary><b><i>See an Example GIVbacks Distribution</i></b></summary>

The year is 2049, it is GIVbacks round 1337...


We have **25 verified projects** that have been boosted with GIVpower. The **maximum GIVbacks factor is 80%, the minimum is 50%**, and the difference between the two is 30%. This would mean the project with the least amount of GIVpower, project ranked #25, would have a GIVbacks Factor of 50% and **every subsequently higher ranked project would have a 1.25% higher GIVbacks factor**.
 
The total GIV to distribute for the round is 1,000,000 and the price of GIV is $0.53.

For demonstration purposes we record that every single ranked project got a flat 100 USD value in donations. Based on this information and some given values for GIVpower staked to a given project our example distribution would look like this:
 
 | Project | GIVpower | Rank | Givbacks Factor | USD Value of Donation | Estimated GIVbacks |
| --- | --- | --- | --- | --- | --- |
| A | 4213.3329017797105 | 1 | 80% | 100 | 150.94339622641508 |
| B | 3511.1107514830924 | 2 | 78.75% | 100 | 148.5849056603774 |
| C | 2925.9256262359104 | 3 | 77.5% | 100 | 146.22641509433964 |
| D | 2438.271355196592 | 4 | 76.25% | 100 | 143.8679245283019 |
| E | 2031.8927959971602 | 5 | 75% | 100 | 141.5094339622642 |
| F | 1693.2439966643003 | 6 | 73.75% | 100 | 139.15094339622647 |
| G | 1411.036663886917 | 7 | 72.50% | 100 | 136.79245283018872 |
| H | 1175.8638865724308 | 8 | 71.25% | 100 | 134.43396226415098 |
| I | 979.8865721436924 | 9 | 70% | 100 | 132.0754716981133 |
| J | 816.572143453077 | 10 | 68.75% | 100 | 129.71698113207555 |
| K | 680.4767862108976 | 11 | 67.5% | 100 | 127.35849056603782 |
| L | 567.0639885090814 | 12 | 66.25% | 100 | 125.0000000000001 |
| M | 472.55332375756785 | 13 | 65% | 100 | 122.64150943396237 |
| N | 393.7944364646399 | 14 | 63.75% | 100 | 120.28301886792464 |
| O | 328.16203038719993 | 15 | 62.5% | 100 | 117.92452830188691 |
| P | 273.46835865599996 | 16 | 61.25% | 100 | 115.56603773584918 |
| Q | 227.89029887999996 | 17 | 60% | 100 | 113.20754716981146 |
| R | 189.90858239999997 | 18 | 58.75% | 100 | 110.84905660377373 |
| S | 158.257152 | 19 | 57.5% | 100 | 108.490566037736 |
| T | 131.88096 | 20 | 56.25% | 100 | 106.13207547169827 |
| U | 109.90079999999999 | 21 | 55% | 100 | 103.77358490566054 |
| V | 91.58399999999999 | 22 | 53.75% | 100 | 101.41509433962283 |
| W | 76.32 | 23 | 52.5% | 100 | 99.05660377358508 |
| X | 63.599999999999994 | 24 | 51.25% | 100 | 96.69811320754737 |
| Y | 53 | 25 | 50% | 100 | 94.33962264150965 |


</details>

**Project ranking will continue to have an important role on Giveth.io and will be incorporated into future roadmap features**, such as [GIVmatching](./givethmatchingpool.md)! In the future, Giveth may also incorporate other metrics or voting tools that will impact a project’s ranking.

[Check out this document](https://github.com/Giveth/impact-graph/blob/staging/docs/powerBoosting.md) to read more technical documentation of how GIVpower is calculated inside the Giveth database.

## Delegation
Giveth plans to implement the ability for users to delegate their GIVpower, letting trusted Givers curate projects on their behalf. You can apply now to become a [GIVpower delegate](https://forum.giveth.io/t/open-call-for-givpower-delegates/779)!
---
id: givstream
title: GIVstream
slug: giveconomy/givstream
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import ReactPlayer from 'react-player'


Welcome to the expanding GIViverse! The GIVstream aligns community members with the long term success of Giveth and the GIVeconomy. With the GIVstream, anyone who adds value to the GIVeconomy receives GIV continuously for up to 5 years from the GIVeconomy launch date. The GIVeconomy begins humbly, but as time passes, the GIViverse expands: More GIV becomes liquid is streamed to our community of GIVernauts.

All GIVstreams flow until December 23, 2026, at which point the GIVeconomy will be in full swing! [Watch your GIVstream flow](https://giveth.io/givstream).

<ReactPlayer playing light='/video/givstream_thumbnail.png'  loop={true} controls url='/video/GIF_GIVETHiverse.mp4' />


## How it Works
At launch, 10% of the total token supply of 1 billion GIV will be liquid and distributed across the [GIVeconomy](https://docs.giveth.io/giveconomy/). The rest supplies the GIVstream which flows for 5 years, releasing more liquid GIV every second. After the 5 year period, 100% of GIV tokens will be liquid.

The following table explains what percentage of GIV is liquid and distributed throughout the GIViverse, and which part is still yet to flow from the GIVstream.


|Date	|Liquid GIV	|GIV flowing from the GIVstream|
|-------|-----------|-----------------|
|Dec 24, 2021	|	10% | 	90% |
|Oct 24, 2022  |   25%	|   75% |
|Mar 15, 2024	|	50% |   50% |
|Aug 04, 2025   |   75%	|   25% |
|Dec 23, 2026	|  100%	|    0% |


## Your GIVstream Flowrate

<img width='85%' alt='flowrate counter' src={useBaseUrl('/img/content/giveconomy/flowrate.png')} />

Your GIVstream flowrate is the rate (GIV/week) at which your GIV becomes liquid. All recipients of the [GIVdrop](https://docs.giveth.io/giveconomy/givdrop) will also receive a GIVstream on Gnosis Chain (formerly xDai Network). If you did not receive a GIVdrop, you can still get a GIVstream by participating in the GIVeconomy.

You can get (or increase) your GIVstream flowrate on Gnosis Chain (formerly xDai Network) by donating (on Gnosis Chain or Mainnet) and getting [GIVbacks](https://giveth.io/givbacks), by wrapping GIV to use in the [GIVgarden](https://giveth.io/givgarden), or by staking in the [GIVfarm](https://giveth.io/givfarm) on Gnosis Chain.

You can get (or increase) your GIVstream flowrate on Ethereum mainnet by providing mainnet liquidity and staking GIV or LP tokens in the [GIVfarm](https://giveth.io/givfarm) on Mainnet.

### Earning Rewards
When you earn GIV through participation in the GIVeconomy, part will be liquid and part will add to your GIVstream flowrate. As time passes and the GIVstream flows, a greater percentage of the total GIV you earn is liquid.

When you earn and/or claim rewards from GIVbacks (Gnosis Chain), the GIVgarden (Gnosis Chain) or the GIVfarm (Gnosis Chain or Ethereum Mainnet), you increase your GIVstream flowrate. Note that when you claim, any GIV liquid from the GIVstream on that chain also get sent to your wallet.

<img width='70%' class="center" alt='GIVgarden Rewards' src={useBaseUrl('/img/content/giveconomy/GIVgardenRewards.png')} />

### History Table

The GIVstream history table is a summary of all the instances in which your GIVstream flowrate increased. When GIVbacks are distributed, the increase in your flowrate is automatically added to the history table. For rewards earned in GIVfarm, you must "harvest" in order to see your GIVstream flowrate increase, and to see the corresponding entry in the history table.

Note: When earning rewards in the GIVfarm, it does not matter if you harvest rewards and increase your flowrate sooner, or later. You total liquid rewards and streaming rewards will be the same in either case.

![](https://i.imgur.com/W9WN7gy.png)

----

The GIVstream nurtures the GIVeconomy at inception by having only 10% of the total supply of GIV liquid and transferrable to start. As the GIVeconomy grows & stabilizes, more GIV becomes liquid and available for everyone. We want to empower those who support the Giveth ecosystem with steadily increasing governance rights, this includes participants who:
- [Donate to Verified Projects](https://giveth.io/projects)
- Vote in the [GIVgarden](https://giveth.io/givgarden), and
- Provide liquidity in the [GIVfarm](https://giveth.io/givfarm)

Participants benefit from their GIVstream flowing as the GIVeconomy flourishes over time, therefore we ensure that Giveth is not just governed by people who buy tokens on the open market but by those who contribute in a more meaningful way.
---
id: gettingStarted
title: Getting started
slug: dapps/gettingStarted
---
import useBaseUrl from '@docusaurus/useBaseUrl'


Giveth.io is a platform where you can easily support projects both with cryptocurrency and fiat that you ❤️. Or create your own project and accept funding from a worldwide audience.

New to crypto? Visit our [FAQ section](./guide5-FAQ.md) where you can find more information or check out our [Donor 101 video course on youtube](https://youtube.com/playlist?list=PL4Artm1rmCWH4Q5XnrQWf8fm0xob3hbdZ&si=EnSIkaIECMiOmarE) to learn how to use the platform better. 

## Sign in

In the top right corner you will see the `sign in` button. Currently you can sign in via two methods, either by *Tor.us*, *Metamask*, *Wallet Connect* or *Gnosis Safe*. You must choose!

#### Sign in with Ethereum
Click the button and choose which wallet you would like to connect with (Metamask, WalletConnect, Torus or Gnosis Safe). Follow your wallet instructions below.


#### Tor.us Sign in
Click on the `Torus` under the sign in drop down menu. You will be given several options of different platforms you can sign in with (e.g., Google, Linkedin, Twitter, Discord, etc.) You can also use the simple email option, which will send you a one-time use code to your email. Follow the Torus prompt and you should find your way in easily.

#### Metamask Sign in
If you're unfamiliar with Metamask or don't already have a wallet, head on over to (https://metamask.io/), and get yourself set up with one! Once your wallet is setup, make sure your Metamask browser extension is enabled and up to date. Click the 'Metamask' option under the sign in drop down menu. You should then be prompted by the Metamask pop up to confirm your signature, and then you should be plugged in and good to go!

#### Wallet Connect
Click on the Wallet Connect icon and scan the QR code with a Wallet Connect compatible wallet or copy to your clipboard. Alternatively, click the desktop tab and choose your preferred wallet.

#### Gnosis Safe Sign in
To sign in with Gnosis you must access Giveth from your Gnosis safe. Click Gnosis safe and follow the prompts.

<img alt='gnosis1' src={useBaseUrl('img/gnosis1.png')} />

<img alt='gnosis2' src={useBaseUrl('img/gnosis2.png')} />

#### Sign in with Email or Social Media
Click on the icon you wish to sign in with.  A blockchain wallet will be created for you once you sign in. If you wish to see more options beyond sign in with Gmail, Facebook, Twitter, Discord, click more options to see the full list. 



## Fill in your profile info
Once you've logged in, it's recommended you fill in some info about yourself. Transparency is a two-way street! In the top right corner you should find now the thumbnail of your account. Click on it, and then click on `My Account`, you can either sign in(note: this is necessary to donate to projects) or click skip for now.

Once you sign in, you will see an overview of your profile with tabs named: **Overview, Boosted Projects, My Donations and Liked Projects**. If you haven't completed your profile you will see a warning message across the top "Your profile is incomplete" click on "Let's do it" and a pop ip will appear with instructions. Alternately, scroll to the bottom of the page and click on the button `Complete profile`. Follow the prompts and fill in the fields given, and hit `SAVE`.

## Donate

More info on donating to a project are in the [user guide.](./projectdonating)

## Create project
Our User Guide page for creating a project can be found [here.](./createproject)
---
id: createproject
title: Create a project
slug: dapps/createproject
---
import useBaseUrl from '@docusaurus/useBaseUrl';

## Contemplate the vision for your project
Think about the project that you want to create: do you have concrete goals? What are you asking for funding for? Can you explain your project and your intentions clearly?

Discover the ins and outs of the project creation process with our detailed demonstration in the [Project Owners 101 video course:](https://youtube.com/playlist?list=PL4Artm1rmCWFi-qEkOtjl9nL4tojSIIKm&si=EnSIkaIECMiOmarE)

[<img alt='SettingProjectYoutube' src={useBaseUrl('img/Settingupproject.jpeg')} width="400"/>](https://youtube.com/watch?v=sOtvDCAqV88&si=EnSIkaIECMiOmarE)

If you ever have any questions you can find us in our [support channel on Discord](https://discord.com/channels/679428761438912522/835168432520429578).

## Creating your project
 Make sure you're signed in, and click the `create project` button.
 <img alt='projectpageforcryptodonation' src={useBaseUrl('img/cryptofundraising1.png')} />

 You may be requested to authorize your wallet on Giveth with a signature if you haven’t already done so. Click the sign button.

Read the submissions guideline popup.

<img alt='submissionguidelines' src={useBaseUrl('img/submissionguidelines.png')} />

Follow the prompts, and input the requested content:

 - Enter your project name.
<img alt='addname' src={useBaseUrl('img/cryptofundraising2.png')} />

 - In 200-500 words tell us about your project. Click how to write a good project description for help.
 <img alt='describeproject' src={useBaseUrl('img/cryptofundraising3.png')} />

 - Pick relevant categories to add 'keywords' to your project. You can choose up to 5 categories for your project.
 <img alt='pickcategory' src={useBaseUrl('img/cryptofundraising4.png')} />

 - State where in the world your project is taking place or click this project has a global impact..
<img alt='picklocation' src={useBaseUrl('img/cryptofundraising5.png')} />

 - Add an image to display with your project (or choose from one of the Giveth defaults).
 <img alt='featuredimage' src={useBaseUrl('img/cryptofundraising6.png')} />

 - Alternatively, click the tab search for photos and enter a keyword.
 <img alt='featuredimage2' src={useBaseUrl('img/cryptofundraising8.png')} />

 - Your recipient address is where donations to your project will be collected. You can choose to set a single recipient address that can receive donations on both Mainnet and Gnosis Chain, or set a different recipient address for each chain:

    - Set one address to receive donations in both Mainnet and Gnosis Chain.
    
    <img alt='setting recipient wallet' src={useBaseUrl('img/receiveFunds1.png')} />

    - Or set two different addresses: One address for each network.
    <img alt='setting recipient wallet' src={useBaseUrl('img/receiveFunds2.png')} />
    
    - Note: You can also choose to raise funds only on one chain.


On the final page double check all the info you entered. If it looks good, hit `PUBLISH`, and boom, your project is live! 

On the confirmation page you can choose to view your project and to share it on social media.
 <img alt='projectcreated' src={useBaseUrl('img/projectcreation.png')} />


## Editing my project after it's been published
If you made a mistake or need to change something on your project, it's super simple to go back and update it. If you're on the homepage, go to the top right, and click on your account, then select `My Projects`. Once you're there, you should see a page of your projects; hover over the project you wish to edit, then click the `EDIT` button. You should see your project's contents; you can scroll through and change the content you wish, and once you're done, just hit save!
---
id: crypto
title: Cryptocurrency donations
slug: dapps/crypto
---

## What is and why Cryptocurrency?
Simply, it is a secure form of digital currency that can be transferred anywhere in the world peer-to-peer, similar to email (where the email's server is replaced with a decentralized network).

More technically, Bitcoin is a type of digital currency that uses cryptography and open source software to regulate the generation of units of currency and verify the transfer of funds, operating independently of a central bank. There is a distinction between Bitcoin, a digital currency, and blockchain the technology, which has many additional potential use cases beyond the currency.

Using cryptocurrency for sending and receiving donations has many advantages against using 'fiat' or regular currency. With the implementation of the blockchain, crypto transactions are recorded and forever stored on the digital ledger or 'blockchain' making currency donations and distribution transparent.

## What is a blockchain?
A blockchain is a decentralized online ledger that is distributed across a network recording all the transactions being made on it. This ledger is continuously updated and distributed. Since there are many copies being updated and verified synchronously, it prevents one bad actor from manipulating the data. In other cryptocurrencies this same technology is being taken to a whole other level.


## What is and why choose Ethereum?
 It's the world's programmable blockchain. Ethereum builds on Bitcoin's innovation, with some big differences. Both let you use digital money without payment providers or banks. But Ethereum is programmable, so you can also use it for lots of different digital assets – even Bitcoin! This also means Ethereum is for more than payments. It's a marketplace of financial services, games and apps that can't steal your data or censor you.

 On Giveth we use these programmable ethereum blocks to create applications that facilitate donations. In the near future we will be using this same technology to potentially mint our own tokens and precipitate the GIVing economy.

## How does it work in the context of the application?
One of these superpowers is to create dApps or Decentralized Applications, these are applications programmed onto the blockchain. dApps can be programmed to work as smart contracts receiving, holding and distributing currency as per the terms written into the contract. This feature removes the need for banks and/or lawyers, cutting through red tape and allowing project creators more autonomy.

When you create or donate to a project, you are interacting with the Giveth dApp. Donations sent or received are recorded on the blockchain and can be viewed by anyone, anytime and anywhere. As donations are faciliated by the Giveth dApp's code, transactions thus can be done straight A -> B without anyone else needing to be involved.

One of the other superpowers is the ability for developers to create tokens or 'coins' which can create alternative economies based on the functionality programmed onto the coin. Giveth is in the works of implementing its own version of a token which will amplify the potential of donations. ***More on this is in development!***
---
id: troubleshooting
title: Troubleshooting
slug: dapps/troubleshooting
---
import useBaseUrl from '@docusaurus/useBaseUrl'


If you are having technical problems with the Giveth DApp, you may find a solution on this page.

## Brave Browser

If you try to sign into the Giveth DApp with Brave browser, Torus (the wallet provider) notifies you that it needs cookies to operate. (Torus needs these permissions for their OAuth services, so our users can be provided easily with their own Ethereum wallet that is tied i.e. their Google account.)

To quickly solve this problem you can:

- click on the site settings (Brave icon)
- change the cookie setting just for Giveth.io to "all cookies allowed"

<img
  alt="Enable Cookies in Brave"
  src={useBaseUrl('img/content/screenshot-brave-cookies.png')}
/>

[Read more about handling cookies in Brave.](https://support.brave.com/hc/en-us/articles/360050634931-How-Do-I-Manage-Cookies-In-Brave-)

### Giveth.io shows a blank screen! Help!

Sometimes updates get pushed to the Giveth.io website, and your cached files and cookies don't always get along well with the new updates on the site, so you'll need to clear your cache, delete your cookies, then refresh the browser.

To clear your cache and cookies on Brave, navigate to: ``Settings -> Additional Settings -> Privacy and Securiy -> Clear Browsing Data `` Once you're arrived there, check off `Cookies` and `Cached images and files`, and make sure at the top of the pop-up window you check off the appropriate Time Range. You can select `All Time` just to be sure you got 'em all.

Clearing your cookies will log you out of most sites. If you don't want to go through the hassle of logging back in to all the websites you frequent, then head to: ``Privacy and Security -> Cookies and othersite data -> See all site cookies and other data`` Then from this menu look up the Giveth domain like so:

<img alt="Deleting Cookies in Brave" src={useBaseUrl('img/content/givethcookies.png')} />

Then click the trash icon to delete the cookie for Giveth. If that's finished, pull up a fresh Brave browser window, head back to Giveth, and get back to giving!
---
id: faq
title: Frequently Asked Questions
author: Giveth
slug: dapps/faq
---

## General

**What is Blockchain?**
In simple terms, a blockchain is a method of storing and transferring information. It can be considered a kind of database that is not stored in a single computer. Instead, many identical copies are distributed in several computers called nodes. Information on a blockchain is stored in a continuous chain of blocks with each block containing essential information (for example, transactions) and the cryptographic hash of the previous block. To change the information in any block, you have to make changes to all subsequent blocks. The content of the blocks is verified by the consensus of all nodes in the network. These two features makes it very difficult to alter any information already included in the blocks, and this difficulty increases with the number of nodes in the network.

**What is Ethereum?**
"It's the world's programmable blockchain. Ethereum builds on Bitcoin's innovation, with some big differences. Both let you use digital money without payment providers or banks. But Ethereum is programmable, so you can also use it for lots of different digital assets – even Bitcoin! This also means Ethereum is for more than payments. It's a marketplace of financial services, games and apps that can't steal your data or censor you."

From [Ethereum.org](https://ethereum.org/) website

**What is Tor.us?**
Tor.us is the non-crypto savvy way to sign in to, and use Giveth.io. It is our wallet option alongside [Metamask](https://metamask.io). For a more detailed answer, see [Tor.us documentation](https://docs.tor.us)

**What is the difference between Bitcoin and Ethereum?**
Bitcoin is intended to function as decentralized means of value transfer whereas Ethereum is a protocol that allows users to develop decentralized applications on top of a blockchain network. As prominent Ethereum developer Vlad Zamfir has confirmed on several occasions, Ethereum is “not money.” Ethereum’s native token, Ether (ETH) exists in order to facilitate the process of building and deploying distributed applications. Meanwhile, the Bitcoin currency exists on the Bitcoin blockchain to facilitate peer-to-peer (P2P) exchange of uncensorable, non-confiscatable money.

From [cryptocompare.com](https://www.cryptocompare.com/)

**Why donate cryptocurrency?**
Cryptocurrency knows no borders and marginalizes no one. It can not be taken from you if you alone hold your keys. Another advantage: When you donate with crypto, you do not realize capital gains from the crypto you hold, and you can deduct it from your taxes. In other words, donating your crypto can often reduce your tax burden. Would you rather donate to the tax agency or your favorite cause?

**Does the IRS recognize cryptocurrency donations?**
The IRS classifies cryptocurrencies as property, so cryptocurrency donations to 501c3 organizations receive the same tax treatment as stocks.

## Giveth

**What is Giveth?**
Giveth is a community focused on Building the Future of Giving using blockchain technology. There are a lot of projects in the Giveth Galaxy, but the core two projects are: Giveth.io and the GIVeconomy.
You can use Giveth to donate to projects or also propose projects that need funding, all using cryptocurrency and soon fiat currencies! We aim to foster a large network of organizations and to build a bright, transparent and decentralized Future of Giving.

**How is Giveth founded?**
Giveth has been adding value to Ethereum since 2016, funded solely by donations and a few grants programs (i.e Panvala, Gitcoin). Our community has come this far without the help of any investors. You can support us by donating to our project.

**Is Giveth recognized as an official charity?**
With the help of SDG impact fund the Giveth DAO and community based organizational structure is represented as a non-profit 501c3 in the United States. We are a community-led project and will not derive any direct profit from the platform. We guarantee all funds will get recycled back into the Community that is ensuring the Giveth Platform becomes adopted widely.

**Is my donation tax deductible?**
We do not support donors in obtaining tax deductions and if a donor receives GIVbacks for donating to a verified project, we can not guarantee that the donation is legally tax deductible.

**Where can I see in detail how Giveth is spending their funds?**
One of the core values of Giveth is transparency. We invite everyone to have a look at our finances. Funding, expenditures and payments relating to Giveth's Treasuries can be seen in many places, including:
* [nrGIV](https://aragon.1hive.org/#/nrgiv/) for Contributor Expenses and GIVbacks
* [GIVgarden](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98) for community initiatives and external funding requests
* Giveth Liquidity Multisig on [Mainnet](https://gnosis-safe.io/app/eth:0xf924fF0f192f0c7c073161e0d62CE7635114e74f/balances) and [Gnosis Safe](https://gnosis-safe.io/app/gno:0xf924fF0f192f0c7c073161e0d62CE7635114e74f/balances) for Liquidity creation for $GIV
* Giveth Main Multisig on [Mainnet](https://gnosis-safe.io/app/eth:0x4D9339dd97db55e3B9bCBE65dE39fF9c04d1C2cd/balances) and [Gnosis Chain](https://gnosis-safe.io/app/gno:0x4D9339dd97db55e3B9bCBE65dE39fF9c04d1C2cd/balances) for Grants and Donations to Giveth

**Are there fees for creating a project?**
Nope! Giveth will never charge any additional fees for creating projects on our platform. If you create a project on Giveth.io it creates an entry in our database that directly points to your chosen Ethereum wallet. You can do this as well with a brand new account that holds zero funds. There are minor fees when using the ethereum network, and if you use other exchanges or services, there are likely associated fees. To learn more, read up on some of the [foundation mechanics of Ethereum](https://ethereum.org/en/eth/).

**What percentage of the donations go directly to the project?**
100% of funds raised on Giveth go directly to the project. Giveth does not charge fees to givers or makers. There are minor fees when using the ethereum network, and if you use other exchanges or services, there are likely associated fees. To learn more about fees and how Ethereum works, visit [their website](https://ethereum.org/en/eth/).

**Can I donate on Giveth if I don't have Crypto?**
Fiat integration (donate funds from your credit card or bank account) is coming soon! Stay tuned... Giveth has also partnered with [SDG Impact Fund](https://www.sdgimpactfund.org/) to make it possible for donors to contribute tax-deductible donations, in fiat or crypto, to altruistic projects on the blockchain. This is a major development in finance innovation to effectively care for the commons. We are very close to having fiat options integrated with the Dapp. Until then, fiat donations will be accepted [here](https://www.sdgimpactfund.org/giveth-foundation). To learn more about the partnership between Giveth and the SDG Impact Fund, please refer to [this blog post](https://medium.com/giveth/giveth-2-0-next-level-community-philanthropy-f7e60d7e78cb).

**I'm a donor. How do I know projects are getting my money?**
Each project description page shows a list of all donations made to that project and by who. Giveth.io does not collect any fees and your donation is sent directly to the project's provided wallet address. You can also find your donation on the blockchain by the link to the transaction on a block explorer (i.e etherscan.io after you make a successful donation.

**How can I be sure my donations are making a difference?**
We believe that every human being should be able to transparently see their funds create good in the world. Transparency is the key to staying focused on the work at hand. Project owners will be responsible for providing updates on how donations to their project are used.

**How do I know the project I contributed to was completed?**
Each project has the opportunity to post updates as its status changes, and donors who contributed to that project will receive notifications when a project owner posts an update. Donors can log back on to Giveth to see photos, written updates, and sometimes videos of a given project. Updates are the responsibility of the project owner, Giveth has no direct control in facilitating these updates.


**Is there a maximum funding cap for a single project?**
There is no maximum funding cap for projects. However, projects are encouraged to define specific funding requirements for better transparency.

**What types of projects are prohibited?**
Projects that are found to exhibit "unacceptable behaviour" and/or violate our [Covenant](https://docs.giveth.io/whatisgiveth/covenant/) and/or [Terms of Use](https://giveth.io/tos) are considered prohibited and will be cancelled immediately and an email will be send to the project owner. Learn more in our [documentation article](https://docs.giveth.io/dapps/listedUnlisted/#cancelled-projects).

**What is a Traceable project?**
A project on Giveth.io that has been verified can choose to become a [Campaign](https://docs.giveth.io/dapps/entitiesAndRoles/#campaigns) on [Giveth TRACE](https://trace.giveth.io/), thus becoming a Traceable project. This enables project creators to manage their donations transparently using [Traces](https://docs.giveth.io/dapps/entitiesAndRoles/#traces). Traces specify how the project is using their donations to achieve the goals of the overarching Campaigns. Upgrading giveth.io projects to Campaigns enables project creators to specify parts of their project requiring funding as different types of [Traces](https://docs.giveth.io/dapps/entitiesAndRoles/#traces). Donors benefit from being able to choose to fund either specific Traces or the overarching Campaign, and are able to trace the flow of their donations. A traceable project appears on both [Giveth TRACE](https://trace.giveth.io/) (as a Campaign) and Giveth.io, allowing for double exposure! To learn how to make your project traceable, visit our [documentation](https://docs.giveth.io/dapps/makeTraceableProject/).

**I still need more detail on how Giveth works. Where can I find this?**
For information about how Giveth works, its governance structure, developer documentation and user guides for the Donation Application please have a look at the [docs](https://docs.giveth.io/). You're always very welcome to join our chatrooms. Please visit the [Join Page](https://giveth.io/join).

**I love Giveth but right now I have no funds to Donate, How else can I contribute?**
We are a very inclusive Community and would love for you to join and see how you can get involved. [Join us on any of our social channels](https://giveth.io/join) and come talk to us!

## GIVeconomy

**Why is Giveth launching a token?**
Giveth’s mission is to reward & empower those who give -- to projects, to society & to the world. The GIV token fuels and drives the GIVeconomy and some has been already distributed to those who have contributed to making Giveth what it is today. Anyone with an Ethereum wallet can get GIV via our [GIVbacks program](https://docs.giveth.io/giveconomy/givbacks/) by donating to verified projects. GIV is a governance token that allows our community to actively participate in shaping the future of Giveth in a decentralized way.

**What nerwork is the GIV token on?**
GIV was deployed on Ethereum Mainnet and is used most heavily on Gnosis Chain (xDai). However, the GIViverse is multi-chained and GIV will likely be bridged/transferred to other chains and Layer 2 networks.

**Why are you using the Gnosis (xDai) network?**
Giveth was part of the creation of Gnosis Chain (formerly xDai Network) and loves the low-gas fees!

**What can I do with GIV?**
With GIV, you can Govern, Donate, Farm & Earn! Explore the GIVeconomy [here](https://giveth.io/giveconomy).

**How can I get (more) GIV?**
You can get GIV by interacting with the GIVeconomy and Giveth in several ways:
* By [donating](https://giveth.io/projects) to verified projects and getting [GIVbacks](https://docs.giveth.io/giveconomy/givbacks/).
* By providing liquidity and staking tokens in the [GIVfarm](https://giveth.io/givfarm).
* By wrapping GIV and voting in the [GIVgarden](https://giveth.io/givgarden).
* By [becoming a contributor](https://giveth.io/join).

**Who is elegible to receive the GIVdrop?**
Recipients of the GIVdrop include members of the "Giveth trusted seed" - our community of crypto philanthropists, Giveth users & builders, Blockchain4Good DAO members, and other ecosystem partners. Check your [GIVdrop](https://giveth.io/giveconomy) or learn more about eligibility in our [documentation](https://docs.giveth.io/giveconomy/givdrop/).

**Will there be another GIVdrop?**
No, there are no more GIVdrops planned, but anyone can get GIV from [GIVbacks](https://docs.giveth.io/giveconomy/givbacks/) by donating to verified projects on Giveth.

**How do I claim my GIVdrop?**
You can check your GIVdrop and claim your tokens [here](https://giveth.io/giveconomy) or read our [tutorial](https://docs.giveth.io/giveconomy/givdrop/#claiming-your-givdrop) on how to claim!

**Why can't I see my successfully claimed GIV in my wallet?**
The GIVdrop is on Gnosis Chain (xDai). Ensure that your wallet is connected to xDai and that you have added GIV to your token list! The address for the GIV token on xDai is 0x4f4F9b8D5B4d0Dc10506e5551B0513B61fD59e75.

**Why don't I have a GIVdrop?**
The GIVdrop has been sent to our community of crypto philanthropists, Giveth users & builders, Blockchain4Good DAO members, and other ecosystem partners. We have made every effort to include all valid addresses in this GIVdrop, at our discretion. Not every person who has ever interacted with Giveth is eligible. If you did not receive GIV, that is because you were not eligible. We will not review past transactions or consider other addresses for inclusion. We appreciate your understanding.

**I didn't receive a GIVdrop. Can I get one now?**
We have made every effort to include all valid addresses in this GIVdrop, at our discretion. Not every person who has ever interacted with Giveth is eligible. If you did not receive GIV, that is because you were not eligible. We will not review past transactions or consider other addresses for inclusion. We appreciate your understanding.

**I'm elegible for the GIVdrop, but I lost the keys to my address. Can you help me?**
If you received the GIVdrop but no longer have access to the eligible address, it is possible for us to redirect the allocation to another ETH address. However, you need to prove who you are and that you do have tokens allocated to you. If this is you, [reach out to our team](https://giveth.io/support) for support. FYI - If no one on the Giveth team knows you, it probably won't work out.

**How do I get involved in governance?**
[Join Discord](https://discord.giveth.io/) to engage with the community. If you have GIV, wrap it in the [GIVgarden](https://giveth.io/givgarden) to unlock your governance voting power. Keep abreast of governance proposals and participate in the discussion in our [Forum](https://forum.giveth.io/).

**What is the GIVbacks program?**
GIVbacks is a revolutionary concept that rewards donors to verified projects on Giveth with GIV. Learn more about [GIVbacks](./givbacks.md) in our documentation.

**What is a 'Verified' Project?**
'Verified' is a top tier status for projects wishing to join the GIVbacks program. The GIVbacks program is a revolutionary concept that rewards donors to verified projects with GIV tokens. By applying for a 'Verified' project status, you will be able to make your project stand out and encourage more donations. Getting your project verified also builds a relationship of trust with your donors by demonstrating your project's legitimacy and showing that the funds are being used to create positive change. This simple verification process requires some additional information about your project and the intended impact of your organization. If you would like to apply to receive the 'Verified' badge, encourage more giving and give back to those who have helped you reach your goals, learn more about how to apply [here](https://docs.giveth.io/dapps/projectVerification/).

**I earned GIVbacks, but the GIVbacks page says my balance is zero. What happened?**
When you harvest GIV rewards on Gnosis Chain (xDai) from the [GIVgarden](https://giveth.io/givgarden), [GIVfarm](https://giveth.io/givfarm), or [GIVstream](https://giveth.io/givstream) pages, you get all liquid GIV allocated to you in our token distro in a single transaction. If you earned GIV but don't see it on the [GIVbacks](https://giveth.io/givbacks) page you may have already claimed this allocation from another page.

**What is the GIVgarden?**
The [GIVgarden](https://giveth.io/givgarden) is the Giveth Community’s DAO governance platform, developed by [1Hive's Gardens team](https://1hive.gitbook.io/gardens/), where GIV token holders can influence the treasury, roadmap and mission of the Giveth ecosystem. To learn more, check out the [GIVgarden documentation](https://docs.giveth.io/giveconomy/givgarden/).

**What is the GIVfarm?**
The [GIVfarm](https://giveth.io/givfarm) is the Giveth liquidity mining program that allows GIV holders to provide liquidity and stake tokens to earn GIV rewards. To learn more, check out the [GIVfarm documentation](https://docs.giveth.io/giveconomy/givfarm/).

**What is the GIVstream?**
The [GIVstream](https://giveth.io/givstream) aligns community members with the long term success of Giveth and the GIVeconomy. With the GIVstream, anyone who adds value to the GIVeconomy gets GIV continuously for up to 5 years. The GIVeconomy starts out small but as more value is created, the GIViverse expands -- More GIV becomes liquid and more GIV spreads out to our community of stakeholders. To learn more, check out the [GIVstream documentation](https://docs.giveth.io/giveconomy/givstream/).

**Why is there a GIVstream?**
The GIVstream nurtures the GIVeconomy at inception by having only 10% of the total supply of GIV liquid and transferable to start. As the GIVeconomy grows & stabilizes, more GIV become liquid and available for everyone. We want to empower those who support the Giveth ecosystem with steadily increasing governance rights, this includes participants who [donate to verified projects](https://giveth.io/projects), vote in the [GIVgarden](https://giveth.io/givgarden) or provide liquidity in the [GIVfarm](https://giveth.io/givfarm). Participants benefit from their GIVstream flowing as the GIVeconomy flourishes over time, therefore we ensure that Giveth is not just governed by people who buy tokens on the open market but by those who contribute in a more meaningful way.

**How do I get a GIVstream?**
You can get (or increase) your GIVstream flow-rate on Gnosis Chain by donating (on Gnosis (xDai) or Mainnet) and getting [GIVbacks](https://giveth.io/givbacks), by wrapping GIV to use in the [GIVgarden](https://giveth.io/givgarden), or by staking in the [GIVfarm](https://giveth.io/givfarm) on Gnosis (xDai). You can get (or increase) your GIVstream flowrate on Ethereum Mainnet by providing Mainnet liquidity and staking GIV or LP tokens in the [GIVfarm](https://giveth.io/givfarm) on Mainnet.

**Can I speed up my GIVstream?**
You can increase your [GIVstream](https://giveth.io/givstream) flow-rate by participating in the GIVeconomy through [GIVbacks](https://giveth.io/givbacks) , the [GIVgarden](https://giveth.io/givgarden), or the [GIVfarm](https://giveth.io/givfarm). You cannot, however, accelerate your GIVstream to decrease the time remaining. The "GIViverse expansion" time period ends on December 23, 2026 and is the same for the entire GIVeconomy.---
id: importTorusMM
title : Import Torus Private Key into Metamask
slug: dapps/importTorusMM
---
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from '../src/css/custom.css'


While the Torus wallet is a great option for newcomers to crypto, it can be more difficult to use when interacting with decentralized applications (dApps). Giveth users have the opportunity to earn [GIV](https://docs.giveth.io/giveconomy/) by interacting with the [GIVeconomy](https://giveth.io/). Torus users can claim [GIVbacks](https://giveth.io/givbacks), stake in the [GIVfarm](https://giveth.io/givfarm), claim their [GIVstream](https://giveth.io/givstream) and [claim their GIVdrop](https://giveth.io/claim) ([if eligible](https://docs.giveth.io/giveconomy/givdrop)), but MetaMask users benefit from a more streamlined user experience.  In addition, at present the [GIVgarden](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98) does not include Torus wallet integration.

We want to empower new-comers to crypto with the means to get fully integrated into the web3 community. MetaMask is a secure crypto wallet and a highly optimized gateway to blockchain apps. The purpose of this guide is to explain how to get funds into a MetaMask wallet, thereby enabling broader functionality and security. Users can do this by either transferring funds to a brand new MetaMask wallet or by importing private keys from an existing wallet like Torus. We recommend transferring the funds to a new wallet. Transferring funds removes the risk of someone accessing the wallet using the username and account used to set up the Torus wallet. For instructions on how to get started with a MetaMask wallet, [check out this article from the Metamask team](https://metamask.zendesk.com/hc/en-us/articles/360015489531-Getting-Started-With-MetaMask).

## Transfer Your Funds to MetaMask
Once you are logged into your Torus wallet, navigate to the transfer page using the navigation bar at the top of the page. 

1. Copy the public key from MetaMask.
2. Paste into the ‘Transfer to’ line.
3. Enter the amount you’d like to send.

Once you are satisfied with the parameters of the transaction, click the transfer button at the bottom of the page.
If you have multiple tokens in your Torus Wallet, you will have to repeat this process for each token. 

<img alt='Download Private Key in Torus' width='75%' height='auto' class='center' src={useBaseUrl('img/content/transferTorusMM.png')} />

## Import Torus Private Key Into MetaMask
### What is a Private Key

Your [private key](https://www.coinbase.com/learn/crypto-basics/what-is-a-private-key) is a string of numbers and letters that allows you to access and manage your funds. <span class='importantText'>It should never be shared with anyone (no community moderators, no Giveth core contributors, no admins, <i>no one!</i> )!</span>. Anyone who has access to your private key has access to your crypto. Importing your Torus private key into MetaMask allows you to access and control your funds from both wallets. This means that you can enjoy full functionality of Giveth and other dApps by using MetaMask, but can still access your funds using your regular Torus login if you wish.
### Get your Torus Private Key
Once you’re signed in to your Torus wallet, navigate to the `Settings` page using the menu at the top of the page. Once on the `Settings` page, click `Account Details` in the `Privacy and Security` section. This will open a pop-up with two options for getting your private key.

<img alt='Download Private Key in Torus' width='75%' height='auto' class='center' src={useBaseUrl('img/content/toruspk.png')} />

The first option is to download a soft copy of your private key as a JSON file. When you select this option you will be prompted to create a password that will later be used to import the file into MetaMask. Create your password, then download the file.
The second option is to show the private key and copy it. This method is less secure since it both shows the private key and copies it to your operating system clipboard. Once copied, your private key can be pasted into MetaMask to import the private key. If you use this option, do not save a copy of your private key. If your system is ever compromised, your private key will be as well.
### Import Private Key
Assuming you are set up and logged in with your Metamask wallet, the next step is to import your private key into MetaMask. First, click the circular icon in the top right corner of your MetaMask wallet. This will open the accounts menu. Click the `Import Account` option in this menu. Here you can use the `Select Type` option to select which option you’d like to use to import your private key.

<img alt='Import Private Key into MetaMask' width='50%' height='auto' class='center' src={useBaseUrl('img/content/mmimportkey.png')} />


If you copied your private key from Torus, the `Private Key` option will let you paste the key into MetaMask. If you downloaded the JSON file, select `JSON File`, then use the `Choose File` button to select the private key JSON you downloaded from Torus. Enter the password you created to download the private key file from Torus, then click `Import`. Your new account should now appear in MetaMask and be ready to interact with the GIVeconomy dApps!

<img alt='Paste Private Key' height='auto' width='40%' class='leftfloat' src={useBaseUrl('img/content/mmimportkey1.png')} />
<img alt='Select Private Key File' height='auto' width='40%' src={useBaseUrl('img/content/mmimportkey2.png')} />
---
id: installGIVeconomy
title: Installing the GIVeconomy Front-End
slug: dapps/installGIVeconomy
---

You can find the Github repository containing the [GIVeconomy](https://giveth.io) front-end at https://github.com/Giveth/liquidity-mining-dapp.

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).
## Prerequisites

- Yarn
- npm
- your own [Infura](https://infura.io/) nodes for Kovan Network and Gnosis Chain (formerly xDai Network)
- your favourite code editor (We recommend VSCode)


## Getting Started

First you'll need to get a local copy on your machine. Clone the repository from github on your computer.

```
git clone git@github.com:Giveth/liquidity-mining-dapp.git
```

:::info
### Environment Variables
copy `.env.example` to `.env.local` and set the values to your Infura nodes as well as your API key
:::


Then to run the development server locally:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result. Open up your code editor and you're ready to start!

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
---
id: givethIO
title: Intro to Giveth.io
slug: dapps/givethIO
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

# Intro to Giveth.io

Giveth.io, [launched in March 2021](https://medium.com/giveth/the-future-of-giving-is-here-d480388a3338), offers a simple and streamlined way for the world to donate to for-good projects via the Ethereum Blockchain.

<img id="contentimg" width="800" height="auto" alt="giveth.io homepage" src={useBaseUrl('img/content/givethio/givethIOhome.png')} />

[Giveth.io](https://giveth.io) boasts a smooth onboarding process for donors and projects. Creating a project can be done in minutes, making donations can be done in seconds. Finding quality projects making social or environmental change is easy.

Our Donation Application uses a direct peer-to-peer donation framework; funds donated are sent to the project owner's Ethereum address. Giveth does not collect any fees from interactions on the platform.

Giveth.io is currently deployed on both Ethereum mainnet and Gnosis Chain (formerly xDai Network).

## Verification and Traceable Projects

Great projects make Giveth thrive! We have a Project Verification process to ensure that we have top quality, credible projects on the DApp. One of the benefits of verification is that approved projects can become a Campaign on [Giveth TRACE](https://trace.giveth.io), and gain access to customizable donation management, features and donation traceability. [Learn more](/dapps/makeTraceableProject).

---
#### Follow any of these links to learn more about Giveth.io:
- Visit [Giveth.io](https://giveth.io) to see the magic happening
- Join our [Discord](https://discord.giveth.io) to meet the community
- For Givers and project owners learn more in [Getting Started](/dapps/gettingStarted)
- For developers, head over to the [Contributor Guide](/dapps/contributors)
---
id: introTrace
title: Intro to Giveth TRACE
slug: dapps/introTrace
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


Giveth is re-engineering charitable giving, by creating entirely free, open-source platforms, built on the Ethereum Blockchain. Giveth TRACE cuts out bureaucracy and enables makers to create a high level of transparency and accountability for Givers. The basic donation hierarchy of Communities, Campaigns and Traces allows for users to specify the scope of their donation. There are multiple reviewer roles and security check points that allow Givers and Makers to use our DApp with confidence. You can read more about the basic components and the **logic behind our DApp (Donation Application) in this [post.](https://medium.com/giveth/what-is-the-future-of-giving-d50446b0a0e4)**

<img alt="Giveth TRACE home page" src={useBaseUrl('img/content/trace/tracefrontpage.png')} />

## Current Status
The [Giveth TRACE DApp](https://trace.giveth.io) is on the Ethereum mainnet, bridged to Rinkeby testnet. We are in active development on the DApp and aiming for a post-beta release in the coming months. The best way to reach out to our team is via [Discord](https://discord.gg/GMQFKmdSGy), feel free to drop in and say hello!


New Projects are currently being added onto Giveth TRACE by a case-by-case vetting process. If you have a simple project looking for funding try out [Giveth.io](https://giveth.io). If you have a community, cause or project that is more complex, and perhaps requiring greater transparency and traceability, then get in touch with us on [Discord](https://discord.gg/qf7XZ48gCU).

Check out the amazing projects onboarded onto our [DApp](https://beta.giveth.io), and register as a user by completing a profile. You can support the development of our Dapp by giving to a Community or Campaign, or funding specific Traces directly and see exactly how your donation creates positive change in the world.

### A Tale of Two Networks
It's been a quest getting to mainnet efficiency, challenged by **scalability issues** that were too prohibitive for real use. In 2017, we found a smooth solution with a bridge between Ethereum mainnet and Rinkeby testnet.

<img alt="Selecting the Rinkeby Network" src={useBaseUrl('img/content/trace/rinkebyselect.png')} class="leftfloat" />

In order to interface with the Giveth application you'll have to [download and install MetaMask](https://metamask.zendesk.com/hc/en-us/articles/360015489531-Getting-Started-With-MetaMask) on your favourite web browser. The Ethereum address used for your MetaMask sign-in will be how we identify your personal profile on the DApp.

This ground-breaking innovation (of its time) allows Giveth and the user to perform smart contract interactions for free, spending only gas on Rinkeby testnet, while still tracking everything on a blockchain. For most tasks on Giveth TRACE you'll want to make sure you're connected to the **Rinkeby** test network.

When you're sending real funds to any entity on Giveth TRACE, you do it with the Ethereum mainnet. Conversely, when you claim funds that have been delegated to a completed Trace you are the recipient of, **Giveth pays the gas** to bridge your transaction to the mainnet and send the funds to you.



To learn more about the Giveth bridge, head over to the documentation [here](https://docs.giveth.io/dapps/bridgeSecurity). There is also a [wonderful Medium article](https://medium.com/giveth/tackling-ethereum-scalability-issues-29bd700b5060) from 2017, that identifies the major scalability issues of that era in crypto and how we found a solution.

### Development
You can follow the development on [Github](https://github.com/Giveth/giveth-dapp), read more in this documentation (add internal link) or join our contributors channel in [Discord](https://discord.gg/qf7XZ48gCU). Our meetings are on the [Giveth calendar](https://calendar.google.com/calendar/embed?src=givethdotio@gmail.com&pli=1), and you are welcome to join!
---
id: leavingTraces
title: Leaving Traces (formerly Creating Milestones)
slug: dapps/leavingTraces
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


*Welcome! If you are super new to Giveth, join the [#🔨contribute](https://discord.gg/qf7XZ48gCU) channel on Discord. You can introduce yourself and ask questions there! This is a living document and will change as bugs are fixed and features added to the DApp.*

### Leaving Traces is one of the most integral features of Giveth TRACE.
As part of our ongoing commitment to transparency Traces, formerly known as Milestones, represent how users can record their work or progress and submit proposals requesting compensation.

 **1.** Go to [Giveth TRACE](https://trace.giveth.io) and select which campaign your Trace is for.

**2.** From the campaign page, click *“Create New”*. You have four options on the following page: **Payment**, **Bounty**, **Expense**, **Milestone**, choose which is most applicable to the form of compensation you're proposing.

<img id="contentimg" alt='Trace Options' src={useBaseUrl('img/content/trace/typesofTraces.png')} />


**3.** Fill in the following form with the details of your Trace. Your Title should be clear and descriptive. If you chose *Payment* or *Expense*  add the Currency type, Amount and Date, if applicable, otherwise select "*No limits*".

<img id="contentimg"  alt='Trace Options' src={useBaseUrl('img/content/trace/tracesDescription.png')} />

**4.** From this point on, consider copying all of your Trace text to a place where you keep your own records. If your reviewer declines to review this milestone, or if it gets caught in the process for any reason, you will have to re-propose the milestone anew.

**5.** In the "Description" text field below add more details. Include proof of work or expenses. You can link to github pages, other documents you worked on, or upload photos of receipts. Show your calculations if any.


**6.** Add a photo for your milestone. It can be related to the work, or not!


<img id="contentimg"  alt='Trace Options' src={useBaseUrl('img/content/trace/tracePictureSelect.png')} />

**7.** From **Payment Options** select how you wish to be compensated. Choose from the cryptocurrency options available and provide an address for which you wish to be sent payment. You can also be awesome and give 3% of your amount received to Giveth to keep the platform running(optional)!

**8.** If at step #2 you chose a *Bounty* or a *Milestone* you have the option to set a Reviewer. Think about who will be the best for the job. The Reviewer is responsible for ensuring that all steps in the Trace have been completed and accomplished before the compensation should be paid out. If possible, choose a different person than the campaign manager. Having the campaign manager, reviewer, and proposer (you) be 3 different people helps ensure against mistakes being overlooked, but the most important thing is that the people approving your Trace understand the work.


**9.** Click “*Propose*” and now monitor your Trace’s progress from the “*My Milestones*” (NEEDS TO BE UPDATED) page. Once your campaign manager approves it, it’s status will read “In Progress.” It’s now your turn to mark it complete, which will push it to the reviewer and status says “Needs Review.” If any of these processes are moving slowly or you notice it went backwards from “Needs Review” to “In Progress,” (this is how it will look to you if the reviewer rejects the milestone) check in with your reviewer.
---
id: listedUnlisted
title: Project Quality Assurance Guide
slug: dapps/listedUnlisted
---
import useBaseUrl from '@docusaurus/useBaseUrl';

In order to ensure the quality of projects on our DApp, we have implemented a processus for pre-screening projects before they are featured on the Giveth homepage. All new projects are initially **unlisted** until they are reviewed and approved by a Giveth Unicorn. Unlisted projects can still receive donations and can be accessed via the project's URL. However, only **listed** projects will appear on the Giveth homepage & projects page, and using our sort, filter and search functionalities.

Once reviewed and approved, listed projects will appear everywhere on the DApp! If a project does not meet the listed critera, the project owner will receive an email asking them to update the project. If the project owner updates their project, it will be reviewed again by our team.

If a project is reviewed and found to violate our **Terms of Use**, it will be **cancelled** immediately, and the project owner will be notified via email.

The following guide is intended to support project owners in creating high quality listings and to support Giveth Unicorns in the review process.


## Listed Projects
In order for a project to be approved and listed on the DApp, it must have the following:
- :heavy_check_mark: Clear project descriptions explaining who they are and what they want to do with the funds
- :heavy_check_mark: A unique or custom banner photo
- :heavy_check_mark: No violations of our [Covenant](../whatisgiveth/covenant/) and/or **Terms of Use**
- :heavy_check_mark: (Optional) Embedded photos, videos or legitimate external links
- :heavy_check_mark: (Optional) For open-source projects, a link to their repository

### Examples of Projects that pass "Listed" criteria

1. [Giveth](https://giveth.io/project/the-giveth-community-of-makers): Unique photo, clear description, external links
<img alt='Giveth' src={useBaseUrl('img/verifiedproject.png')} />

2. [The Commons Simulator](https://giveth.io/project/The-Commons-Simulator:-Level-Up): Unique photo, clear description, embedded video, external links
<img alt='CommonsSimulator' src={useBaseUrl('img/verifiedproject2.png')} />

## Unlisted Projects
A project is likely to remain unlisted due to the following:
- :x: No project description
- :x: Vague project description
- :x: No unique or custom banner photo

However, in order to remain active, the unlisted project must still exhibit:
- :heavy_check_mark: No violations of our [Covenant](../whatisgiveth/covenant/) and/or **Terms of Use**

### Examples of Projects that do not pass "Listed" criteria

1. danger dan defi: No description
![](https://i.imgur.com/ln7nrO2.png)

2. Giving your hands to help: Strange/vague description: "We want to do favours all over Canada"
![](https://i.imgur.com/TV9lNqw.jpg)

3. Pritesh
   - Very minimalistic description: "We are helping poor Bangladeshi people after the crash. We are giving out rice and clothes to people around us."
    - No clarity given in the details of what crash and the exact process for "giving rice and clothes"
![](https://i.imgur.com/e22OlGd.png)

4. Cats
   - Very minimalistic description: "We're collecting funds to give to the local cat shelter. We always need moar funding for cats."
   - No website, no clear explanation of how they will use the funds to help cats
![](https://i.imgur.com/P0fvJXE.png)

## Cancelled Projects

Projects that are found to exhibit "unacceptable behaviour" and/or violate our [Covenant](../whatisgiveth/covenant) and/or **Terms of Use** will be cancelled immediately, and an email will be send to the project owner.

### Examples of unacceptable behaviour include:
- :x: The use of violent or sexualized language or imagery, and sexual attention or advances of any kind
- :x: Trolling, insulting, derogatory, abusive or vulgar comments, and personal, political, or religious attacks
- :x: Public or private harassment
- :x: Publishing others’ private information, such as a physical or email address, without their explicit permission (including doxing)
- :x: Other conduct which could reasonably be considered inappropriate in a professional setting
---
id: projectUpdates
title: Adding Updates to Your Project
slug: dapps/projectUpdates
---

import useBaseUrl from '@docusaurus/useBaseUrl'





# Adding Updates to Your Project


Are you the proud owner of a verified project on Giveth? If so, it's important to keep your donors in the loop and maintain your active status by posting updates every 3 months. 

If your project isn’t verified, posting updates is optional. However, it is always helpful. Providing updates that show the impact of donations helps to build trust with potential donors and previous donors are more likely to continue donating. You can show impact in numerous ways such as posting measurable results and statistics and sharing case studies, stories, and videos. 



Don't worry, it's easy! Simply sign in to your account and click on the `Updates` section of your project page. 

<img alt="Add Project Update" src={useBaseUrl('img/content/updates1.png')} />



From there, select a title that accurately reflects the content of your update. 

<img alt="Edit Project Update" src={useBaseUrl('img/content/updates2.png')} />


But don't stop there! As mentioned above, adding relevant content such as photos, videos, and receipts will show your donors exactly where their funds are going and build a relationship of trust. 

[Click here](https://youtu.be/sRhp74CcGU8) for a helpful video guide on posting updates. 


Remember that staying active and keeping your donors informed is the key to success when it comes to your Giveth project.
---
id: niceToken
title: $nice Token
slug: /giveconomy/niceToken
---
import useBaseUrl from '@docusaurus/useBaseUrl';


The $nice token was launched in Q3 2022 in an effort to promote direct donations to the Giveth Organization.

When users on the Giveth Dapp make a donation to the [Giveth Project](https://giveth.io/project/the-giveth-community-of-makers) in certain eligible tokens they'll receive $nice in return.

<a href="https://giveth.io/project/the-giveth-community-of-makers"><img alt="nice token banner"  src={useBaseUrl('img/content/niceBanner.png')} /></a>


The following tokens have been listed as eligible for $nice when donated to Giveth:

import NiceTokenList from '../_niceTokenList.mdx'

<NiceTokenList />

$nice is matched at a 1:1 ratio of the USD value of the donations at the time the donation was made. For example if you donated 50 DAI to Giveth (assuming it holds its $1 peg) you would receive 50 $nice.

Eligible donations are registered on the same bi-weekly rounds that [GIVbacks](https://docs.giveth.io/giveconomy/givbacks/) follow. Distribution of $nice, once calculated, is done at the same time that GIVbacks are sent out.

#### Token Address
- Giveth $nice token (Gnosis Chain): [0xde378ea32af41b4a2b9c8baee1655761d526c0df](https://gnosisscan.io/token/0xde378ea32af41b4a2b9c8baee1655761d526c0df)

## Utility

The first of many features of $nice will be the ability to redeem it for swag on the [Giveth swag shop](https://swag.giveth.io/). You can get Giveth branded clothing and more delivered right to your door for supporting Giveth.

Some other exciting utilities down the road might include:
- Early Access to and Redemption of $nice for [Giveth PFPs](https://forum.giveth.io/t/the-givers-pfp-collection-initial-sketches/656/5).
- Leaderboards and Social Media promotion of top Giveth donors and $nice holders.
- GIV rewards program for $nice holders.

The sky's the limit for $nice and the Giveth team is actively building and experimenting with features and future utilities of this new token.

## Use of Funds

Giveth will use the acquired funds for a very direct strategy to ensure the stability and growth of Giveth and the GIVeconomy. 

50% of the USD value of eligible donations received will be used to buy back GIV. The other 50% will be used to create a liquidy pool pair with the bought back GIV.

Let's look at an example:
> Over a 3 month period Giveth acquires $100,000 of eligible donations in DAI.
> 
> We use $50,000 worth of the DAI received to buy back GIV from the circulating supply.
> 
> Subsequently we take this $50,000 worth of GIV we just bought back and combine it with the remaining $50,000 of DAI to supply a $100,000 DAI/GIV LP position on Uniswap v2 that is owned by the Giveth multisig.

This effectively allows Giveth to create strong DAO-owned liquidity positions over time. This in turn helps to mitigate the volatility that liquidity farming programs can have on the GIV token economy.

Giveth may employ new strategies for received funds at any given point in the future.

---
id: giverspfp
title: The Givers PFP Collection
slug: dapps/giverspfp
---
import useBaseUrl from '@docusaurus/useBaseUrl';


“The Givers” NFT’s are not just NFT’s but integrated Giveth PFPs! Giveth's first PFP collection was a [community proposed initiative](https://forum.giveth.io/t/the-givers-the-giveth-ecosystem-pfp-collection/478) begun in March 2022. The intention of the PFP collection is to raise funds for the Giveth DAO and continue our mission of building the Future of Giving. The Givers was launched for public minting on March 24, 2023 at 11am CST. 

**To mint a Giver head on over to [the minting page](https://giveth.io/nft)**! 


<img alt="Givers base image" src={useBaseUrl('img/content/GiversHidden.png')} />


:::info
### About the Giveth DAO
Since 2016, Giveth has focused on supporting public goods through a community-driven ecosystem of collective support and value creation. This has resulted in streamlined donation tools and mechanisms powered by blockchain technology, which have onboarded over 1,700 projects and has facilitated hundreds of thousands of donations.

We’re launching the Givers PFP collection as a fundraiser to allow us to continue improving our donation platform and build tools that empower non-profits and impact projects.
:::



## Supply & Minting

There will be a total of 1,250 NFTs in the collection, and no more than 100 of them will be used for promotional purposes by the DAO. Minting can be done on Ethereum Mainnet for 100 DAI each. To ensure an even distribution, no single address can hold more than 5 Givers PFPs.

## Art parameters

Every art NFT is created out of several individual layers of artwork. In some cases some of the layered artwork may be unseen as they get covered by others above it, as for instance the art tattoos. You will however be able to see all of your unique art's traits and rarity on Rarible or in the token's metadata.


## Secondary Market

You can trade your Giver but keep in mind that for any trades on the secondary market, a 10% royalty fee will be imposed. All Givers (unless stated otherwise) are licensed under Creative Commons CC0 or "No Rights Reserved". The easiest way to trade is using the [Rarible Collection Page](https://rarible.com/the-givers-pfp/items).


## Benefits

Givers PFP owners are able to have their NFTs integrated on their Giveth.io profile when logged in! Show your flair and support for Giveth almost anywhere on the DApp. Below is a preview of how Givers show up on the Giveth.io platform.
<a href="/img/content/PFPbenefits.png" target="_blank" rel="noopener noreferrer">
<img alt="pfp holder benefits on the dapp" src={useBaseUrl('img/content/PFPbenefits.png')} />
</a>
<p>
When you set your Giver as your profile picture on Giveth.io it will be show up as a badge next to your name on any projects that you have created as well as when you make donations or boost projects with GIVpower. Users can also get an up close look at your Giver by navigating to your user profile.  
</p>
  
  

Giveth is also partnering with Punk Domains to provide Givers NFT holders a **50% discount on the Giveth domain names.** Anyone is able claim their unique “yourname.giveth” domain name, which will also be linked to your account. You can check out [Giveth domain names here](https://giveth.punk.domains/#/).

We're still working on providing more benefits to Givers PFP holders, so stay tuned for more updates!

## Setting your Givers PFP

Setting your Givers PFP as your profile picture on giveth.io is very simple. First login with your web wallet that hold your Givers PFP NFT. Then head over to `My Account` from the dropdown menu in the top right and click on the link next to your profile picture that says `Set your Givers PFP`. From there you'll be taken to a menu where you can select your Givers PFP from your wallet and set it as your profile picture. Click `Save` and you're done! 

## Contract Address

GiversPFP Contract (Mainnet): [0x78fde77737d5b9ab32fc718c9535c7f1b8ce84db](https://etherscan.io/token/0x78fde77737d5b9ab32fc718c9535c7f1b8ce84db)

----

Mint a Givers PFP here: https://giveth.io/nft  
View the Givers collection on Rarible here: [Giveth Givers PFP](https://rarible.com/the-givers-pfp/items)---
id: projectdonating
title: How do I donate to a Project?
slug: dapps/projectdonating 
---
import useBaseUrl from '@docusaurus/useBaseUrl';


## Find a project that you like.
Have a good look at the projects already created, read the descriptions, and do your homework! 

You can browse projects through different categories and sort them by [GIVpower](./GIVpower.md) rank or other options.
<img alt='cryptodonation' src={useBaseUrl('img/projectcategories.png')} />

Once you found a project you would like to donate to, hit the `DONATE` button.

## Select how you want to donate your funds.
Once you're at the donation page, you need to select if you want to make your contribution in crypto or fiat currency.

#### Crypto Donations
We accept ETH and a wide variety of ERC-20 tokens on both Mainnet and Gnosis Chain (formerly xDai Network). Choose the amount of cryptocurrency you would like to donate. Once you've entered the amount you can click on `DONATE`, at which point your wallet will prompt you to validate the transaction. If you would like to use a different wallet than the one you use to sign into your account, click on `change wallet` in the drop down menu in the top right of the homepage.

<img alt='cryptodonation' src={useBaseUrl('img/cryptodonation.png')} />

When the transaction has been signed off and processed, you're done! Nice work! You'll be taken to the confirmation page, and you can track the transaction details by following the link on the page.

Take a look at our [Donor 101 video course](https://youtube.com/playlist?list=PL4Artm1rmCWH4Q5XnrQWf8fm0xob3hbdZ&si=EnSIkaIECMiOmarE) to get a better idea of how to use the platform for donations.

**[Step by step instructions for donating via Metamask can be found here.](./donatingmetamask.md)**

**[If you'd like to make a donation in fiat currency follow this guide.](./torusonramp.md)**
---
id: projectVerification
title: Project Verification Process and Guidelines
slug: dapps/projectVerification
---
import useBaseUrl from '@docusaurus/useBaseUrl'

Giveth is making use of project verification to review a project’s legitimacy and to reward donors to those projects via the [GIVbacks program](https://docs.giveth.io/giveconomy/givbacks). Project owners can apply directly from their project page after signing in by clicking **VERIFY YOUR PROJECT**.

<img alt="Verify My Project" src={useBaseUrl('img/content/Verifymyproject.png')} />

This document serves as a guide to understanding the Project Verification process, what information is needed to apply, as well as what qualifies/disqualifies a project for participation in the GIVbacks program.

## Benefits of Becoming a Verified Project

- Create greater legitimacy for your Project.
- Build deeper trust and transparency with Donors.
- Make your Project stand out.
- Get listed as a ‘Verified Project’ on our platform and searchable by that category.
- Become eligible for our GIVbacks program, which rewards Givers for philanthropic donations. Once your project is verified, the supporters who donate to your project will be rewarded with GIV tokens which they can use to participate in the GIVeconomy. Participation in the GIVbacks program will greatly increase the likelihood of your project receiving donations.
*Note that verified Project addresses will not receive GIV for donations made to their own project or other verified projects.*

## Qualifying Measures for Project Verification

The verification process will require some additional information about a project and the intended impact of the organization.

Projects must submit their application forms at least one week before the start of a round in order to qualify for that round. Once approved, its status is updated on Giveth, and it is given a `Verified` badge on the Homepage and on the Projects Page. 

**Verified badges will automatically expire after 3 months of project inactivity.
Be sure to share your progress with the world by adding regular updates!** 

<img alt="GIVbacks Rounds Schedule" src={useBaseUrl('img/content/givBacksRounds.png')} />

Here is the information you will need to provide in the application:

1. Your full name
2. Your email address
3. If your project is part of a registered non-profit organization, you will need to upload documentation to prove your registered status. Having obtained non-profit status is not a requirement, but it is helpful for the verification process.
4. If your project is not a registered non-profit, the team will need to know how your organization is structured.
5. Links and/or usernames to the social media accounts that are owned by both you and the organization. eg. Twitter, Github, Discord, Facebook, etc.
6. The name of your project
7. Information about the history of your project, e.g., when it was founded, which milestones your organization/project has achieved since conception, etc. Please provide links to photos, videos, testimonials or other evidence of your project's impact.
8. The funds raised are expected to be used for public benefit and not for personal gain - Giveth will need to know how you will use the funds that your project raises. We are looking for detailed funding goals as well as an overall roadmap/action plan of the project.
9. A list of all wallet addresses used for managing funds within your project.
10. In order to ensure that you are actually a representative of the project you're applying for, we ask that you post/share a link to your Giveth project **from the organization's Twitter or social media account.** You will need to provide a link to the Twitter or social media post.
11. Confirm “Yes”: We pledge that funds raised will be used for public benefit, not for personal gain.
12. Confirm “Yes”: We understand Giveth will be analyzing all donations looking for fraud or abuse. If Giveth has any reason to suspect abuse, we understand our donors may not receive any GIVbacks and that Giveth may share any evidence of fraud publicly.
13. Confirm “Yes”: We will only accept new, external donations through Giveth, and we understand that if we are found to be recirculating our own funds through Giveth, this will be considered abuse of the system.
14. Confirm “Yes”: We understand our donation data will be reviewed, and if it seems like in any way we are abusing the system, our donors will not receive GIVbacks, and we will lose our verified status.
15. Our goal is to ensure there is no fraudulent use of GIVbacks. We will need to know what reputation is at stake for you and/or your project if you were to be found participating in malicious activity. *Please provide links to proof of reputation if available.

## Disqualifying Factors for the GIVbacks Program

Once a GIVbacks round ends, there is a period of time allocated for our team to review flagged projects and donations for disqualifying factors before GIV is distributed to donors. A project could have their Verified status revoked if any of these factors are found. Donors to projects who are found with any of the following activity may also be denied GIVbacks for that round. Disqualification factors are as follows:

1. **Giving/offering goods or services to donors in exchange for their donation.** A project owner cannot offer goods such as a sponsorship for a conference, Girl Scout cookie purchases or tickets for a dinner, even if the proceeds go to charity. Project owners cannot provide services like acting as a crypto exchange for their donors. They can explain how to use an exchange, but they cannot convert the money for their donors.
2. **Circulating donations raised by other means.** Only “first touch” donations count for GIVbacks. If a project receives funding from a donor and is found to be circulating these donations within the Giveth platform to receive GIVbacks, they will be disqualified. For example, a project should not be sending fiat donations received elsewhere back to their donors and asking them to donate on Giveth with crypto.
3. **The funds are not being used for what is expressed in the project page or submitted verification application.** Verified projects are responsible for keeping their projects up-to-date with information on how the funds are being used. If the project states explicitly that they are, for example, using the funds to develop education programs but are found to be using the funds to employ developers, they may be disqualified from the GIVbacks program.
4. **Unscrupulous or fraudulent activity.** This can be the use of violence, breaking laws, or other behaviour that does not uphold the values of the Giveth community. Projects found to be violating our Terms and Conditions will not only lose their verification status, but they also will be canceled.

The Giveth Project Verification team is responsible for monitoring GIVbacks activity and the Project Verification system and will ultimately use their discretion to determine whether a project’s actions are unscrupulous and/or disqualifying.

## Graduated Sanctions for flagged projects

The activity and donation history of Verified Projects will be periodically reviewed. Verified projects that are flagged for any of the disqualifying factors above will be analyzed and discerned according to the graduated sanctions outlined here:

- A project that has been flagged and deemed to be disqualified for the **first time** will be notified and their donors will not receive GIVbacks for that round and the next. They will not, however, lose their verified status immediately and will have the opportunity to make any changes necessary to keep it.
- A project that has been flagged and deemed to be disqualified for the **second time** will be notified that their project has been flagged and that the donors for that round and all future rounds will not be receiving GIVbacks. Once a project has received a second flag, it will lose its `Verified` badge.
---
id: referral
title: Giveth Referral Program
slug: giveconomy/referral
---
import useBaseUrl from '@docusaurus/useBaseUrl'



# Giveth Referral Program


The [Giveth referral program](https://giveth.io/referral) is a way for users to earn rewards for donating to good causes and inviting their friends and network to do the same. With every donation made on Giveth, users can earn extra GIV tokens through the [GIVbacks program](https://docs.giveth.io/giveconomy/givbacks).

With this new referral program, users can earn even more rewards! By encouraging their friends and network to donate on Giveth through their own referral link, users can earn up to 50% of their friend's GIVbacks as well (an equivalent of up to 40% of the value of the donation amount).

## How much can you earn?


For this initial launch of the program, you could receive up to 50% of the GIVbacks for any referred donations! If you refer someone to donate $100, you could receive the equivalent of up to $40 in GIV rewards! 🤯
Who is eligible to participate?


This referral program is open to everyone! It doesn't matter if you're a project owner, a recurrent donor or just a passionate person for public goods. If you'd like to increase your rewards and positive impact, you can generate your own referral link and share it on social media, your website and favorite community channels.

For the first time, with the referral program project owners will be able to earn GIVbacks too, every time a donation is made through their referral link.
Past donors can also use the program to earn GIVbacks without actually donating: by sharing their referral links and getting rewarded for donations made to their favorite projects.

## How to get started


Simply go to the [Giveth Chainvine website](https://app.chainvine.xyz/giveth), connect your wallet, then copy your unique link from the "Your Referral Link" section, and start sharing it to encourage your network to give to good causes.

<img alt='Chainvine Campaign' src={useBaseUrl('img/chainvine.png')} />

<img alt='Chainvine Link' src={useBaseUrl('img/chainvine2.png')} />


That's it! You'll now be eligible for rewards in our next [GIVbacks round](https://docs.giveth.io/giveconomy/givbacks) (2 weeks intervals). Not only will you be making a positive impact, but you'll also be earning rewards (up to 50% of the GIVbacks amount from the donation) for your efforts.

## How rewards work

![image](https://user-images.githubusercontent.com/75490971/229162633-9b67d524-f29f-43d5-99b7-45f1e3b3787c.png)

For the initial phase of this program, you can earn up to 50% of the GIVbacks amount for anyone you refer!

This calculation varies based on the status of the referred donor: a new user to Giveth or an existing Giveth user (someone who has interacted with the Giveth dApp in the past).

### For new users

You will earn 50% of the GIVbacks for a given donor in the current and subsequent GIVbacks rounds. For example, if you refer a new user to donate in GIVbacks round 30, you will be entitled to 50% of all GIVbacks generated from all donations made in GIVbacks round 30 and 31 from that user.

### For existing users you refer

You will earn 50% of the GIVbacks that would have been allocated to that user for a period of 24 hours from when that user clicks on your referral link. For example, if a returning user clicks on your referral link at 9am, you will be entitled to 50% of all GIVbacks generated from all donations made by that user until 9am the following day (24 hours).
---
id: regenFarmContracts
title: Regen Farm Smart Contract Guide
slug: dapps/regenFarmContracts
---


GIVeconomy is a collection of audited smart contracts which work together to provide capabilities, including: token streaming, airdropping, and various types of farming. Contracts and scripts can be found at the **Giveth** [giv-token-contracts](https://github.com/Giveth/giv-token-contracts) repository.

## Contracts
### Streaming
The streaming allows any rewards (e.g. airdrop, liquidity mining reward, ...) to be released gradually across a given time span instead of the whole sum moving immediately to the end user's wallet. To achieve that, every reward payment to users will be an `allocate` on stream instead of a traditional `transfer/safeTransfer`.

Each instance of a **Stream** is deployed with these configuration parameters:

* **Total Tokens:** Total amount of tokens that will be distributed over the stream period
* **Start Time:** The time stamp that the stream begins
* **Duration:** Total duration of the stream. At the end of stream 100% of tokens are released and can be claimed by recipients.
* **Cliff Period:** The length of an initial period after the start of the stream. During this period, only the intitial percentage of the stream can be claimed and not more.
* **Initial Percentage:** The percentage of immediately claimable rewards during the *Cliff Period*  


The **TokenDistro** is the smart contract which has implemented the streaming feature.  Any eligible smart contract or eligible user can call `allocate` method on the **TokenDistro** to add to the recipient's balance of their stream. Eligible contracts or users who can call `allocate` should have the **DISTRIBUTOR** role for the **TokenDistro** smart contract. They are called **Distributors**. Each Distributor has a balance that they can distribute. Therefore, on each allocation the allocated amount sent is decreased from the distributor's balance and is added to recipient's balance.

A percentage of the allocated amount is claimable immediately, and the remaining percent goes into increasing recipient's stream flowrate. The flowrate is an expression of how many tokens become claimable from their stream over a weekly period. Over time, a greater percentage of the recipient's balance will be claimable immediately following the continued expansion of the stream.


### Air Drop

The initial token distribution can be done by the **MerkleDistro** smart contract. It utilizes *Merkle Tree* theory and each eligible recipient should provide its own unique proof data to claim their air drop. The air drop value actually will be allocated by calling `allocate` on **TokenDistro** and will be added to user's stream balance.

Each instance of **MerkleDistro** is deployed with these configuration parameters:

* **Merkle Tree Root:** The key of the merkle tree root (read blow).
* **Token Distro Address:** The address of the deployed TokenDistro instance.

In order to deploy the **MerkleDistro** smart contract, the deployer must generate a merkle tree. The value of root will be used on the smart contract at deployment time, and the whole tree data is needed to obtain each user unique path to root. In [giv-token-contracts](https://github.com/Giveth/giv-token-contracts) repo, there is a script to generate merkle tree data.
```
ts-node scripts/generate-merkle-root.ts --input <airdrop json file path> --output <output file path>
```

A JSON format of the airdrop data is not easy to generate for everyone, an `airdrop json file` can be generated by a separate script from a CSV file, which is a more convenient format.
```
ts-node scripts/csv2json.ts <airdrop csv list path> <airdrop json file path>
```

### Farming

Giveth uses the **UnipoolTokenDistro**, a derivative of the *Unipool* smart contract, for farming purposes. The difference is that **UnipoolTokenDistro** pays stakers' rewards by calling `allocate` method on the *TokenDistro(stream)* instead of transferring real tokens to the recipient's address.

Generally, the Unipool contract rewards stakers based on the liquidity they have staked. The liquidity token is named `uni` deposited by stakers, and can be any token such as native token (e.g. GIV, FOX, ...)  or a LP token obtained by staking in a pool (e.g. UniswapV2, SushiSwap, HoneySwap, ...).

The Unipool reward amount is set by calling the `notifyRewardAmount(uint256 reward)` method by the **rewardDistribution**. **rewardDistribution** can be set by the **owner** role and in the deployment script, deployer set its own address as **rewardDistribution** by default. Each time this method is called, the Unipool will set to disperse rewards in the `duration` length period to stakers. Therefore, the reward distributor need to regularly call `notifyRewardAmount` to keep a positive reward rate, and adjust the reward rate as it can be different on each round.
Each instance of the **UnipoolTokenDistro** is deployed with these configuration parameters:

* **TokenDistro Address:** The address of deployed TokenDistro instance.
* **Uni Token Address:** The liquidity token address
* **Duration:** Each rewarding program round length


## Deployment
Deployment of a stream with farms and an airdrop is complicated and would be error prone to be done manually. Therefore, [giv-token-contracts](https://github.com/Giveth/giv-token-contracts) has scripts to make it easier. Most of these scripts are tailored for GIVeconomy use cases.

However, a script is ready for DAOs to deploy their own stream (tokenDistro) and farming programs (Unipools). The script can be found in the path `deployments/regenFarms/1_regenFarm.ts`. The script reads the deployment configuration from `deployments/regenFarms/config.ts` file. The configuration format in `config.ts` is as below:
```
const config: IRegenConfig = {
    alreadyDeployedTokenDistroAddress: "",
    newTokenDistroParams: {
        startTime: <start time timestamp>
        cliffPeriod: <cliff time duration seconds>
        duration: <duration seconds>
        initialPercentage: <percentage number, like 20_00>, // two decimals of precision, 20_00 means 20%
        tokenAddress: <Reward token address>
        totalTokens: <Total number of tokens to distribute limit>, // In ether format
        cancelable: <boolean>, // whether admins can cancel an allocation
    },
    unipools: {
        <Key>: {
            uniTokenAddress: <unit token address>,
            lmDuration: <unipool reward round duration seconds>
            rewardAmount: <Unipool balance on token distro>, // Number of tokens it can allocate
        },
        ...
    },
};
```

To deploy via script these environmental variables should be set:
* **INFURA_PROJECT_ID:** When the network is not xDai (Gnosis-Chain)
* **PRIVATE_KEY:** The private key of deployer account, used when network is not xDAI (Gnosis-Chain)
* **PRIVATE_KEY_XDAI:** The private key of deployer account, used when network is xDAI (Gnosis-Chain)


The script can be run by this command
```
HARDHAT_NETWORK=<network e.g. xDAI, mainnet, kovan> ts-node deployments/regenFarms/1_regenFarm.ts
```
---
id: regenFarms
title: Regen Farms
---
import useBaseUrl from '@docusaurus/useBaseUrl';


[RegenFarms](https://giveth.io/givfarm) is the next generation of ReFi liquidity mining opportunities for DAOs and regens alike. Using our contracts for the [GIVfarm](https://giveth.io/givfarm) and the [GIVstream](https://giveth.io/givstream), we are empowering other for-good DAOs to launch liquidity mining incentive programs, “RegenFarms”, with streams of their own.

## Background
Utilizing the [GIVstream](https://docs.giveth.io/giveconomy/givstream), all rewards earned in the [GIVfarm](https://giveth.io/givfarm) (until December 23, 2026) include some part liquid and some part streaming. This allows the GIVfarm to offer high APRs without creating excessive sell pressure. Thanks to the GIVstream, Giveth has pioneered an elegant evolution to traditional liquidity mining that offers lucrative rewards while attracting and rewarding long-term hodlers, and keeping participants invested in the project for years to come.

## For Interested DAOs
We are now offering this technology [as a service](https://forum.giveth.io/t/crazy-idea-stream-as-a-service-giviverse-multiverse-now-called-regenfarms/295) to other [Blockchain4Good](https://twitter.com/search?q=%23blockchain4good&src=typed_query) DAOs! Interested DAOs must be able to prove that they are a “Regen Economy”, i.e., are creating a positive impact for society such as by supporting or building public goods in some way. **If your DAO is interested in applying to kickstart a RegenFarm, [fill out this form](https://giveth.typeform.com/regenfarms).**
We use [snapshot](https://snapshot.org/#/giv.eth/) to get approval from GIV token holders before accepting a new DAO for RegenFarms. Once accepted, the interested DAO will need to work with our team to provide their RegenFarm [parameters](https://www.notion.so/giveth/Regen-Farm-Parameters-a5b474e75f334d03ad1c1c43f5d923d4) and the funds to kickstart their farm.

## Funding
To justify the cost of initiating the farm, a base fee of $5000 (equivalent USD value in the DAO’s token) is provided by the RegenFarm DAO to Giveth. $2500 of this will be sent to donation.eth for the [Giveth Matching Pool](https://giveth.io/project/donation-eth) to fund donations to verified for-good projects. The remaining $2500 will be sent to the [Giveth liquidity multisig](https://blockscout.com/xdai/mainnet/address/0xf924fF0f192f0c7c073161e0d62CE7635114e74f/transactions) and will be used by Giveth provide $GIV / [DAO token] liquidity.

RegenFarm DAOs also provide the funds to reward their Liquidity Providers. Before initiating the farm, 1% of these funds are sent to the [Giveth liquidity multisig](https://blockscout.com/xdai/mainnet/address/0xf924fF0f192f0c7c073161e0d62CE7635114e74f/transactions) to be used, as above, for liquidity, and an additional 1% of these funds are sent to the [Giveth Matching Pool](https://giveth.io/project/donation-eth) to fund donations to verified projects.

## RegenFarms UI

<img alt='shapeshift' src={useBaseUrl('img/Regenfarm1.png')} />

Liquidity mining opportunities for RegenFarms can be found on the [GIVfarm page](https://giveth.io/givfarm). You can provide liquidity (by following the `provide liquidity` link at the bottom of the card) and stake LP tokens to begin earning rewards. When you "harvest" your earnings, the liquid part will be sent to your wallet, and the streaming part will kickstart your corresponding RegenStream. Liquid rewards earned from your RegenStream are claimable at the bottom right. Note that when you harvest rewards from the RegenFarm card, all liquid rewards from your RegenStream are also sent to your wallet.

<img alt='foxfarm' src={useBaseUrl('img/Regenfarm2.png')} />

To learn more about the RegenFarm's mission, click the `?` in the top right corner of the Regen Farm Card.

---

[Our mission](https://docs.giveth.io/whatisgiveth/) at Giveth is to reward and empower those who give. RegenFarms is creating win-win opportunities for everyone who interacts with them. To summarize the benefits:

- Blockchain4good DAOs benefit from the ready-made UI, network effects of offering incentives among other Regen Economies, and the novel benefits of combining rewards with a streaming service.
- Stakers benefit from high yields and a wealth of farming opportunities, as well as the opportunity to explore for-good web3 projects.
- Verified projects benefit from boosted Giveth Matching Pool contributions, courtesy of for-good DAOs.
- The GIVeconomy benefits from additional liquidity and strengthened partnerships in the Blockchain4Good ecosystem.

Explore [RegenFarms](https://giveth.io/givfarm) today.
---
id: technicalWhitePaper
title: Technical White Paper
slug: technicalWhitePaper
---
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


The purpose of our technology is to give cryptocurrency users the ability to donate effortlessly to Campaigns focused on making the world a better place. They can use the Giveth platform to find those Campaigns and donate directly, or they can pledge their crypto to a cause and have a Delegate choose an appropriate Campaign or Trace for them. As an alternative to traditional donation systems, our ***Liquid Pledging*** contract allows Givers to take back their pledge if they disagree with how their donations were allocated. This can only occur before it has been locked into a Campaign for a specific purpose.

#### To make this new way of giving possible, we have to overcome a few challenges:

**1.** How to offer a means for Givers to donate without losing ownership of their funds.
**2.** How to allow third parties to distribute these crypto donations to individuals who can use them effectively.
**3.** How to securely transfer ownership to the individuals who are making the world a better place.
**4.** How to determine whether ownership of distributed Ethereum tokens should be transferred or not. In other words: How to be sure a recipient deserves the donated crypto before we transfer it.

#### Challenge #1 - Donate without losing ownership
This is handled by our [vault](https://github.com/Giveth/vaultcontract) contract. This is a solidity smart contract that can safely store crypto on behalf of the cryptocurrency’s owner. This is how and why a Giver may control or take back their donations. When a giver donates cryptocurrency through Giveth, the coins are actually stored in a vault with the Giver as the owner.

Once stored in the vault, the cryptocurrency is held in place and cannot be moved further without the owner's permission.

#### Challenge #2 - Distribute collected funds
 Our [Minime](https://github.com/Giveth/minime) contract partly handles this challenge. This is a solidity smart contract that can represent Ether and ERC-20's with replica tokens.

Instead of transferring actual Ethereum tokens to individuals for their efforts to do good, we can distribute Minime tokens with the assurance that the real crypto is stored in the vault. Minime tokens are used by a number of well-known projects in the Ethereum space.

Our Giveth TRACE uses another strategy for flexible transfers. [***Liquid Pledging***](https://github.com/Giveth/liquidpledging) is a solidity smart contract that allows us to redistribute Ether in a myriad of networked permutations (aka a graph). It's a bit like liquid democracy, but there is no voting (unless you add that as a plugin).

At its core, Liquid Pledging maintains a list of Ethereum token transfers and owners. These two lists serve as the data structure for the graph. The contract's API provides the means to donate, delegate, and transfer Ethereum tokens stored in the vault.

#### Challenge #3 - Transfer ownership
Once again, this is resolved by our [vault](https://github.com/Giveth/vaultcontract) contract. Ethereum tokens are only ever released to addresses whitelisted with the permission of the original donor. In order to fully meet the requirements of challenge #3, we must set some sort of approval process.

#### Challenge #4 - Determine if transfer should occur
The rules for how transfers are approved are handled by liquid-pledging plugins (lpp). These plugins are separate contracts referenced by the Liquid Pledging contract (*see challenge #2*).

For example, you could use our [lpp-milestone](https://github.com/Giveth/lpp-milestone) plugin to require reviewer approval as a condition to releasing Ether from its original donor. In this case, the reviewer is another Ethereum address. If 'acceptMilestone' is called from this approved reviewer address, then the ownership of donated Ether can be released to the Trace (formerly Milestone) recipient's address.

You don’t have to use our lpp-milestone plugin. You can make your own with whatever you want. Use a contract that mandates the rules you need for your community.

This concludes the Giveth TRACE Technical White Paper for now. Reach out to us on [Discord](https://discord.gg/qf7XZ48gCU) if you have something you want to do with the ideas listed. We are an open-source project, and it is our mission to help communities.
---
id: termsForProposals
title: Terms & Conditions for Submitting or Challenging a Proposal
slug: giveconomy/termsForProposals
---

### 1. **ACCEPTANCE OF TERMS**

These Terms & Conditions constitute an agreement between the Proposal Creator or the Challenger (both may be referred to as “You” in terms and conditions that are applicable for both individualsand Giveth (“We” or “Giveth”), which resides on the Gnosis Chain (formerly xDAI network), regarding either the submission of or challenging a Proposal to Giveth in the GIVgarden.

“Proposal Creator” is any individual who submits a Proposal to GIVgarden for Conviction Voting, while “Challenger” is anyone who disputes or challenges a submitted Proposal to GIVarden.

“Proposal” means any project requesting funding for creating and coordinating value for society at large submitted to the [GIVgarden](https://gardens.1hive.org/#/xdai/garde0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98) via our Conviction Voting System.

By accessing and using the GIVgarden, you accept and agree to be bound by these Terms & Conditions and all applicable laws of your jurisdiction and all of it as it may be modified, changedsupplemented or updated from time to time. Please read these Terms & Conditions (“Terms”) before submitting or challenging a Proposal in the GIVgarden.

If you do not agree with the Terms, you shall not submit or challenge a Proposal in the GIVgarden.

### 2. **MODIFICATIONS OF TERMS OF USE**

The Giveth community reserves the right, at its sole discretion, to modify or replace these Terms & Conditions at any time. The most current version of these Terms will be posted on our [docs](https://docs.giveth.io/). You shall be responsible for reviewing and becoming familiar with any such modifications. Submission of or disputing Proposals after any modification to the Term constitutes your acceptance of the Terms & Conditions as modified. To participate in the GIVgarden you are assumed to have read and accepted these Terms.

### 3. **ELIGIBILITY**

As a Proposal Creator or Challenger, you represent and warrant that you: (a) are of legal age to form a binding contract; (b) have not previously been suspended or removed from using the GIVgarden and (c) have full power and authority to enter into this agreement and in doing so will not violate any other agreement to which you are a party.

By submitting or challenging a Proposal, you represent and warrant that you will not submit or challenge a Proposal if the laws applicable to you due to your country of residency and/or citizenshi prohibit you from doing so in accordance with these Terms.

Pursuant to applicable laws and regulations, the Giveth community maintains the right to select its markets and jurisdictions to operate and may restrict or deny Proposal submission/disputes fro certain countries at its discretion.

**US residents or those domiciled in the US are prohibited from using the Site.** Further, residents or domiciliaries of any country embargoed or restricted by Alderney may not use this Site including, Belarus, Burundi, Central African Republic, Congo, DPRK (North Korea), Guinea, Guinea-Bissau, Iran, Iraq, Lebanon, Libya, Mali, Myanmar(Burma), Republic of South Sudan, Somalia, Sudan Syria, Ukraine, Venezuela, Yemen, Zimbabwe.

### 4. **PROPOSAL GUIDELINES**

All proposals are bound by the [Giveth Covenant](https://gardens.1hive.org/https://docs.giveth.io/whatisgiveth/covenant/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98/covenant). If you haven't taken the time to read through it yet, please make sure you do so. To participate in Giveth you are assumed to have read, understood and agreed to be bound by the Giveth Covenant.  

Before submitting a Proposal, the Proposal Creator must first create a post on the [Giveth Forum](https://forum.giveth.io/). This post should explain why the Proposal is beneficial to the community and (if applicable) what the requested funds will be used for. Only submitted Proposals linked to a post in the Forum are subject to Conviction Voting.

### 5. **DEPOSIT AND OTHER FEES**

1. **“Deposit Manager”**-  The Proposal Creator or the Challenger will be required to add Giveth tokens (GIV) into the GIVgarden’s [Deposit Manager](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98/collateral) before submitting or challenging a Proposal. The Giveth tokens in the Deposit Manager can be withdrawn at any time, as long as they are not actively being used as collateral for a “Proposal Deposit” or “Challenge Deposit”.
2. **“Proposal Deposit”** - When the Proposal Creator makes a Proposal, an amount of GIVs previously deposited in the Deposit Manager will be used as the collateral while the Proposal is being voted on to attest that the Proposal is aligned with [Giveth Covenant](https://docs.giveth.io/whatisgiveth/covenant/). This collateral is referred to as the Proposal Deposit.
3. “**Challenge Deposit”**- When the Challenger disputes a Proposal, the Challenger is required to stake some tokens as collateral. This amount is taken from the tokens the Challenger already deposited using the Deposit Manager. Backing challenges with collateral helps to ensure they have some amount of seriousness behind them. The Challenge Deposit can be forfeited in case the [Celeste Keepers](https://1hive.gitbook.io/celeste/key-concepts#keepers) rule against the Challenger, if the Proposal was [raised to Celeste](https://1hive.gitbook.io/gardens/actions-for-community-members/disputes/raise-to-celeste).

:::info
[**Celeste**](https://1hive.gitbook.io/celeste/) is a decentralized court of DAOs built by [1hive](https://wiki.1hive.org/). It allows for challenged and disputed proposals to be flagged and brought to the consideration of a randomized group of jurors, called “Celeste Keepers”. This ensures that contentious proposals are not able to be passed without due process.
:::
4. **“Settlement Offer”** -  In case the Proposal is challenged, the Proposal Creator has a set amount of time, called the “[Settlement Period](https://1hive.gitbook.io/gardens/actions-for-community-members/disputes/settle-a-proposal#what-is-the-settlement-period)”, either to dispute the challenge by [raising the issue to Celeste](https://1hive.gitbook.io/gardens/actions-for-community-members/disputes/raise-to-celeste) or to resolve the challenge by paying the Settlement Offer and taking down the Proposal. The Settlement Offer will define an amount of the Proposal Deposit that will be sent to the Challenger if the Proposal is not taken to Celeste. If the Proposal Creator does not take action before the end of the Settlement Period, the Proposal is automatically considered “settled”, is removed from the voting interface, and the Proposal Creator gets back the Proposal Deposit minus the Settlement Offer.  \

5. **“Gas Fees”** -  All Proposals are subject to varying gas fees required by the Gnosis Chain to carry out transactions. “Gas Fees” refers to the cost necessary to perform a transaction on the network. Gas Fees are set by the user at the time of transaction and are dependent on supply and demand for the computational power of the network needed to process smart contracts and other transactions on the network, therefore, Giveth shall not have any liability for the determination of Gas Fees, nor does it receive any compensation related to them.

### 6. **DISPUTABILITY**

A dispute can be created by another community member (the Challenger) by challenging the Proposal and committing GIVs and HNY (1Hive’s token honey) to support the dispute.

If after being challenged, the Proposal Creator agrees to pay the Challenger the Settlement Offer and withdraw the Proposal, the Proposal Deposit will be returned to the Proposal Creator minus the Settlement Offer.

If after being challenged and the Proposal Creator fails to take any action before the Settlement Period ends, the Challenger’s dispute is considered valid and the Proposal Creator will be considered to have accepted the Settlement Offer. The Proposal is withdrawn and the Proposal Deposit will be returned to the Proposal Creator minus the Settlement Offer.

If after being challenged and the Proposal Creator decides to counter-challenge the dispute by staking HNY, [Celeste](https://1hive.gitbook.io/celeste/) will be used to settle the dispute while the Proposal Creator retains the right to appeal that decision. If the Celeste Keepers would rule in favor of the Proposal Creator, the Proposal Creator can be rewarded the Challenger’s Deposit.

Celeste Keepers are expected to review all disputed Proposals, the Giveth Covenant, evidence submitted by the Proposal Creator and Challenger, and related past disputes in order to provide a judgment that they feel best aligns with the established norms and intention of the Giveth community.

### 7. **PARTNERSHIPS**

Each Proposal Creator and Challenger acknowledges and agrees that these Terms do not constitute a partnership agreement  of any kind. Despite this, in the event that a court or tribunal determines any aspect of these Terms is found to constitute or cause a partnership to arise, you hereby waive any rights against each other partner in respect of the released Claims howsoever arising, including any obligation to account or account for any profit or loss or any other cause of action that a partner would have against another partner in the context of a partnership.

Each Proposal Creator and Challenger acts independently from Giveth, acknowledges and agrees that these Terms do not constitute any form of joint venture, employment relationship or partnership agreement of any kind. Despite this, in the event that a court or tribunal determines any aspect of these Terms is found to constitute or cause a partnership to arise, you hereby waive any rights against each other partner in respect of the released Claims howsoever arising, including any obligation to account or account for any profit or loss or any other cause of action that a partner would have against another partner in the context of a partnership.

### 8. **PLATFORM SECURITY**

Gnosis Chain, on which the GIVgarden resides, is provided on an “as is” basis. You acknowledge and agree that using the Gnosis Chain or submitting/challenging a Proposal is at your own discretion and risk and that you assume full responsibility for use of the Gnosis Chain.

Giveth disclaims all warranties of any kind, expressed or implied, including, but not limited to, the warranties of merchantability, fitness for a particular purpose, and non-infringement. You understand and agree that Giveth doesn’t warrant: (i) that any information provided by you is complete, accurate, or useful; (ii) that the Gnosis Chain will be operational or free from failures, disruptions, errors, or delays, including without limitation processing any kind of activity; (iv) that the Gnosis Chain will be secure, safe, or free from viruses or other malicious code being introduced; (v) that third parties may obtain unauthorized access to information stored in the Gnosis Chain, such as your wallet address, private key, seed phrase, or personal data.

You acknowledge and accept that Giveth has no control over and has no duty to take any action: (i) regarding failure of hardware, software, or Internet connections; (ii) regarding changes to or errors in the Gnosis Chain; (iii) regarding risks related to cryptographic and cryptoeconomic systems, virtual currencies, tokens, such as change in transaction costs; (iv) regarding legal or regulatory risk, inquiry, or action; (v) regarding third-party content accessed through the Gnosis Chain.

### 9. **DISSOLUTION**

The GIVgarden can be dissolved in various ways by a Giveth token holder vote. If this happens, the Proposals to the GIVgarden will be considered null and void.

### 10. **NO THIRD PARTY RIGHTS**

You agree that, except as otherwise expressly provided in these Terms, there shall be no third-party beneficiaries to the Terms. The Terms & Conditions will not be construed as creating or implying any relationship of agency, franchise, partnership, or joint venture between you and Giveth, except and solely to the extent expressly stated in these Terms.

### 11. **GENERAL RISKS**

You are fully aware of, understand and agree to assume all the risks (including direct, indirect or ancillary risks) associated with participating in Giveth including:

* **11.1** THE NECESSITY FOR YOU TO TAKE YOUR OWN SECURITY MEASURES FOR THE ADDRESS USED TO PARTICIPATE TO AVOID A LOSS OF ACCESS: Giveth does not provide any central entity that can store or restore the access data of Giveth Proposal Creators and Challengers. You need to keep your private keys, seed phrases or other credentials necessary to access your public address in safe custody.

* **11.2.** THE IMMUTABILITY AND IRREVERSIBILITY OF GNOSIS TRANSACTIONS: Errors, false inputs or other errors are solely the responsibility of each individual Giveth Proposal Creator and Challenger. Neither Giveth nor any of its affiliates and service providers, and each of their respective community members shall have an obligation whatsoever to reverse or assist to reverse any false transaction.

* **11.3.** REMAINING SMART CONTRACT RISKS: DESPITE SECURITY AUDITS, THERE MAY BE VULNERABILITIES IN THE DEPLOYED SMART CONTRACTS: You may experience damage or loss (including financial loss) caused by the existence, identification and/or exploitation of these vulnerabilities through hacks, mining attacks (including double-spend attacks, majority mining power attacks and “selfish-mining” attacks), sophisticated cyber-attacks, distributed denials of service or other security breaches, attacks or deficiencies.

* **11.4.** THE POTENTIAL EXISTENCE OF PHISHING WEBSITES WHICH PRETEND TO BE A Giveth INTERFACE DUE TO MINIMAL VARIATIONS IN SPELLING: It is your obligation to carefully check that you are accessing the correct domain.

* **11.5.** CONSTANT AND DYNAMIC REGULATORY DEVELOPMENTS WITH REGARD TO CRYPTO ASSETS: Applicable laws may be uncertain and/or subject to clarification, implementation or change.

* **11.6.** TRANSPARENCY OF TRANSACTIONS: Without the use of privacy-protecting systems, blockchain transactions are traceable on-chain. By using cryptanalysis methods, conclusions can be drawn about further on-chain transactions and, regularly, associations to real-world identities can be made.

### 12. **INTERNATIONAL USERS**

The Smart Contract System is controlled, operated and administered by Giveth from Alderney and is not intended to subject Giveth to the laws or jurisdiction of any state, country or territory other than that of the Alderney. Giveth does not represent or warrant that the Smart Contract System or any part thereof is appropriate or available for use in any particular jurisdiction other than Alderney. Those who choose to access the Smart Contract System do so on their own initiative and at their own risk, and are responsible for complying with all local statutes, orders, regulations, rules, and other laws. You are also subject to Alderney export controls and are responsible for any violations of such controls, including without limitation any Alderney embargoes or other federal rules and regulations restricting exports. Giveth may limit the Smart Contract System’s availability, in whole or in part, to any person, geographic area or jurisdiction we choose, at any time and in our sole discretion.

### 13. **INDEMNITY**

You agree, to the fullest extent permitted by applicable law, to release and to indemnify, defend and hold harmless Giveth and its parents, subsidiaries, affiliates and agencies, as well as the officers, directors, employees, shareholders and representatives of any of the foregoing entities, from and against any and all losses, liabilities, expenses, damages, costs (including attorneys’ fees and court costs) claims or actions of any kind whatsoever arising or resulting from: (a) your participation in Giveth or the GIVgarden, (b) your violation of these Terms & Conditions, (c) any of your acts or omissions that implicate publicity rights, defamation, invasion of privacy, confidentiality, intellectual property rights or other property rights, (d) any misrepresentation by you and (e) any disputes or issues between you and any third party. Giveth reserves the right, at its own expense, to assume exclusive defense and control of any matter otherwise subject to indemnification by you and, in such case, you agree to cooperate with Giveth  in the defense of such matter.


### 14. **LIMITATION ON LIABILITY**

You understand and agree that, to the fullest extent permitted by applicable law, neither Giveth nor its subsidiaries, affiliates and agencies, as well as its Stewards, members, stakeholders or representatives of any of the foregoing entities will be liable to you for any direct, indirect, incidental, special, consequential, punitive, exemplary or other damages of any kind, including, but not limited to, damages for loss of profits, goodwill, use, data or other tangible or intangible losses or any other damages based on contract, tort (including, in jurisdictions where permitted, negligence and gross negligence), strict liability or any other theory (even if Giveth had been advised of the possibility of such damages), resulting from the site or service; the use or the inability to use the site or service; unauthorized access to or alteration of your transmissions or data; statements or conduct of any third party on the site or service; any actions we take or fail to take as a result of communications you send to us; human errors; technical malfunctions; failures, including public utility or telephone outages; omissions, interruptions, latency, deletions or defects of any device or network, providers, or software (including, but not limited to, those that do not permit participation in the service); any injury or damage to computer equipment; inability to fully access the site or service or any other website; theft, tampering, destruction, or unauthorized access to, images or other content of any kind; data that is processed late or incorrectly or is incomplete or lost; typographical, printing or other errors, or any combination thereof; or any other matter relating to the site or service.


### 15. **PUBLICITY**

You agree not to issue any press release or otherwise make any public announcement related to the participation and transactions contemplated in the Conviction Voting System without the prior written approval of Giveth.
---
id: testingGIVeconomy
title: GIVeconomy Testing Guidelines
slug: dapps/testingGIVeconomy
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import styles from '../src/css/custom.css';


This is a guide for thorough user testing scenarios for the GIVeconomy DApp. Testing should be done on the staging server which can be found at https://staging.giveth.io/.


## Requirements

* Please use a modern browser. If you encounter a bug, please try the same thing with another browser. Please make an issue in any case, but tell us if the issue might be browser specific
* Use issues in [GitHub](https://github.com/Giveth/GIVeconomy/issues) for reports and feedback.

## Use Cases

The following actions are defined as core functionality. If one of these steps is buggy, that represents a critical error.

### General

- Buttons on "Overview" page are responsive
- Tabs `GIVgarden`, `GIVfarm`, etc.. are responsive
- Navbar Header buttons are responsive
- Can successfully sign in on Navbar with Web Wallet (currently optimized for MetaMask)
- Footer links are working and link correctly


### GIVgarden
The GIVgarden staging deployment uses both Kovan Network and Gnosis Chain (formerly xDai Network). The token used for this deployment is *DRGIV3*.

:::info
DRGIV3 can be wrapped in the [DRGIV3 Garden](https://gardens-staging.1hive.org/#/xdai/garden/0x16388d99199a74810fc572049b3d4d657e7d5deb) to receive gDRGIV3. This is the same action as staking your DRGIV3 in the GIVgarden Staking in the GIVfarm on Gnosis Chain.
:::  

- Buttons linking to GIVgarden are working
- `LEARN MORE` links are working
- Wrap DRGIV3 on the GIVgarden - Check that your Token amount updates on the GIVgarden Staking in the GIVfarm on Gnosis Chain.
- Unwrap DRGIV3 on the GIVgarden - Check that your Token amount updates on the GIVgarden Staking in the GIVfarm on Gnosis Chain.


### GIVfarm
The GIVfarm staging deployment uses both Gnosis Chain and Kovan (Mainnet) Network. The token used for this deployment is *DRGIV3*:
- `0x83a8eea6427985C523a0c4d9d3E62C051B6580d3` on Gnosis Chain
- `0x29434a25abd94ae882aa883eea81585aaa5b078d` on Kovan

Test tokens used for providing liquidity on Gnosis Chain are as follow:
- Gnosis Chain TestHNY: `0x69F79C9eA174d4659B18c7993c7EFbBbB58cF068`
- Gnosis Chain TestWETH:`0x736a98655049433f79dCcF5e54b887E8890b63D1`  

On Kovan, regular Kovan ETH is used for providing liquidity and paying gas.
<Tabs className='tabs'>
  <TabItem value='gnosis' label='Gnosis Chain' default>
<h3>Gnosis Chain (formerly xDai Network) Test Cases</h3>
<ul>
<li>Gnosis Chain/Ethereum Network toggle works</li>
<li><code>?</code> hover tooltips work</li>
<li>Provide Liquidity with DRGIV3 & TestHoney on Honeyswap</li>
<li>Provide Liquidity with DRGIV3 and TestETH on Sushiswap</li>
<li>Can stake LP tokens in respective GIV/HNY or GIV/ETH farms - LP Token amounts to Stake/Unstake update on UI</li>
<li>Can stake DRGIV3 in GIVgarden Staking - Token amounts to Stake/Unstake update on UI</li>
<li>After staking DRGIV3, check wrapped token amount (gDRGIV3) amount updates on the <a href='https://gardens-staging.1hive.org/#/xdai/garden/0x16388d99199a74810fc572049b3d4d657e7d5deb' target='_blank' alt='DRGIV3 Garden'>DRGIV3 Garden</a></li>
<li>APR is displaying correctly (if it shows 0% that's bad)</li>
<li>Clicking `?` on APR row opens APR modal, links are functional in modal</li>
<li>Claimable amount updates over time</li>
<li>Streaming amount is shown (up to 2 decimal places)</li>
<li>If the amount is very small  <code>0.0001</code> is shown</li>
<li>"Your GIVfarm Rewards" (top right of page) displays correctly total pending rewards from all farms combined.</li>
<li>Harvesting from each farm - Transactions are successful and Claimable, Streaming, and GIV in wallet amounts update correctly</li>
<li>Can Unstake Tokens from all farms - Token amounts to Stake/Unstake update on UI</li>
<li>After unstaking DRGIV3 from the GIVgarden farm, check wrapped token amount (gDRGIV3) amount updates on the <a href='https://gardens-staging.1hive.org/#/xdai/garden/0x16388d99199a74810fc572049b3d4d657e7d5deb' target='_blank' alt='DRGIV3 Garden'>DRGIV3 Garden</a></li>
</ul>
  </TabItem>
  <TabItem value='kovan' label='Kovan Testnet' default>
<h3>Kovan (mainnet) Network Test Cases</h3>
<ul>
<li>Gnosis Chain/Ethereum Network toggle works</li>
<li><code>?</code> hover tooltips work</li>
<li>Mint Univ3 NFT with DRGIV3 & ETH on Uniswap (Kovan)</li>
<li>Provide Liquidity with DRGIV3 and WETH on Balancer (Kovan)</li>
<li>Can stake Univ3 NFT in GIV/ETH Uniswap farm - NFT amount updates below Stake/Unstake buttons</li>
<li>Can stake LP tokens in GIV/ETH Balancer farm - LP Token amounts to Stake/Unstake update on UI</li>
<li>Can stake DRGIV3 in Single Asset Staking - Token amounts to Stake/Unstake update on UI</li>
<li>APR is displaying correctly (if it shows 0% that's bad)</li>
<li>Clicking <code>?</code> on APR row opens APR modal, links are functional in modal</li>
<li>Claimable amount updates over time</li>
<li>Streaming amount is shown (up to 2 decimal places)</li>
<li>Your GIVfarm Rewards" (top right of page) displays correctly total pending rewards from all farms combined.</li>
<li>Harvesting from each farm - Transactions are successful and Claimable, Streaming, and GIV in wallet amounts update correctly</li>
<li>Can Unstake Tokens from all farms - Token amounts to Stake/Unstake update on UI</li>
</ul>
  </TabItem>
</Tabs>

## GIVbacks

To learn how to create a test GIVback distribution, contact a Developer or mitch (divine_comedian#5493) on Discord to help you.

You'll have to make a legitimate donation to a verified project on Giveth.io in order to test GIVbacks with your own Ethereum Address.

 Once you have executed a test distribution you can verify a few pieces of the `GIVbacks` page:

:::info
GIVbacks are only available on Gnosis Chain (formerly xDai Network).
:::

- Verify your GIVbacks Reward amount, checking that the calculations align with the donations you made to a verified project during your defined GIVbacks period.
- Your GIVbacks claimable amount should be a set amount (not increasing like GIVfarm rewards).
- Your GIVbacks streaming amount should be in the GIVstream history table at the time of GIVbacks distribution.
- Harvest GIVbacks is successful.
- `DONATE` and `VERIFY` buttons work.

## GIVstream
The GIVstream is available on both Gnosis Chain and Kovan. Make sure you have pending farming rewards on both networks to fully test the GIVstream.

-Gnosis Chain/Ethereum Network toggle works
- Buttons for `PROJECTS`, `PROPOSALS`, `OPPORTUNITIES` and `LEARN MORE` work.
- Can Harvest GIVstream rewards in the top right modal on both Gnosis Chain and Kovan.
- `?` image on GIVstream rewards modal shows pop-up when clicked, links and button within modal are functional
- '?' hover tooltips work
- `GIViverse Expansion` displays correctly (if it's 0% that's bad.)
- `Time remaining` shows correctly (GIVstream ends on December 23, 2026)
- GIVstream flowrate increases are shown in the history table. GIVfarm rewards should appear in the table after claiming from the GIVfarm. GIVbacks rewards should appear in the table at the moment of GIVbacks distribution.


---

Don’t forget to participate in the Platform Circle’s weekly meetings to stay in the loop. Read up on our [Development Contributor’s guide](./contributors) for all the information you need to become a regular contributor to Giveth Development & Testing.
---
id: torusonramp
title: Donating with Fiat via the Torus on-ramp
slug: dapps/torusonramp
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

This guide will take you through the steps of donating your fiat currency using Torus. To do so, you'll use a third party payment provider to send your fiat to Torus, which will 'top-up' your Torus wallet with your chosen cryptocurrency. That cryptocurrency that was converted from fiat will then be donated to the project you've selected. There are fees associated with this conversion from Torus as well as the third party provider that you choose. We'll walk you through the steps, but depending on your native currency, the payment provider you use and the crypto you're converting to, things might look a bit different.

Once you’re logged in with your Torus wallet, click “Donate” on the project you’ve selected.

<img id="contentimg" alt='Donating to the Project' src={useBaseUrl('img/content/projectselect.png')} />

A transaction pop-up window will then say, 'Insufficient Funds'. OK, let's fix that.
<img alt='Top up Torus Wallet' src={useBaseUrl('img/content/nofunds.png')} />

Open up your wallet in the Torus app. If you’re asked to log in, make sure to use the same social media account that you used to log in on Giveth.io. From your Torus wallet, click on the `Top up` tab in the top menu.
<img alt='Top up Torus Wallet' src={useBaseUrl('img/content/topup.png')} />

From there you'll get a list of third party payment providers; look through the fees and currencies they support, and choose the best match for you.

<img id="contentimg" alt='Select Payment Provider' src={useBaseUrl('img/content/selectprovider.png')} />

On the following screen, enter the amount of fiat you would like to donate. Note that the estimate of fees will be reflected here and will be dependent upon the payment provider you selected.

<img id="contentimg" alt='Enter fiat amount to donate' src={useBaseUrl('img/content/torusramp.png')} />

Next you'll be redirected to the website of your selected payment provider. Follow the prompts, which will be different depending on which provider you choose.

An example from the Ramp Network:
<img id="contentimg" alt='Ramp Network Example' src={useBaseUrl('img/content/paymentmethod.png')} />

Once you've completed that, you'll be taken back to the Torus top-up window. You should see your funds there.

Now that you have the funds in your wallet, you can go back to your selected project and proceed to donate!

You can follow up to watch the transaction being confirmed on the block explorer by clicking `View transaction details`. From this point your donation should be done! Thank you and well done!
---
id: torusUserGuide
title: Using the Torus Wallet
slug: dapps/torusUserGuide
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'

The Torus wallet is a great option for newcomers to crypto. Using web3 technology it allows you to create an Ethereum wallet that's linked to your identity via your chosen social media platform. With the Torus wallet, you can send and receive cryptocurrencies and buy crypto with fiat currency using the Torus "wallet top-up" option.


## Sign-In
Using the Giveth.io Application, it's very easy to get started. On the homepage click `sign-in`, and you will be given a choice of which platform you want to use to confirm your identity (e.g., Gmail, Twitter, Discord, Facebook, etc.). After choosing your platform, approve the "Permission" pop-up, and that's it! Torus automatically generates an Ethereum wallet address for you that you can view on the drop down menu in the top right of the Giveth.io homepage.

<img alt="Finding your Torus Wallet" src={useBaseUrl('img/content/givethio/myWalletTorus.png')} />


You can access your Torus wallet direcly from the [Torus website](https://app.tor.us/) by signing in using the same social media account that you used on Giveth.io. From the Torus page, you'll see lots of important information, including your wallet balance, your Ethereum address and other useful settings.

*If you aren't sure what an Ethereum wallet or Ethereum address is, this is a good time to take 10 minutes and **learn about some basic fundamentals relating to Ethereum** and cryptocurrency in general. We recommend reading some of the great ethereum.org documentation, particularily on [wallets](https://ethereum.org/en/wallets/) and [what Ethereum is](https://ethereum.org/en/what-is-ethereum/).*

## Managing Your Wallet

From the [Torus page](https://app.tor.us/) you can check your wallet balance across a wide range of different different networks. You can also see your public address, and copy it to your clipboard in the top right area of the page.

<img alt="Torus Account Homepage" src={useBaseUrl('img/content/givethio/torusAccountpage.png')} />

Presently, Giveth projects can receive donations either on Gnosis Chain (formerly xDai Network) or Mainnet. By default, Torus will show you your Mainnet wallet balance. If you received donations on Gnosis Chain, you can check your balance by changing the network on the network drop down menu to Gnosis Chain.

### Finding your Tokens
If you received a donation to your project but it doesn't show up in your Torus wallet, you likely have to specify which token Torus should look for. This is done by adding the token address. Check your project's donations page on Giveth.io to see in which token(s) you've received donations.

<img alt="Checking your Project Donations" src={useBaseUrl('img/content/givethio/projectDonations.png')} />

You can look up the token on several different crypto analytics sites. [CoinGecko](https://www.coingecko.com/en) or [CoinMarketCap](https://coinmarketcap.com/) are reputable sites. Search for your token by its name or ticker symbol, then copy the "Contract Address" from the token's information page. Here is an example for UNI:


<img alt="CoinGecko Contract Address" src={useBaseUrl('img/content/givethio/tokenAddresscoingecko.png')} />



Paste the string of characters into the `Add Token` pop-up window from your Torus account. Clicking `Next` should auto-fill the rest of the information. Your token should now show up, and you can view and manage it from you wallet.

<img alt="Adding Tokens in Torus" height="500"  width="auto" class='center' src={useBaseUrl('img/content/givethio/addTokenTorus.png')} />

### More Functions
If you want to buy crypto using fiat currency, you can do so using the "Top Up" option. We have written a small guide to help you out with the fiat [on-ramping process](./torusonramp.md).

To send crypto you own to another wallet use `Transfer`. You will need Ethereum (ETH) in your wallet to be able to "pay the gas" necessary for your transaction. More on gas [here](https://ethereum.org/en/developers/docs/gas/).



### Interacting with the GIVeconomy

To interact with the [GIVeconomy](https://giveth.io/) and other dApps using the Torus wallet, you will have to connect your wallet. To connect, click the `Connect Wallet` icon in the upper right corner of the site, then select Torus and verify. The Torus wallet allows users to sign in with accounts from many different web services, so be sure to sign in with the same account you used to set up the wallet.

<img alt="Signing in with Torus on the GIVeconomy" width="75%" height="auto" class='center' src={useBaseUrl('img/content/giveconomyTorusConnect.png')} />

If you are using the Brave browser, you will need to turn off Brave’s Shield feature. To do this, click the Brave logo to the right of the search bar, then toggle the Shield to off.

<img alt="Turning shields off with Brave" class='center'  width="50%" height="auto" src={useBaseUrl("img/content/giveconomyShieldsDown.png")} />


### Other Wallets
As mentioned, the Torus wallet is great for beginners. Using familiar social media platforms for managing your identity is a great way to get started. However, if you decide to get serious about crypto, there is a vast array of other wallets out there. Some wallets are easier to integrate with other chains, offer more privacy or allow for more advanced interactions. Some wallets exist as web3 extensions like Torus, others are a physical device, like a hardware wallet that you need to connect to your computer to access and manage your crypto. If you decide to go wallet shopping, you can find a list of the most popular ones [here](https://ethereum.org/en/wallets/find-wallet/).
---
id: makeTraceableProject
title: Getting your project on TRACE
slug: dapps/makeTraceableProject
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


This guide will show you how to make your project traceable. We will go over the steps for first getting your project verified then upgrading it into a Campaign on [Giveth TRACE](https://trace.giveth.io).

**Verified** is a top tier status for projects wishing to join the GIVbacks program and also for project creators looking to expand into a [new suite of tools](https://medium.com/giveth/giveth-trace-is-live-e91b0be1e1f6) that provide their donors with extra ways to give. A project that is Verified can choose to become a [Campaign](/dapps/entitiesAndRoles#campaigns) on [Giveth TRACE](https://trace.giveth.io), enabling project creators to manage their donations transparently using [Traces](/dapps/entitiesAndRoles#traces). Traces specify how the project is using their donations to achieve the goals of the overarching Campaigns.

Upgrading projects to Campaigns enables project creators to specify parts of their project requiring funding as different types of [Traces](/dapps/entitiesAndRoles#traces). Donors benefit from being able to choose to fund either specific Traces or the overarching Campaign and are able to trace the flow of their donations. A Campaign is listed on both Giveth.io and [Giveth TRACE](https://trace.giveth.io) allowing for double exposure!  

## The Process

We have a rigorous, human-handled process for screening projects asking for verification. Before getting started, here are some considerations you should make regarding your project:
 - Do you have any relevant and verifiable social media accounts?
 - How exactly will you use funds received?
 - In what ways can you prove that your project is real?
 - How is your project's organization structured?

Once you've sufficiently pondered the answers to these questions, then the road to verification lies ahead!

### Step 1 - Click the Button!
Go to your project page on Giveth.io, and on the right-hand side click on `Verify your project`.

<img width="400" height="auto" alt="Clicking Verify Project" src={useBaseUrl('img/content/givethio/clickButton.png')} />



### Step 2 - Fill out the Typeform
A typeform page will open up in your browser. Fill out the requested information as accurately as possible. Someone from the Giveth team will be reviewing and verifying this information!

<img width="600" height="auto"  alt="Verification Typeform" src={useBaseUrl('img/content/givethio/verifiedTypeform.png')} />



### Step 3 - Wait for Review
After you've submitted your application, a member of the Giveth Team will review your typeform submission. Hang tight while we verify the information you provided and reach a decision on approving your request.

### Step 4 - Check Your Inbox
You'll receive an email letting you know if your request for verification has been approved or rejected. If you've been approved, follow the directions in the email to continue! If you've been rejected, follow any steps outlined in the email to improve your project and re-apply for verification.

<img width="500" height="auto" alt="Verification Approval Email" src={useBaseUrl('img/content/givethio/verifiedEmail.jpg')} />


### Step 5 - Complete the Migration Wizard
Once your project is verified, you can choose to add it to Giveth TRACE by following the instructions in your email, and entering the project migration wizard. This will handle the process of upgrading your Project to a Campaign. Sign-in with your Web3 wallet and connect to _Rinkeby Network_.

Confirm the information requested on each section of the Wizard, then sign the transaction with your wallet to create your Campaign!

<img width="600" height="auto" alt='Verification Wizard Tool' src={useBaseUrl('img/content/givethio/verifiedWizard.png')} />


### Step 6 -  Magic!
Once you make it to the "Congratulations" page, you can click `GO TO YOUR PROJECT` to visit your new space! Get started by exploring Giveth TRACE's UI, and create some Traces to encourage more donations to your Campaign. To learn more about how Giveth TRACE works, read the [DApp documentation](https://docs.giveth.io/dapps/introTrace).

<img width="600" height="auto" alt="Verification Approval Email" src={useBaseUrl('img/content/givethio/verifiedTraceCampaign.jpg')} />

Enjoy your new Campaign, and let everyone in your social networks know about your upgraded funding portal!
---
id: traceContracts
title: Contracts, Bridges and Multisigs Technical Information
slug: dapps/traceContracts
---
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


## Contracts:
* GivethBridge on Mainnet
* ForeignGivethBridge on Rinkeby
* LiquidPledging contracts on Rinkeby
* Escapable contracts to Mainnet for each contract on Rinkeby


#### Mainnet multisigs:
* [Giveth Mainnet: 0x8f951903c9360345b4e1b536c7f5ae8f88a64e79](https://etherscan.io/address/0x8f951903c9360345b4e1b536c7f5ae8f88a64e79) (6 of 13 multisig)
* [Giveth Overflow: 0x16fda2fcc887dd7ac65c46be144473067cff8654](https://etherscan.io/address/0x16fda2fcc887dd7ac65c46be144473067cff8654) (4 of 7 multisig)
* [EscapeHatch Caller: 0x1e9f6746147e937e8e1c29180e15af0bd5fd64bb](https://etherscan.io/address/0x1e9f6746147e937e8e1c29180e15af0bd5fd64bb) (1 of x multisig)

#### Rinkeby multisigs:
* [EscapeHatch Caller: 0xc3b2128ca330871037d35fdc5f7b05e195aac5ce](https://rinkeby.etherscan.io/address/0xc3b2128ca330871037d35fdc5f7b05e195aac5ce) (1 of x multisig)
* [Dapp God/EscapeHatch Destination: 0x20fc2ec2518dec7041b4c3e82663d6071bae953f](https://rinkeby.etherscan.io/address/0x20fc2ec2518dec7041b4c3e82663d6071bae953f) (3 of 6 multisig)


 ## Contract Roles/params:
### Mainnet
 - [**GivethBridge**: 0x30f938fED5dE6e06a9A7Cd2Ac3517131C317B1E7](https://etherscan.io/address/0x30f938fED5dE6e06a9A7Cd2Ac3517131C317B1E7)
     - Owns the bridge.
     - Receives and deals with donations.
     - Can cancel payments in the bridge.
     - Can pause and unpause the bridge.
     - Add tokens to whitelist.
     - Can change the max security guard delay.
     - Can change the security guard.
     - Can change the 2 day time lock in the bridge.
     - Can change the escape hatch caller.
     - Can remove/change ownership.
     - Can call the `escapeHatch(address _token)` in an emergency to move all the money out of the bridge for the specified token.
     - Can call `escapeFunds(address _token, uint _amount) ` to move some of the money out of the bridge to be extra cautious.
     - Has all the powers needed to decentralize the bridge.
 - [**Giveth Overflow**: 0x16fda2fcc887dd7ac65c46be144473067cff8654](https://etherscan.io/address/0x16fda2fcc887dd7ac65c46be144473067cff8654)
     - Receives overflow/escaped funds from the bridge.
     - Sends funds back to the bridge when funds get low using `depositEscapedFunds()`.
 - [**EscapeHatch Caller**: 0x1e9f6746147e937e8e1c29180e15af0bd5fd64bb](https://etherscan.io/address/0x1e9f6746147e937e8e1c29180e15af0bd5fd64bb)
     -  Can call the `escapeHatch(address _token)` in an emergency to move all the money out of the bridge for the specified token.
     -  Can call `escapeFunds(address _token, uint _amount) ` to move some of the money out of the bridge to be extra cautious.
 - [**SecurityGuard**: 0xDAa172456F5815256831aeE19C8A370a83522871](https://etherscan.io/address/0xDAa172456F5815256831aeE19C8A370a83522871)
     - MaxSecurityGuardDelay:  1 month

### Rinkeby
 - [**ForeignGivethBridge**: 0xfF9CD5140e79377feB23f6DFaF1f8b558C0FE621](https://rinkeby.etherscan.io/address/0xff9cd5140e79377feb23f6dfaf1f8b558c0fe621)
      - Mints tokens on Rinkeby.
      - Can delegate tokens to Liquidpledging.
 - [**EscapeHatch Caller**: 0xc3b2128ca330871037d35fdc5f7b05e195aac5ce](https://rinkeby.etherscan.io/address/0xc3b2128ca330871037d35fdc5f7b05e195aac5ce)
     - In case there is a weird unexpected movement of Rinkeby tokens (which represent our accounting in the bridge), this Multisig would be able to get the tokens out to maintain our accounting.
 - [**Dapp God/EscapeHatch Destination**: 0x20fc2ec2518dec7041b4c3e82663d6071bae953f](https://rinkeby.etherscan.io/address/0x20fc2ec2518dec7041b4c3e82663d6071bae953f)
     - This multisig has a special place in the AragonApp it: authorizes upgrades to any smart contract in our system.
     - Also acts as the escape hatch destination for the Rinkeby LP Vault.
- [**Token Factory:** 0xf3012a211fAcf4a1590086A14482Aaa88397aF15](https://rinkeby.etherscan.io/address/0xf3012a211facf4a1590086a14482aaa88397af15)
    - Mints Minime tokens to be sent to Liquid Pledging.
#### Liquid Pledging Contracts (Rinkeby)
 - [LPVault: 0xA2B1485Bd9ad623b9e51FC41952B226313250Ada](https://rinkeby.etherscan.io/address/0xa2b1485bd9ad623b9e51fc41952b226313250ada)
    - Constructor params: None
 - [LiquidPledging: 0x8eB047585ABeD935a73ba4b9525213F126A0c979](https://rinkeby.etherscan.io/address/0x8eb047585abed935a73ba4b9525213f126a0c979)
    - Constructor params: None
 - [LPPCampaignFactory: 0x71408CE2125b1F07f614b93C8Bd0340e8Fc31CFA](https://rinkeby.etherscan.io/address/0x71408CE2125b1F07f614b93C8Bd0340e8Fc31CFA)
    - Constructor params: 000000000000000000000000a018199569d94c9dfb6de1d8e8cb37928f20d444
 - [milestoneFactoryAddress: 0x8E8d4840568c786E2e4c83C761ca002F256aD9c2](https://rinkeby.etherscan.io/address/0x8e8d4840568c786e2e4c83c761ca002f256ad9c2)
    - Constructor params: 000000000000000000000000a018199569d94c9dfb6de1d8e8cb37928f20d444
 - [LPPCappedMilestoneFactory: 0x19e88e279844f0201079b39c736a94b87b32b6b6](https://rinkeby.etherscan.io/address/0x19e88e279844f0201079b39c736a94b87b32b6b6)
    - Constructor params: 000000000000000000000000a018199569d94c9dfb6de1d8e8cb37928f20d444


**NOTE:** All escapeHatches for liquidPledging contracts (not bridge) have been replaced with the recoveryVault functionality of AragonOS. We will register 1 recoveryVault (Giveth Multisig on Rinkeby) in the kernel and all app will be “escapable” to that vault.

**Wallet Funding Account:** 0xf94230D278b36a29fD1363Bd57D12AEb8b8D426B
---
id: TRACEinstallation
title: Installing Giveth TRACE for Local Development
slug: dapps/TRACEinstallation
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import TraceDeprecated from './_traceDeprecated.mdx'

<TraceDeprecated />


 This is a comprehensive guide that will walk through new contributors on how to run Giveth TRACE locally. We'll be dealing with 2 repos found in the Giveth Github: the [**`giveth-dapp`**](https://github.com/Giveth/giveth-dapp) for the front-end and [**`feathers-giveth`**](https://github.com/Giveth/feathers-giveth) for smart contract interfacing and the back-end database.

## Feathers Installation
<img alt='Feathers Installation Header' src={useBaseUrl('img/content/trace/feathers-header.png')} />

#### Packages and Applications Needed:
- yarn
- NodeJS v10.24.0
- MongoDB
- Redis
- MetaMask


#### Linux
  If your operating system is any distrubution of Linux, you can use the all-in-one installation scripts, special thanks to Dapp contributor Jurek Brisbane, available [here](https://github.com/Giveth/giveth-dapp/files/3674808/givethBuildStartScripts_2019-09-29.zip) along with a Youtube [video](https://www.youtube.com/watch?v=rzLhxxAz73k&feature=youtu.be).


#### Any OS
  1. Click **Star** on this repo near the top-right corner of this web page (if you want to).
  2. Join our [Contributors Discord](https://discord.giveth.io) if you haven't already.
  3. Fork this repo by clicking **Fork** button in top-right corner of this web page. Continue to follow instruction steps from your own feathers-giveth repo.
  5. The rest of these steps must be done from your machine's command line. Clone your own "feathers-giveth" repo. Copy the link from the "Clone or download" button near the top right of this repo's home page.
      ```bash
      git clone git@github.com:Giveth/feathers-giveth.git
      ```
  6. Change directories to feathers-giveth:
      ```bash
      cd feathers-giveth/
      ```
  5. Make sure you have [NodeJS](https://nodejs.org/) (v10.24.0), [yarn](https://www.yarnpkg.com/) (v0.27.5 or higher), and npm (5.4.1 or higher) installed.
  6. Install dependencies from within feathers-giveth directory:
      ```bash
      yarn install
      ```
  7. Install Mongo (we recommend installing via [Brew](https://treehouse.github.io/installation-guides/mac/mongo-mac.html)).
  8. Run Mongo in a terminal window `mongod` or in the background `mongod --fork --syslog`.
  9. Install Redis (we recommend install via Brew `brew install redis`).
  10. Run Redis in terminal window `redis-server` or in the background `redis-server --daemonize yes`.
  11. (optionally) Install [IPFS](https://ipfs.io/docs/install/) (we recommend installing via [Brew](https://brew.sh/)).
     **If you don't install ipfs, image uploading will be affected. You can update the config `ipfsGateway` value to use a public ipfs gateway ex. [https://ipfs.io/ipfs/](https://ipfs.io/ipfs/), however your uploads will be removed at some point.*

### Run server
The Feathers server will need to connect to an Ethereum node via WebSocket. Typically this will be a local TestRPC instance.
The configuration param `blockchain.nodeUrl` is used to establish a connection. The default nodeUrl is `ws://localhost:8545`

1. We need to deploy any contract to that we intend to call. *NOTE:* The following cmd will clear the `data` dir, thus starting off in a clean state.

   ```bash
   yarn deploy-local
   ```

   After deploying local, make sure to copy-paste the MiniMeToken address in default.json.

2. We provide an easy way to start the bridge & 2 ganache-cli instances. *VERY IMPORTANT:* this command enables Home Ganache and Foreign Ganache networks; if you are using MetaMask you will need to **add a Custom RPC** to your networks config; `http://localhost:8546` will be Foreign Ganache, and Home Ganache is normally added by default which is `http://localhost:8545` if needed.

    ```bash
    yarn start:networks
    ```
3. Since the bridge & ganache-cli is now running, open a new terminal window, and navigate to the same feathers-giveth directory.

4. Optionally open a new terminal window and start the ipfs daemon.

   ```bash
   ipfs daemon
   ```
5. Run db migration files (if this the first time you want to start application, it's not needed to run migrations).
   ```bash
    ./node_modules/.bin/migrate-mongo up
   ```
5. Start your app.

    ```bash
    yarn start
    ```

### Kill Ganache
If you run into errors like wallet balance not loading, it is very likely that Ganache is stuck.
`netstat -vanp tcp | grep 8545`
Find the process that is listening on `*.8545` and `127.0.0.1.8545`, and kill it with `kill -9 PID` (which is in the last colomn).

### IPFS Support
If the `ipfsApi` is a valid ipfs node that we can connect to, we will pin every ipfs hash that is stored in feathers. We currently do not remove any orphaned (hashes with no references in feathers) ipfs hashs. In the future we will provide a script that you can run as a cronjob to unpin any orphaned hashes.

### Video Walkthrough
Video tutorial walkthrough here: https://tinyurl.com/y9lx6jrl


### Scripts

The `feathers-giveth/scripts` directory contains a few scripts to help development.

* `deploy.js` - deploys a new vault & liquidPledging contract

* `getState.js` - prints the current state of the deployed vault & liquidPledging contracts

* `confirm.js` - confirms any payments that are pending in the vault

* `makeUserAdmin.js` - make a user admin

### Testing

Simply run `yarn test`, and all your tests in the `/src` directory will be run.
It's included some integration tests, so for running tests, you need to run a mongodb in your local system (on port 27017).

### Debugging

You can control the logging level with the `LOG_LEVEL` env variable. Available levels can be found at: https://github.com/winstonjs/winston/tree/2.x#logging-levels

To enable debug logging simply start the server with `LOG_LEVEL=debug yarn start`.

## Production

We use docker-compose for orchestration of our docker containers in our production servers.
* make Make sure you have a file named `production.json` in config folder.
* Install docker and docker-compose on your server.
* run this command: `docker-compose -f docker-compose-production.yml up -d`.

PS: It's good to see Github Actions config(`./.github/workflows/CI-CD.yml`) to better understand the deployment structure.

## RSK

1. You will need to download the [rsk node](https://github.com/rsksmart/rskj/wiki/Install-RskJ-and-join-the-RSK-Orchid-Mainnet-Beta). After installing, you will run the node w/ the `regtest` network for local development.

  ```
  java -jar rskj-core-0.5.2-ORCHID-all.jar co.rsk.Start --regtest
  ```
  or
  ```
  java -Drsk.conf.file=rsk.conf -jar rskj-core-0.5.2-ORCHID-all.jar co.rsk.Start
  ```

2. We need to deploy any contracts that we intend to call. *NOTE:* You will also need to ensure that your rsk node is in a clean state (reset) for the configured addresses to be correct.

   ```
   npm run deploy-local:rsk
   ```

3. Optionally open a new terminal window and start the ipfs daemon.

   ```
   ipfs daemon
   ```

4. Start your app.

    ```
    yarn start:rsk
    ```

## Audit Log
The Audit log system logs every Create, Update, Patch and
Remove on **Campaigns**, **Traces**, **Events**, **Users**,
**PledgeAdmins**, **Communities**, **Donations**.
For enabling audit log locally you should change `enableAuditLog`
in config to `true`, then
* cd elk
* docker-compose up

You can see the logs after logging in `localhost:5601` with user:`elastic`, password: `changeme`.

### Usage

Each of these services are available via rRest or WebSocket:

```
campaigns
communities
donations
donationsHistory
traces
uploads
users
emails
homePaymentsTransactions
subscriptions
```
If the server is using default configurations, you can see data for any of these services through your web browser at `http://localhost:3030/SERVICE_NAME`

PS: For accessing all features like creating `communities` and `campaigns` it's suggested to
make `isAdmin` field true, for your user in you local MongoDb.

## Giveth DApp (Giveth TRACE front-end) Installation
<img alt='Giveth-DApp Installation Header' src={useBaseUrl('img/content/trace/giveth-dapp-header.png')} />

### Getting Started
In the following sections you will learn all you need to know to run the DApp locally and to start contributing. All the steps are also described in this amazing [Video Tutorial Walkthrough](https://tinyurl.com/y9lx6jrl) by Oz.

#### Prerequisites
- NodeJS v10 LTS.
- yarn (v1.22.10 or higher)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Install
1. Click **Star** on the [`giveth-dapp`](https://github.com/Giveth/giveth-dapp) repo near the top-right corner of this web page (if you want to).
2. Join us on [Element](http://join.giveth.io) or [Discord](https://discord.gg/Uq2TaXP9bC) if you haven't already.
3. Fork this repo by clicking **Fork** button in top-right corner of this web page. Continue to follow instruction steps from your own giveth-dapp repo.
4. Clone your own "giveth-dapp" repo. Copy the link from the "Clone or download" button near the top right of this repo's home page.
5. The rest of these steps must be done from your machine's command line. See the [OSX and Linux](#for-osx-and-linux) or [Windows](#for-windows) section to continue.

#### <a id='for-osx-and-linux'>OSX and Linux</a>
If your operative system is any distribution of Linux you can use the all-in-one installation scripts, special thanks to Dapp contributor Jurek Brisbane, available [here](https://github.com/Giveth/giveth-dapp/files/3674808/givethBuildStartScripts_2019-09-29.zip) along with a Youtube [video](https://www.youtube.com/watch?v=rzLhxxAz73k&feature=youtu.be), otherwise try the following:

1. From the desired directory you wish to copy the "giveth-dapp" folder with source files to.
    ```bash
    git clone git@github.com:Giveth/giveth-dapp.git
    ```
   NOTE: Please use `develop` branch for contributing.
    ```bash
    git clone -b develop git@github.com:Giveth/giveth-dapp.git
    ```
2. Change directories to giveth-dapp:
    ```bash
    cd giveth-dapp
    ```
3. Make sure you have [NodeJS](https://nodejs.org/) (v10) and [yarn](https://yarnpkg.com/) (v1.22.10 or higher) installed.
4. Install dependencies from within giveth-dapp directory:
    ```bash
    yarn install
    ```
5. That is it - you are now ready to run the giveth-dapp! Head to the [Run DApp](#run) section for further instructions.

#### <a id='for-windows'>Windows</a>
1. Install the latest version of Python from this [Link](https://www.python.org/downloads/). (Make sure Python is added to $PATH.)
2. Install Microsoft Visual Studio 2017 (double-check the version) from this [link](https://download.visualstudio.microsoft.com/download/pr/3e542575-929e-4297-b6c6-bef34d0ee648/639c868e1219c651793aff537a1d3b77/vs_buildtools.exe). Giveth-Dapp needs the node-gyp module, and node-gyp needs VS C++ 2017 Build Tools to be installed.
3. After downloading, install the packages marked from this [image](https://cdn.discordapp.com/attachments/849682448102457374/850480734291623946/unknown.png).
4. Then run command below in command prompt
   ```bash
   npm config set msvs_version 2017
   ```
5. After installing the above, you should install NodeJS version 10 [LTS](https://nodejs.org/dist/latest-v10.x/) (it is better to be v10.24.1 LTS).
6. Download and run the node-v10.24.1-x64.msi installer, then continue through the installation as normal. Be sure to have the "Enable in PATH" option enabled before installing.
7. Open the command line in administrator mode by right-clicking on the cmd.exe application and selecting "Run as administrator"
8. In the administrator command prompt, change to the directory where you want to store this repository.
   ```bash
   cd C:\some\directory\for\repositories
   ```
9. Double-check the node version with CMD command:
   ```bash
   node -v
   ```
10. After that, install the latest version of Yarn.  Be careful not to install packages with NPM. If you have already tried "npm install", you should first delete "node modules" folder.
    ```bash
    yarn install
    ```
11. That is it - you are now ready to run the giveth-dapp!

### <a id='run'>Run</a>
1. The Giveth dapp will need to connect to a [feathers-giveth](https://github.com/Giveth/feathers-giveth) server. Follow the feathers-giveth readme instructions to install and run server before proceeding further. Alternatively, you could change the configuration to connect to the `develop` environment, see the [Configuration](#configuration) section.
2. Start the dapp.
    ```bash
    yarn start
    ```
3. Once the dapp is up in your browser, click "Sign In" from the main menu.
4. For testing locally, choose any of the wallet files found in the `giveth-dapp/keystores/` folder using the wallet password: `password`. **DO NOT USE THESE ON ANY MAINNET EVMs.**

5. Using the test token
   To use the test token you need to import the keystore.json you use for your account to MetaMask.
   After importing, click on 'Add token' > 'Custom token', and enter the MiniMe Token address that can be found when deploying the contracts
   (should be `0xe78A0F7E598Cc8b0Bb87894B0F60dD2a88d6a8Ab` by default but make sure to check).
   The token balance should show up automatically, and the token symbol is MMT.
   However, in the DApp the token symbol is referred to as ANT, b/c the DApp needs to be able to fetch a conversion rate.

NOTE:
When resetting feathers or redeploying the contracts, you need to remove the keystore from Metamask and follow this procedure again.

### Build
```bash
yarn run build
```

NOTE: due to some web3 libraries that are not transpiled from es6, we have to use our [giveth-react-scripts](https://github.com/Giveth/create-react-app/tree/master/packages/react-scripts) fork of react-scripts.

### <a id='configuration'>Configuration</a>
The DApp has several node environment variables which can be used to alter the DApp behaviour without changing the code. You can set them through `.env` or `.env.local` files in the DApp folder.

Variable name | Default Value | Description |
---|---|---|
PORT | 3010 | Port on which the DApp runs |
REACT_APP_ENVIRONMENT | 'localhost' | To which feathers environment should the DApp connect. By default it connects to localhost feathers. Allowed values are: `localhost`, `develop`, `release`, `alpha`, `mainnet`. See [Deployment Environments](#deploy-environments). |
REACT_APP_DECIMALS | 8 | How many decimal should be shown for cryptocurrency values. Note that the calculations are still done with 18 decimals. |
REACT_APP_FEATHERJS_CONNECTION_URL | Differs per REACT_APP_ENVIRONMENT | Overwrites the environment injected feathers connection URL. |
REACT_APP_NODE_CONNECTION_URL | Differs per REACT_APP_ENVIRONMENT | Overwrites the EVM node connection URL for making EVM transactions. |
REACT_APP_LIQUIDPLEDGING_ADDRESS | Differs per REACT_APP_ENVIRONMENT | Overwrites the Liquid Pledging contract address. |
REACT_APP_DAC_FACTORY_ADDRESS | Differs per REACT_APP_ENVIRONMENT | Overwrites the Communities contract address. |
REACT_APP_CAMPAIGN_FACTORY_ADDRESS | Differs per REACT_APP_ENVIRONMENT | Overwrites the Campaign Factory contract address. |
REACT_APP_MILESTONE_FACTORY_ADDRESS | Differs per REACT_APP_ENVIRONMENT | Overwrites the MilestoneFactory contract address. |
REACT_APP_TOKEN_ADDRESSES | Differs per REACT_APP_ENVIRONMENT | Overwrites the bridged token addresses. This is a JSON object string w/ token name: token address. |
REACT_APP_BLOCKEXPLORER | Differs per REACT_APP_ENVIRONMENT | Overwrites the block explorer base URL. The DApp assumes such blockexplorer api is `\<BLOCKEXPLORER\>/tx/\<TRANSACTION_HASH\>` |
REACT_APP_DEFAULT_GASPRICE | 10 | Overwrites the default gasPrice that is used if ethgasstation service is down. The value is in gwei. |
REACT_APP_ANALYTICS_KEY | "" | Overwrites `Segment` analytics key.

Example of `.env.local` file that makes the DApp run on port 8080, connects to the **develop** environment and uses custom blockexplorer:

```bash
PORT=8080
REACT_APP_ENVIRONMENT='develop'
REACT_APP_BLOCKEXPLORER='www.awesomeopensourceexplorer.io'
```

The rest of the configuration can be found in `configuration.js`

### Analytics
Segment Analytics can be enabled by setting REACT_APP_ANALYTICS_KEY.

### Query Strings
The milestone creation/proposal view now supports query string arguments!
The following arguments are available:

| Argument | Expected Values | Type |
|------------------|------------------------------------------------------------|--------|
| title | The title of the milestone | string |
| description | The description of the milestone | string |
| recipientAddress | The address of the recipient | string |
| reviewerAddress | The address of the reviewer | string |
| selectedFiatType | A valid fiat type (i.e. USD) | string |
| date | A valid milestone date string | string |
| token | A valid token symbol (i.e. DAI) | string |
| tokenAddress | A valid token address | string |
| maxAmount | A valid max amount of ETH or token | number |
| fiatAmount | A valid max amount of fiat (dependant on selectedFiatType) | number |
| isCapped | Determines whether the milestone should be capped | 0 or 1 (boolean) |
| requireReviewer | Determines whether the milestone should require a reviewer | 0 or 1 (boolean) |

### Local Development
At first you would like to run the DApp locally. When running `testrpc` locally in `deterministic` mode, you can use any of the keystores in the `giveth-dapp/keystores` as your wallet.
This will provide you access to the testrpc accounts for local development. Each keystore uses the same password: `password`. **DO NOT USE THESE ON ANY MAINNET EVMs**

The keystores are seeded with 10.000 ANT tokens for testing donations. To get started with testing donations,
make sure to add your account's keystore to MetaMask and swith MetaMask to Ganache. The donation modal should
then show the appropriate balance when donating in ANT tokens.

**NOTE**: If you get a nonce error in MetaMask or if the DApp fails to load with your MetaMask unlocked, it could be because MetaMask is confused. You should go to "settings" -> "Reset Account" in MetaMask in order to reset the nonce & cached account data.

### Development and PR Testing
1. The Giveth Dapp is auto deployed from the develop branch and is live on Rinkeby [develop.giveth.io](https://develop.giveth.io). All pull requests are autodeployed, and the PR preview will be generated upon submission. To learn how to access PR previews see [Development Process & Quality Assurance](https://wiki.giveth.io/documentation/DApp/product-development-testing/) on our wiki.
2. In order to use the DApp you will need to create account. If this is your first time, click "sign up" to create an account. If you already have a valid keychain file, use it to sign in.
3. You will need test ether on the Rinkeby network. Go to the "wallet" page to see your new address (0x..). Copy that address, and use the Faucet to get some: https://faucet.rinkeby.io/.


### <a id='deploy-environments'>Deployment Environments</a>
At Giveth, we are using the [gitflow](http://nvie.com/posts/a-successful-git-branching-model/) branching model to deploy to 4 different environments.

Name | Blockchain | Branch Deployed | Auto Deploy | Use |
-----|------------|-----------------|-------------|-----|
[mainnet](https://mainnet.giveth.io) | Ethereum Main Network | master | no | Main network deployment for now abandoned due to high transaction costs until sustainable solution is found.
[alpha](https://alpha.giveth.io)  | Rinkeby Test Network | master | no | Environment used as a production version until scalability is resolved.
[release](https://release.giveth.io) | Rinkeby Test Network | release | yes | Environment for release candidate quality control testing by non-devs.
[develop](https://develop.giveth.io) | Rinkeby Test Network | develop | yes | Development environment for integrating new features. Feature and pull request branches are also automatically deployed to this environment.

You can change the environment to which the DApp connects through the node environment variables. See the [Configuration](#Configuration) section for more details.
---
id: givethioinstallation
title: Installing Giveth.io for Local development
---

import useBaseUrl from '@docusaurus/useBaseUrl'

This guide will document the steps to set up and run Giveth.io locally for the purposes of development.The setup process was documented using Ubuntu 20.04 LTS.

**You'll need a couple prerequisites to get started.**

 - [Redis](https://redis.io/topics/quickstart)
 - [Postgres](https://www.postgresql.org/download)
 - Bash CLI
 - [Gatsby CLI](https://www.gatsbyjs.com/docs/reference/gatsby-cli/)
 - Configure NodeJS
      * [For Linux](https://www.gatsbyjs.com/docs/how-to/local-development/gatsby-on-linux/)
     * [For Windows](https://www.gatsbyjs.com/docs/how-to/local-development/gatsby-on-windows/)
 - Your Favourite Code Editor (VScode for linting presets)

### Install impact-graph from GitHub
In order to develop locally you need to clone the backend server as well. We are using https://github.com/Giveth/impact-graph for this.

- via SSH on the CLI:
    ```bash
    git clone git@github.com:Giveth/impact-graph.git
    cd impact-graph
    npm i
    cp .env.example .env
    ```


### Create a Database and User in Postgres using psql
Follow this tutorial on PSQL to setup your username and create the database.
https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)

**TL;DR**
```bash
sudo -u postgres psql
postgres=# create database <databaseName>;
postgres=# create user <userName> with encrypted password '<passwordHere>';
postgres=# grant all privileges on database <databaseName> to <userName>;
```
### Clone and Install the Frontend
  Head on over to https://github.com/Giveth/giveth-2 and clone the repo.
  - via the CLI:
  ```bash
  git clone git@github.com:Giveth/giveth-2.git
  cd giveth-2
  npm i
  ```

### Get the Environment Variables
 In order to run the local build for Giveth.io you'll need to ask for the environment variables. Head on over to our [Contributors Discord](https://discord.giveth.io) say Hi and get in touch with one of the developers.

### Launch the Development Server and Environment
 Start up the `impact-graph` backend server and redis.
  - Run redis by using the command `redis-server`
  - From the impact-graph repo start with `npm start`

 To take advantage of linting presets, please use **VSCODE**:
 * Select *File -> Open Workspace*
 * Navigate into the giveth-2 directory
 * Open the workspace file `giveth2-full-stack.code-workspace`
 * Install recommended extensions (Prettier and StandardJS plugins)

 Then fire up the local development server.

 ```bash
 gatsby develop
 ```

### Start Editing!

Open up the giveth2 repo on your code editor.

Giveth.io is now running locally at `http://localhost:8000`!

<img alt='Giveth Running Locally' src={useBaseUrl('img/content/givethlocalresized.png')} />

You can also expiremnt with querying your data via GraphQL - you'll find it at this link here - `http://localhost:8000/___graphql`
Learn more about using this tool in the [Gatsby tutorial](https://www.gatsbyjs.org/tutorial/part-five/#introducing-graphiql).

  Save your changes and the browser will update in real time!

**Current Build Statuses**

[master](https://v2.giveth.io)

[![Netlify Status](https://api.netlify.com/api/v1/badges/f914ac7e-ce27-4909-bd3e-14d749731a52/deploy-status)](https://app.netlify.com/sites/giveth2/deploys)

[staging](https://staging.giveth.io)

[![Netlify Status](https://api.netlify.com/api/v1/badges/2f325b5b-e159-443e-bac7-c5e15f3578c0/deploy-status)](https://app.netlify.com/sites/giveth-website-staging/deploys)
<br />
---
id: adviceProcess
title: Advice Process
---

*(freely adopted from ['Reinventing Organizations'](https://reinventingorganizationswiki.com/theory/decision-making/) by Frédéric Laloux)*

*****************************************************************

Giveth, as a decentralized organization, relies on the principles of self-management. Giveth is a team of individuals with aligned values who decide to act together towards a common purpose. We have different backgrounds, expertise, methodologies and mental frameworks, and through self-management we are tapping into the potential of such different perspectives to solve Giveth's challenges.

**Advice Process** is used whenever proposing an action or making a decision that will have an impact on the community. Any decision, big or small, should use Advice Process. Before formally making a proposal, it is important to get feedback from the people it will impact, and from the person who has the most relevant expertise around the subject. The intentions are to improve proposals before they are made, preemptively resolve conflicts and to inform related parties. Compromise is a great solution, but not always plausible. The advice process allows objections to be heard and for proposal creators to consider the potential consequences before taking action.

Everyone is empowered to make proposals but must consider that they will also be held accountable for the effects of the outcome. However, if Advice Process has been followed, there will be an idea of the reasons why one takes an initiative and all affiliated parties will have contributed to bring the initiative to the best possible outcome (or to not start it at all). If the proposal fails or has challenging consequences after properly using Advice Process it is therefore hard to fault the instigator for trying. **It's OK to fail, as long as you do it properly!**

### Where does Advice Process happen?

Our most active channel for discussion is the [Giveth Forum](https://forum.giveth.io/). Advice Process can be implemented publicly or privately; however, to remain aligned with our value of transparency, we heavily encourage community discussion to remain in public channels whenever appropriate to do so.

In our current DAO configuration, anyone can make a proposal on our [Aragon DAO Template](https://aragon.1hive.org/#/giveth/). rGiv Governance Token Holders can then vote on these proposals. This process is usually reserved for more critical decisions affecting the organization.

---

With this system, tensions might arise over whether a decision was made properly or not. Therefore, in order to **decentralize power** there needs to be a process to which one can refer. This process ensures that, even if there are disagreements with a proposal, it  was made with the best intentions for the organization and has taken into account feedback and advice from all relevant parties.


### The Advice Process Flow:

1.  **Ideation**:

    In ideation, problems or opportunities are taken on by the person who notices them, or deferred to someone better-qualified. Self-management implies **responsibility**. Tensions are not passed along a hierarchy as in traditional organizations, but are rather addressed by the person with the necessary energy or expertise.


    ***Channels:*** The channel for communication in this phase is open. This can be informal so chat, make time for a call, have discussions, fireside chats, generate ideas.


2.  **Sounding / Meta thinking**:

    Prior to a creating a proposal, the decision-maker may seek input to "sound out" perspectives before proposing action. This is the stage where ideas can be tested against other people's sentiments.


    Some questions to ask:

    *   Am I generating value if I pursue this idea?
    *   Is this a problem that I want to spend my time on?
    *   Am I right in my assumptions and aligned with other people's views about the issue?
    *   What are the possible options I can suggest and what are the caveats that I need to solve before I present an action?

    ***Channels:*** The communication channel for this phase is also informal, as above.

3.  **Advice**:

    The initiator makes a proposal and seeks advice from those affected and those with expertise.


    For minor decisions, there may be no need to seek advice. For larger decisions, advice can come through various channels, including one-on-one conversations, meetings, or broader community discussions.


    There is no specific time frame to gather advice. It will depend on the scope of the decision.


    ***Channels:*** If it is a minor decision, you can consult individuals or the group via Discord. For larger decisions, our [Giveth DAO Aragon Template](https://aragon.1hive.org/#/giveth/) is the place to create formal proposals.

    *It is your responsibility to reach out to related parties, depending on the importance of the proposal.*

4.  **Decision Making:**

    Taking advice into account, the proposal is made and its creator informs those who have given advice.

    ***Channels:*** Announcements can be made in the Giveth Discord, community call and/or governance call.

## Benefits (from [Reinventing Organizations website](https://reinventingorganizationswiki.com/theory/decision-making/)):

*   **Community**: It draws people whose advice is sought into the question at hand. They learn about the issue. The sharing of information reinforces the feeling of community. The person whose advice is sought feels honoured and needed.
*   **Humility**: Asking for advice is an act of humility, which is one of the most important characteristics of a fun workplace. The act alone says, "I need you". The decision maker and the adviser are pushed into a closer relationship. This makes it nearly impossible for the decision-maker to ignore the advice.
*   **Learning**: Making decisions is on-the-job education. Advice comes from people who have an understanding of the situation and care about the outcome. No other form of education or training can match this real-time experience.
*   **Better decisions:** The chances of reaching the best decision are greater than under conventional top-down approaches. The proposal maker has the advantage of being closer to the issue and has to deal with the consequences of the proposal outcome. Advice provides diverse input, uncovering important issues and new perspectives.
*   **Fun:** The process is just plain fun for the decision-maker, because it mirrors the joy found in playing team sports. The advice process stimulates initiative and creativity, which are enhanced by the wisdom from knowledgeable people elsewhere in the organization.


## Underlying mindsets (adapted from [Reinventing Organizations website](https://reinventingorganizationswiki.com/theory/decision-making/)):

Advice Process is a tool that helps decision-making via collective intelligence. Much depends on the spirit in which people approach it. When the advice process is introduced, it might be worthwhile to consider not only the mechanics but also the mindset underlying effective use.

Advice Process can proceed in several ways, depending on the mindset people bring to it:

*   The initiator can approach it authoritatively ("I don't care about what others have said" or, alternatively, "I fully comply with what others have said").
*   They can approach from a perspective of negotiation or compromise ("I'll do some of what they say so they're happy, but I will feel a little frustrated").
*   They can approach it **co-creatively**, *which is the spirit of the advice process* ("I will listen to others, understand the real need in what they say, and think creatively about an elegant solution").




### Disclaimer
**This document is not:**
*   A process to run governance meetings: as a decentralized organization, there are challenges with making decisions in a confined time slot. The governance meeting should be seen as the right moment to engage in some stages of Advice Process and make decisions if all the affected parties are present.
*   A dispute mechanism: Giveth is currently in the process of redefining our conflict resolution process.. Stay tuned!
*   A stone tablet of rules: this document has been created through Advice Process and it can be modified by it as well. 
---
id: brandBook
title: Design & Brand Guidelines
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'



The Giveth Brand Book, designed by Marko Prljic.

<iframe  width="800" height="450" src="https://www.figma.com/embed?embed_host=share&url=https%3A%2F%2Fwww.figma.com%2Fproto%2FbV3f7aLHK2pIs7tlzLGVgH%2FGiveth.io-Branding%3Fpage-id%3D387%253A0%26node-id%3D387%253A1%26viewport%3D255%252C254%252C0.03944773226976395%26scaling%3Dscale-down-width" allowfullscreen></iframe>


<a href="../downloads/Giveth.io_Branding_23-May-2021-195534.pdf" download="GivethBrandBook.pdf" target="_blank" ><strong>PDF version available to download here.</strong></a>
---
id: codeofconduct
title: Code of Conduct
---

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic address, without explicit permission
- Disrespectful, harassing, entitled or trolling behaviour related to airdrops
- Other conduct which could reasonably be considered inappropriate in a professional setting
 
## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behaviour.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, documentation edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other actions that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies within all project spaces, and it also applies when an individual is representing the project or its community in public spaces. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behaviour may be reported by contacting the project team at givethdotio@gmail.com or by submitting an issue to [support](https://giveth.io/support). All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

Attribution This Code of Conduct is adapted from the Contributor Covenant, version 1.4, available [here](https://www.contributor-covenant.org/version/1/4/code-of-conduct.html).

For answers to common questions about this code of conduct, see [here](https://www.contributor-covenant.org/faq).
---
id: commsContributorGuide
title: Communications Contributor Guide
---
import useBaseUrl from '@docusaurus/useBaseUrl'
import styles from '../src/css/custom.css'



This is a guide to get you started with the Comms Working Group. It walks you through the steps to take to get onboarded and contributing, while also giving you some information on the structure of Giveth, what tools we use, and how to orient yourself in general. 


## **What is Giveth?**

Giveth is a platform to support for-good projects through cryptocurrency and fiat donations.


<table>
  <tr>
   <td><a href="https://www.youtube.com/watch?v=-JXwwIGJGQQ&feature=emb_logo">Why Giveth?</a> - Giveth Donor 101 Course
   </td>
   <td><a href="/whatisgiveth/">MVV</a> - Mission, Vision and Values
   </td>
  </tr>
</table>



## **Structure and Working Groups**


<table>
  <tr>
   <td>
<ol>

<li><strong><a href="/whatisgiveth/introCommunity">Community Circle</a></strong>
</li>
</ol>
   </td>
   <td>
<ul>

<li>Comms WG</li>

<li>Connect WG - outreach and project liaison</li>

<li>Conflict Resolution WG</li>

</ul>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li><strong><a href="/whatisgiveth/introPlatform/">Platform Circle</a></strong>
   
</li>
Product development
</ol>
   </td>
   <td>
<ul>

<li>Design WG</li>

<li>Devs WG</li>

<li>GIVeconomy WG</li>

</ul>
   </td>
  </tr>
  <tr>
   <td>
<ol>

<li><strong><a href="/whatisgiveth/introGIVernance/">GIVernance Circle</a></strong>
</li>
</ol>
   </td>
   <td>
<ul>

<li>Governance WG</li>

<li>DAO WG</li>

</ul>
   </td>
  </tr>
</table>


For more detailed information and to learn more about how to participate throughout the DAO, please read our docs including: 

* [Governance process](/whatisgiveth/governanceProcess/)
* [Advice process](/whatisgiveth/adviceProcess/)
* [Conflict resolution](https://docs.google.com/spreadsheets/d/1PhvCZJFkk_j63Q8Aszay2DAn2qg39x6zJDSLlj924TY/edit#gid=679275498)
* [Developer guidelines](/dapps/)
* [Development process](/dapps/developmentProcess/)
* [General contribution steps in Github](https://github.com/Giveth/giveth-dapp/blob/develop/CONTRIBUTING.md)


## Joining the Comms Party

The Comms WG is an integral part of the Community Circle, which encompasses everything related to human contact and isn’t either development or governance. In addition to communications, that includes outreach and donor relations.


To participate in engaging with the Comms WG, you must have accounts on the following platforms: Discord, Github with Zenhub extension, Discourse and preferably also Telegram and Twitter. If you do not have these accounts, we can help you set them up.



### 1. Join the weekly meeting

**Discord:** Hop on a [Comms call](https://calendar.google.com/event?action=TEMPLATE&tmeid=bnQ4NmJwOGVzdjVudjc3Z2tlc3U4ZHBiZ2FfMjAyMjA3MTlUMTYwMDAwWiBnaXZldGhkb3Rpb0Bt&tmsrc=givethdotio%40gmail.com&scp=ALL) held Tuesdays at 12h CST (18h CET). Here you will meet the team and learn about what is going on. You will be able to volunteer during the call for anything you think you can add value to as the team goes through the various issues. Don’t worry, we will help guide you! [Here](/whatisgiveth/meetingsGuide/) is also a detailed explanation of how Giveth meetings function.

### 2. Getting started with your first issue

**Github/Zenhub:**  The Zenhub extension turns Github into a project management board.

<img alt="planning board for comms with zenhub" src={useBaseUrl('/img/content/planningBoardComms.png')} />



You will need to [download it and add it to your browser](https://www.zenhub.com/extension) to establish this user-friendly interface with Github. 


After you have shared your Github handle with the Comms lead, go to the [Giveth Planning board](https://app.zenhub.com/workspaces/giveth-planning-5f08ce1f9264b300166a0185/board?repos=278726184), and have a look at the "[good first issue](https://github.com/Giveth/giveth-dapp/labels/good%20first%20issue)" tag (or potentially the “[help wanted](https://app.zenhub.com/workspaces/giveth-planning-5f08ce1f9264b300166a0185/board?labels=help%20wanted&repos=278726184)” tag) to see where you can jump in and contribute. Contributors move their issues across the board as they pass through different stages of completion from “new” to “in progress” to “review” and “done” with several other nuanced options such as “icebox” and “epic”. Be sure to keep up with the status of your issue: do you need help? Tag someone in your issue, and add a comment. Are you done and need to start the review process? Tag at least two others to review your work. Once finished, you can close it! Below are explanations for each stage of an issue on its way to completion.


#### Different stages of an issue on the planning board:


**New issues:** new issues discussed in comms meetings or something that you think is relevant to our vision and will provide value to the cause go here. 

**Icebox:** non-priority issues are listed here.

**Epics:** ongoing/larger tasks that are divided into separate smaller issues. 

**Backlog:** issues that will be added to future sprints. 

**Sprint Backlog:** issues assigned as part of that week’s work. 


**In progress:** issues being actively worked on with ideal completion within next 1-2 weeks. There should only be 1-2 issues per assignee “in progress”.


**Review/QA:** issues ready for review where 2 senior contributors should be tagged for feedback and support.

**[Learn more about issues and understand the workflow.](https://github.com/Giveth/giveth-planning/issues/373)** 



### 3. Working on an issue

**HackMD and Google Docs: **Documents are created through Google Docs or HackMD. Material uploaded to Giveth's documentation must use markdown formatting. You can choose to draft with Google Docs and convert (post-review) to markdown format using the Chrome extension "[Docs To Markdown](https://workspace.google.com/u/0/marketplace/app/docs_to_markdown/700168918607?hl=en&pann=docs_addon_widget)”.


Make your new Google doc available for edit for reviewers and collaborators either by allowing anyone with the link to edit or at least comment. Submit your work for review (Q/A) to at least two others before implementing. Request reviews both during and after you complete your work by tagging reviewers in your Github issue and adding the doc link. During your work, this review request allows you to consult with team members who may be able to assist not only with various questions but with a general review on the progression of the work. When you are finished, you will tag and consult with at least two reviewers before the issue can be considered executable and finally closed.


Communications Working Group Steward** - Lauren**

Discord handle: **karmaticacid#1218**

Below is more detailed information on Giveth’s workflow design.


## Giveth Toolbox


<table>
  <tr>
   <td>Amplitude 
   </td>
   <td>
<ul>

<li>Analytics
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://aragon.1hive.org/#/giveth/">AragonDAO</a>
   </td>
   <td>
<ul>

<li>Propose and vote on important governance topics using token-weighted voting.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://discord.giveth.io">Discord</a>
   </td>
   <td>
<ul>

<li>Discord is where our team communicates. Introduce yourself, give feedback, find out how to contribute, or just say hello! </li>

<li>Join the Community Call (11h CST/17h CET) and/or any other call that interests you via <a href="https://calendar.giveth.io/">Google calendar</a> or <a href="https://calendar.google.com/calendar/ical/givethdotio%40gmail.com/public/basic.ics">iCal</a>.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://docs.giveth.io/">Docs.Giveth</a>
   </td>
   <td>
<ul>

<li>User and Developer Guides, Technical Documentation
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="http://doodle.com">Doodle</a>
   </td>
   <td>
<ul>

<li>Polls to schedule meeting times
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="http://figma.com">Figma</a> 
   </td>
   <td>
<ul>

<li>Design mockups and collaboration
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://forum.giveth.io/">Forum</a>
   </td>
   <td>
<ul>

<li>Engage with relevant topics and proposals, discussion about governance and Giveth tech, as well as participation in conviction voting for GIVgardens.</li>

<li>Uses the Discourse platform.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://github.com/Giveth/ ">GitHub</a>
   </td>
   <td>
<ul>

<li>We use Github to track all issues and tasks.</li>

<li>giveth-planning for comms/community action items</li>

<li>giveth-next for technical issues/user testing on giveth.io</li>

<li>giveth-dapp for technical issues/user testing on giveth trace</li>

<li>giveth-docs for issues on the giveth documentation</li>

<li>V1 is Giveth TRACE repo.</li>

<li>V2 is Giveth.io repo.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://drive.google.com/drive/folders/0B2gzflwFITCBbmVSd052WWpuNFU?resourcekey=0--3HypbiRwLLGa0n6vHQ5kg&usp=sharing">Google Drive</a>
   </td>
   <td>
<ul>

<li>Collaborative documents before it is added to Notion or docs.Giveth
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://hackmd.io/Qqhlz_EYQH-J8aXTgeqCWg">HackMD</a>
   </td>
   <td>
<ul>

<li>Used for documentation written in markdown formatting
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://medium.com/giveth/">Medium</a> 
   </td>
   <td>
<ul>

<li>Publication for regular development and community updates
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://www.notion.so/giveth/Giveth-2c97e0eca91e43238565c8f79dfe5e8d">Notion</a>
   </td>
   <td>
<ul>

<li>Meeting notes and internal document storage
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://t.me/Givethio ">Telegram</a>
   </td>
   <td>
<ul>

<li>Group bridged directly to #general channel in the Giveth Discord where all messages arrive.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://twitter.com/givethio">Twitter</a>
   </td>
   <td>
<ul>

<li>Stay up-to-date on exciting shares about the Future of Giving!
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Youtube
   </td>
   <td>
<ul>

<li><a href="https://www.youtube.com/channel/UClfutpRoY0WTVnq0oB0E0wQ">Giveth</a> presentations and interviews</li>

<li>Meeting recordings are uploaded in the <a href="https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg/featured">Giveth Transparency Channel</a>.
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td><a href="https://app.zenhub.com/workspaces/giveth-planning-5f08ce1f9264b300166a0185/">Zenhub</a> 
   </td>
   <td>
<ul>

<li>Used for issue tracking, visible in Github
</li>
</ul>
   </td>
  </tr>
</table>

---
id: communityCommsGuide
title: Community Communications Guide
---


As an organization, we want everyone to be aligned with our values and principles. We want to ensure respect, cohesiveness, and wild innovation. We want to foster a healthy, diverse and human-centered working ecosystem. We highly value different opinions, perspectives, and personalities. In order to progress to ever-changing landscapes, we need to have a solid foundation of shared practices and values.

Here in this **Giveth Community Communication Guide**, we share our communication agreements and outline some best practices for participating in our various channels that help us to guide our energies toward Building the Future of Giving.

## We adhere to these communication agreements:

### Honor Self

If you have a need, meet it.

If you have a boundary, state it.

If you have an opinion, voice it.

We are all encouraged to respect ourselves by tending to our self-care and using our voice to express when we want and need to.

### Honor Others

In a similar coin, recognize others as reflections of yourself and hold a high level of integrity when dealing with them.

We follow the golden rule: treat others as you wish to be treated.

If someone states a boundary, please respect it or at least kindly express why you are unable to from your perspective.

If someone does great work and leaves an impression on you, acknowledge them for this by giving !praise and sharing about your positive experience with them in our community call. It feels good to recognize and be recognized.  

### Listen Fully  

The first step to any effective communication is listening fully and being completely present in the moment. Listen to information objectively, without judgment. Listen to the details. So many miscommunications and problems can be completely avoided by actively listening.

### Be Honest and Transparent

As a decentralized autonomous organization (DAO), Giveth values transparency. We record all of our meetings and share our tools and processes openly with the public. Rather than reinvent the wheel, we utilize wisdom and resources shared from others and adapt them to our unique organization. We believe it is wise to steward common goods collectively.

Along these lines, in our communication with one another, we encourage honesty, authenticity and transparency. If you have a tension, it’s important to use [our Giveth Forum](https://forum.giveth.io/) to express it openly or to use our DAO to create proposals that resolve tensions and to vote ‘yes’ and ‘no’ when you feel so inspired. The variety of perspectives, skills and experiences helps us to grow and transform.

### Disagree & Commit

Everything in our organization can be questioned and changed. We encourage curiosity and understand change is constant. Disagree & Commit is a management principle where individuals are allowed to disagree while a decision is being made, but that once a decision has been made, everybody must commit to it. Ongoing dissent and resentment are toxic to the execution of the decision. We must give our best effort and 100% support.

Nothing is perfect. No process is perfect. No decision is perfect. We try our best to find the solution that works for all situations and circumstances. Many times we must commit the best option and just go with it. This is a process of experimentation, not perfectionism.

### Ask Questions

It’s better to ask a question than make a mistake. We want to foster a supportive learning environment, so ask as many questions as you want!



### Say “Sorry”

If you make a mistake, apologize as soon as possible. Saying sorry is a sign of strength. Oftentimes, the people who do the most work, make the most mistakes. When we share our mistakes, others can learn and the mistake is less likely to be repeated. It takes courage to apologize, and you can do it!



### Say “No”

If we can’t trust your “No,” how can we trust your “Yes?” The ability to say “No” will improve your quality of work and happiness. We encourage strong work boundaries and don’t expect you to do everything. Sometimes, saying “No” to a larger workload is an indicator that our organization has grown and we need to hire more people or distribute the workload.

### Keep Commitments

Follow through on what you say you will do. Simple. Ensure your talk and walk are the same. Integrity.

### Have Fun

Once a Unicorn, always a Unicorn…

Here at Giveth and in navigating the blockchain for good cryptosphere, we like to have fun. We do this by welcoming a culture of kindness, praising one another, co-creating together, keeping the vibes high and, of course, creating spicy memes.

**Here are best practices when participating in our channels: **

## We encourage…


* _New ideas._ Thoughtful, engaging conversations that move us forward.
* _Feedback._ Listen to feedback and be open to change.
* _Expression._ Expressing tensions with clear requests and/or solutions.
* _Collaboration._ We opt to minimize the duplication of efforts whenever possible.
* _Quality over quantity!_ We invite Givers, Makers and Donors to collaboratively _Build the Future of Giving_. That means we want people who actively contribute and engage in our platform and channels rather than a bunch of empty followers who are not committed to our vision and mission.
* _Trust._ Trusting your team, Trusting your community and Trusting your system.
* _Emojis._ Using emojis to show emotional response to others’ posts when we don’t have more to say that would continue the conversation forward or fork it in a new direction.
* _Memes._ Creating memes with the Giveth logo watermarked to encapsulate big ideas, trending topics and promote upcoming releases and events.
* _Gamification._ Create a great user experience. Make donating a fun thing to do.

## It’s best to avoid…

* _1-word posts_ that do not bring new perspectives to conversations but rather clutter our channel threads, requiring readers to scroll through unnecessary posts to get to the meat. For example, simply posting ‘thanks’ or ‘yeah’ does not suffice.
* _Competition._ We look at other organizations as ‘partners’ and ‘allies’ rather than ‘competitors’. We’re here to altruistically make the world a better place, and we believe we can more readily do that when we pool our resources together.
* _Sharing personal information._ We never post wallet addresses or other personal details. We value security and protection of private information.

## This is how we transform conflict:



* _Conflict._ Is a golden opportunity to gain clarity and connection. Many times some of the best ideas, strategies, and solutions arise from conflict. Don’t shy away from voicing your ideas and opinions. However, communicate in a manner that still values the personhood and ideas of others.
* _Compromise._ Be flexible and open to the ideas of other people. Sometimes we have to make concessions. Remember to have humility. Some of the most innovative solutions are born from compromise.
* _Open to Criticism._ Accepting constructive feedback often streamlines improvement to processes and products. Don't defend a point to win an argument or double-down on a mistake. Remember, it’s not personal!
* _Feedback._ Focus on giving feedback about the work, not the person. Give examples of the work. No personal attacks, and consider if the person is going through a difficult time in their life in their personal life.
---
id: conflictResolution
title: Conflict Resolution Working Group
---

# Conflict Resolution Working Group

A working group of Gravitons who implement Gravity and provide education and support around conscious communication, empathic listening, and issue revelation and alleviation.

We aim to bring people together and promote resilience in the Giveth DAO by training our members in non-violent communication, understanding and analyzing conflict and techniques to manage it (internally, individually and collectively). The mission is to help build a culture of wellbeing and high vibes, while also pointing out clear steps to strategically manage disputes whenever they arise.


### What is Gravity?

Gravity aims to establish a culture of voluntary compliance around Giveth’s [Community Covenant](https://docs.giveth.io/whatisgiveth/covenant), [Code of Conduct](https://docs.giveth.io/whatisgiveth/codeofconduct), and [Community Communications Guide](https://docs.giveth.io/whatisgiveth/communityCommsGuide). It proposes the recognition and application of conflict management mechanisms to shape harmonious interactions between the members of its community.


### What is a Giveth Graviton?

* Someone enthusiastic about conscious communication, conflict resolution, authentic relating and connection
* Has completed Gravity’s Graviton training
* Contributes to the Giveth Conflict Resolution working group
* A point of contact for reporting conflicts in Giveth
* Gathers information to develop cases and activities
* Delegates conflict mediation cases to other Gravitons
* Provides inter-Graviton support
* Promotes conscious communication strategies for Gravity & Giveth
* Fosters Gravity from their active participation in other working groups within Giveth


### Who are the Giveth Gravitons?

@Forest Soleil is leading the Conflict Resolution working group at Giveth with support from @Juan Carlos Bell Llinás and @bends#3537 at Gravity.

_Trained & Actively contributing—_

Forest (Active Graviton; Conflict Mediator)

Ben (Gravity Support)

Juanka (Active Graviton; Conflict Mediator; Gravity Support)

_Givethers who also completed the Graviton training—_

Mateo

Griff

Ashley

Lauren

Suga

👉🏼 DM @Juan Carlos Bell Llinás if you are interested in joining.

The training is offered twice or more per year with the intention of forming Gravitons: a team of individuals equipped with knowledge and social tooling to address and mediate emerging conflicts or any uncomfortable situations in the best way possible.


### Main Actions

* Everyone in the community can fill the Gravity [typeform](https://the-commons-stack.typeform.com/to/rCVsK5RK) _(currently utilizing the Gravity form, but plan to create a unique one for Giveth)_ or approach any of the Gravitons to request support for conflicts and any sort of uncomfortable or undesired situations.
* In case of conflict, Gravitons can approach the parties involved to collect information on the issues.
* Gravitons can take actions to [regulate unwanted behavior according to the graduated sanctions](https://forum.tecommons.org/t/scale-of-conflicts-graduated-sanction-guideline/234) _(Giveth Conflict Resolution Working Group is currently utilizing TEC Gravity’s graduated sanctions while concurrently meeting to adapt our own)._
* All community members can propose new methodologies to approach **graduated sanctions** and **mutual monitoring** as well as upgrade current ones through [Advice Process](https://token-engineering-commons.gitbook.io/tec-handbook/tec-agreements-1/collective-agreements/advice-process) and [Forum Voting](https://forum.giveth.io/).
* Gravitons can submit conflicts or issues to the Gravity Registry, that is a database of the cases managed by Gravity.
* Conflict resolution calls and chats are closed to Gravitons and parties involved to respect privacy and vulnerability.
* The Giveth Conflict Resolution working group can facilitate safe spaces, skills up leveling workshops, and collaborate with TEC’s Gravity working group to host training and capacitate individuals to become Gravitons.
    * The Gravity training is free and open for all.
* Gravity can remove proposals from all the voting categories if they receive **flags** and/or are seen as harmful for the community based on our rules, boundaries, T&C’s, [Community Covenant](https://docs.giveth.io/whatisgiveth/covenant),[ Code of Conduct](https://docs.giveth.io/whatisgiveth/codeofconduct), and [Community Communications Guide](https://docs.giveth.io/whatisgiveth/communityCommsGuide).

**What actions or outcomes are required or encouraged?**

* All members should be aware of the [guidelines for scale of conflict and graduated sanctions](https://forum.tecommons.org/t/scale-of-conflicts-graduated-sanction-guideline/234).
* All members should commit to respect the protocol for [Giveth Meetings](https://docs.giveth.io/whatisgiveth/meetingsGuide).
* Gravitons should comply to Giveth’s [Community Covenant](https://docs.giveth.io/whatisgiveth/covenant), [Code of Conduct](https://docs.giveth.io/whatisgiveth/codeofconduct), and [Community Communications Guide](https://docs.giveth.io/whatisgiveth/communityCommsGuide) and the additional [Graviton Code of Conduct](https://forum.tecommons.org/t/gravity-role-design/174).
* Gravitons should accept cases based on their competence and communicate to the Conflict Resolution working group if they don’t feel capable of handling an issue.
* Gravitons should promote trust and good relationships between the community.
* It is required to complete the Graviton Training successfully to become a Graviton.
* Gravitons should update the Gravity Registry with the information of possible agreements or the final resolutions.
* All members should respect the arrangements made about the situations issued.

**What actions or outcomes are discouraged?**

* Violating the agreements stated in this working group’s documentation on this page.
* Violating the requirements for the Graviton Role (Any member can monitor Gravitons actions and report to other Gravitons, fill in the typeform, or contact community stewards.)
---
id: covenant
title: Giveth Community Covenant
---

The Giveth DAO is a self-governed organization dedicated to revolutionizing philanthropy and "Building the Future of Giving" by bridging the Ethereum and non-profit worlds. Giveth's mission is to build a culture of giving that empowers and rewards those who give - to projects, to society, and to the world.

Giveth envisions a future in which giving is effortless and people all around the world are rewarded for creating positive change. The Giveth platforms aim to be free for donors and projects, globally accessible and self-sustaining. Giveth aims to facilitate the efficient, transparent flow of funds directly to where they have the most positive impact.

The Giveth community [values](https://docs.giveth.io/whatisgiveth/) decentralization, innovation, altruism, empowerment, trust, transparency and collaboration. This social layer is the foundation on which our DAO is built.

The GIVeconomy represents the economic layer where GIV is issued and distributed programmatically. GIV tokens will be allocated to fund proposals passed in the GIVgarden. GIV distribution from the GIVgarden is henceforth determined by the community who is empowered to use their GIV to vote.

The growth of Giveth is directly related to the community's ability to foster an inclusive and welcoming culture that people feel proud and delighted to adopt as their own. When someone chooses to participate in the Giveth community, they are implicitly supporting the community's culture, values and norms.

Therefore, Giveth rests on an ever-evolving social contract, which sets expectations for how members should engage both with the protocol and with one another. The Giveth Community Covenant attempts to lay out this social contract. This Covenant first lays out our pledge to each other to make the Giveth community a welcoming and safe environment for everybody.  Second, the Covenant discusses the way both off-chain and on-chain decisions are made and how those decisions are judged to be successful.  As a community-driven DAO, the Covenant is subject to change via the community.  

## The Pledge
We as members, contributors and leaders pledge to make participation in Giveth a harassment-free experience for everyone, regardless of age, body shape, visible or invisible disability, ethnicity, sexual characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

We pledge to act and interact in ways that are in agreement with the [Giveth mission, vision and values](https://docs.giveth.io/whatisgiveth/), and contribute to an open, welcoming, diverse, inclusive and healthy community.

### Our Standards
Examples of behaviour that contributes to a positive environment for our community include: 
- Demonstrating empathy and kindness toward other people 
- Being respectful of differing opinions, viewpoints and experiences 
- Giving and gracefully accepting constructive feedback 
- Accepting responsibility and apologizing to those affected by our mistakes, while learning from the experience 
- Focusing on what is best not just for us as individuals, but for the overall community

Examples of unacceptable behaviour include: 
- The use of sexualized language or imagery, and sexual attention or advances of any kind 
- Trolling, insulting or derogatory comments, and personal or political attacks 
- Public or private harassment 
- Publishing others’ private information, such as a physical or email address, without their explicit permission (commonly called doxing)
- Other conduct which could reasonably be considered inappropriate in a professional setting

## On-chain

### Decision Making

Giveth uses the [Gardens](https://gardens.1hive.org/#/home/) governance platform to manage the GIVgarden configurations and allocate funds to projects that are aligned with its [mission, vision and values](https://docs.giveth.io/whatisgiveth/). 

On-chain decision making mechanisms for the GIVgarden include [Conviction Voting](https://forum.tecommons.org/t/conviction-voting-tl-dr/308?u=liviade) and [Tao Voting](https://forum.tecommons.org/t/tao-voting-formerly-disputable-voting-parameters-general-discussion/267). Conviction Voting should be used primarily for funds allocation. Tao Voting should be used for updating parameters, bug fixes, adding new features to the DAO and/or for emergency situations such as an attack to the DAO treasury. 

Additional polycentric governance processes used by Giveth are specified in [this living document](https://docs.giveth.io/whatisgiveth/governanceProcess) and might change according to the community’s decisions.

### Enforcement

The on-chain mechanism for enforcement depends on [Celeste](https://1hive.gitbook.io/celeste/) -  a subjective oracle that uses predictable, inclusive, and democratic means to resolve disputes arising from optimistic actions.

The ability for Giveth to enforce this covenant is limited to the direct interactions that community members have with the protocol, specifically the ability for community members to submit proposals to allocate GIV issuance or adjust protocol parameters.

When using the GIVgarden, the proposer will be required to deposit GIV when submitting a proposal, attesting that the impact of the proposal could be reasonably considered to align with Giveth's social contract. A dispute can be created by another community member if they disagree with the proposer's attestation by challenging the proposal and staking an equivalent amount of GIV. If after being challenged the proposal is not withdrawn, a decentralized oracle (Celeste) will be used to settle the dispute. If the oracle responds in favour of the proposer, the proposal will be unlocked and the challenger’s stake will be transferred to the proposer. On the other hand, if the dispute resolves in favour of the challenger, the proposal will be removed from consideration and the proposer's stake will be given to the challenger.

Participants in the dispute resolution protocol are expected to review the proposal, this covenant and related past disputes in order to provide a judgement that they feel best aligns with the established norms and intention of the Giveth community.

## Off-chain

### Decision Making

Giveth uses an [Advice Process](https://docs.giveth.io/whatisgiveth/adviceProcess) as its primary practice for flat decision making to empower contributors with agency to move their cultural proposals forward. Advice Process is written in the Giveth documentation and promoted verbally in community calls. When a non-financial, no-code decision will likely affect a large part of the community, the use of off-chain voting using polls in the Discord or Forum is implemented. A decision is considered legitimate when it respects this covenant, is promoted to the awareness of the community and its results aren’t challenged within 2 weeks. 

Giveth community spaces, including the Giveth [Forum](https://forum.giveth.io/), [GitHub](https://github.com/Giveth) and [Discord](https://discord.gg/JxF38Tj364), as well as other off-chain forums that may emerge in the future, are expected to adhere to this covenant.

### Enforcement

Giveth intends to use [Gravity Conflict Management](https://forum.tecommons.org/t/gravity-general-process/173) and make use of its graduated sanctions in order to ensure community standards. 

---
id: externalContributors
title: Working with Giveth as an External Collaborator
---

**Hey buidler!**

We are stoked that you are interested in helping us buidl the Future of Giving. This short doc will give you the tips and tricks to work effectively with Giveth. 
 
If you don’t here are a few ways to get inspired: 


* Check out the [ideas Channel on Discord](https://discord.com/channels/679428761438912522/689535474532221030).
* Have a look at our [Dework board](https://app.dework.xyz/test-120/giveth-dapps-v2/view/board-5901) (alpha version) and [community suggestions](https://app.dework.xyz/test-120/giveth-dapps-v2/community).
* Find issues suggested in [Tokenlog.](https://tokenlog.xyz/giveth/roadmap)
* Go to [meetings](https://calendar.google.com/calendar/u/1?cid=Z2l2ZXRoZG90aW9AZ21haWwuY29t) & ask around on Discord.

Once you have an idea, contributing to Giveth is as easy as 1-2-3! Here’s what to do:



### 1. Create a proposal

Anyone is welcome to create a proposal on [Giveth’s Forum](https://forum.giveth.io/). Proposals can be very detailed or intentionally broad to get some feedback and polish the details in the advice process. Here is a [proposal template](https://forum.giveth.io/t/proposal-template/303) to help you rock this step. If you are not that comfortable writing a proposal in the forum yet, you can go to the [collab chat channe](https://discord.com/channels/679428761438912522/990973636603179079)l on Discord to get advice  or join the AMA community orientation call (Wednesdays at 10 am CST). 



### 2. Get signaling and feedback

Your proposal must be active in the forum for 5 days for the “[advice process](./adviceProcess.md#the-advice-process-flow)”. Signaling for support or specific details on the proposal can be achieved by inserting polls into the proposals. It’s strongly recommended to seek community engagement. To that end, you might consider using the following:



* Giveth Discord channels
* GIVernance meeting - where our governance working group discusses active proposals in the forum (Mondays at 9 am CST). 

### 3. Final decision

After the 5-day advice process, the proposal can be updated using the collected feedback & moved to the voting phase. When the proposal doesn’t require a budget, it should be posted and voted on [Giveth Snapshot](http://snapshot.org/#/giv.eth/). If funding is necessary it should be posted and voted on in the [GIVgarden](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98). 

Don’t forget to post a link to the Snapshot or GIVgarden vote on the original Forum post. To learn more about these voting apps & their requirements, check out our [documentation](./governanceProcess.md). 


:::tip
* Ask for help. Giveth Discord is full of people who want to help! 
* If the proposal requires funding, be clear about how you will use the funds.
* If you are unfamiliar with Giveth processes or the Giveth Dapp, try to find a champion who can help you understand how to create more value for Giveth (@Cotabe#4096 supports external collaborators).
:::

Good! Now you know what’s the best way to work with Giveth as an external collaborator, it would be awesome to join us in the journey of Building the Future of Giving.---
id: finances
title: Giveth Finances
---
**Donations**

Every donation and pledge made through Giveth is traceable and projects can be held accountable, unlike with traditional charities. You always know exactly where your donation went and can get a good sense of the impact it made through communication with your chosen beneficiary.

Giveth is both a non-profit organization and an open-source platform for transparent philanthropy in support of your favorite causes. You can support us in building the future of giving by donating to us through the Giveth DApps too! The easiest way is to give directly at [donate.giveth.io](https://giveth.io/donate/giveth). For more specific funding of specific circle activities, log into trace.giveth.io via MetaMask, place and trace your donations, and join other Givers on the [Giveth Funding Leaderboard](https://www.trace.giveth.io/community/giveth-dac).

If you prefer to donate directly to our address or via MyCrypto or MetaMask, you can send ETH or ERC20 tokens to the following address: revolution.eth (which resolves to: 0x8f951903c9360345b4e1b536c7f5ae8f88a64e79).

**Operational Expenses**
Giveth related expenses can be claimed by creating a Trace in a Giveth Circle's Campaign at trace.giveth.io. If you have not had an expense with Giveth before, you need to [contact the team](https://discord.gg/cCsYnNDkq2) first.

The individual Circles (see [Giveth Circles](https://docs.giveth.io/whatisgiveth/givethCircles)) are responsible for expenses of their members, including but not limited to:

- Office expenses (rent, utility bills, equipment, groceries for Giveth Team Meetups)
- Transportation to and from official Giveth Team Meetups
- Suitable accommodation for the duration of official Giveth Team Meetups
- Tickets to Represent Giveth at Conferences
- Food and non-alcoholic drinks consumed while at official Giveth Team Meetups

By default, only expenses with valid receipt are covered. Expenses must be submitted via trace.giveth.io. The refund will be made at earliest convenience for the requested token to recipient wallet provided.

**Regular Rewards**
The members working full-time for Giveth are regularly compensated. Regular Reward requests and payments are managed by the Governance Circle following the approval process through Giveth's Reputation DAO (nrGIV token holders) every 4 weeks.

**RewardDAO**
Special contributions to building the Future of Giving with us by participating in the Giveth Community on Discord, attending Giveth calls and completing tasks, and fulfilling special assignments may be rewarded via the [RewardDAO Campaign](https://www.trace.giveth.io/campaign/rewarddao). Simply create a TRACE describing what you did and come to a Governance call to represent yourself!
---
id: fundraisingGuide
title: Fundraising Campaign Guide with Giveth
---

There are many resources and guides on the internet to help you run a successful fundraising campaign but here are some fundamental steps to launching your crypto fundraising campaign with Giveth.


## 1. Soft Launch

Soft launching means sharing your campaign to a few dedicated supporters or those that have previously fundraised for your cause. Ask them to donate crypto to kickstart your campaign before the official launch to your wider supporter base. People are more likely to donate when they see you’ve received donations. In addition, soft launching your campaign means that you can discover bugs, errors, typos or broken links before sharing far and wide.

Contact your early supporters (email or 1-1 at this stage) - what feedback do they have? Is the fundraising message clear and exciting? Is there anything they would change? 

Momentum generated in soft launch should carry over when you are ready for your fundraising launch and you will reach your fundraising goal faster.


## 2. Your Brand is your Identity 

‘Brand’ is important and is anything that identifies your organisation/project, makes it stand-out and memorable. It is more than just a logo, it can be the colours you use, the style of your communications, patterns, photos and videos. There are lots of resources online to help you develop a brand and consistency can help your potential supporters get to know your project/organisation better, build trust and confirm that the campaign belongs to your project. This is especially important as you spread the word about your campaign across different communication channels and social media.


## 3. Link Donations with Impact

Show your donors how their support is making a difference in the real world. If possible, explain what could be achieved in relation to specific donation amounts to help donors visualise the impact their donation could make. Consider using powerful and authentic photos of your project in action (remember to get permission from those in the shot and take care not to include faces etc. if you are working with vulnerable people). Use descriptive text to show how donations are being used. Post these as updates on the Giveth platform and share to your communications channels and social media. When donors feel connected to your project, they donate more and spread awareness of your cause.


## 4. Campaign Video

Make a campaign video. There are numerous resources out there providing tips and tricks for making a successful campaign video. People who watch a nonprofit’s video are more likely to make a donation. Videos bring your organisation/project to life in a way that potential donors can understand and relate to, and are a powerful way to ask for donations. Once you have your video, don’t forget to post it on Giveth and share through all your communication channels and social media.

Some ideas for your video: record your team in action or through interviews, feature stories that show the impact of the work you do or interview supporters. Seize opportunities to show people how they can get involved. Videos really are one of  the most powerful ways to connect to donors through your media channels


## 5. Celebrate Success

Establish milestones and tell everyone about it when you achieve them. It’s really important! Celebrating milestones maintains momentum for your fundraiser. Showcase your creative ideas and fundraising successes to keep your community engaged and inspired to reach the next big goal. You cannot talk about your fundraiser too much or overshare your successes on social media. 

Consider setting smaller, incremental goals that are achievable to celebrate together along the way. As you hit each goal, post on all your channels and send milestone emails to your community and team.


## 6. ‘Verification’ Badge

If your project is for Public Good (see our standard of what Public Goods means), we recommend that you get verified on Giveth platform. Applying for project ‘verification’ through Giveth gives your project extra credibility and rewards your donors with ‘GIVbacks’ (donors receive a portion of the dollar value of their donations back in GIV tokens, streamed over time). The more a donor gives the more they receive in GIVback rewards. Check out the resource about [GIVbacks](https://docs.giveth.io/giveconomy/givbacks).


## 7. Social Media

Having an active Twitter account and growing your following through Twitter helps attract crypto donors.

Here are some ideas for messages to share with your supporters and donors. 


### Social media message ideas@



* Zero fees - maximising your donation!
* Low gas with most tokens
* Transparency! Traceability

#### For verified projects

* Give and get GIV
* Keep Giving and make change
* Your giving gives back
* Keep the GIVing going
* Giveth - where the giving gives back
* Giveth - where the giving GIVs back
* GIVbacks give rights! - have your say in governance


## 8. Stewardship plan

Stewardship is important to donors - it’s a way of showing that your organisation / project is using donors’ funds within your project, as intended. It includes thanking donors, progress updates and showing their gifts ‘in action’. Consider how best to thank donors: direct contact, an update on your Giveth profile, tweet about their contribution and what it does etc. 

You will begin to build a relationship with donors, keep them engaged and involved with your project/organisation, which may result in further donations or at least, continued support and sharing the news about your cause.

## 9. Gift acceptance policy

Your organisation may or may not have some kind of gift acceptance policy or a guide that outlines the types of gifts your organisation/project can accept and treatment of those gifts once received. You should consider how you will use your crypto donations when received and create a plan and revise your gift acceptance policy (tip and example from every.org). Things to consider:



* Offramping: when and how 
* Centralised vs decentralised exchange
* Wallet ownership
* Treatment of volatile vs stable coins 

## 10. Value Proposition

Your value proposition on Giveth is a simple and clear description on your project page that tells your supporters and donors why they should support your organisation or project. What sets you apart from other organisations and makes you stand out from the crowd? The value proposition of your organization needs to be front and center of your messaging and should answer the following question: “Why should a donor give to you (and not any other organisation) now?”


#### ‘Call to Action’



* Your Giveth profile should have a call to action: ie ‘donate now to help’, ‘make a difference now by…’. It is very important to ask for action in your messaging (what can the donors do now?)
* Segment your audience starting with those closest to you, who are they?: family, friends, existing donors, event attendees (who provided contact information) etc
* And send them a personal message with call to action (donate on Giveth) as part of the soft launch, discussed earlier

## 11. New Donors

Have a strategy to attract new donors, who are they? Where will you find them? How will you reach them? Newsletters, Tweets, events, podcasts, interviews, videos etc.

Useful links to other crowdfunding campaign resources:

 [https://www.boostyourcampaign.com/kickstarter-marketing-tips/?gclid=EAIaIQobChMIjcuD3YXm9wIVCqh3Ch2MKgO5EAAYASABEgIT1PD_BwE](https://www.boostyourcampaign.com/kickstarter-marketing-tips/?gclid=EAIaIQobChMIjcuD3YXm9wIVCqh3Ch2MKgO5EAAYASABEgIT1PD_BwE)

[https://www.nibusinessinfo.co.uk/content/seven-tips-how-run-successful-crowdfunding-campaign](https://www.nibusinessinfo.co.uk/content/seven-tips-how-run-successful-crowdfunding-campaign)

## 12. Promotion through Giveth Community

Gain extra project exposure and campaign promotion through Giveth community:



* Join the weekly Giveth community call and showcase your project in the ‘Community Spotlight’ Present
* Showcase your project through Giveth events like “Meet the Makers”
* Tweet your project and gain extra exposure with amplification and shares through Giveth Community

Don’t forget to include these hashtags:  #futureofgiving #giveth when posting about your Giveth fundraiser.

## Project Fundraising Checklist

- [ ] Talk to friends and existing supporters of your project’s fundraising goals and Giveth platform and ask them to spread the word
- [ ] Have a twitter account, if not, create one
- [ ] Tweet about your Giveth profile when it’s created and when it’s verified (if applicable) 
- [ ] Post on other social media accounts where your donors can be reached about your Giveth profile
- [ ] Email message to your existing supporters and make sure to include a call to action and a link to your Giveth profile
- [ ] Create messaging regarding accepting crypto either in your Gift Acceptance Policy or for your board and supporters
- [ ] Create a thank-you message for donors who you are able to reach once they donate
- [ ] Have a timeline on project milestones when you can report and celebrate your project or fundraising success
---
id: givethCircles
title: Giveth Circles
---

Our organization can be sub-divided into 3 internal circles: GIVernance, Platform, and Community. The goals of each individual circle are unique, but are aligned with our core values, our mission and our vision to build the future of giving. The circles and their respective goals are outlined in the sections below.

## Community
This circle is held down by the Communications team yet comprised of representatives from the other two Circles, as well as various working groups that may form. Here is where new contributors, project owners, campaign managers, collaborators, conspirateurs, catalysts and really all the cool cats come to play, learn, give and grow.

### Goals
* **Build Community around For-Good Projects** by nourishing relations between Givers, Makers and the greater community through meaningful engagement, outreach, trust facilitation and conflict resolution - creating a safe space for community members to communicate their passion projects, then recruit help or guidance from peers.
* **Offer a Clear & Supportive Onboarding Process** as Giveth develops the Dapps, economy, DAO and ongoing new features. The community circle provides a well-defined, transparent and helpful onboarding process that supports the needs of Contributors, Communities, Campaigns, Projects and Donors as well as functions as a bridge for newcomers into the crypto space.
* **Coordinate External and Internal Communications** when broadcasting or sharing activity and development progress externally through the Giveth channels and social media - ensuring that the voice of Giveth as an organization is aligned with our overarching Values, Vision, Mission and Goals and that all Giveth Circles are represented.
* **Create a Network of Partners** by way of collaboration, relationship building and support of common goals with various strategic partner organizations as well as community members focused on blockchain4good and improving the ethereum commons - providing resources, education and sharing of best practices.
*Partners currently include communities like [Commons Stack](https://commonsstack.org/), [TEC](https://forum.tecommons.org/), [DAppNode](https://dappnode.io/), [BrightID](https://www.brightid.org/), [1Hive](https://about.1hive.org/), [Panvala](https://panvala.com/), [GitCoin](https://gitcoin.co/) and [MetaGame](https://wiki.metagame.wtf/).*

## GIVernance

Giveth aims to be a donor-focused organization that GIVs back to those who use our platform to transparently and accountably support change in the world.

We value transparent, holistic governance and hope to be a shining example of it. We explore and readily adopt new innovations that support us in embodying these values. We believe in the self-organizing power of sociocracy, which we apply in the organization of tasks, participation in the [Proposal](https://forum.giveth.io/t/proposal-template/303) and [Advice Process](https://docs.giveth.io/whatisgiveth/adviceProcess/), and facilitation of our governance meetings.

Our circle is uniting the power of our [Decentralized Autonomous Community (DAC)](https://trace.giveth.io/community/giveth-dac) with the non-profit advantages of our [Donor Advised Foundation (DAF)](https://www.sdgimpactfund.org/giveth-foundation) to iterate upon creation of our governing [Decentralized Autonomous Organization (DAO)](https://aragon.1hive.org/#/giveth/).

### Goals
- **Demonstrate Fiscal Accountability** by responsibly provisioning funds and skills toward team structure, conflict resolution, administration, financial transparency, organization of team gatherings and quality assurance. Meet the resource needs of the Giveth community, platform and economy.
- **Innovate Internal Governance** through experimenting with and documenting decentralized governance systems within the Giveth DAO structure (e.g. Sociocracy, RewardDAO, Conviction Voting, SourceCred, etc.) that could prove useful for future Decentralized Altruistic Organizations to learn from and implement their own versions.
- **Collaborate with the Ethereum Ecosystem** to develop collaborative tools that generate mutual benefit and success by partnering with and participating in the governance of other mission-aligned organizations such as: [Commons Stack](https://commonsstack.org/), [Token Engineering Commons](https://forum.tecommons.org/),  [DAppNode](https://dappnode.io/),  [BrightID](https://www.brightid.org/),  [1Hive](https://about.1hive.org/),  [GitCoin](https://gitcoin.co/) and [MetaGame](https://wiki.metagame.wtf/).
- **Create Regenerative Value** that nurtures and grows the Giveth Token Economy (GIVeconomy) by empowering individuals toward inclusive decentralized decision making with outcomes that have real impact on the organization and positive change in the world when cascaded through our listed projects.

## Platform
The Giveth Platform Circle is the terminal for designers, developers, testers, systems engineers and product managers alike, and is where the Future of Giving is being built. We collaborate with the Community Circle to get feedback from our users and design experiences that make it easy for people to create, give, receive and trace.

The Platform Circle, while building high-quality products, proclaims success by encouraging its members to learn, grow, collaborate and celebrate achievement together. By building workflows that are inclusive, transparent and well-structured, we thereby build strong teams of talented and inspired contributors.

### Goals
* **Develop Digital Public Goods** that serve as open-source, efficient and free platforms that bridge Givers and project owners, harnessing the revolutionary funding opportunities of digital currencies.
* **Product Development and Maintenance** that empowers contributors to research emerging technology and implement best practices to create robust, stable, secure and scalable platforms.
* **Improve User Experience, Usability and Accessibility of Blockchain Technology** by engineering and continually creating intuitive interfaces and powerful user experiences to make donating easy, rewarding and effective.
* **Build DApps by and for the Community** by implementing user feedback to create products that meet their needs and maintain a high level of transparency to support a network of value-aligned projects.
---
id: givethdao
title: The Giveth DAO
---

## What is a DAO?

A DAO is an acronym for a **Decentralized Autonmous Organization**. In short it's a decentralized application programmed on the blockchain to facilitate governance and organization of an enterprise or community. DAO's take governance to the next level by allowing its members to transparently and equitably make decisions. Some exciting examples are being able to mint and distribute your own currency or tokens, creating proposals and facilitating voting processes. Each DAO is designed different so make sure you do your homework before jumping into one! A greater explanation of what a DAO is can be found [here](https://blockchainhub.net/dao-decentralized-autonomous-organization/).

## The Giveth DAO

#### What is the Giveth DAO's purpose?

#### Who is allowed to particpate?

**What is Conviction Voting?**
Conviction Voting is a coordination module that allows communities governing a shared resource to choose priorities in a decentralized way. 

Let’s look at some of the properties of Conviction Voting:
* Voting is continuous, its much more like signaling.
* The emitter can change their “vote” anytime
* A fundamental property of this particular system is that votes grow stronger over time (as long as the vote is not changed).

Learn more about the differences between Conviction Voting and Ad-Hoc voting [here](https://medium.com/giveth/conviction-voting-34019bd17b10).---
id: givtoken
title: The GIV Token
---
## What is the GIV token?

## How do I receive GIV tokens?

## What can they be used for?

#### GIV Token Staking

---
id: governanceProcess
title: Governance Process
---
import useBaseUrl from '@docusaurus/useBaseUrl'


Giveth Governance benefits from a robust design and utilizes several platforms to aggregrate and foster advice, consensus, signalling, voting and all the other wonderful actions enabled by Web3 decision-making systems.

We can divide governance participants into three categories based on their possible actions and the platforms they can use to participate. They are **GIV token holders**, **rDAO members**, and **the greater community** (or simply, the community).


#### (Or skip to the <a href="#TLDR">**TL;DR**</a>)


## The Community
Being part of the community has no requirements. If you know about Giveth and want to get engaged then we welcome you openly with our highest of vibes and spiciest of memes.

The best place for formal conversations around Giveth take place on our [Discourse forum](https://forum.giveth.io/). Our forum invites a wide variety of topics for anyone to introduce in-depth discussion, however more importantly, this is the quintessential launchpad where any legitimate governance proposal must start from.

Anyone in the community can create a proposal, however there are some considerations to make:
- <span id="proposal">Proposals</span> ideally have a clearly defined intention that outlines actions to be taken, potential consequences and funds requested (if applicable).
-  We adhere to a [**Community Covenant**](https://docs.giveth.io/whatisgiveth/covenant) which is our main reference point for any disputes or contentions.
-  We use [**Advice Process**](https://docs.giveth.io/whatisgiveth/adviceProcess/) to gather feedback and refine proposals.
- Proposals must remain on the forum, open for Advice Process, for a **minimum of 5 days**.

If all conditions have been met, including time requirements for Advice Process, proposals can move on into either the GIVgarden or the rDAO DApps for voting.  In order to participate in these DApps you must hold either GIV or nrGIV, respectively. All Giveth Governance DApps are deployed on Gnosis Chain (formerly xDai Network).

**If a proposal desires to skip or shorten the Advice Process,** in the case of financial urgency for example, they may do so while providing a written disclaimer and a reason for doing so on their proposal. Skipping or shortening the Advice Process decreases the chances of a proposal passing, **do so with great discretion!**

:::note
### Soft-Consensus
 We often use polls inside the forum or on Discord to get soft-consensus for preferred outcomes. It's acceptable to use these same methods for [informal or low-impact decisions](#informal-decisions). However, for formal proposals they must indicate a clear intended outcome to keep objectives as clear as possible. The on-chain voting systems we use do not support multiple-choice voting.*
:::

## GIV Token Holder

GIV token holders can get involved in decision making via the <a href="https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98" target="_blank">GIVgarden</a>. It leverages [Conviction Voting](https://forum.giveth.io/t/conviction-voting/154) and [Tao Voting](https://forum.giveth.io/t/tao-voting-explained/155) systems to allow GIV token holders to create, signal and vote on proposals using their GIV tokens. Decisions made in here revolve around community funding requests and suggestions as well as any metagovernance modifications. To learn more [visit our documentation regarding the GIVgarden](../giveconomy/givgarden).

### Snapshot Voting
Snapshot allows all of a users GIV holdings, including GIV staked in GIVfarms or the GIVgarden to be counted and calculated towards their total voting power used on the [Giveth Snapshot](https://snapshot.org/#/giv.eth) Snapshot is gasless and chain-agnostic and is a magnificient tool to capture community sentiment on proposals and issues that do not directly request funds from Giveth.

Giveth has whitelisted three types of votes that can be used for proposals on Snapshot: **Basic Voting**, **Single Choice Voting** and **Ranked Choice Voting**. Any other types of voting methods are considered invalid at this time.

#### Single Choice Voting OR Basic Voting
This is a simple Single choice voting strategy. You'll have a range of options and you can only pick one. In Basic Voting you'll be able to choose between For (Yes), Against (No) or Abstain (Undecided/No Opinion).

**A single choice or YES option needs to receive 88% support in order to pass.** To arrive at the YES % we remove the abstain votes and divide the YES votes against the total amount of YES and NO votes. 

Our Quorum is the total amount of GIV tokens that need to particiapte in a vote in order for it to be considered valid. **The Quorum will be set to 1 Million GIV**

#### Ranked Choice Voting
This voting method allows you to select multiple options, signalling your most preferred outcome and then your 2nd favourite option, 3rd, 4th and so on.. (depending on how many options there are)

**There are no required support percentages for Ranked Choice voting.** Snapshot will calculate which option received the most support and we will choose the top result as the winner. 

**Quorum, will be set to 1 Million GIV**.

### Tokenlog 
Tokenlog is a voting tool for token-weighted backlog planning. Giveth uses it for decentralized roadmap planning and **allows GIV holders to have a say in what Giveth prioritizes building**. Features, improvements and core roadmap items for Giveth and it's products are captured in github issues and can be voted on using the [Tokenlog interface](https://tokenlog.generalmagic.io/Giveth/Roadmap). New ideas and proposals are reviewed by our product managers, if they make sense and align with Giveth's values they will be added to the Tokenlog for voting. 

Currently your Tokenlog voting power is calculated from your address' GIV and [wrapped GIV (gGIV)](../giveconomy/GIVgarden#wrapping-giv--earning-rewards) balances on Gnosis Chain. Your voting power is calculated from the sum of both aforementioned token balances where one token is equal to one vote.

You can access the [**Giveth Tokenlog** here](https://tokenlog.generalmagic.io/Giveth/Roadmap). If you have an idea for a feature or improvement for Giveth you can jump into our [discord](https://discord.giveth.io) or drop your idea on the [forum](https://forum.giveth.io/).

## nrGIV Token Holder

This is a form of executive council held for trusted Giveth contributors. nrGIV DAO members hold nrGIV and use an [Aragon DAO deployment](https://aragon.1hive.org/#/nrgiv/) to create and vote on proposals using simple Yes/No voting mechanics. Only nrGIV holders can vote or make proposals. Proposals will remain open for voting for 5 days and must adhere to the Quorum and Support Required percentages or else it will fail.

 In order to get nrGIV you must be a regular contributor to Giveth for at least 3 months and have an approved role proposal. If you're an eligible contributor and it's your first time, then you must request a current nrGIV holder to propose minting nrGIV tokens for you on your behalf, only during the quarterly minting periods. Forum posts will be made for each quarterly distribution and will be announced on our weekly Governance and Community calls.

### Role Proposals 

Role proposals are our way of keeping everyone in touch with what are the roles each contributor is filling. This takes the form of a document and a short description in a topic posted on [our forum](https://forum.giveth.io), which is then left open for comment and approval via [advice process](./adviceProcess.md). Only contributors who have finished their trial period can move to create a role proposal. Once passed advice process, it is put up as a vote for on the nrGIV DAO for on-chain voting; if the vote passes, you're in as an official Giveth regular contributor!

If you have a work agreement and work casually for Giveth, usually there is no explicit need to go through the entire role proposal process. However if you record 30 or over hours monthly for 3 consecutive months then it is required for you to create a role proposal in order to continue to be paid by the Giveth DAO.


:::info
When the first tokens are minted for a quarterly nrGIV distribution, all eligible contributors have 1 month from that date to request tokens. After this period the round is closed and no more token requests will be accepted for this period. Eligible contributors will still be able to request tokens for the next token distribution.
:::

Learn how to become a contributor (and get nrGIV) in our [Giveth Basics document](https://www.notion.so/giveth/Giveth-Basics-bff76dceaec64839b73aa89ba2fb8be4).  
## Informal Decisions
Not all decisions require formal on-chain votes. There is room for making low-impact, agile decisions via a range of platforms that Giveth's community utilizes. For the most clarity we refer to the Covenant's section on [off-chain decision making](./whatisgiveth/covenant/#off-chain):

> Giveth uses Advice Process as its primary practice for flat decision making to empower contributors with agency to move their cultural proposals forward. Advice Process is written in the Giveth documentation and promoted verbally in community calls. When a non-financial, no-code decision will likely affect a large part of the community, the use of off-chain voting using polls in the Discord or Forum is implemented. A decision is considered legitimate when it respects this covenant, is promoted to the awareness of the community and its results aren’t challenged within 2 weeks.  

> Giveth community spaces, including the Giveth Forum, GitHub and Discord, as well as other off-chain forums that may emerge in the future, are expected to adhere to this covenant.

<h2 id="TLDR">TL;DR</h2>

1. Make a <a href="#proposal">proposal</a> on the Giveth <a href="https://forum.giveth.io" target="_blank">forum</a>.
    - Allow a minimum of 5 days for advice process.
2. Create a proposal in the DApp for on-chain voting; this should link to your forum proposal.
    - [GIVgardens](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98) for GIV token holders requesting funds
    - [Snapshot](https://snapshot.org/#/giv.eth) for GIV token holders regarding issues or proposals not directly requesting funds
    - [rDAO](https://aragon.1hive.org/#/nrgiv/) for nrGIV token holders
3. Wait for results.
4. Execute required actions.
---
id: history
title: The History of Giveth
---

Giveth has a rich history, from humble beginnings to grand visions, building the Future of Giving. Here we share our story in hopes of inspiring other communities that want to work in a decentralized way.

## 2016
In the second half of 2016, Giveth is founded by Griff Green, Jordi Baylina and a couple of other members of the White Hat Group. They wrote the [MiniMe Token](https://medium.com/giveth/the-minime-token-open-sourced-by-giveth-2710c0210787) contract, [Vault](https://medium.com/giveth/the-vault-contract-open-sourced-by-giveth-fe2261f7b91b) contract and [MilestoneTracker](https://github.com/Giveth/milestonetracker) contract.  Near the end of the year Vojtech Simetka and Grace Torrellas join to round out the team and the Giveth Slack is created.


## 2017
### Q1
A first project website is published under [https://giveth.io](https://giveth.io)

### Q2
A first version of the Donation Application (DApp) is [launched](https://medium.com/giveth/giveth-donation-3-0-the-soft-launch-bf00d3bddca8) on the Ethereum mainnet.

### June
[Meeting](https://youtube.com/playlist?list=PL4Artm1rmCWGyz-BWv1-8Ip26XIauCLo9) of core contributors in Berlin to talk about the [concept and vision behind Giveth](https://youtu.be/i8kjxGxGSkA).

### July

On July 19, the White Hat Group was finishing up a Giveth Product meeting when they heard that a hacker had stolen the equivalent of $32 million of ETH by breaching a wallet. The Giveth Devs immediately began protecting 500 susceptible wallets by taking advantage of the same vulnerabilities and emptying the wallets’ cryptocurrency before the other hacker could.

In the only first account, they rescued a staggering 47,000 ETH! They went on to empty each of the 500 vulnerable wallets, siphoning the funds into a secure Giveth account. The Giveth team maintained transparency via Reddit so the wallet owners knew they would see their funds again.

By July 31, the Giveth team had created new, secure wallets for each of these accounts, and gave access back to their rightful owners. At the time, they rescued over $208 million worth of crypto, and stated they would not be accepting any donations for their work.

[Team meeting](https://youtube.com/playlist?list=PL4Artm1rmCWFUC5cP7Vw0y9wp7l0y5Fq0) in Barcelona to set a governance structure for team organization and to talk about the Giveth culture and the technology that has to be built.

**The Giveth team declares itself to be a [Decentralized Altruistic Community](https://medium.com/giveth/giveth-introduces-decentralized-altruistic-communities-dacs-d1155a79bdc4)** of Unicorns finding their way to #maketheworldabetterplace.


### August
The team decides to be organized in a [holacratic](https://www.holacracy.org/) way. Circles are created and governance meetings are held every week.

The [Reward DAO](https://medium.com/giveth/how-rewarddao-works-aka-what-are-points-7388f70269a) (a system to reward contributors for their work) is reworked and given stronger focus.

The Dev Team lays the groundwork for the new Giveth DApp in architecture and re-organization of code.

### September
[Team meeting](https://youtube.com/playlist?list=PL4Artm1rmCWE7j1ekvOrKg7ecUVivPA7O) in Barcelona is held to organize and align the team efforts for `Devcon3`, where we want to present the DApp to the Ethereum developers community.

Reorganization of roles and Circles commences and the resulting structures are getting clearer. This is still an experiment; the team is not yet at the “end” of its exploration.

### October
[Preparation for `Devcon 3`](https://youtube.com/playlist?list=PL4Artm1rmCWEV2ID_zjNj9cQcv5QUn1pr). The team concentrates on organizing and preparing for the event, every Circle is contributing in its own way and the team is making a big effort.

Governance meetings are maintained, the general structure of Holacracy is working well.

Giveth [introduces](https://youtu.be/U3ajJiKLetY) it’s new logo to the world.

### November
`Devcon 3`  - The team is doing an amazing job representing and promoting [Giveth at Devcon](https://youtu.be/BzZ3otHnYf4). The effort is amazing and inspiring. We feel the full transcendence of every single team member and the Giveth DAC radiates as the sum of our parts align.

Discussions about Governance structure, projects, and budgeting that had been initiated before Devcon are discussed in the aftermath of the conference. A consolidation and reduction of roles is considered.

### December
A reduction of roles occurs - especially of those requiring regular rewards. The team is still in the process of finding the right way to organize themselves. For now the team is organized in four Circles:

  - **Governance** (modeling the DAC, organization & administration of the team, Reward DAO)
  - **Communications** (for the external communications of Giveth)
  - **Dapp Development** (all aspects concerning the Giveth DApp and its integration with the Ethereum blockchain)
  - **Social Coding** (as a laboratory for open source culture, tool and infrastructure-focused software development)

Due to the new budget, certain people have to change their roles within the team. Governance meetings are ongoing and holacracy is still the preferred organizational structure. The team's effort as a decentralized community is ongoing. In finding what works best, we realize it takes a whole lot of adaptability and trust when structures are in a constant flux (in our case established through familiarity between members). It takes bravery to look upon emerging technologies and dive in, looking for consensus. Alas, this is the nature of an exploratory venture.

## 2018

### January
The Flagship Giveth DApp is released at the height of the Ethereum bullrun - which unfortunately means the system we built is not affordable anymore for those seeking funding. At the time of release, the gas fees rise to a point where starting a campaign costs around USD 80 in gas fees.

Therefore Giveth becomes one of the first DApps [trying out new approaches](https://medium.com/giveth/tackling-ethereum-scalability-issues-29bd700b5060). Because no really usable sidechains exist at this point, we decide to try an experiment: to let most interactions occur on the Rinkeby testnet and bridge them to the Ethereum mainnet.

### February
Some members meet up in Chiang Mai, Thailand, to stay and hack together.

Inspired by Truebits "Merry Merkle" a small, easily forkable donation app is deployed - the "Donation Leaderboard".

Edu realizes a portal to record contributions as videos, called the ["Wall of Fame"](https://medium.com/giveth/it-takes-a-village-the-story-of-giveths-wall-of-fame-c9e9a8b4904f).

### March
Although the market entered a bear phase, gas cost remains high enough for us to be prompted to organize an initiative around scaling Ethereum mainnet. We invite the most promising teams in Ethereum to meet up and talk about different ways to increase transaction throughout and reduce fees for users. The mini-conference is called ["Scaling Now"](https://medium.com/giveth/scalingnow-summit-transcript-ea5373be8523) and takes places over two days, featuring workshops and speakers from projects such as: `Aragon`, `Status`, `Web3 Foundation`, `POA Network`, `TrueBit`, `Swarm City`, `Cryptokitties`, `Spankchain` and many more.

We meet an enthusiastic young engineer who calls himself Dapplion. He will become one of the driving forces of the DAppNode project.

### May
Giveth [participates](https://youtu.be/nBfqUcbkuxw) in Edcon’s Super Demo in Toronto and [wins first place](https://twitter.com/Givethio/status/992891817904562177)!

### June
Another, smaller scale, meetup follows. We discuss many internal things and try to resolve differences about the direction Giveth wants to take going forward.

DAppNode is being split off the core Giveth team as a separate team with Edu leading development, Dapplion coding full stack and Jordi as a guardian angel and first product owner.

After thoroughly testing and deploying the bridge solution, Giveth officially (but quite silently) moves the entire platform to the beta environment.

### July
A [collaboration with Aragon](https://aragon.org/blog/aragon-dac-a-new-community-effort-to-foster-aragons-development-led-by-giveth) begins (which will be short lived) and is a great learning experience for both teams involved.

### August
[`Camp Decentral`](http://www.decentralizeddanceparty.com/2017/09/07/camp-d%CE%BEcentral-at-burning-man-was-a-success/) is erected at Burning Man, Black Rock City - giving talks about crypto, blockchain and digital sovereignty all week.

### October
`Devcon 4`, the Ethereum developers conference, is coming to Prague and Giveth is present again with a huge delegation. Many new and old acquaintances are made and important connections within the blockchain space are formed. A blockchain enthusiast called Willy is handed a T-shirt by Lorelei and Dani - this is actually a significant event as demonstrated later in our history.

## 2019

### January/February
We meet up at our headquarters in Barcelona because it is time to move to a bigger place! Together we empty the big apartment and move to a huge inner city house that is still known and operated as [`the Giveth House`](https://numundo.org/center/spain/the-giveth-hacker-house). To this day it stands as a place open to all friends of Giveth.

### April
A delegation from Giveth and other friendly Devs tramp to the biggest hackathon in the world (they claim) - ODYSSEY in Groningen, NL - to hack together on some core concepts of the newly imagined ["Commons Stack"](https://medium.com/giveth/the-commons-stack-scaling-the-commons-to-re-prioritize-people-and-the-planet-fdc076aec4eb).

### June
The Giveth team has a [big meeting](https://youtube.com/playlist?list=PL6oqELoqsEmpP1JQJFrtVj1OWMPHZX6kL) at their new headquarters in Barcelona. We spend almost a week reshaping roles and goals for Giveth. The agenda is seemingly endless and we touch on all the points that are important to us: the DAO, the DApp and how we want to shape the future of Giveth and the Commons Stack.

### July
The crypto bear market takes its toll. It has become more and more quiet with the Giveth team as funding continues to be scarce. The decision is made to continue in "maintenance mode" - essentially quitting all of Giveth's non-essential operations. Feature development on the DApp is halted and Comms Circle goes into submarine mode, emerging only to sparsely tweet from time to time.

### Winter
Amin - a contributor to the DApp who surfaced through Gitcoin is starting to "freshen up" the DApp little by little.

## 2020
### February
Griff attends EthDenver 2020 as a judge where he meets Willy who, together with a couple of friends, realize their own donation platform during the hackathon. Their app is called "Coz" (Cause) and [wins](https://youtu.be/VU56KNY5uFc) the "Impact Track". Full of enthusiasm, Griff captures the crew with the idea to build a new DApp - a new Giveth together with the Coz team.

### July
The pace is picking up again. The first design phases for "Giveth 2" (later called Giveth.io) are finished by Marko.

Some old team members flock back to the mother goose to work on developing the new DApp (Giveth.io). Organizational patterns are re-introduced and more people are sought after to grow the team again.

### December
Amin was able to make the original Giveth DApp (now Giveth TRACE) beautiful, functional and stable within the last year.  He now assembles a team of rockstars to help him make it even better. Two distinct teams form to work on the two distinct DApps.

Dani brings in a bunch of enthusiastic people to build out the Community and Communications Circles. Giveth is now in "full swing" again.

## 2021

### February
Hiring spree on full time contributors. The Costa Rica Team emerges, significantly improving community outreach, communications and the organizational fabric of Giveth.

### March
“Giveth 2” officially [launches](https://medium.com/giveth/the-future-of-giving-is-here-d480388a3338) with the name **Giveth.io**. Boasting a simple UX, easy project creation and peer-to-peer donations with functionality on both Mainnet and xDai network.

Amin’s team of developers become a force to be reckoned with, dubbed the Middle East team. Their main focus is still, at this time, to take the original Giveth DApp (now called “Giveth TRACE”) to the finish line and launch it out of beta.

### April
Work begins in earnest on the next big Giveth project, rumours emerge about designing an “Economy of Giving”....

### June
The Costa Rica team meets Griff face-to-face and there is a gathering of Giveth minds to revamp the Giveth Vision, Values and Roadmap. The Middle East team meets in person across the puddle and the two groups connect over the web.

### July
The OG Giveth DApp from 2017 officially [launches](https://medium.com/giveth/giveth-trace-is-live-e91b0be1e1f6), with tremendous contributions from the Middle East Team. The flagship DApp sheds the husk of “beta” taking its final form as **Giveth TRACE**.

Another localized gathering of Givethers occurs at EthCC[4] in Paris. It’s a special moment for Giveth and the Ethereum community, having been the first large gathering since the beginning of the pandemic.

Griff [drops the bomb](https://youtu.be/_fATr5kA4h8) at [The DAOist](https://youtu.be/hBV5All5yM8) conference, also in Paris, announcing the GIVeconomy to the unsuspecting attendees and subsequently broadcasted to the world at large. The plot thickens.


### August
Integration begins on the technical level between Giveth.io and Giveth TRACE, both teams of developers begin merging into one.


# Offline Meetings

Quarterly, most of the team meets in person at a dedicated team meeting or a very big conference. The list below shows our past events.
- **2021/07 Paris, France** [EthCC4](https://ethcc.io/)
- **2021/06 Nosara, Costa Rica**
- **2021/06 Somewhere in the Middle East**
- **2019/08 Black Rock City**
- **2019/06 Barcelona**
- **2019/04 Cardona, Catalonia**
- **2019/02 Barcelona**
- **2019/01 Chiang Mai**
- **2018/10 Prague** Devcon4
- **2018/08 Black Rock City**
- **2018/06 Barcelona**
- **2018/04 Toronto** [Edcon](https://www.edcon.io/)
- **2018/03 Barcelona**
- **2018/01 Chiang Mai**
- **2017/11 Cancun** [Devcon3](https://blog.ethereum.org/2017/11/16/devcon3/)
- **2017/09 Barcelona**
- **2017/07 Barcelona**
- **2017/05 Berlin**
- **2017/01 London**


---
id: introCommunity
title: Community
---

**COMMUNITY…** has always been the foundation of Giveth, the sum of all parts.

**COMMUNICATION…** is the glue that holds these parts together.

**COMMONS…** is the publicly accessible resources that are shared, cultivated and managed together.

## Welcome to the Giveth Community Circle!

This circle is held down by the Communications team yet comprised of representatives from the other two Circles, as well as various working groups that may form. Here is where new contributors, project owners, campaign managers, collaborators, conspirateurs, catalysts and really all the cool cats come to play, learn, give and grow.

## Mission

Our mission is to be the living and breathing core of Giveth, an ecosystem of collective support, abundance and communication where we cultivate relationships and assist innovative projects with a focus on blockchain4good. We connect Givers and Makers with the Giveth Community through transparent, intentionally crafted and clearly communicated stories and resources.

## Goals

* **Build Community around For-Good Projects** by nourishing relations between Givers, Makers and the greater community through meaningful engagement, outreach, trust facilitation and conflict resolution - creating a safe space for community members to communicate their passion projects, then recruit help or guidance from peers.
* **Offer a Clear & Supportive Onboarding Process** as Giveth develops the Dapps, economy, DAO and ongoing new features. The community circle provides a well-defined, transparent and helpful onboarding process that supports the needs of Contributors, Communities, Campaigns, Projects and Donors as well as functions as a bridge for newcomers into the crypto space.
* **Coordinate External and Internal Communications** when broadcasting or sharing activity and development progress externally through the Giveth channels and social media - ensuring that the voice of Giveth as an organization is aligned with our overarching Values, Vision, Mission and Goals and that all Giveth Circles are represented.
* **Create a Network of Partners** by way of collaboration, relationship building and support of common goals with various strategic partner organizations as well as community members focused on blockchain4good and improving the ethereum commons - providing resources, education and sharing of best practices.
*Partners currently include communities like [Commons Stack](https://commonsstack.org/), [TEC](https://forum.tecommons.org/), [DAppNode](https://dappnode.io/), [BrightID](https://www.brightid.org/), [1Hive](https://about.1hive.org/), [Panvala](https://panvala.com/), [GitCoin](https://gitcoin.co/) and [MetaGame](https://wiki.metagame.wtf/).*

## How to Engage

* Community Calls are held every Thurday in the appropriate voice channel in the [Discord server](https://discord.gg/DAFkKdkykr) and can be found scheduled on the [Giveth calendar](https://calendar.google.com/calendar/u/0/embed?src=givethdotio@gmail.com&ctz=America/Costa_Rica). Feel free to join us!
* If you want to get a feel of what we discuss during the Community Call, most of the recordings can be found on our [Giveth Transparency YouTube channel](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg).
* You can read more on all of our initiatives on our [Medium blog](https://medium.com/giveth/) as well as engage with releveant topics and proposals on the [Giveth Forum](https://forum.giveth.io/).
* If you have any questions or are interested in contributing, feel free to reach out in the Discord server or [Telegram chat](https://t.me/Givethio). 
---
id: introDiscord
title: Discord Introduction and Tutorial
---

If you haven’t used Discord before, fear not! Use this guide to help you get started - enjoy the journey and discover welcoming spaces and channels that spark your interest. So, if you’re ready to dive in, here’s a brief introduction to get you started.


## Links
Onboarding site - https://giveth.io/join

Direct link to join Discord community - https://discord.giveth.io/

## How to join the Giveth Discord server

Log in to Discord or make a new user. - https://discord.com/ or download the app ([iOS](https://apps.apple.com/us/app/discord-talk-chat-hang-out/id985746746), [Android](https://play.google.com/store/apps/details?id=com.discord&hl=en_CA&gl=US))

[How to Use Discord](https://support.discord.com/hc/en-us/articles/360045138571-Beginner-s-Guide-to-Discord) : Video ([Beginner to Advanced](https://www.youtube.com/watch?v=tNUq5Aqv60s))

[Getting Started with Discord](https://support.discord.com/hc/en-us/articles/360033931551-Getting-Started)

Join the Giveth community server https://discord.giveth.io/
Inside each server, you can have a unique nickname so feel free to change yours to whatever you would like to be known as.

Once you have joined the server, a bot will send you a message with a Captcha to solve - you're not a robot are you? It should look something like this:

![](https://i.imgur.com/XCaAhgo.png)


## Channel Descriptions

### Welcome (start here)
**`#🤝welcome`** is our landing channel and contains tips to get you started, including links and basic faqs.   
**`#👋say-hi`** to the community and tell us what you're working on, what brought you here or what you need help with.     
**`#✋assign-roles`** allows you to assign yourself to roles, which automatically opens the relevant channels and gets you tagged in working-group related posts.    


### Notice Board   
**`#📢announcements`** is where you will find announcements from the Giveth community.   
**`#📅event-calendar`** weekly and regular meetings and events are listed here in your local time. You can click to add events to your Google calendar.    
**`#📌team availability`** accessible to team members only - the place where you can find who is on vacation or not available. Let us know when you are on vacation or not available, so we don’t bug you when you’re AFK.    
**`#📋help wanted`** if you’re interested in joining Giveth and our greater contributor Galaxy - connect here to learn about open job positions.   
**`#📚partner-updates`** is where you will find announcements from our Galaxy partners.  


### Support  
**`#💬support`** if you run into any problems, or need to ask a general question, post it here; please tag @admin or @support. Don’t forget to search the channel to see if there is already info on that topic.   

Hop over to any of these channels if your question relates to any of the following:    

- project-onboarding   
- project-verification  
- givbacks  
- faq (in MAKER and GIVER channels)  
- using-crypto channels if your question relates to any of these topics.  

**`#🤝project-onboarding`** is where prospective project owners can go for suggestions or advice about the project creation flow and how to create engaging and impressive projects on the DApp.  
**`#⭐project-verification`** channel is where the Project Verification Team collaborates to review new applications and nominations for future verification invites.  


### Community
**`#😄 communitas-headquarters`** a place of new ideas, initiatives and co-creation to make Giveth Community a better place for every member.   
**`#🙂 daily happiness`** share what makes you happy.   
**`#❤ praise`** rain praise upon your teammates! Let them know that you recognize the value they add to the various Giveth projects and community by typing "/praise '@username' for 'awesome thing that they did'" and ensure they get rewarded with GIV tokens for their contribution to the community. Follow Praise Bot’s instructions to activate your Praise account (you will need to connect your ETH wallet) and start collecting your rewards when someone /praises you.   
**`# general`** for when your post doesn’t seem to fit nicely into one of our channels? Jump into the General channel and let us know what’s on your mind. We can chat there or guide you to a channel that fits.  
**`#💡 ideas`** is a place for you to share inspirating and creative suggestions.  
**`#✨ shtsnggls`** is for pure fun.  
**`#🐦 tweeeeeter`** is where you will find all things related to the Giveth Twitter. It can be used for suggesting or drafting tweets, feedback regarding Twitter and sharing or promoting tweets to get more engagement. Please ask to become part of our Tweeeeter team to amplify Giveth message on Twitter using our Tweet bot.  
**`#🐸 memes`** are powerful! We host weekly meme parties where we listen to music and pump out spicy memes. The schedule can be found in the [calendar](https://calendar.google.com/calendar/u/0/embed?src=givethdotio@gmail.com&ctz=America/Costa_Rica).  
**`#💸 shill-your-project`** share info about your project, join discussions and expand fundraising frontiers in support of fulfilling Giveth's mission.   
**`#➿ feedback`** through Typeform collected on the platform (giveth.io) is displayed in this channel.  


### Global  
**`#🌎 latam`**  
**`# PT português`**  
**`# ES español-spanish`**  


### Collaborator Space
**`#🥇 bounties`** view tasks and apply for bounties in this channel. Click on each task to discover what’s required, what skills are needed, rewards offered, how to apply and the status.   
**`#🤝 partner-threads`**  
**`#💬 collab-chat`**  want to collaborate with Giveth? Have a proposal? Head to the collab-chat channel and we’ll let you know the next steps.  


### Giver Space
**`#❔faq`**  
**`#👣 project-activity`**  
**`#🎁 givbacks`** go here if you want to keep up-to-date with GIVback rounds, distributions and support?  
**`#💬 giver-chat`**  is a great space for givers to talk about projects they support and causes they are interested in.  


### Maker Space
**`#❓ faq`**  
**`#🧮 fundraising-101`**  share tips and learn about fundraising in crypto.  
**`#💱 using-crypto`** this channel is for sharing info and support on all the different ways to access and use your crypto donations.   
**`#💬 maker-chat`**  this channel is a great space for makers to network with other makers.  


### Communications
**`#📣 communications`**  hub of the Communications Team. You can find us here creating content, performing outreach and all things that are included in the Communications Circle. If you need the attention of the team, you can tag @Comms Stars in your message.  
**`#🗒 docs`**  let's talk about Giveth docs!    
**`#🖋 docs-translations`**    


### GIVernance  
**`#🌐 dao`** provides links to DAO proposals and informs the community when it's time to vote. You can discuss anything proposal-related in this channel.  
**`#👍 governance`** is where we experiment with decentralized governance and document anything that could be useful for future communities like ours.  
**`#🔑 multisigs`** channel is for the operators and signatories on the Giveth multisigs.  
**`#   giveth-trace-payments`** is used to communicate information about payment transactions happening on the Giveth TRACE bridge. You can find more information about how the bridge works [here](https://docs.giveth.io/dapps/bridgeSecurity).  
**`#🏆 rewards`**  is where the rewards team hang-out.  


### Devs
**`#👌 all-dev`** is the channel for general development discussions that include the Giveth Development Team as a whole.  
**`#☝ givethtrace-dev`** is the hub of communications for the Giveth TRACE DApp Development Team.  
**`#🐇 test-reports`** is for test reports and testing communication for both Giveth DApps.  


### Design  
**`#🌈 design`** is for design idea sharing and creative activity on the look, feel and language of any UI or UX updates in the pipeline for Giveth products.  


### GIVeconomy
**`#💹 giv-economy`** is the place to share information about about Giveth tokenomics and its continuous evolution.  
**`#🧲 giveth-fundraising`** is where the fundraising team hang-out.
**`#🔬 givbacks-distribution`** is where the GIVbacks review team hang-out and post GIVback distribution voting links are posted.


### Operations
**`#🚨 raise-incident`** A message sent in this channel will trigger automated incident management - be careful, you might wake somebody :)  
**`#❔ incident-status`**   
**`#   ops`**  


### Bridges
**`#🐝 1hive`** serves as bridge channel to our busy bee neighbors at [1Hive](https://about.1hive.org/).  
**`#🌐 te-commons`** links the Giveth server to the vast community of token engineers over at the [TEC](https://tecommons.org).    
**`#🐙 metagame`** bridges to a channel in the [Metagame](https://about.1hive.org/) discord server.  
**`#✨ general-magic`** allows our server to be connected to our friends at [Panvala](https://panvala.com/).  


### Monitoring
**`#  devops-monitoring`**  
**`#  github-log`** is to cross notify pull requests and new Issues in Github in order to increase transparency, and engagement on Github.  
**`#  giveth-io-event-log`**  is used as a log for Segment events that are tracked on Giveth.io.  
**`#  segment-dev`**  relays events from dev environments.  


### Server Stats  
**`#  daily-stats`**  


### Voice Channels
These channels are used for voice and / or video chats with community members.

**`#chip-playlist`** is a text channel used for typing Chip Bot commands. <a href='#chip'>(More about bot commands **below**)</a>  
**`Community`** is used as a meeting place for the Community Circle working groups as well as weekly Community Calls.  
**`🦄-only`** is used as a meeting place for Giveth core-team members.  
**`Communications`** is where the Communications Team gathers for weekly syncs and hack sessions.  
**`DAO only`**
**`Developers`** is a meeting place for the Platform Circle working groups.  
**`Governance`** is the voice channel for our weekly Governance and DAO working group discussions.  
**`GIVeconomy`** is where GIVeconomy working groups gather for weekly syncs and hack sessions.

**All meeting times can be found on the [Giveth Calendar](https://calendar.google.com/calendar/u/0/embed?src=givethdotio@gmail.com&ctz=America/Costa_Rica).*

### Tagging
You can tag certain roles by using "@" followed by the role. You also can tag an individual with "@" followed by the person's handle or nickname.

#### Roles

### Roles that can be self-assigned in the "assign-roles" channel
**@Giver** People who love funding for-good projects. You can assign yourself this role in the `#🤝welcome` channel by reacting to the bot message with the 💝 emoji.  
**@Maker** People who are working hard to make the world a better place. This role can also be self assigned in the `#🤝welcome` channel by reacting to the bot message with a 🦄 emoji.  
**@Collborator** People who want to collaborate or complete bounties.  
**@Community Circle** People who want to get involved with our community.    
**@Givernance Circle** People who are interested in discovering more about Giveth governance.  
**@Platform Circle** People who are interested in the development of the Giveth platform.  

**@Unicorn** - People who regularly attend calls and are very actively contributing to Giveth.  
**@DAO** - rGIV token holders. You can obtain rGIV tokens by consistently contributing to the community.  
**@Comms Stars** - Communications Team members.  
**@Community Support** - Members of the Community Support working group.  
**@Governance** - Members of the Governance wroking group.  
**@Design** - Members of the Design working group.  

### Bot Commands

#### PraiseBot
At Giveth, we love to acknowledge the value that each member brings to the community and provide recognition for the awesomeness that they contribute. The praise given is tracked by PraiseBot and used to calculate rewards for active contributors.

You can praise a fellow community member in any channel by typing **`/praise`** followed by "@" and their username. Don't forget to mention why you're praising them.

**For example:** `/praise @WhyldWanderer for creating such an amazing Discord Guide` :stuck_out_tongue:

Once you have typed your praise, you will know that the bot has tracked it because a ✅ emoji will appear as a reaction to your message.

When you receive praise, you will be notified by the bot in your direct messages with a link to the message where you were praised.


#### Simple Poll Bot
This bot can be used to create a straw poll such as this one:

![](https://i.imgur.com/ExLeqzW.png)


To create the poll shown above, you would simply type the command as follows:
`/poll "What is the best poll bot?" "Simple Poll" "R2D2"`

By following this template, you can create as many answers to the question you would like and community members can answer by reacting with the corresponding emoji.
`/poll` `"Question"` `"Answer #1"` `"Answer#2"` `"Answer #3"` ..etc.

#### <span id='chip'>Chip Bot</span>

[Chip bot](https://chipbot.gg/home) can be invited to any of the voice channels on the server. Once you have invited the bot into the channel, anyone can type commands in the **`#chip-playlist`** text channel to start playing or queuing songs. Here is a list of the available commands:

**`ch!p`** *'`link or search query`'* - Loads your input and adds it to the queue; If there is no playing track, then it will start playing  
**`ch!queue`** - Displays the current song queue  
**`ch!skip`** - Skips to the next song  
**`ch!clear`** - Removes all tracks from the queue  
**`ch!skipto`** *'`track position or title`'* - Skips to the specified track  
**`ch!lyrics`** - Displays lyrics for the currently playing track  
**`ch!pause`** - Pauses playback  
**`ch!resume`** - Resumes playback  
**`ch!remove`** *'`track position or title`'* - Removes the specified track from the queue   
**`ch!stop`** - Disconnects the bot from your voice channel and clears the queue  
**`ch!shuffle`** - Randomizes the current order of tracks in the queue  
**`ch!nowplaying`** - Displays information about the current playing track.  

Chip bot can play music from a multitude of sources including Spotify, YouTube, Soundcloud, etc. In order to have Chip bot play from Spotify just click on Share > Copy Playlist Link > copy this into your chat with the `ch!p` tag and you’re all set.

### Support
If you run into any problems, or need to ask a question, please tag `@admin` or ask in the `#💬support` channel. 
---
id: introGIVernance
title: GIVernance
---

**GIVE**… to the causes, projects and actions you care about.

**GET**… the tokens that give back to those who are GIVing forward for positive change.

**GOVERN**… project curation, product development and a new economy based on altruism.

## Welcome to the GIVernance Circle!

Giveth aims to be a donor-focused organization that GIVs back to those who use our platform to transparently and accountably support change in the world.

We value transparent, holistic governance and hope to be a shining example of it. We explore and readily adopt new innovations that support us in embodying these values. We believe in the self-organizing power of sociocracy, which we apply in the organization of tasks, participation in the [Proposal](https://forum.giveth.io/t/proposal-template/303) and [Advice Process](https://docs.giveth.io/whatisgiveth/adviceProcess/), and facilitation of our governance meetings.

Our circle is uniting the power of our [Decentralized Autonomous Community (DAC)](https://trace.giveth.io/community/giveth-dac) with the non-profit advantages of our [Donor Advised Foundation (DAF)](https://www.sdgimpactfund.org/giveth-foundation) to iterate upon the creation of our governing [Decentralized Autonomous Organization (DAO)](https://aragon.1hive.org/#/giveth/).

## Mission

We are progressively decentralizing the Giveth decision-making process by building a community and a token-based economy around our platform that recognizes contributions, values participation and rewards altruism.

## Goals

- **Demonstrate Fiscal Accountability** by responsibly provisioning funds and skills toward team structure, conflict resolution, administration, financial transparency, organization of team gatherings and quality assurance. Meet the resource needs of the Giveth community, platform and economy.
- **Innovate Internal Governance** through experimenting with and documenting decentralized governance systems within the Giveth DAO structure (e.g. Sociocracy, RewardDAO, Conviction Voting, SourceCred, etc.) that could prove useful for future Decentralized Autonomous Organizations to learn from and implement their own versions.
- **Collaborate with the Ethereum Ecosystem** to develop collaborative tools that generate mutual benefit and success by partnering with and participating in the governance of other mission-aligned organizations such as: [Commons Stack](https://commonsstack.org/), [Token Engineering Commons](https://forum.tecommons.org/),  [DAppNode](https://dappnode.io/),  [BrightID](https://www.brightid.org/),  [1Hive](https://about.1hive.org/),  [GitCoin](https://gitcoin.co/) and [MetaGame](https://wiki.metagame.wtf/).
- **Create Regenerative Value** that nurtures and grows the Giveth Token Economy (GIVeconomy) by empowering individuals toward inclusive decentralized decision making with outcomes that have real impact on the organization and positive change in the world when cascaded through our listed projects.

## How to Engage

- The [Discord channel for all things Governance can be found here](https://discord.com/channels/679428761438912522/762764762164887562). If you haven’t already joined our Giveth Discord server, [we invite you to connect with us here!](https://discord.com/invite/965AGEaz)
- Participate in the weekly GIVernance Meeting online, as scheduled on the [Giveth calendar](https://calendar.google.com/calendar/embed?src=givethdotio%40gmail.com&ctz=America%2FCosta_Rica). To get a feel of what we discuss during our weekly meetings, recordings of past calls can be found on our [Giveth Transparency YouTube channel](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg).
- Anyone can create and submit a proposal to members of [Giveth's Reputation DAO](https://aragon.1hive.org/#/giveth/)! We request that proposals go through an Advice Process by starting with a [discussion on our Forum](https://forum.giveth.io/).
- You can read more about all of our initiatives on our [Medium blog](https://medium.com/giveth/), and find documentation in the [Governance 2 folder](https://drive.google.com/drive/folders/1Jv2xcYsbMTqmUtDOfWV6yT0vy51PVW1J?usp=sharing) on Google Drive. Historical information on previous Giveth Governance iterations are archived in this [Trace Governance folder](https://drive.google.com/drive/folders/15LF6NQx9KJDRtT1hACKIrNFr1rwAbAgZ?usp=sharing).
---
id: introPlatform
title: Platform
---

**DESIGN**… the best user experience in a beautifully simplistic interface.

**DEVELOP**… innovative, feature-rich, safe and productive tools for transparency.

**DELIVER**… seamlessly connected products (giveth.io and TRACE) that work well together.

## Welcome to the Giveth Platform Circle!

The Giveth Platform Circle is the terminal for designers, developers, testers, systems engineers and product managers alike, and is where the Future of Giving is being built. We collaborate with the Community Circle to get feedback from our users and design experiences that make it easy for people to create, give, receive and trace.

The Platform Circle, while building high-quality products, proclaims success by encouraging its members to learn, grow, collaborate and celebrate achievement together. By building workflows that are inclusive, transparent and well-structured, we thereby build strong teams of talented and inspired contributors.

## Mission

To empower our contributors with the knowledge and resources to build and maintain platforms that bridge communities, meet user needs and advance blockchain technology.

## Goals

* **Develop Digital Public Goods** that serve as open-source, efficient and free platforms that bridge Givers and project owners, harnessing the revolutionary funding opportunities of digital currencies.
* **Product Development and Maintenance** that empowers contributors to research emerging technology and implement best practices to create robust, stable, secure and scalable platforms.
* **Improve User Experience, Usability and Accessibility of Blockchain Technology** by engineering and continually creating intuitive interfaces and powerful user experiences to make donating easy, rewarding and effective.
* **Build DApps by and for the Community** by implementing user feedback to create products that meet their needs and maintain a high level of transparency to support a network of value-aligned projects.

## Our Products

We maintain two Donation Applications that facilitate contributions to for-good projects on the Ethereum blockchain:

* [**Giveth.io**](http://giveth.io/) - Boasting a streamlined UI and an easy user experience, it offers direct peer-to-peer giving. Giveth.io grants anyone the ability to create projects and receive funding in minutes.

* [**Giveth TRACE**](http://trace.giveth.io) - Our original DApp, has a larger scope - offering enhanced complexity and traceability for projects. It also allows users to specify and track their donations.

The **GIVeconomy** is also being built by this circle and will involve the creation and deployment of on-chain systems to ensure the yet-to-launch Giveth Token Economy remains secure, efficient and accessible.

## How to Engage

* Weekly Developer meetings are held in the[ Giveth Discord](https://discord.gg/vaTcgqMwVp) -[ Add to your calendar](https://calendar.google.com/calendar/u/0/r?cid=givethdotio@gmail.com)
* Join the[ #all-dev](https://discord.gg/vaTcgqMwVp) or[ #design](https://discord.gg/T6SYzH3rnD) channels in Discord to follow development and design discussions
* Watch meeting recordings on the[ Giveth Transparency Youtube](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg)
* Track development and fork our code on[ Github](https://github.com/Giveth)
---
id: meetingsGuide
title: Meetings Guide
---

## Meeting Planning
* Please announce the meeting a few days in advance. You might want to use the advice process and [Doodle](https://doodle.com/dashboard) to find a date if the meeting is not regular.
* Be sure that there is at least one person taking notes in the meeting.
* Be sure that there will be somebody present who is capable of streaming the meeting.
* We use [Interspace](http://breakout.interspace.chat/) or [Discord](https://discord.gg/cCsYnNDkq2) for our meetings.
* Please don't forget to announce the meeting in the #scheduling channel of Discord before you begin.
* There should always be an introductory round and a closing round.
* After the meeting, please make sure the notes are saved in [Notion](https://www.notion.so/giveth/Giveth-2c97e0eca91e43238565c8f79dfe5e8d), a link to the notes is posted in the #meetingnotes channel of Discord, and the video is published to our [Transparency YouTube channel](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg).

## Note Taking
* There should be a designated note taker for each meeting.
* We use [Notion](https://www.notion.so/giveth/Giveth-2-0-2c97e0eca91e43238565c8f79dfe5e8d) for record keeping of our meeting notes.

## Streaming and Video Recording

We record and/or livestream our online video conferences for record keeping, to support our team and to uphold our values of transparency and accountability. You can find recordings of our meetings on the [Giveth Trasnparency YouTube Channel](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg).


#### How to record meetings for Giveth Transparency:


* We use OBS to livestream and record our video calls. You can download it [here](https://obsproject.com/).
* During installation select "Optimize for streaming, recording is secondary".
* Select YouTube as the streaming service and input the Giveth Transparency YouTube Stream Key. If you need access to the Stream Key, please ask one of our team members.
* In general, the recommended settings in the setup wizard are already optimized for your device, but feel free to adjust them.
* Setup your video and audio sources; we recommend using Window Capture for streaming calls.
* When you are ready to stream the meeting, select the appropriate window to capture and select "Start Streaming". Your video will be automatically livestreamed on YouTube.
* For a more thorough setup guide, check out [this video](https://www.youtube.com/watch?v=qiRu-NRgso0) from our friends at the Token Engineering Commons (TEC).

# Governance of Meetings

*If you are looking for more notes on past Giveth DAC/Community Meetings, you can find this [here](https://wiki.giveth.io/dac/meeting-notes).*

## Meeting Types & Intentions
Giveth aims to operate meetings that are  efficient, connective, fair, transparent and heart-centered. We do this by honoring time and agreements that the collective has agreed to. Some meetings like our weekly Sunday Community Call are intended to deliver updates and highlights so that all circles can understand the latest and greatest of one another, and be in alignment. In our Community Call, the time is not to brainstorm ideas or make decisions but rather to share updates.

Other meetings, like our weekly Monday Governance Call aka GIVernance, are intended to present proposals and field objections or feed-forward from the group. Besides these larger, recurring group meetings, Contributors can schedule 1 on 1 or small group work sessions to bring a specific task through to completion. These meetings gather necessary participants to focus on a goal and drive it home.

## Meeting Roles
*There are specific roles to be filled. In general, we use roles to avoid things getting personal. For instance, it is not that Griff is interrupting Dani, but rather that the Facilitator is making sure the Smart Contract Reporter respects the meeting's process.*

### The Facilitator
The Facilitator needs to stay curious and calm. They make sure the meeting process is RESPECTED at all costs, like a referee. The Facilitator is encouraged to interrupt when people are getting off topic and is discouraged from making extra commentary or from coaching. It is very important that the Facilitator stay neutral.

The Facilitator holds the space so that people can process their tension on their own and react as they need to express themselves freely in a safe, controlled environment.


### The Note Taker
Note taking is important because it allows us to capture meeting highlights in a clear, organized way and store them in Notion, our shared transparent tool. The Facilitator can also be the Note Taker for smaller meetings, but in general it is best if they are 2 different people.

The most important task is to record the agenda items. Everything else recorded is bonus :-D. The Note Taker has the responsibility the go to the person when there is a conflict interpreting the results of the meeting.

After the meeting, the Note Taker will share a link to the meeting notes in the #meetingnotes Discord channel.

### The Livestream Recorder
The Livestream Recorder is in charge of recording and publishing the audio/video recording of the meeting in the Giveth Transparency YouTube channel. In order to properly fulfill this responsibility, it is important that the Livestream Recorder be on time and present for the duration for all meetings that they are responsible for recording to ensure everything is being captured and shared transparently.

### The Proposer
The Proposer is the person who put a tension on the agenda for the group to discuss. A 'tension' is languaging commonly used in sociocracy and holacracy. When someone has an objection, it's an issue, or tension, that needs to be processed - usually by way of creating or adapting the proposal until the tension is alleviated and the proposal/solution can be passed.

It is the Proposer's responsibility to propose a solution to the tension and it is their responsibility to make sure that their solution will alleviate the tension. It is NOT their responsibility to solve other people's problems. One tension at a time.

Don't feel pressured to solve other people's problems with your solution. Everyone is an adult and we need everyone to take care of themselves. That starts with you taking care of your responsibilities. You do not have to take any of the feedback you received.

### The Reactors
The Reactors are everyone who is not the Proposer during the decision making process. They are encouraged to freely react however they want during the reaction round.

### The Objector
The Objector needs to stay curious and calm. They are anyone who believes the proposed solution to the Proposer's tension would cause harm or move Giveth backwards. If they have a simple concern about the proposal or think something should be added to the proposal but don't believe the proposal would concretely cause harm or move Giveth backwards, then it is not a valid objection and it should be ruled as an invalid objection by the Facilitator.

## Sample Meeting Flow

*A Facilitator and a Note Taker for the meeting should have been chosen ahead of time and once everyone is at the meeting, the meeting can begin.*

For our GIVernance Call specifically, we follow many of the sociocratic principles. This meeting is structured following the example of governance meetings in sociocracy.

The purpose of a governance meeting is to:
- Create, remove or modify the Roles of the Circle
- Create, remove or modify the Policies of the Circle
- Elect people to the core roles of the Circle

Now we will walk through a sample meeting flow and governance process:

#### 1. *Optional Centering*
The Facilitator may choose to begin the meeting by leading the group through a centering practice to ground everyone's energy and tune into the same frequency. This may look like breathwork, a short meditation or visualization, sharing an inspirational quote or a combo platter.

#### 2. Check in
Everyone voices what is most alive for them, reveals any momentary personal distractions and states a 30 second or less intention for the meeting. One person speaks at a time. This is not a time for responses or discussion.

#### 3. Facilitator States Meeting Logistics
A simple space to triage any administrative and logistical issues to take into account for the meeting. E.g., We have 2 hours for the meeting; Jen needs to leave early; this meeting is being live streamed and has 25 viewers so far; we'll be bringing lunch at 1pm; etc.

#### 4. Building the Agenda
The Faciliator introduces the pre-prepared meeting agenda and then opens the space for additional agenda requests before diving in. Agenda items may be submit ahead of time via Discord, previous meeting discussion and/or curated by the Meeting Facilitator.

The goal is to build an agenda of tensions, or topics, to process. There is no specific order and anyone can add items to the agenda. The Note Taker captures the agenda items for everyone. The Facilitator will determine the order these agenda items are processed.

#### 5. Process each agenda item with the Integrative Decision Making process
The Facilitator encourages everyone to take notes and determines the order these agenda items are processed on the fly.

##### Present Proposal
Either the Meeting Facilitator shares the update/highlight with the group *-or-* the Proposer describes the tension and in one sentence makes a proposal to resolve it. The proposal should in general be a creation of a circle, role or policy. Only the proposer speaks during this time.

##### Clarifying Questions
All the meeting participants may ask clarifying questions about the tension or proposal to ensure they have a good understanding. The Proposer then has a chance to respond to questions. This is not a space for back and forth discussion.

It's NOT allowed to use clarifying questions to give an opinion about the proposal. Opinions, suggestions, reactions... all should be left for the Reaction Round coming next. The Facilitator will cut off any question that's conveying an opinion or isn't intended to better understand the proposal. There is no hard line between clarifying question and reaction, and it's at the Facilitator's discretion to discern between the two.

##### Reactions
One at a time, each person reacts to the proposal as they see fit. No response or interruption is allowed during someone's reaction. Any type of reaction is welcome, from intellectual critiques to emotional outbursts. The only caveat is that reactions should not be engaging someone in particular. Everyone reacts except the Proposer.

Reactions are the only step of the governance meeting when people can speak freely. It's a perfect phase for providing different perspectives and suggesting improvements to the proposal, so that the Proposer can integrate those changes if he or she likes them.

This is the dangerous part of this meeting if people want to keep talking and talking… that is ok, and HAS to be allowed. This could make these meetings long.

##### Amend & Clarify
After all reactions are complete, the Proposer can optionally clarify the intent of the proposal, or amend it based on the reactions. Only the proposer speaks; no discussion allowed.

Although the proposer can modify the proposal however they want, the goal is for the Proposer to amend their proposal if they found a better way to address their tension. It's not his or her job to address all the concerns and reactions heard during the reaction round, or even to make improvements that were suggested by other participants.

Watch out for proposal creep.

##### Objection Round
One at a time, the Facilitator asks each participant if they see "any reason why adopting this proposal would cause harm or move Giveth backwards." The proposer also gets the opportunity to raise an objection. Objections are stated, tested and captured without discussion. One person may have several objections, and everyone's objections must be captured before we move to the next step.

If there is no objection, the proposal is adopted and we move to the next agenda item.

The Facilitator will need to test the objection occasionally to determine if the objection is valid or to help the Objector clarify the objection. To test, there are 3 questions to ask:

* How do you believe adopting this proposal would cause harm or move Giveth backwards?
* Does this objection still exist if this proposal wasn't implemented?
* Is the proposal good enough for now and safe enough to try, knowing we can readdress this later if problems arise?

##### Integration
If one or several Objections were raised, the Facilitator moves to the Integration step. The goal is to amend the proposal so that it would not cause the Objection, and would still address the proposer's original tension. Objections are integrated one at a time. For each objection, the Facilitator facilitates a discussion to help integrate the objection. Mostly the Objector and the Proposer speak, but others can help as well. The discussion stops as soon as the Objector and the Proposer have both agreed that an amended proposal would not cause an objection while still addressing the Proposer's tension. This is not a place to debate the value of the proposal or the objection! We need to focus on finding an acceptable amendment to the proposal that both the Objector and Proposer agree on. MOVE FORWARD ASAP!

Once all objections are integrated, go back to an Objection Round to ensure there is no new objection.

#### 6. Check out
Each person has an opportunity to share a closing reflection on this meeting. No discussion.

#### 7. Transparency Publishing
The Note Taker posts the meeting notes in the #meetingnotes channel on the Giveth Discord.

The Livestream Recorder publishes the audio/video recording of the meeting in the Giveth Transparency YouTube channel. 
---
id: toolsDecentralizedCommunities
title: Tools for Decentralized Communities
---
### Distributed teams need distributed tools!

Although we try to meet in person too, the most important aspect of running interconnected teams whose members are scattered around the globe comes down to the tools at our disposal. We always try to find the most open and expandable software tools to improve our organizational capability.

When we are looking at available software for organization, open-source comes first, usability second. Sometimes we have to make our own tool or most likely expand on the work previously done by others. Explore our world-readable logs on Youtube, our Docs and the Chat - It should give you a good impression of who we are and what we are working on.

### Chat
The Giveth community mainly communicates through these platforms:
[Discord](https://discord.gg/DAFkKdkykr) is currently the recommended option for joining the community. We also have a telegram chat that is bridged to our server.
[Telegram](https://t.me/Givethio) is also used and the chat group is bridged to the general channel in Discord.

### Documents and Files
The Giveth DAC uses cloud-storage services for transparent document management. Most of our working documents are hosted and shared within [Notion](https://www.notion.so/giveth/Giveth-2c97e0eca91e43238565c8f79dfe5e8d).

### Organization
Currently we are evaluating [AragonDAO](https://aragon.1hive.org/#/giveth/) which is an excellent decentralized solution for decision-making.

### Accounting
Transparent tracking of spending on our own [Donation Application](https://trace.giveth.io/community/giveth-dac).

### Medium
You can find news and updates on our [Medium](https://medium.com/giveth) page.

### Youtube
[Giveth Main Content](https://www.youtube.com/givethio)
[Giveth Transparency Channel](https://www.youtube.com/channel/UCdqmP4axeI1hNmX20aZsOwg)
---
id: whatisgiveth
title: What is Giveth?
slug: /
---


Giveth is building a culture and economy that rewards and empowers those who give. Our goal is to use web3 to radically transform how public goods are funded by helping nonprofits evolve out of systems that depend on sacrifice into ones that create win-win situations for everyone involved. Beginning with a free and direct crypto donation platform on Ethereum, we onboard for-good projects and support them so that they can eventually blossom into DAOs with their own regenerative economies, with Giveth itself becoming an impact investment hub for public goods.

Currently with its fundraising platform, Giveth rewards donors directly through the GIVbacks program with GIV, which they can then stake to support projects and earn returns via GIVpower. Other recent and forthcoming radical innovations can be seen in the Giveth Roadmap below. Also visit our [calendar](https://calendar.google.com/calendar/u/1?cid=Z2l2ZXRoZG90aW9AZ21haWwuY29t) for meeting times and [Join Page](https://giveth.io/join) to get more involved.

## **Our Mission**
**To build a culture of giving that rewards and empowers those who give - to projects, to society, and to the world.**

## **Our Vision**

**Giving is effortless, and people all around the world are rewarded for creating positive change.**

## **Our Values**

**Giveth encourages decentralization:**

- Giveth offers innovative open-source solutions built on blockchain technology, which is inherently decentralized.
- Giveth is pioneering and experimenting with decentralized governance and communication techniques and supporting their adoption by other communities.

**Giveth promotes Altruism:**

- Giveth is an open, non-hierarchical global initiative empowering social, environmental, and humanistic impact projects with modern technologies.
- Giveth supports many like-minded initiatives that are adding value to the world without necessarily having a direct profit motive.
- Giveth is building a self-sustaining giving economy that encourages and rewards altruistic intention.

**Giveth believes in the power of Community:**

- Giveth is an inclusive community united around a common goal.
- Giveth is a community-owned platform, building and developing our DApps based on feedback from our members.
- Giveth enables trust within communities by increasing transparency and accountability through blockchain technology.
- Giveth proactively reaches out to similar initiatives which we see as potential collaborators, as opposed to competitors.

---
## **Our Roadmap**
Giveth supports for-good projects and public goods in a myriad of capacities, one only needs to look at our token economy (GIVeconomy) roadmap features:

**[GIV](https://docs.giveth.io/whatisgiveth/givtoken/)** - A transferable ERC-20 token that lies at the heart of the Future of Giving.

**[GIVbacks](https://giveth.io/givbacks)** - A donors rewards program that is the first step in the ambitious GIVeconomy leading projects to become regen economies. The GIVbacks program allows donors who contribute to verified projects to receive GIV in return. This feature flips the script on the concept of the tax deductible donation, creating a decentralized and borderless way of incentivizing donations. (LAUNCHED ✅ )

**[GIVgarden](https://gardens.1hive.org/#/xdai/garden/0xb25f0ee2d26461e2b5b3d3ddafe197a0da677b98)** - A voting platform built by 1Hive where GIV token holders are able to propose and vote on how to use the Giveth community treasury, including funding external builders, sponsorships and public goods. (LAUNCHED ✅ )

**[GIVpower](https://docs.giveth.io/giveconomy/givpower)** - A staking mechanism where donors can lock their GIV tokens for GIVpower and use them to boost and curate fundraising projects on the [Giveth.io](http://giveth.io) platform. Projects with more GIVpower are ranked higher and in turn, their donors are rewarded with more GIVbacks. (Q3 2022)

**[GIVmatching](https://docs.giveth.io/givethMatchingPool)** - A matching program where top-ranked public goods and for-good projects on the [Giveth.io](http://giveth.io) fundraising platform will have the opportunity to have their donations matched via a collectively funded matching pool. (Q2 2023)

**[GIVfi](https://docs.giveth.io/giveconomy/#givfi)** - A smart contract system for generating yield on idle donations. Utilizing unclaimed donations, Giveth earns a yield through low-risk yield bearing strategies. Projects are able to claim 100% of their donation, while the yield earned goes to funding the DAO and buying back GIV. (TBA)

**[Gurves](https://docs.giveth.io/giveconomy/#gurves)** - Bonding curves collateralized by GIV that projects on Giveth can launch to evolve into DAOs with their own micro-economies. Gurves enable donors to invest GIV into their favorite projects and provide upside potential for entrepreneurs in the public goods space. Donors become investors, volunteers become shareholders with a voice, and Giveth becomes the Schelling point for impact investments. (TBA)

---

## **What are the Giveth DApps?**

The Giveth Donation Applications (DApps) create bridges between for-good projects and Givers wanting to make a difference. Giveth has two Donation Applications (DApps), [Giveth TRACE](http://trace.giveth.io/) and [Giveth.io](http://giveth.io/), each with unique features and benefits for philanthropic projects looking for funding.

**Giveth.io** has been designed to facilitate ease of use so that anyone can get involved. Creating an account is easy; donating to and creating projects can be done in minutes. Giveth is home to a wide range of philanthropic ventures and is widely recognized across the Ethereum ecosystem, so naturally it's a great place to get exposure for your mission!

**Giveth TRACE** is our original DApp that has been continually evolving since 2017. It offers a robust system to allow project owners to define their funding objectives via [tiered donation entities](../dapps/entitiesAndRoles). Givers benefit from this extra layer through the ability to specify and trace the movement of their donations on the DApp. Giveth pioneered the first bridge between Ethereum networks and this is where it was built. We leverage a Mainnet and Rinkeby bridge to make managing, tracing and withdrawing funds easy and gas-less.

**_Giveth TRACE has officially been deprecated. After 5 years of faithful service, Giveth and its platform, services and products have fully migrated to [Giveth.io](https://giveth.io). With the deprecation of the Rinkeby network and low user activity, the Giveth DAO decided to sunset its original dApp in Q3 of 2022. The code has and will forever be open-source, and you can find it in [Giveth's Github repositories](https://github.com/Giveth)._**

## **Why should I donate to a project on Giveth?**

The Giveth DApps use blockchain technology to track and record cryptocurrency donations, allowing them to be recorded and forever accessible. We build systems to provide potential donors with high-quality, verified projects and design economies that give back to those who give. Giveth has had a long and critical role in the development of Ethereum, and is one of the most trusted names in the blockchain community.

## **Who owns Giveth?**

Giveth is governed by an ever expanding community of developers, designers, philanthropists, decentralists, visionaries, engineers, writers and blockchain enthusiasts. Our eclectic mix of humans from the Ethereum and non-profit worlds, are formally known as the Giveth Decentralized Altruistic Community (or DAC). We are passionate to provide the tools for anyone to build a global community around a cause. Our current DAO structure is based on a model of sociocracy, with governing rights distributed regularly to active contributors.

## **Is Giveth recognized as an official charity?**

Giveth is a part of the [SDG impact fund](https://www.sdgimpactfund.org/) which is a registered donor-advised fund. The Giveth organization, under this legal architecture, is represented as a non-profit 501c3 in the United States. We are a community-led project and do not derive any direct profit from the platform. We strive to model our organization as one of the first not-for-profit blockchain based entities. We guarantee all funds will get recycled back into the Community that is ensuring the Giveth Platform gets adopted widely. 
