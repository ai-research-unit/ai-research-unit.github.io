# __The Signed Sandwich on an Algebra__

## Introduction

The sandwich operator of the group `- Operator Theory` multiplies an element on the left and on the right, $x \mapsto a x b$. When the algebra carries an automorphism $\alpha$ of order two, the product can be twisted by it in the middle, and the **signed sandwich**

$$
S_{a,b}(x) = a\,\alpha(x)\,b
$$

is the result. The twist is by the **grade involution** when the algebra is $\mathbb{Z}/2$-graded — the automorphism that is $+1$ on the even part and $-1$ on the odd part — and it is by an arbitrary involutive automorphism in general. The twisted operator is the one that realises the reflections of the algebra, and it is the reason the reflections are two-sided operators and not one-sided ones.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra, with $n = \dim_k A$ when finite-dimensional. The algebra carries an **involutive automorphism** $\alpha$, that is an algebra automorphism with $\alpha^2 = \mathrm{id}$; the canonical instance is the grade involution of a $\mathbb{Z}/2$-grading, and the general theory of gradings and of the sign rule belongs to *Superalgebras and Graded Structures*, which is named here but not used. The unsigned sandwich is the operator $T_{a,b}$ of *The Sandwich Operator on an Algebra*, and the involutive automorphisms are those of *Automorphisms and Derivations of Algebras* and of *Involutive Bilinear Algebras*.

## The Involutive Automorphism

### Definition

**Definition.** An **involutive automorphism** of $A$ is an algebra automorphism $\alpha : A \to A$ with $\alpha^2 = \mathrm{id}$, that is $\alpha(xy) = \alpha(x)\alpha(y)$, $\alpha(x + y) = \alpha(x) + \alpha(y)$, and $\alpha(\alpha(x)) = x$ for all $x, y \in A$. It is unital when $A$ is, since $\alpha(1) = \alpha(1)^2$ and $\alpha(1) \neq 0$.

The word **grade involution** is used for the instance in which $A$ carries a $\mathbb{Z}/2$-grading $A = A^0 \oplus A^1$ and $\alpha$ is the automorphism acting by $\alpha(x) = x$ on the even part and $\alpha(x) = -x$ on the odd part. That $\alpha$ is an automorphism is associativity read on the parity of the product; the general theory of the grading itself is *Superalgebras and Graded Structures*, and everything below uses only the two properties $\alpha^2 = \mathrm{id}$ and multiplicativity.

### The Decomposition

**Proposition.** The involutive automorphism $\alpha$ gives a direct sum decomposition

$$
A = A^+ \oplus A^-, \qquad A^+ = \{x : \alpha(x) = x\}, \qquad A^- = \{x : \alpha(x) = -x\},
$$

and the summands multiply as

$$
A^+ A^+ \subseteq A^+, \qquad A^+ A^- \subseteq A^-, \qquad A^- A^+ \subseteq A^-, \qquad A^- A^- \subseteq A^+ ,
$$

so that the decomposition is a $\mathbb{Z}/2$-grading of $A$ whose grade involution is $\alpha$.

*Proof.* The two sets are the eigenspaces of $\alpha$ for the eigenvalues $1$ and $-1$, so they are subspaces intersecting in $0$ and summing to $A$ when $2$ is invertible, by the averaging $x = \frac12(x + \alpha(x)) + \frac12(x - \alpha(x))$; when $2 = 0$ no element is negated by an order-two map and $A^- = 0$, and the second statement below is read with that collapse. If $\alpha(x) = \epsilon x$ and $\alpha(y) = \epsilon' y$ with $\epsilon, \epsilon' \in \{1,-1\}$, then $\alpha(xy) = \alpha(x)\alpha(y) = \epsilon \epsilon' xy$, which is the multiplication table of $\mathbb{Z}/2$.

The identity $A = A^+ \oplus A^-$ is the reason an involutive automorphism is an operator that also *is* a structure: it produces a grading. Conversely a grading of $A$ whose odd part squares to the even part and which is compatible with the product produces the grade involution, so an involutive automorphism and a "splitting of $A$ into a plus and a minus part" are the same datum. The article *Involutive Bilinear Algebras* proves the grading of an involutive automorphism from the multiplication table in the same way, and it owns the general theory of the involutions of the elements; the present article uses only the operator $\alpha$.

