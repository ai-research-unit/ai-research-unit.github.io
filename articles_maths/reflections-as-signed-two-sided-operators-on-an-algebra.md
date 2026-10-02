# __Reflections as Signed Two-Sided Operators on an Algebra__

## Introduction

A reflection is an order-two symmetry, and on an algebra the symmetries are the automorphisms. The reflections that an algebra carries with respect to an involutive automorphism $\alpha$ are the automorphisms of order two of the form

$$
\rho_u(x) = u\,\alpha(x)\,u^{-1},
$$

one for each unit $u$ whose product $u\,\alpha(u)$ with its twist is central. Each such $\rho_u$ is a **signed two-sided operator**, the signed sandwich $S_{u,u^{-1}}$ of *The Signed Sandwich on an Algebra*, and it is an automorphism of the algebra of order two. The present article studies the correspondence between these reflections and the units that produce them, computes the fixed subalgebra and the negated part, and records the cases in which the correspondence fails.

Throughout, $k$ is a field and $A$ is a unital associative $k$-algebra with an involutive automorphism $\alpha$, $\alpha^2 = \mathrm{id}$; the grade involution of a $\mathbb{Z}/2$-grading is the standard instance and the grading theory belongs to *Superalgebras and Graded Structures*. The signed sandwich and the signed conjugation are those of *The Signed Sandwich on an Algebra*, the automorphisms and the inner automorphisms are those of *Automorphisms and Derivations of Algebras*, and the operator-theoretic conventions are those of the group `- Operator Theory` of this category.

## The Reflector

### Definition

**Definition.** A **reflector** of $A$ with respect to $\alpha$ is a unit $u \in A^\times$ with

$$
u\,\alpha(u) \in Z(A),
$$

that is, a unit whose product with its twist is central. The **reflection** determined by a reflector $u$ is the signed conjugation

$$
\rho_u : A \to A, \qquad \rho_u(x) = u\,\alpha(x)\,u^{-1} = S_{u,\,u^{-1}}(x).
$$

The set of reflectors is written $R^\times(A,\alpha)$ and the set of reflections is written $\mathrm{Ref}(A,\alpha)$.

The word is chosen to match the classical case: on a Clifford algebra the signed conjugations by the odd elements of square one are the reflections in the vectors, and the product $u\alpha(u) = -u^2$ is then a scalar and hence central. The algebra carries the reflector, and the reflection is the operator it produces.

### The Reflection Is an Involutive Automorphism

**Theorem.** For every reflector $u$ the signed conjugation $\rho_u$ is an automorphism of the $k$-algebra $A$ with

$$
\rho_u^2 = \mathrm{id},
$$

so that $\rho_u$ is an involutive automorphism of $A$. Conversely, if a signed conjugation $\rho_u$ is an involutive automorphism, then $u$ is a reflector.

*Proof.* The signed conjugation is the composite of the automorphisms $\alpha$ and $\iota_u$, hence an automorphism. Its square was computed in *The Signed Sandwich on an Algebra* as $\rho_u^2 = \iota_{u\alpha(u)}$, the inner automorphism by $u\alpha(u)$; the inner automorphism by an element is the identity exactly when the element is central, so $\rho_u^2 = \mathrm{id}$ exactly when $u\alpha(u)$ is central, which is the definition of a reflector. The converse is the same computation read backwards.

**Corollary.** The reflections are exactly the involutive automorphisms of $A$ that are **signed inner**, that is, of the form $\alpha$ composed with an inner automorphism; the word "signed" records the insertion of $\alpha$, and a reflection is neither an inner automorphism in general nor a signed sandwich with arbitrary two factors.

**Corollary.** The unit $1$ is a reflector — its product $1\cdot\alpha(1) = 1$ with its twist is central — and the reflection it determines is $\rho_1 = \alpha$, the involutive automorphism itself; the family is therefore never empty, and the identity automorphism lies in it exactly when the twist is trivial, $\alpha = \mathrm{id}$.

### The Eigenvalue Decomposition

**Proposition.** Let $u$ be a reflector and let $\rho = \rho_u$ be its reflection. Then $A$ decomposes as

$$
A = A^+_\rho \oplus A^-_\rho, \qquad A^+_\rho = \{x : \rho(x) = x\}, \qquad A^-_\rho = \{x : \rho(x) = -x\},
$$

the summands are the fixed subalgebra and the negated part, and

