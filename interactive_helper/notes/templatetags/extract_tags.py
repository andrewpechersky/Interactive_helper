from django import template

register = template.Library()


def tags(note_tags):
    return ', '.join([str(name) for name in note_tags.all()])


<<<<<<< HEAD
register.filter('tags', tags)

=======
register.filter('tags', tags)
>>>>>>> 5c0fd8c183086e956fdcce7b8b08f99ae901e3f2