### The Automorphism as an Operator

**Proposition.** The involutive automorphism $\alpha$ is an element of $\operatorname{End}_k(A)$ with $\alpha^2 = \mathrm{id}$, and it is an operator of order two in the group $\operatorname{Aut}_k(A)$ of algebra automorphisms of *Automorphisms and Derivations of Algebras*.

*Proof.* It is $k$-linear and multiplicative, hence in $\operatorname{End}_k(A)$, and it is invertible with inverse itself, hence in the unit group of the endomorphism monoid, which is the automorphism group of the algebra. The order is two by hypothesis.

**Remark.** The involutive automorphisms of $A$ form the elements of order dividing two in the automorphism group, and they are the operators of the present article. A single one is fixed throughout, and it is written $\alpha$; when it is the identity the whole theory reduces to the unsigned one.

## The Signed Sandwich

### Definition

**Definition.** Let $a, b \in A$. The **signed sandwich** determined by $a$ and $b$ is the operator

$$
S_{a,b} : A \to A, \qquad S_{a,b}(x) = a\,\alpha(x)\,b .
$$

The **signed sandwich space** is the image of the bilinear map $S : A \times A \to \operatorname{End}_k(A)$, $(a,b) \mapsto S_{a,b}$.

The signed sandwich is $k$-linear in $x$, because $\alpha$ and the two multiplications are; and it is $k$-bilinear in $a$ and in $b$. The definition differs from that of $T_{a,b}$ in exactly one place, the middle argument, which is now $\alpha(x)$ in place of $x$. When $\alpha = \mathrm{id}$ the signed sandwich is the unsigned one, $S_{a,b} = T_{a,b}$, and the two theories coincide.

### Elementary Properties

**Proposition.** For all $a, b \in A$ and $x \in A$,

**(a)** $S_{1,1} = \alpha$;

**(b)** $S_{a,b} = T_{a,b} \circ \alpha = \alpha \circ T_{\alpha(a), \alpha(b)}$;

**(c)** $S_{a,b}(1) = a\,b$;

**(d)** $S_{a,b}\bigl(\alpha(y)\,\alpha(c)\bigr) = S_{a,b}\bigl(\alpha(y)\bigr)\,\alpha(c)$, so $S_{a,b}$ is right $A$-linear on the image of $\alpha$.

*Proof.* (a) $S_{1,1}(x) = \alpha(x)$. (b) $T_{a,b}(\alpha(x)) = a\alpha(x)b = S_{a,b}(x)$, and $\alpha(T_{\alpha(a),\alpha(b)}(x)) = \alpha(\alpha(a)x\alpha(b)) = a\alpha(x)b$. (c) $\alpha(1) = 1$. (d) By multiplicativity of $\alpha$, $S_{a,b}(\alpha(y)\alpha(c)) = a\alpha(\alpha(y)\alpha(c))b = a\,y\,\alpha(c)\,b = S_{a,b}(\alpha(y))\,\alpha(c)$.

The identity (b) is the precise sense in which the signed sandwich is the unsigned sandwich followed by the involution: $S_{a,b} = T_{a,b}\alpha$ as operators, the involution acting first. It is the reason the signed operator can be read off from the unsigned one whenever $\alpha$ is known, and the reason a statement about the signed sandwich is a statement about the pair $(T_{a,b}, \alpha)$.

### Composition

**Theorem.** For all $a, b, c, d \in A$,

$$
S_{a,b}\,T_{c,d} = S_{a\alpha(c),\,\alpha(d)b}, \qquad
T_{a,b}\,S_{c,d} = S_{ac,\,db}, \qquad
S_{a,b}\,S_{c,d} = T_{a\alpha(c),\,\alpha(d)b} .
$$

In particular the product of two signed sandwiches is an unsigned sandwich, and the signed sandwiches are not closed under composition unless $\alpha = \mathrm{id}$.