$$
A^+_\rho A^+_\rho \subseteq A^+_\rho, \qquad A^+_\rho A^-_\rho \subseteq A^-_\rho, \qquad A^-_\rho A^+_\rho \subseteq A^-_\rho, \qquad A^-_\rho A^-_\rho \subseteq A^+_\rho .
$$

*Proof.* The map $\rho$ is an involutive automorphism, so its eigenvalues are $\pm 1$ and the decomposition and the multiplication table are those of the eigenspaces of an involutive automorphism, as in *The Signed Sandwich on an Algebra*. When $2 = 0$ the negated part is zero and the decomposition collapses, since an order-two automorphism is the identity.

**Corollary.** A reflection is determined by its fixed subalgebra, equivalently by its negated part: if $\rho$ and $\rho'$ are involutive automorphisms with the same fixed subalgebra, then $\rho = \rho'$.

*Proof.* An automorphism of order two is determined by its action on the eigenspaces, and the $\pm1$ eigenspaces determine each other by $A = A^+ \oplus A^-$.

The corollary is the algebraic replacement for the geometric statement that a reflection is determined by its mirror: the mirror is the fixed subalgebra, and the negated part is the perpendicular direction, which is a Part II object and is not named here.

## The Correspondence

### The Map from the Reflectors

**Theorem.** The assignment $u \mapsto \rho_u$ is a map from the reflectors of $A$ onto the reflections of $A$, and it is constant exactly on the cosets of the centre: for units $u$ and $v$,

$$
\rho_u = \rho_v \qquad \Longleftrightarrow \qquad v^{-1} u \in Z(A)^\times .
$$

Hence the reflections are parametrised by the reflectors modulo the units of the centre,

$$
\mathrm{Ref}(A,\alpha) \;\cong\; R^\times(A,\alpha) / Z(A)^\times ,
$$

and the reflection $\rho_1 = \alpha$ is the class of the central units.

*Proof.* Suppose $\rho_u = \rho_v$, that is $u\alpha(x)u^{-1} = v\alpha(x)v^{-1}$ for every $x$. Multiplying by $v^{-1}$ on the left and by $u$ on the right gives $(v^{-1}u)\alpha(x) = \alpha(x)(v^{-1}u)$ for every $x$; since $\alpha$ is surjective, this says that $v^{-1}u$ commutes with every element, that is $v^{-1}u \in Z(A)$. Both are units, so the element lies in $Z(A)^\times$. Conversely a central unit is absorbed by the conjugation. Finally the image of $Z(A)^\times$ is $\alpha$, since a central unit commutes with everything and $\rho_u = \alpha$ when $u$ is central.

### The Element Acting by an Involution

**Proposition.** Let $u$ be a reflector and let $\rho = \rho_u$. Then

$$
\rho(u) = \alpha(u),
$$

and $\rho$ is the composite $\rho = \iota_u \circ \alpha$ of the inner automorphism by $u$ and the twist. Equivalently, $u$ acts on $A$ through the inner automorphism that corrects $\alpha$ to $\rho$.

*Proof.* Since $u\alpha(u)$ is central, $u$ commutes with it, so $\rho(u) = u\alpha(u)u^{-1} = \alpha(u)$. The composite form is the definition: $\iota_u(\alpha(x)) = u\alpha(x)u^{-1} = \rho(x)$.

**Corollary.** Every reflection is the composite of the fixed involutive automorphism $\alpha$ with an inner automorphism, $\rho_u = \iota_u \alpha$, and the reflector $u$ is the element whose inner automorphism corrects the twist to the desired reflection. The correspondence of the theorem is therefore the statement that the reflections form the coset $\iota_{A^\times}\alpha$ of the inner automorphism group inside the automorphism group, restricted to the elements of order two.

*Proof.* The identity $\rho_u = \iota_u\alpha$ is the definition read as a composite. Two coset representatives give the same reflection exactly when their ratio is central, by the theorem; the inner automorphism $\iota_u$ depends on $u$ only through its class modulo the centre, so the restriction to reflectors cuts out the reflections among the elements of order two.

### The Correspondence in the Automorphism Group

**Proposition.** The reflections of $A$ relative to $\alpha$ are the involutive automorphisms lying in the coset $\iota_{A^\times} \alpha$ of the inner automorphism group, and the map

$$
A^\times / Z(A)^\times \longrightarrow \mathrm{Out}(A) = \operatorname{Aut}_k(A)/\operatorname{Inn}_k(A), \qquad [u] \mapsto [\iota_u]
$$

