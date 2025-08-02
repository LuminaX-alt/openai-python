// middleware/noCache.js
from no_cache import no_cache_middleware
app.middleware("http")(no_cache_middleware)
module.exports = function noCache(req, res, next) {
    res.set('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
    res.set('Pragma', 'no-cache');
    res.set('Expires', '0');
    next();
};
const noCache = require('./middleware/noCache');
app.get('/agent/status', noCache, (req, res) => {
    res.json({ status: agent.getStatus(), updatedAt: new Date().toISOString() });
});
from fastapi import Request
from fastapi.responses import Response

async def no_cache_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    if request.url.path.startswith("/agent/status"):
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, proxy-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
    return response
package middleware

import "net/http"

func NoCache(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/agent/status" {
            w.Header().Set("Cache-Control", "no-store, no-cache, must-revalidate, proxy-revalidate")
            w.Header().Set("Pragma", "no-cache")
            w.Header().Set("Expires", "0")
        }
        next.ServeHTTP(w, r)
    })
}
http.Handle("/agent/status", middleware.NoCache(http.HandlerFunc(agentStatus)))

