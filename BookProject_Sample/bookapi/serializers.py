from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Authors,Books
class AuthorSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
                    view_name='author_detail', 
                    lookup_field='pk'
                )
    class Meta:
        model = Authors
        fields =('author_name','url',)

class AuthorDataSerializer(ModelSerializer):
    class Meta:
        model=Authors
        fields="__all__"

class BookSerializer(ModelSerializer):
    author_name = AuthorSerializer(many=True)
    

    class Meta:
        model = Books
        fields =('book_name','author_name','pub_year','price','summary',)

    def create(self, validated_data):
        authors_data = validated_data.pop('author_name')
        print(authors_data)
        book = Books.objects.create(**validated_data)
        for author in authors_data:
            author,created=Authors.objects.get_or_create(author_name=author['author_name'])
            book.author_name.add(author)

        book.save()
        return book
    # def update(self, instance, validated_data,partial=True):
    #     author_name = validated_data.pop('author_name')
    #     instance.book_name = validated_data['book_name']
    #     instance.price = validated_data['price']
    #     instance.summary = validated_data['summary']
    #     authors_list = []
    #     for author in author_name:
    #         author, created = Authors.objects.get_or_create(author_name=author['author_name'])
    #         authors_list.append(author)
    #     instance.author_name.set(authors_list)
    #     instance.save()
    #     return instance

    def update(self, instance, validated_data):
        authors_list = []

        try:
            author_name = validated_data.pop('author_name')
            
            for author in author_name:
                # print(author)
                author, created = Authors.objects.get_or_create(author_name=author['author_name'])
                authors_list.append(author)
            # instance.author_name.set(authors_list)
            
        except:
            for author in instance.author_name.all():
                authors_list.append(author)
            

        instance.author_name.set(authors_list)
        instance.book_name = validated_data.get('book_name', instance.book_name)
        instance.pub_year=validated_data.get('pub_year', instance.pub_year)
        instance.price = validated_data.get('price', instance.price) 
        instance.summary = validated_data.get('summary', instance.summary)
        instance.save()
        return instance










   

   