*Proof.* Use the two readings $S_{p,q} = T_{p,q}\alpha = \alpha T_{\alpha(p),\alpha(q)}$ of elementary property (b) and $\alpha^2 = \mathrm{id}$. For the first, $S_{a,b}T_{c,d} = T_{a,b}\alpha T_{c,d} = T_{a,b}T_{\alpha(c),\alpha(d)}\alpha = S_{a\alpha(c),\alpha(d)b}$. For the second, $T_{a,b}S_{c,d} = T_{a,b}T_{c,d}\alpha = S_{ac,db}$. For the third, multiply the first two: $S_{a,b}S_{c,d} = T_{a,b}\alpha T_{c,d}\alpha = T_{a,b}T_{\alpha(c),\alpha(d)}\alpha^2 = T_{a\alpha(c),\alpha(d)b}$.

**Remark.** The three rules are the complete multiplication table of the two-sided operators: a signed sandwich followed by an unsigned one is signed, an unsigned followed by a signed is signed, and two signed sandwiches compose to an unsigned one. The signed sandwiches are the coset $G_0\alpha$ of the group $G_0$ of invertible unsigned sandwiches, and the union $G_0 \cup G_0\alpha$ is a subgroup of $\operatorname{End}_k(A)$ of index two over $G_0$ generated by $\alpha$; the multiplication is the one displayed.

**Corollary.** The map

$$
a \otimes b \longmapsto S_{a,b}, \qquad A \otimes_k A^{\mathrm{op}} \longrightarrow \operatorname{End}_k(A)
$$

is $k$-linear onto the signed sandwich space, and its products obey the table above; when $\alpha = \mathrm{id}$ it is the sandwich homomorphism of *The Sandwich Operator on an Algebra* and the three rules collapse to $T_{a,b}T_{c,d} = T_{ac,db}$.

### Invertibility

**Theorem.** Let $A$ be finite-dimensional. The signed sandwich $S_{a,b}$ is invertible in $\operatorname{End}_k(A)$ if and only if $a$ and $b$ are units of $A$, and then

$$
S_{a,b}^{-1} = S_{\alpha(a)^{-1},\, \alpha(b)^{-1}} .
$$

*Proof.* The form $S_{a,b} = T_{a,b}\alpha$ is the composite of the invertible operator $\alpha$ with the sandwich $T_{a,b}$, so it is invertible exactly when $T_{a,b}$ is; by *The Sandwich Operator on an Algebra* this is exactly when $a$ and $b$ are units. For the inverse, apply the composition rule for two signed sandwiches: $S_{a,b}S_{\alpha(a)^{-1},\alpha(b)^{-1}} = T_{a\alpha(\alpha(a)^{-1}),\,\alpha(\alpha(b)^{-1})b} = T_{a\alpha(a)^{-1},\,b^{-1}b} = T_{1,1} = \mathrm{id}$, using $\alpha(\alpha(a)^{-1}) = a^{-1}$ and $\alpha(\alpha(b)^{-1}) = b^{-1}$; the same computation in the other order gives the two-sided inverse.

**Remark.** The inverse $S_{\alpha(a)^{-1},\alpha(b)^{-1}}$ is again a signed sandwich, so the invertible signed sandwiches are stable under inversion; they are not stable under composition, because the product of two of them is an unsigned sandwich. The stable object is the union of the invertible signed and the invertible unsigned sandwiches, which is the subgroup $G_0 \cup G_0\alpha$ of the remark above. When $\alpha = \mathrm{id}$ the signed and the unsigned sandwiches coincide and this union is the ordinary group of invertible sandwiches.

## The Signed Sandwich and the Reflections

### The Signed Conjugations

**Definition.** For a unit $u \in A$ the **signed conjugation**, or **signed inner automorphism**, by $u$ is the operator

$$
\rho_u = S_{u,\, u^{-1}} : A \to A, \qquad \rho_u(x) = u\,\alpha(x)\,u^{-1} .
$$

