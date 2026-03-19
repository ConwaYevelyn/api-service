package helpers

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"

	"github.com/dgrijalva/jwt-go"
)

// CustomError represents a custom error type
type CustomError struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}

func (ce *CustomError) Error() string {
	return fmt.Sprintf("%d: %s", ce.Code, ce.Message)
}

// NewCustomError returns a new CustomError instance
func NewCustomError(code int, message string) *CustomError {
	return &CustomError{Code: code, Message: message}
}

// GenerateJWT returns a JWT token for the given user
func GenerateJWT(user interface{}) (string, error) {
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"username": user.(map[string]interface{})["username"],
		"exp":      strconv.Itoa(3600), // expires in 1 hour
	})
	return token.SignedString([]byte("secret"))
}

// GetRequestIP returns the client's IP address from the request
func GetRequestIP(r *http.Request) string {
	if r.Header["X-Forwarded-For"]!= nil {
		return r.Header["X-Forwarded-For"][0]
	}
	return r.RemoteAddr
}

// ValidateJSON validates the JSON payload
func ValidateJSON(w http.ResponseWriter, r *http.Request) error {
	decoder := json.NewDecoder(r.Body)
	err := decoder.Decode(&struct{}{})
	if err!= nil {
		log.Println(err)
		http.Error(w, "Invalid JSON", http.StatusBadRequest)
		return err
	}
	return nil
}