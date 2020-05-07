import React, { Component } from 'react';
import './App.css';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.css';

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      formData: {
        NewsBody: 'almost 100,000 people left Puerto Rico last year',
        Subject: 'economy',
        Speaker: 'jack-lew',
        JobTitle: 'Treasury secretary',
        Party: 'democrat'
      },
      result: ""
    };
  }

  handleChange = (event) => {
    const value = event.target.value;
    const name = event.target.name;
    var formData = this.state.formData;
    formData[name] = value;
    this.setState({
      formData
    });
  }

  handlePredictClick = (event) => {
    const formData = this.state.formData;
    this.setState({ isLoading: true });
    fetch('http://127.0.0.1:5000/prediction/', 
      {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(formData)
      })
      .then(response => response.json())
      .then(response => {
        this.setState({
          result: response.result,
          isLoading: false
        });
      });
  }

  handleCancelClick = (event) => {
    this.setState({ result: "" });
  }

  render() {
    const isLoading = this.state.isLoading;
    const formData = this.state.formData;
    const result = this.state.result;


    return (
      <Container>
        <div>
          <h1 className="title">Fake News Detection</h1>
        </div>
        <div className="content">
          <Form>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>News Body</Form.Label>
                <Form.Control 
                  type="text" 
                  placeholder="News Body"
                  name="NewsBody"
                  value={formData.NewsBody}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Subject</Form.Label>
                <Form.Control 
                  type="text" 
                  placeholder="Subject"
                  name="Subject"
                  value={formData.Subject}
                  onChange={this.handleChange} />
              </Form.Group>
            </Form.Row>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>Speaker</Form.Label>
                <Form.Control 
                  type="text"
                  placeholder="Speaker"
                  name="Speaker"
                  value={formData.Speaker}
                  onChange={this.handleChange}>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Job Title</Form.Label>
                <Form.Control 
                  type="text"
                  placeholder="Job Title"
                  name="JobTitle"
                  value={formData.JobTitle}
                  onChange={this.handleChange}>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Party</Form.Label>
                <Form.Control 
                  type="text"
                  placeholder="Party"
                  name="Party"
                  value={formData.Party}
                  onChange={this.handleChange}>
                </Form.Control>
              </Form.Group>
            </Form.Row>
            <Row>
              <Col>
                <Button
                  block
                  variant="success"
                  disabled={isLoading}
                  onClick={!isLoading ? this.handlePredictClick : null}>
                  { isLoading ? 'Making prediction' : 'Predict' }
                </Button>
              </Col>
              <Col>
                <Button
                  block
                  variant="danger"
                  disabled={isLoading}
                  onClick={this.handleCancelClick}>
                  Reset prediction
                </Button>
              </Col>
            </Row>
          </Form>
          {result === "" ? null :
            (<Row>
              <Col className="result-container">
                <h5 id="result">{result}</h5>
              </Col>
            </Row>)
          }
        </div>
      </Container>
    );
  }
}

export default App;