sends the reflectors to the classes of the reflections. In particular, if every automorphism of $A$ is inner — for example if $A$ is a central simple algebra, by *Central Simple Algebras and the Brauer Group* — then every involutive automorphism is a reflection up to a choice of $\alpha$.

*Proof.* The first statement is the corollary above. The map $[u] \mapsto [\iota_u]$ is the standard identification of the inner automorphism group with $A^\times/Z(A)^\times$. For a central simple algebra the outer automorphism group is trivial, so every automorphism lies in the inner coset, and an involutive automorphism lies in the inner coset of the appropriate $\alpha$.

## The Degenerate Cases

### The Failure of Order Two

**Proposition.** For a unit $u$ that is not a reflector, the signed conjugation $\rho_u$ is an automorphism and its square is the inner automorphism $\iota_{u\alpha(u)} \neq \mathrm{id}$; hence $\rho_u$ has infinite order whenever $u\alpha(u)$ has infinite order as an inner automorphism. Such an operator is a signed two-sided operator but not a reflection.

*Proof.* The square is $\iota_{u\alpha(u)}$ by the computation of *The Signed Sandwich on an Algebra*. If $u\alpha(u)$ is not central, its inner automorphism is not the identity, and the powers of $\rho_u$ are governed by the powers of $u\alpha(u)$; the inner automorphism $\iota_w$ has finite order exactly when some power of $w$ is central, so $\rho_u$ has infinite order when no power of $u\alpha(u)$ is central.

**Example.** Let $A = M_n(k)$ with $\alpha = \mathrm{id}$ and let $u$ be a noncentral invertible matrix. Then $\rho_u = \iota_u$ is an inner automorphism whose order is the order of the class of $u$ in $A^\times/Z(A)^\times$; for a generic $u$ this order is infinite. The signed conjugation is thus not a reflection, and the reflector condition $u\alpha(u) = u^2 \in Z(A)$, which for $\alpha = \mathrm{id}$ reduces to $u^2$ scalar, is the obstruction.

### The Central Case

**Proposition.** If $u$ is central, then $\rho_u = \alpha$, whatever $u$ is. Hence the central units contribute only the reflection $\alpha$, and the correspondence is not injective at the centre. This is exactly the kernel computed in the theorem.

*Proof.* A central unit commutes with everything, so $\rho_u(x) = u\alpha(x)u^{-1} = \alpha(x)$.

### The Characteristic-Two Case and the Trivial Twist

**Proposition.** When $2 = 0$ in $k$, or more generally when $\alpha = \mathrm{id}$, the signed conjugation is the ordinary inner automorphism $\iota_u$, the condition for a reflector is $u^2 \in Z(A)$, and the reflections are the inner involutions. In particular the family may be trivial.

*Proof.* With $\alpha = \mathrm{id}$ one has $\rho_u = \iota_u$ and $u\alpha(u) = u^2$; the criterion of the theorem gives the reflector condition, and the reflections are the inner automorphisms of order two. When $2 = 0$ every involutive automorphism is the identity in the sense that its negated part is zero, so the only reflections of order two that remain are the inner involutions whose square is the identity, and the decomposition of a reflection into fixed and negated parts collapses.

### The Non-Inner Involutions

**Proposition.** An involutive automorphism of $A$ that is not signed inner is not a reflection of the family. In particular, if the outer automorphism group of $A$ is nontrivial, there are involutive automorphisms outside the coset $\iota_{A^\times}\alpha$.

*Proof.* The reflections lie in the coset $\iota_{A^\times}\alpha$ by the correspondence theorem, and an automorphism outside that coset represents a nontrivial class in $\mathrm{Out}(A)$, so it cannot be a reflection.

The four cases are the failure of the correspondence in the two directions: a signed conjugation need not be a reflection when the reflector condition fails, and an involutive automorphism need not be a signed conjugation when it is outer. The correspondence is exact only under the two hypotheses — the reflector condition for the operator and the innerness of the automorphism.

## The Examples

### A Matrix Algebra with a Diagonal Twist

Let $A = M_n(k)$ and let $D$ be an invertible diagonal matrix with $D^2 = I$; the map $\alpha(X) = DXD^{-1}$ is an involutive automorphism, the conjugation by a sign matrix, and it is the grade involution of the grading that puts the entries in the $+1$ blocks in even degree and the entries in the $-1$ blocks in odd degree. A unit $U$ is a reflector exactly when $U\alpha(U) = U D U D^{-1}$ is a scalar, and the reflection is $\rho_U(X) = U D X D^{-1} U^{-1} = (UD)\,X\,(UD)^{-1}$: the reflection is the inner automorphism by the product $UD$, and the reflectors are the units $U$ for which $UDU D^{-1}$ is scalar. For $D = I$ this reduces to the case in which the reflections are the involutive inner automorphisms by matrices whose square is scalar.

