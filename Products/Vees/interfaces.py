from zope.interface import Interface
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.directives import form
from collective.z3cform.datagridfield.registry import DictRow
from collective.z3cform.datagridfield import DataGridFieldFactory
from plone.app.textfield import RichText
from plone.supermodel import model
from plone.app.textfield.value import RichTextValue


class IVee(Interface):
    template_index = schema.Choice(
        title=u'Vee Template',
        vocabulary='Products.Vees.vocabularies.templates')


class ISection(Interface):
    hide = schema.Bool(title=u'Hide')
    goal = schema.Text(title=u'Section Goal')
    tasks = schema.Text(title=u'Section Tasks')
    max_height = schema.Int(title=u'Max Height', default=-1)


FONT_SIZES = SimpleVocabulary([
    SimpleTerm('small', 'small', u'Small'),
    SimpleTerm('normal', 'normal', u'Normal'),
    SimpleTerm('large', 'large', u'Large')
])


DEFAULT_TEMPLATE = {
    'title': 'Generic ResearchVee Template',
    'authors': 'Authors of the default content are Laurence Loewe and David '
               'Groos.',
    'purpose': 'This very general template is inspired by the workflow of '
               'professional scientists. Starting with big picture problems, '
               "scientists develop specific 'testable' questions and then "
               'find methods to collect data of potential interest. Data is '
               'analyzed in search for what claims it may support. All '
               'sections of the ResearchVee get adjusted repeatedly '
               '--back-and-forth-- just as professional scientists go back and'
               ' forth between theory and data. Create new templates to fit '
               "your lessons' particular needs.",
    'left_column_width': 400,
    'vee_width': 160,
    'right_column_width': 400,
    'top_font': 'large',
    'top2_font': 'normal',
    'top3_font': 'normal',
    'sections_font': 'normal',
    'min_allowable_score': 0,
    'max_allowable_score': 10,
    'general_help': RichTextValue(u"""
<ol>
    <li>First think, then write. It can be helpful to scribble some rough
        ideas on a piece of paper and quietly reflect on whether they make
        sense before starting to type into a screen that is much more formal.
    </li>
    <li>Revise. Do not try to write the perfect text in the first round.
        Rather, plan to go back and revise. Really good texts are rewritten
        several times before they become that good. You are no exception,
        especially if you are just getting started. Revisiting your text after
        some time or having it read by others can work miracles to improve
        your text.
    </li>
    <li>Practical tips for writing in Plone. In the sections of the ResearchVee
        in addition to text you can add a broad range of different types of
        content like tables, images, links, just like on any Plone page you
        write.
    </li>
</ul>"""),
    'assessment_schema': RichTextValue(u"""
<p>How well does the solution fulfill the tasks laid out for that section? This
   is a scale that reviewers and instructors and authors use to assess the
   quality of an entry:</p>
<table class="listing">
    <thead>
        <tr>
            <th>Assessment score Meaning</th>
            <th>Meaning</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>4</td>
            <td>Solution fully satisfies task. Excellent writing style.
                Innovative ideas.</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Solution fully satisfies task.</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Minor problems. Perhaps sloppy writing.</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Solution attempted, but major gaps in the writing or logic.
            </td>
        </tr>
        <tr>
            <td>0</td>
            <td>No solution attempted.</td>
        </tr>
    </tbody>
</table>"""),
    'main_content_table': [{
        'hide': False,
        'location': 'top',
        'section_title': 'Focus Question',
        'section_goal': 'Highlight what you are trying to find out.',
        'section_tasks': """
1. This is an art that requires you to make a statement about

(i) what you think is interesting and what not, and

(ii) what you think you can find out by research

2. Write down a precise question. Example: How does [a cause or variable

you study] affect [an effect you study] in [a system you study]?
""",
        'max_height': 50
    }, {
        'hide': False,
        'location': 'top2',
        'section_title': u'Authors',
        'section_goal': 'List all authors that worked on this research',
        'section_tasks': """How to determine authorship:

1. All authors must

(i) agree with all content as presented in all sections

(ii) have contributed substantially to the work in at least 2 of the sections.

2. Adding authors must be done by the owner of a ResearchVee: go to the

“Sharing” tab and share with your other authors to give them the right to

edit the Vee.

Then this section will automatically list all relevant names.""",
        'max_height': 25
    }, {
        'hide': False,
        'location': 'top3',
        'section_title': u'Abstract',
        'section_goal': 'Provide a very brief overview of this ResearchVee.',
        'section_tasks': """How to write a good abstract:

1. Provide a very brief summary of background and methods.

2. Summarize your key finding and its importance.

3. Ask all authors to read and revise it for brevity and clarity.""",
        'max_height': 50
    }, {
        'hide': False,
        'location': 'l6',
        'section_title': u'Field',
        'section_goal': 'Describe the general field to which the focus '
                        'question belongs.',
        'section_tasks': """How to provide a good introduction to the field of
research:

This is the most general background introduction available on the

ResearchVee. Its purpose is to take the general reader by the hand and

provide a focused introduction that motivates the further study that follows.

1. Name the field of research to which the focus question belongs.

2. What are the broader questions in the field and why are they important?

3. Provide a reference to a good textbook providing a broader introduction

to the relevant background in the field.

4. If your study were to be presented in a textbook, what would the unit be

about?""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'l5',
        'section_title': u'Big Ideas',
        'section_goal': 'Name and describe existing big ideas answering '
                        'the focus question.',
        'section_tasks': """How to best describe existing big ideas?

1. Be aware of the relevant big ideas that (i) address the focus question and

(ii) have already been worked out. This requires you to do some detailed

background research. Visit your library.

2. Name and describe existing big ideas relevant to the focus question and

provide details and references for your sources.

3. What exactly do these big ideas try to explain and what not? Do they

completely answer the focus question or do they open more questions?

4. Do you have an image explaining the big ideas? You can draw,

scan and upload or else get images from sites such as http://

search.creativecommons.org/. Make sure you acknowledge sources, respect

copyright and keep image size appropriate.

5. Avoid discussing ideas and images that are not relevant.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'l4',
        'section_title': u'Glossary',
        'section_goal': 'Dictionary of key words. Define all important '
                        'words and concepts needed for understanding '
                        'all other sections.',
        'section_tasks': """How to write a good glossary:

Often researchers develop their own language when needed, as it is easier

to use the science terms of their field to communicate their research. While

they should avoid jargon where they can, new words and special terms are

sometimes unavoidable. Your glossary is like a dictionary that helps the

rest of us to understand your research.

1. When you talk about anything related to your study of the focus

question, are there special words you would use that are not commonly

used in that way (or at all)?

2. Are there special words related to the methods (or equipment) you use?

3. List all these words and give a simple definition, ideally one that your

grandmother would understand and if that is not possible, one that makes

sense to your peers.

4. Provide references and stick to accepted “fair use” guidelines if you cite

other works.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'l3',
        'section_title': u'Assumptions',
        'section_goal': 'Spell out important simplifying assumptions '
                        'you make in your analysis of observations that may '
                        'affect the conclusions you can draw.',
        'section_tasks': """How to best spell out your assumptions:

Assumptions are assumed to be true without having a proof. It is impossible

to do anything in our world without building on assumptions. Most

assumptions cannot be tested due to a lack of time (or resources). Thus

we all have to risk making bad assumptions if we want to do anything. In

research bad assumptions can substantially change what your result mean.

That is why it is important for you to be aware of the assumptions you

make and to develop an intuition about their quality.

1. The list of assumptions that you make while observing and interpreting

your data is much longer than you can list here. Focus on the most

important assumptions that may affect the conclusions you can draw from

your observations.

2. Check the simplifying assumptions that you make to help you to save

time when observing and analyzing your data. These can render your

results worthless if they cannot be properly justified. Think about how the

conclusions change if a certain assumption is wrong.

3. Examples for such assumptions include (i) assuming the absence of

biases in your data even though you know there are some biases, (ii)

assuming that all important aspects of the system have actually been

observed, (iii) if you sort observations into categories you assume that these

categories are appropriate, (iv) many more.

4. Develop an awareness of critical assumptions.

5. Do not become perfectionist and demand assumption free results.

Explicitly stating important assumptions and evaluating them in light of

other reasonable assumptions is usually enough.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'l2',
        'section_title': u'Methods',
        'section_goal': 'How did you make your observations and analyze'
                        'your data?',
        'section_tasks': """How to best describe your methods:
Describe only methods you use in your study. Include enough detail so your

peers can replicate your observations if they have your materials. Be

sensitive to limitations in your claims caused by assumptions in your methods.

1. Write out the specific individual steps you do to make your raw

observations. Include all aspects that you consider to be important for

someone who would like to repeat your observations. 

2. Do the same for the methods you plan to use when you analyze your

observations.

3. How do you expect the choice of your methods to impact your observations?

What are other limitations of your methods?

4. If possible, draw an easy to understand overview picture of your

methods and how they relate to materials you use.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'l1',
        'section_title': u'Materials',
        'section_goal': 'Describe the materials you use to make the '
                        ' observations reported in your study.',
        'section_tasks': """How to best describe your materials:

1. Describe any tangible materials, samples or other sources that you

use to make your observations. Describe their quality and where you obtained

them. Give references as needed.

2. Provide enough detail that your peers can replicate your observations if

they use your methods.

3. Argue why you chose the materials you chose. Are these appropriate in

light of the focus question? 

4. How do you expect the choice of your materials to impact your observations?

Be sensitive to potential limitations in your claims caused by the choice of

your materials.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'Bot.',
        'section_title': u'Raw Data',
        'section_goal': 'Report low-level observations as made, without '
                        'analyzing or filtering.',
        'section_tasks': """How to best report your raw data:

This reflects the “Raw Data” part of your research log book if you have one.

Everything gets recorded chronologically.

1. Consult your research community to follow accepted standards for reporting

raw data. Only develop new forms if no appropriate standard exists already.

If your data is simple, use tables, texts, images or similar forms to

represent raw data.

2. Label everything appropriately, so others (including yourself in 2 years

time) still stand a chance to understand what you reported.

3. Provide context: Many details of your study seem obvious while you do it,

but unless you write them down, they will be deeply puzzling to everybody else.

4. Reliability: record any information or data that can later help assess the

reliability of the data you report.

5. If appropriate and possible, put your raw data in a public database and cite

only the accession numbers here.

6. Do not report a “data dump”. Make intelligent choices about what to record

and how to organize it based on the focus question and avoid filling up storage

space with irrelevant details.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'r1',
        'section_title': u'Data Summary',
        'section_goal': 'Summarize data to highlight patterns that support '
                        'your claim or that invalidate your claim.',
        'section_tasks': """How to best summarize your data:

You can only summarize your data appropriately when you know which claim

(or hypothesis) you want to test. This will guide your choice of methods

for summarizing data. Your summary of data should make explicit what you

are doing in the process of summarizing. 

This section reflects the “Data Analysis” part of your research log book

if you have one. Everything gets recorded chronologically; filtering out

‘boring’ analyses happens at a later stage.

For each section of your data summary do the following:

1. State the focus of your summary: Which small question, hypothesis or

idea are you testing? Write it down.

2. Decide what analysis, transformation or statistic best shows the

difference (or similarity) you want to highlight. Find appropriate

representations like graphs, tables, categorizations, statistics etc that

highlight patterns in the data you want to demonstrate for documenting

your claim. Then try to prove the opposite from your data to see if you

have a solid claim or whether the data is inconclusive.

3. Apply a statistical test to see if your observations could also have

been generated if the most boring alternative explanation answering your

question was true.

4. Prepare a convincing and cleaned up presentation of your analyzed data

in table or graph form.

5. Provide appropriate labels and explanations and summarize the conclusions

of each section in an appropriate sentence.

6. Do not repeat the Methods or Raw Data sections here, but rather focus on

analyses close to the data. Leave all interpretations for later sections.

7. Do not omit data that does not fit your expectations! Do not omit analyses

that lead to ‘boring’ results, where you would have expected ‘exciting’

results. If done properly, much can be learned from the discussion of such

analyses.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'r2',
        'section_title': u'Results',
        'section_goal': 'Summarize the broader interesting patterns you see '
                        'in your observations after you have analyzed the '
                        'data.',
        'section_tasks': """How to best describe your results:

Results build on the Data Summary section and highlight the most relevant

analyses from the previous section with respect to the focus question.

1. Describe at a high level but without generalizing which patterns you

find in your observations. Point to specific results that are interesting

without getting lost in details.

2. Uninteresting results get only a very brief mention, even if producing

them was a lot of work.

3. Be careful not to bias your reporting of results for or against certain

ideas. All results relevant for addressing the focus question need to be

discussed.

4. Be careful to distinguish between correlation and causation. Silly

example: Correct correlation: “Everybody who went to the moon has two legs.”

False causation: “Having two legs makes you go to the moon!” Real examples

appear less silly, but are not more correct.

5. Do not repeat the previous section, but rather provide a high-level

overview of the results of the analyses performed in the previous section.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'r3',
        'section_title': u'Limits',
        'section_goal': 'Describe limitations of observations and weaknesses '
                        'of the methods and how they affect claims.',
        'section_tasks': """How to best describe limitations and weaknesses:
        
Every study that is not a correct mathematical proof has limitations and

weaknesses. Here these are defined by

(i) the broader claims of a study and

(ii) the inability to rigorously justify that these claims are accurate

under all circumstances. Some limitations are silly (“You have not checked

if this is true on the Moon”), others are serious (“A fellow researcher could

not replicate these results”). It is important to investigate the key limits.

Good research is aware of its own limitations and shows that. Bad research

does not care about its own limitations.

1. List limits of your observations you think are important.

2. List weaknesses of your methods you think are important.

3. Describe how these could affect your claims.

4. Discuss if they actually affect your claims.

5. What could be done to address these weaknesses?""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'r4',
        'section_title': u'Claims',
        'section_goal': 'What about the focus question have you learned '
                        'from your observations?',
        'section_tasks': """How to best find and describe valid claims:

A new claim is only valid if it can be justified by corresponding

observations and analyses. Try to take the position of a critic. If you

would find your analysis convincing, even if it would go against your

beliefs, then you probably have a valid claim. A better test is to have a

real critic look at your analysis, which is the purpose of peer review.

After you are convinced your claims survive such a critical look, try to

answer the focus question in one sentence to summarize all your claims.
For each claim do the following:

1. Summarize the claim in one sentence or paragraph.

2. Explain the claim: How is it supported by your observations and how

does it relate to existing big ideas about the focus question?

3. Other lessons learned: New questions? Improvements for your methods?

Other lessons?""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'r5',
        'section_title': u'Importance',
        'section_goal': 'How important is this study in the field?',
        'section_tasks': """How to best assess the importance of this study:

Often researchers develop their own language when needed, as it is easier

to use the science terms of their field to communicate their research. While

they should avoid jargon where they can, new words and special terms are

sometimes unavoidable. Your glossary is like a dictionary that helps the

rest of us to understand your research.

1. When you talk about anything related to your study of the focus

question, are there special words you would use that are not commonly

used in that way (or at all)?

2. Are there special words related to the methods (or equipment) you use?

3. List all these words and give a simple definition, ideally one that your

grandmother would understand and if that is not possible, one that makes

sense to your peers.

4. Provide references and stick to accepted “fair use” guidelines if you cite

other works.""",
        'max_height': 100
    }, {
        'hide': False,
        'location': 'r6',
        'section_title': u'Possible uses',
        'section_goal': 'Can your findings be applied outside of their '
                        'field and who might use such applications?',
        'section_tasks': """How to best assess possible uses of this study:

It is very difficult for researchers to foresee possible uses of their

results, especially before the research has started. Possible uses can

become more apparent after completing the research.

1. Applications: Which practical problems could the new insights help solve?

2. Audience: Who might be interested in or use your new insights? In its

field? In other fields? Generally?

3. Funding: Who might pay for such research?""",
        'max_height': 100
    }




        ]
}


class IVeeContent(model.Schema):

    hide = schema.Bool(title=u'Hide')
    location = schema.TextLine(title=u'Location on Vee')
    section_title = schema.TextLine(title=u'Section Title')
    section_goal = schema.Text(title=u'Section Goal')
    section_tasks = schema.Text(title=u'Section Tasks')
    max_height = schema.Int(title=u'Max Height', default=-1)


class IVeeTemplate(model.Schema):

    title = schema.TextLine(title=u'Template title')

    authors = schema.TextLine(title=u'Template Authors')

    purpose = schema.Text(title=u'Template Purpose')

    left_column_width = schema.Int(
        title=u'Width of left column in pixels',
        default=400)

    vee_width = schema.Int(
        title=u'Width of left column in pixels',
        default=160)

    right_column_width = schema.Int(
        title=u'Width of left column in pixels',
        default=400)

    form.fieldset("fonts", label=u"Font sizes for contents of...", fields=[
        'top_font', 'top2_font', 'top3_font', 'sections_font'
    ])
    top_font = schema.Choice(title=u'Top font', vocabulary=FONT_SIZES,
                             default='large')
    top2_font = schema.Choice(title=u'Top2 font', vocabulary=FONT_SIZES,
                              default='normal')
    top3_font = schema.Choice(title=u'Top3 font', vocabulary=FONT_SIZES,
                              default='normal')
    sections_font = schema.Choice(title=u'All other sections font size',
                                  vocabulary=FONT_SIZES, default='normal')

    form.fieldset('assessmentsetup', label='Assessment setup', fields=[
        'min_allowable_score', 'max_allowable_score', 'assessment_schema'
    ])
    min_allowable_score = schema.Int(title=u'Min allowable score', default=0)
    max_allowable_score = schema.Int(title=u'Max allowable score', default=10)
    general_help = RichText(
        title=u'General help for authors',
        description=u'General help for authors (adjust to highlight specific '
                    u'learning goals for writing in this ResearchVee'
    )
    assessment_schema = RichText(
        title=u'Assessment schema for authors',
        description=u'adjust as needed'
    )

    form.widget(main_content_table=DataGridFieldFactory)
    main_content_table = schema.List(
        title=u'Main content table',
        default=[],
        value_type=DictRow(
            title=u"Field",
            schema=IVeeContent)
    )
