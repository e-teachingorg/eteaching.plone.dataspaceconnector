
import inspect
from DateTime import DateTime

class AMBMetadata(object):
    """ Schema for AMB Metadata (https://dini-ag-kim.github.io/amb/latest) """

    def get_amb_metadata(self, context=None):

        if context:
            self.context = context
        elif not hasattr(self, "context"):
            self.context = self

        amb = {
             "@context": self.amb_context(),
             "id": self.amb_id(),
             "type": self.amb_type(),
             "name": self.amb_name(),
             "description": self.amb_description(),
             "about": self.amb_about(),
             "keywords": self.amb_keywords(),
             "inLanguage": self.amb_inlanguage(),
             "image": self.amb_image(),
             "trailer": self.amb_trailer(),
             "creator": self.amb_creator(),
             "contributor": self.amb_contributor(),
             "affiliation": self.amb_affiliation(),
             "dateCreated": self.amb_date_created(),
             "datePublished": self.amb_date_date_published(),
             "dateModified": self.amb_date_date_modified(),
             "publisher": self.amb_publisher(),
             "funder": self.amb_funder(),
             "isAccessibleForFree": self.amb_is_accessible_for_free(),
             "license": self.amb_license(),
             "conditionsOfAccess": self.amb_conditions_of_access(),
             "learningResourceType": self.amb_learning_resource_type(),
             "audience": self.amb_audience(),
             "teaches": self.amb_teaches(),
             "assesses": self.amb_assesses(),
             "competencyRequired": self.amb_competency_required(),
             "educationalLevel": self.amb_educational_level(),
             "interactivityType": self.amb_interactivity_type(),
             "isBasedOn": self.amb_is_based_on(),
             "isPartOf": self.amb_is_part_of(),
             "hasPart": self.amb_has_part(),
             "mainEntityOfPage": self.amb_main_entity_of_page(),
             "duration": self.amb_duration(),
             "encoding": self.amb_encoding(),
             "caption": self.amb_caption()
         }
        # delete elements that are None
        clear_amb = {k: v for k, v in amb.items() if v is not None}
        return clear_amb

    language = "de"

    def amb_context(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#context
        Attribute: @context
        Required: True
        """
        return [
            "https://w3id.org/kim/amb/context.jsonld",
            "https://schema.org",
            {"@language": self.language}
        ]

    def amb_id(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#id
        Attribute: id
        Required: True
        """
        return self.context.absolute_url()

    def amb_type(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#type
        Attribute: type
        Required: True
        """
        amb_type = ["LearningResource"]
        return amb_type

    def amb_name(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#name
        Attribute: name
        Required: True
        """
        return getattr(self.context, "title", "")

    def amb_description(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#description
        Attribute: description
        Required: False
        """
        amb_description = getattr(self.context, "description", None)
        return amb_description if amb_description else None

    def amb_about(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#about
        Attribute: about
        Required: False
        """
        return None

    def amb_keywords(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#keywords
        Attribute: keywords
        Required: False
        """
        amb_keywords = []
        subject = getattr(self.context, "subject", None)
        for i in subject:
            if isinstance(i, (list, tuple)):
                for element in i:
                    amb_keywords.append(element)
        return amb_keywords if amb_keywords else None

    def amb_inlanguage(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#inlanguage
        Attribute: inLanguage
        Required: False
        """
        return [self.language, ]

    def amb_image(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#image
        Attribute: image
        Required: False
        """
        return None

    def amb_trailer(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#trailer
        Attribute: trailer
        Required: False
        """
        # There is currently no known case here
        return None

    def amb_creator(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#creator
        Attribute: creator
        Required: False
        """
        return None

    def amb_contributor(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#contributor
        Attribute: contributor
        Required: False
        """
        # There is currently no known case here
        return None

    def amb_affiliation(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#affiliation
        Attribute: affiliation
        Required: False
        """
        # There is currently no known case here
        return None

    def amb_date_created(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#datecreated
        Attribute: dateCreated
        Required: False
        """
        c = getattr(self.context, "created", None)
        if inspect.ismethod(c):
            if isinstance(c(), DateTime):
                return c().ISO8601()
        return None

    def amb_date_date_published(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#datepublished
        Attribute: datePublished
        Required: False
        """
        c = getattr(self.context, "effective", None)
        if inspect.ismethod(c):
            if isinstance(c(), DateTime):
                if c().year() > 2000:
                    return c().ISO8601()
                else:
                    return self.amb_date_created()
        return None

    def amb_date_date_modified(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#datemodified
        Attribute: dateModified
        Required: False
        """
        c = getattr(self.context, "modified", None)
        if inspect.ismethod(c):
            if isinstance(c(), DateTime):
                return c().ISO8601()
        return None

    def amb_publisher(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#publisher
        Attribute: publisher
        Required: False
        """
        return None

    def amb_funder(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#contributor
        Attribute: funder
        Required: False
        """
        return None

    def amb_is_accessible_for_free(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#isaccessibleforfree
        Attribute: isAccessibleForFree
        Required: False
        """
        return None

    def amb_license(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#license
        Attribute: license
        Required: False
        """
        return None

    def amb_conditions_of_access(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#conditionsofaccess
        Attribute: conditionsOfAccess
        Required: False
        """
        return None

    def amb_learning_resource_type(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#learningresourcetype
        Attribute: learningResourceType
        Required: False
        """
        return None

    def amb_audience(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#audience
        Attribute: audience
        Required: False
        """
        return None

    def amb_teaches(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#teaches
        Attribute: teaches
        Required: False
        """
        # This time we do not use a competency-based model
        return None

    def amb_assesses(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#assesses
        Attribute: assesses
        Required: False
        """
        # This time we do not use a competency-based model
        return None

    def amb_competency_required(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#competencyrequired
        Attribute: competencyRequired
        Required: False
        """
        # This time we do not use a competency-based model
        return None

    def amb_educational_level(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#educationallevel
        Attribute: educationalLevel
        Required: False
        """
        return None

    def amb_interactivity_type(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#interactivitytype
        Attribute: interactivityType
        Required: False
        """
        # This time We have no information on whether learning processes with this
        # resource are more expositive or active.
        return None

    def amb_is_based_on(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#isbasedon
        Attribute: isBasedOn
        Required: False
        """
        return None

    def amb_is_part_of(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#ispartof
        Attribute: isPartOf
        Required: False
        """
        return None

    def amb_has_part(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#haspart
        Attribute: hasPart
        Required: False
        """
        return None

    def amb_main_entity_of_page(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#mainentityofpage
        Attribute: mainEntityOfPage
        Required: False
        """
        # No idea what this is good for
        return None

    def amb_duration(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#duration
        Attribute: duration
        Required: False
        """
        return None

    def amb_encoding(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#encoding
        Attribute: encoding
        Required: False
        """
        return None

    def amb_caption(self):
        """
        https://dini-ag-kim.github.io/amb/latest/#caption
        Attribute: caption
        Required: False
        """
        return None