### A Group Algebra with a Parity

Let $A = k[G]$ and let $\chi : G \to \{\pm 1\}$ be a homomorphism, extending to the involutive automorphism $\alpha$ of *The Signed Sandwich on an Algebra*, so that $\alpha(x_h) = \chi(h)x_h$ on a group element. A group element $g$ is a reflector exactly when $\chi(g)\,g^2$ is central, and the reflection acts on a group element by
$$
\rho_g(x_h) = g\,\alpha(x_h)\,g^{-1} = \chi(h)\,x_{ghg^{-1}} = \alpha\bigl(x_{ghg^{-1}}\bigr),
$$
so the sign is the parity of the element acted on and not of the conjugating element. Every central element is a reflector, and so is every element of order two, since $\chi(g)$ is a scalar; the reflections are therefore the conjugations by those group elements modulo the centre.

### The Exterior Algebra

Let $A = \Lambda(V)$ with the degree grading. For a unit $u$ the signed conjugation is $\rho_u(x) = u\alpha(x)u^{-1}$, and the reflector condition is $u\alpha(u) \in Z(A)$. For an even unit $u$ this is $u^2$ central, and for an odd unit it is $-u^2$ central. The exterior algebra is not a Clifford algebra, so an odd vector $v$ has $v^2 = 0$ and is not a unit; the reflections by vectors therefore require the Clifford quotient, where $v^2$ is a scalar by construction, and that construction belongs to *Quadratic Forms and Clifford Algebras* of Part II.

## Summary

A **reflector** is a unit $u$ with $u\alpha(u)$ central, and the **reflection** it determines is the signed two-sided operator $\rho_u(x) = u\alpha(x)u^{-1} = S_{u,u^{-1}}(x)$. Each reflection is an automorphism of $A$ of order two, being the composite $\iota_u\alpha$ of the inner automorphism by $u$ and the fixed involutive automorphism $\alpha$; the square is $\rho_u^2 = \iota_{u\alpha(u)}$, so the reflector condition is exactly the condition that the reflection be of order two. A reflection is determined by its fixed subalgebra $A^+_\rho$, the decomposition $A = A^+_\rho \oplus A^-_\rho$ has the multiplication table of a $\mathbb{Z}/2$-grading, and the negated part is a Part II object when it is read geometrically.

The correspondence between reflections and reflectors is $\mathrm{Ref}(A,\alpha) \cong R^\times(A,\alpha)/Z(A)^\times$, with $\rho_u = \rho_v$ exactly when $v^{-1}u$ is central; the class of the central units is the reflection $\rho_1 = \alpha$. The reflections are the involutive automorphisms in the coset $\iota_{A^\times}\alpha$ of the inner automorphism group. The correspondence fails in the degenerate cases: a signed conjugation with $u\alpha(u)$ noncentral is an automorphism of infinite order and not a reflection; the central units all give $\alpha$; when $\alpha = \mathrm{id}$ the reflections are the inner involutions $u^2 \in Z(A)$; and an involutive automorphism that is outer is not a signed conjugation at all. On $M_n(k)$ with a diagonal twist the reflections are the inner automorphisms by the products $UD$, and on a group algebra with a parity they are the conjugations dressed by the parity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | the field of scalars |
| $A$ | a unital associative $k$-algebra |
| $\alpha$ | the fixed involutive automorphism, $\alpha^2 = \mathrm{id}$ |
| $R^\times(A,\alpha)$ | the reflectors, the units $u$ with $u\alpha(u)$ central |
| $\rho_u(x) = u\alpha(x)u^{-1}$ | the reflection by the reflector $u$ |
| $\mathrm{Ref}(A,\alpha)$ | the reflections, $\cong R^\times(A,\alpha)/Z(A)^\times$ |
| $A = A^+_\rho \oplus A^-_\rho$ | the fixed and negated parts of a reflection |
| $\rho_u = \iota_u \alpha$ | the reflection as a composite |
| $\rho_u^2 = \iota_{u\alpha(u)}$ | the square, the identity exactly for a reflector |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the inner automorphisms and the coset structure of the automorphism group.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the involutive automorphisms and the gradings they define.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the reflections realised by the signed conjugations.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions and the automorphisms of the classical algebras.