The signed conjugation is the signed sandwich with $b = u^{-1}$, exactly as the inner automorphism $\iota_u$ is the unsigned sandwich with $b = u^{-1}$. It is an automorphism of $A$ for every unit $u$, being the composite of the automorphisms $\alpha$ and $\iota_u$. The reflections are the signed conjugations of order two, and their detailed study is *Reflections as Signed Two-Sided Operators on an Algebra*; the present article fixes the operator and states the criterion for it to be a reflection.

**Proposition.** For every unit $u$ the signed conjugation is an automorphism of $A$, and

$$
\rho_u^2 = \iota_{u\,\alpha(u)}, \qquad \text{that is} \qquad \rho_u^2(x) = u\,\alpha(u)\, x\, (u\,\alpha(u))^{-1} .
$$

Hence $\rho_u$ is an involution — a reflection — exactly when $u\,\alpha(u)$ is central, and then $\rho_u^2 = \mathrm{id}$.

*Proof.* Compute on $x$: $\rho_u(\rho_u(x)) = u\alpha(u\alpha(x)u^{-1})u^{-1} = u\alpha(u)\,\alpha^2(x)\,\alpha(u)^{-1}u^{-1} = (u\alpha(u))x(u\alpha(u))^{-1}$, using the multiplicativity of $\alpha$ and the inversion rule $\alpha(u^{-1}) = \alpha(u)^{-1}$. The operator is the inner automorphism by $u\alpha(u)$, so it is the identity exactly when $u\alpha(u)$ is central.

**Corollary.** If $u$ is an **odd** element of a $\mathbb{Z}/2$-graded algebra, $\alpha(u) = -u$, then $\rho_u^2 = \iota_{-u^2}$; in particular, if $u^2$ is central, then $\rho_u$ is a reflection. The Clifford algebras supply the standard instances, and their metric reading belongs to *Quadratic Forms and Clifford Algebras* of Part II and is not made here.

*Proof.* With $\alpha(u) = -u$ one has $u\alpha(u) = -u^2$, which is central when $u^2$ is central; the criterion of the proposition then applies.

### The Relation to the Unsigned Sandwich

**Proposition.** The signed sandwich and the unsigned sandwich determine one another through the involution,

$$
S_{a,b} = T_{a,b}\,\alpha = \alpha\, T_{\alpha(a),\, \alpha(b)}, \qquad T_{a,b} = S_{a,b}\,\alpha .
$$

*Proof.* The first identity is elementary property (b). For the second, compose the first on the right with $\alpha$ and use $\alpha^2 = \mathrm{id}$.

**Corollary.** The signed sandwich space is the image of the unsigned sandwich space under composition with $\alpha$, and the two spaces have the same dimension. In particular the signed sandwich space is all of $\operatorname{End}_k(A)$ exactly when the unsigned sandwich space is, which for a central simple algebra is the case by *The Sandwich Operator on an Algebra*.

The corollary is the reason the signed theory is not a second theory but the unsigned one with one operator inserted: the involution $\alpha$ acts on the operator space by composition, and the signed sandwich is the image of the unsigned sandwich under that action.

## The Examples

### A Trivial Grading

Let $A = A^0$ be concentrated in even degree; then $\alpha = \mathrm{id}$, the signed sandwich is the unsigned sandwich, $S_{a,b} = T_{a,b}$, and every statement of the article reduces to the corresponding statement of *The Sandwich Operator on an Algebra*. This is the degenerate case, and it is the reason the word "signed" is reserved for the case in which $\alpha \neq \mathrm{id}$.

### A Group Algebra with a Parity

Let $A = k[G]$ for a group $G$ and let $\chi : G \to \{\pm 1\}$ be a homomorphism; extending $\chi$ linearly gives an involutive automorphism $\alpha$ of $A$, the grade involution of the grading that puts each $g$ in degree $\chi(g)$. Then $S_{a,b}$ is the sandwich twisted by the sign of the group elements, and for $a = g$, $b = g^{-1}$ the signed conjugation acts on a group element by
$$
\rho_g(x_h) = g\,\alpha(x_h)\,g^{-1} = \chi(h)\,x_{ghg^{-1}} = \alpha\bigl(x_{ghg^{-1}}\bigr),
$$
the ordinary conjugation dressed by the parity of the element acted on — not of the conjugating element, and the two agree only when the parities coincide. The reflector condition is $\chi(g)g^2 \in Z(A)$, so every central element is a reflector and so is every element of order two; the signed conjugations are the conjugations dressed by the parity, and the reflections are the classes of those elements modulo the centre.

