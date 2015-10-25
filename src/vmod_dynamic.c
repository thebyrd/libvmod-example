#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "vrt.h"
#include "cache/cache.h"

#include "vcc_if.h"

int
init_function(struct vmod_priv *priv, const struct VCL_conf *conf)
{
	return (0);
}

VCL_STRING
vmod_backend_hostname(const struct vrt_ctx *ctx, VCL_STRING hostname)
{
	char *p;
	unsigned u, v;

	u = WS_Reserve(ctx->ws, 0); /* Reserve some work space */
	p = ctx->ws->f;		/* Front of workspace area */

	char *buffer;
	buffer = malloc(sizeof(char) * strlen(hostname));
	strcpy(buffer, hostname);

	buffer[strlen(buffer)-strlen(".xip.io")] = 0; /* chop off .xip.io */
	v = snprintf(p, u, "%s", buffer);

	v++;
	if (v > u) {
		/* No space, reset and leave */
		WS_Release(ctx->ws, 0);
		return (NULL);
	}
	/* Update work space with what we've used */
	WS_Release(ctx->ws, v);
	return (p);
}
