from todo import create_app
import pytest

app = create_app()

class TestViews:
    def setup(self):
        app.testing = True
        self.client = app.test_client()
        print('before')

    @pytest.mark.run(order=6)
    def test_x(self):
        assert 1+1 == 2
    
    @pytest.mark.run(order=1)
    def test_create_todo(self):
        response = self.client.post(
            '/todos/todo/create', 
            json={
                'title': 'created test title', 
                'description': 'created test description'
                })
        assert response.status_code == 201
        todos = self.client.get('/todos')
        assert todos.json[-1].get('title') == 'created test title'

    @pytest.mark.run(order=2)
    def test_get_by_id_todo(self):
        response = self.client.get('/todos/todo/3')
        assert response.status_code == 200
        result = response.json
        assert result['title'] == 'created test title'

    @pytest.mark.run(order=3)
    def test_get_all_todo(self):
        response = self.client.get('/todos')
        assert response.status_code == 200
        results = response.json
        assert len(results) > 0

    @pytest.mark.run(order=4)
    def test_update_todo(self):
        response = self.client.put(
            '/todos/todo/update/3', 
            json={
                'title': 'updated test title',
                'description': 'updated test description'
                })
        assert response.status_code == 200
        updated_todo = self.client.get('/todos/todo/3')
        assert updated_todo.json['title'] == 'updated test title'

    @pytest.mark.run(order=5)
    def test_delete_todo(self):
        response = self.client.delete('/todos/todo/delete/3')
        assert response.status_code == 200

    @pytest.mark.run(order=7)
    def test_y(self):
        assert 1+1 == 2

    def teardown(self):
        print('after')