### The Exterior Algebra

Let $A = \Lambda(V)$ be the exterior algebra of a $k$-module $V$, graded by the degree, with grade involution $\alpha$ negating the odd part. The signed sandwich is the two-sided multiplication twisted by the parity, and the signed conjugations $\rho_u(x) = u\,\alpha(x)\,u^{-1}$ for an odd element $u$ are the reflections of the algebra; for a vector $v$ with $v^2 = 0$ the element $v$ is not a unit and the operator $\rho_v$ is not defined as a conjugation, which is the degenerate case. The exterior algebra and its involution belong to *The Exterior Algebra* of the anti-symmetric category, and its relation to the metric case is Part II.

## Summary

Fix an involutive automorphism $\alpha$ of $A$, $k$-linear and multiplicative with $\alpha^2 = \mathrm{id}$; the grade involution of a $\mathbb{Z}/2$-grading is the standard instance, and the grading theory itself belongs to *Superalgebras and Graded Structures*. The **signed sandwich** is $S_{a,b}(x) = a\alpha(x)b$, $k$-linear in $x$ and $k$-bilinear in $a$ and $b$, with $S_{1,1} = \alpha$, $S_{a,b}(1) = ab$, and the two readings $S_{a,b} = T_{a,b}\alpha = \alpha T_{\alpha(a),\alpha(b)}$ of the unsigned sandwich. The signed sandwiches satisfy $S_{a,b}T_{c,d} = S_{a\alpha(c),\alpha(d)b}$, $T_{a,b}S_{c,d} = S_{ac,db}$ and $S_{a,b}S_{c,d} = T_{a\alpha(c),\alpha(d)b}$, so the product of two signed sandwiches is an unsigned sandwich; and $S_{a,b}$ is invertible exactly when $a$ and $b$ are units, with inverse $S_{\alpha(a)^{-1},\alpha(b)^{-1}}$.

The signed conjugation $\rho_u = S_{u,u^{-1}}$, $\rho_u(x) = u\alpha(x)u^{-1}$, is an automorphism for every unit $u$ and satisfies $\rho_u^2 = \iota_{u\alpha(u)}$; hence $\rho_u$ is a reflection exactly when $u\alpha(u)$ is central, which for an odd element $u$ of a graded algebra with $u^2$ central is the case $u\alpha(u) = -u^2$. The reflections are the signed conjugations of order two and are treated in *Reflections as Signed Two-Sided Operators on an Algebra*; the one-sided signed operators are the subject of *The Signed Left Multiplication on an Algebra*, and the signed adjoints are the subject of *The Signed Adjoint Sandwich on an Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A$ | a unital associative $k$-algebra |
| $\alpha$ | an involutive automorphism, $\alpha^2 = \mathrm{id}$ |
| $A = A^+ \oplus A^-$ | the $\pm1$ eigenspaces, a $\mathbb{Z}/2$-grading |
| $T_{a,b}(x) = axb$ | the unsigned sandwich |
| $S_{a,b}(x) = a\alpha(x)b$ | the signed sandwich |
| $\mathcal{S}^{\mathrm{s}}(A)$ | the signed sandwich space |
| $S_{a,b} = T_{a,b}\alpha = \alpha T_{\alpha(a),\alpha(b)}$ | the relation to the unsigned sandwich |
| $S_{a,b}S_{c,d} = T_{a\alpha(c),\alpha(d)b}$ | the composition rule for two signed sandwiches |
| $\rho_u = S_{u,u^{-1}}$, $\rho_u(x) = u\alpha(x)u^{-1}$ | the signed conjugation |
| $\rho_u^2 = \iota_{u\alpha(u)}$ | the square of a signed conjugation |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the graded algebras with an involutive automorphism and the regular representations.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the multiplication algebra and the two-sided operators.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the twisted sandwiches and the reflections in the general algebraic setting.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the reflections realised by the signed conjugations of a Clifford algebra.
