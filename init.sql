-- public.conversations definition

CREATE TABLE public.conversations (
	id uuid NOT NULL,
	title text NOT NULL,
	created_at timestamp NOT NULL,
	CONSTRAINT conversations_pk PRIMARY KEY (id)
);


-- public.messages definition

CREATE TABLE public.messages (
	id uuid NOT NULL,
	"role" varchar(10) NOT NULL,
	message text NOT NULL,
	created_at timestamp NOT NULL,
	conversation_id uuid NOT NULL,
	CONSTRAINT messages_pk PRIMARY KEY (id),
	CONSTRAINT messages_conversations_fk FOREIGN KEY (conversation_id) REFERENCES public.conversations(id) ON DELETE CASCADE ON UPDATE CASCADE
);