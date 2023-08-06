import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LoadingDots from '../../Home/components/Loading';

const ReviewsCard = ({ personId }) => {
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`http://localhost:8000/person/review/${personId}`)
      .then(response => {
        setReviews(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, [personId]);

  return (
    <div className="card reviews-card">
      <h2>Reviews</h2>
      {loading ? (
        <LoadingDots />
      ) : (
        <ul>
          {reviews.map(review => (
            <li key={review.id}>
              <strong>{review.company}</strong> - " {review.review} "
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ReviewsCard;
