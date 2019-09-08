import React, {Component} from "react";
import PropTypes from "prop-types";

class Form extends Component {
    static propTypes = {
        endpoint: PropTypes.string.isRequired
    };
    state = {
        followers_count_start: 0,
        followers_count_stop: 100,
        man_percent_start: 0,
        man_percent_stop: 100
    };
    handleChange = e => {
        this.setState({[e.target.name]: e.target.value});
    };
    handleSubmit = e => {
        e.preventDefault();
        const {
            followers_count_start, followers_count_stop,
            man_percent_start, man_percent_stop
        } = this.state;
        const lead = {followers_count_start, followers_count_stop, man_percent_start, man_percent_stop};
        const conf = {
            method: "get",
            body: JSON.stringify(lead),
            headers: new Headers({"Content-Type": "application/json"})
        };
        fetch(this.props.endpoint, conf).then(response => console.log(response));
    };

    render() {
        const {followers_count_start, followers_count_stop, man_percent_start, man_percent_stop} = this.state;
        return (
            <div className="column">
                <form onSubmit={this.handleSubmit}>
                    <div className="field">
                        <label className="label">Кол-во подписчиков от:</label>
                        <div className="control">
                            <input
                                className="followers-count-start"
                                type="number"
                                name="followers_count_start"
                                onChange={this.handleChange}
                                value={followers_count_start}
                                required
                            />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Кол-во подписчиков до:</label>
                        <div className="control">
                            <input
                                className="followers-count-stop"
                                type="number"
                                name="followers_count_stop"
                                onChange={this.handleChange}
                                value={followers_count_stop}
                            />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Доля мужчин от:</label>
                        <div className="man-percent-start">
                            <input
                                type="number"
                                name="man_percent_start"
                                onChange={this.handleChange}
                                value={man_percent_start}
                            />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Доля мужчин до:</label>
                        <div className="man-percent-stop">
                            <input
                                type="number"
                                name="man_percent_stop"
                                onChange={this.handleChange}
                                value={man_percent_stop}
                            />
                        </div>
                        <div className="control">
                            <button type="submit" className="button is-info">
                                Подобрать
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        );
    }
}

export default Form;
