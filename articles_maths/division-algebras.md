
# __Division Algebras__

## Introduction

A division algebra is an algebra with identity in which every nonzero element is invertible. The examples of the corpus — the real numbers, the complex numbers and the quaternions, together with the finite-dimensional algebras over other fields — are the building blocks of the structure theory, because the Wedderburn–Artin theorem writes every finite-dimensional semisimple algebra as a product of matrix algebras over division algebras. This article develops the definition and its elementary consequences, the classification of the finite-dimensional associative division algebras over $\mathbb{R}$ (Frobenius), the theorem that every finite division ring is a field (Wedderburn), and the Hurwitz classification of the normed division algebras, together with the reason the doubling chain terminates at dimension eight.

The ground ring is a field $k$ unless stated otherwise. The division algebras produced by the Cayley–Dickson construction beyond the quaternions are not associative, and the article marks the point at which each algebraic property is lost.

## Definition and Elementary Properties

**Definition.** A **division algebra** over $k$ is an associative $k$-algebra $D$ with unit $1 \neq 0$ such that every nonzero element is a unit; that is, $D^\times = D\setminus\{0\}$.

For a finite-dimensional $D$ this is equivalent to the absence of zero divisors, as the next proposition shows; a division algebra is also simple, its only two-sided ideals being $0$ and $D$, and a commutative division algebra is a **field**.

**Proposition (finite-dimensional criterion).** Let $A$ be a finite-dimensional unital $k$-algebra. Then $A$ is a division algebra if and only if $A$ has no zero divisors.

*Proof.* A division algebra has no zero divisors, since $ab = 0$ with $a \neq 0$ implies $b = a^{-1}(ab) = 0$. Conversely, suppose $A$ has no zero divisors and let $a \neq 0$. The linear map $L_a : A \to A$, $L_a(x) = ax$, is injective: if $ax = 0$ then $x = 0$. An injective linear map of a finite-dimensional space is bijective, so there is $b$ with $ab = 1$. Applying the same argument to the right multiplication $R_a$ gives $c$ with $ca = 1$, and then $c = c(ab) = (ca)b = b$, so $a$ has the two-sided inverse $b$. $\square$

**Proposition (ideals and quotients).** A division algebra has exactly two left ideals and exactly two right ideals, namely $0$ and the whole algebra; hence it is simple, and every nonzero algebra homomorphism from a division algebra is injective. A finite-dimensional simple algebra over $k$ is, by Wedderburn–Artin, of the form $M_n(D)$ for a division algebra $D$ and an integer $n \geq 1$, and it is a division algebra exactly when $n = 1$.

*Proof.* If $I \neq 0$ is a left ideal and $0 \neq a \in I$, then $1 = a^{-1}a \in I$, so $I = A$. Injectivity of a homomorphism $\varphi$ follows because $\ker\varphi$ is a proper two-sided ideal, hence $0$. The last statement is Wedderburn–Artin: a simple finite-dimensional algebra is $M_n(D)$ for a division algebra $D$, and $M_n(D)$ is a division algebra only for $n = 1$. $\square$

**Example.** $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and every field are division algebras. The algebras $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$, $M_n(k)$ for $n \geq 2$, $k[x]$ and $k[G]$ for nontrivial finite $G$ are not, by the zero divisors listed in *Examples of Algebras*. The pattern is instructive: $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ are the division algebras among the number systems, and each of them has a norm form that vanishes only at the origin.

## Finite-Dimensional Division Algebras over $\mathbb{R}$: Frobenius

**Theorem (Frobenius, standard).** Every finite-dimensional associative division algebra over $\mathbb{R}$ is isomorphic to one of

$$
\mathbb{R}, \qquad \mathbb{C}, \qquad \mathbb{H}.
$$

*Proof (outline).* Let $D$ be such an algebra, of dimension $n$ over $\mathbb{R}$, and let $Z$ be its centre.

If $D$ is commutative, then $D$ is a field extension of $\mathbb{R}$ of finite degree $n$. Every element of $D$ has a minimal polynomial over $\mathbb{R}$, which is irreducible because $D$ is a field; over $\mathbb{R}$ the irreducible polynomials have degree $1$ or $2$, since every real polynomial of odd degree has a real root. Hence $n \leq 2$ and $D$ is $\mathbb{R}$ or $\mathbb{C}$.

Suppose $D$ is not commutative. Its centre $Z$ is a field extension of $\mathbb{R}$ of finite degree, hence $\mathbb{R}$ or $\mathbb{C}$ by the previous paragraph; and $Z = \mathbb{C}$ is impossible, because then every element $u \in D$ has $u - \lambda$ non-invertible for some $\lambda \in \mathbb{C}$ — the $\mathbb{C}$-linear map $x \mapsto ux$ has an eigenvalue — and a non-invertible element of a division algebra is zero, so every element would be central and $D$ commutative. Hence $Z = \mathbb{R}$, and $D$ is central over $\mathbb{R}$. Choose $u \in D\setminus\mathbb{R}$; then $\mathbb{R}[u]$ is a proper field extension of $\mathbb{R}$, hence $\mathbb{R}[u] \cong \mathbb{C}$. Now $D$ is a left module over this copy $C$ of $\mathbb{C}$, so $\dim_\mathbb{R}D = 2\dim_C D$. The inner automorphisms of $D$ preserve $C$ and act on it by the only nontrivial possibility, complex conjugation; analysing the conjugation action shows $\dim_C D \leq 2$, so $\dim_\mathbb{R}D \leq 4$. The case $\dim_\mathbb{R}D = 2$ is commutative, and the case $\dim_\mathbb{R}D = 4$ forces $D \cong \mathbb{H}$: the subalgebra generated by two independent anticommuting square roots of $-1$ is quaternion, and the dimension count leaves no room for anything more. $\square$

**Corollary.** The only commutative finite-dimensional real division algebras are $\mathbb{R}$ and $\mathbb{C}$; the only non-commutative one is $\mathbb{H}$. In particular there is no three-dimensional real division algebra, which is the obstruction met.

**Remark (the hypotheses are sharp).** Frobenius' theorem concerns associative algebras. Dropping associativity admits the octonions, of dimension $8$; keeping associativity but dropping the requirement that the ground field be $\mathbb{R}$ admits the division rings of the next section; and dropping non-degeneracy of the norm, while keeping finite dimension, admits the split algebras $\mathbb{D}$, $\mathbb{H}_{\mathbb{D}}$ and $\mathbb{B}$, all of which have zero divisors.

## Wedderburn's Little Theorem

**Theorem (Wedderburn, standard).** Every finite division ring is a field: if $D$ is a division ring with finitely many elements, then $D$ is commutative.

*Proof (sketch).* The centre $Z$ of $D$ is a finite field $\mathbb{F}_q$, and $D$ is a finite-dimensional $Z$-vector space of dimension $n$, so $|D| = q^n$. Counting the conjugacy classes of the multiplicative group $D^\times$ and using the class equation, together with the fact that the size of every conjugacy class is the index of a centraliser and hence of the form $(q^n-1)/(q^d-1)$, one shows that the cyclotomic polynomial $\Phi_n(q)$ divides $q - 1$ whenever $n \geq 2$. Since $\Phi_n(q) > q - 1$ for $n \geq 2$ and $q \geq 2$, this is impossible, so $n = 1$ and $D = Z$ is a field. $\square$

The theorem is the boundary case of the structure theory over finite fields: because there are no finite non-commutative division rings, every finite simple ring is a matrix algebra over a finite field, by Wedderburn–Artin. It also shows that the construction of $\mathbb{H}$ genuinely needs an infinite ground field.

## Normed Division Algebras and Hurwitz

**Definition.** A **normed division algebra** is a finite-dimensional real algebra $A$ with unit and with a positive definite quadratic form $N$ such that

$$
N(uv) = N(u)N(v), \qquad N(u) \neq 0 \ \text{ for } u \neq 0 .
$$

The form is then multiplicative and non-degenerate, so $A$ is a division algebra; $N$ is called the **norm**.

**Theorem (Hurwitz, standard).** The only normed division algebras over $\mathbb{R}$ are, up to isomorphism,

$$
\mathbb{R}\ (\dim 1), \qquad \mathbb{C}\ (\dim 2), \qquad \mathbb{H}\ (\dim 4), \qquad \mathbb{O}\ (\dim 8).
$$

The algebra $\mathbb{O}$ of **octonions** is non-associative; $\mathbb{H}$ is associative but non-commutative; $\mathbb{C}$ is commutative but not real-closed; and $\mathbb{R}$ is the base case. The positive definite multiplicative norm exists in no other dimension.

**Remark (the octonions).** The octonions are a real division algebra of dimension $8$ with a multiplicative norm, but they are not associative: the associator $[u,v,w] = (uv)w - u(vw)$ does not vanish identically. They are **alternative**, meaning that every subalgebra generated by two elements is associative, and this weaker property is what survives the loss of associativity at dimension eight.

## The Cayley–Dickson Construction

The four normed division algebras are produced by a single recursive construction. Given a real algebra $A$ with a conjugation $u \mapsto \bar u$ and norm $N(u) = u\bar u$, define the **double** $\mathbb{D}(A) = A \oplus A$ with

$$
(u, v)(u', v') = (uu' - \bar{v'}v, \ v'u + v\bar{u'}), \qquad \overline{(u,v)} = (\bar u, -v).
$$

Starting from $\mathbb{R}$ and iterating,

$$
\mathbb{R} \longrightarrow \mathbb{C} \longrightarrow \mathbb{H} \longrightarrow \mathbb{O} \longrightarrow \mathbb{S},
$$

one obtains $\mathbb{R}$, $\mathbb{C}$ (dimension 2), $\mathbb{H}$ (dimension 4), $\mathbb{O}$ (dimension 8) and the **sedenions** $\mathbb{S}$ (dimension 16). The norm form doubles at each step, $N\bigl((u,v)\bigr) = N(u) + N(v)$, and it stays multiplicative through the octonions but **fails to be multiplicative for the sedenions**. Each doubling costs one algebraic property:

| Stage | Algebra | Dimension | Property lost |
|---|---|---|---|
| $\mathbb{R} \to \mathbb{C}$ | $\mathbb{C}$ | $2$ | order |
| $\mathbb{C} \to \mathbb{H}$ | $\mathbb{H}$ | $4$ | commutativity |
| $\mathbb{H} \to \mathbb{O}$ | $\mathbb{O}$ | $8$ | associativity |
| $\mathbb{O} \to \mathbb{S}$ | $\mathbb{S}$ | $16$ | the multiplicative norm |

**Proposition (the sedenions have zero divisors).** $N(uv) = N(u)N(v)$ fails in $\mathbb{S}$, and consequently $\mathbb{S}$ is not a division algebra.

*Proof (sketch).* The doubling formula gives $N\bigl((u,v)(u',v')\bigr) = N(uu' - \bar{v'}v) + N(v'u + v\bar{u'})$, and expanding it with the multiplicativity of $N$ in $A$ shows that multiplicativity on the double is equivalent to a bilinearity condition on the associator of $A$: it holds for the associative composition algebras $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and fails for $\mathbb{O}$, hence for the double $\mathbb{S}$. The failure is witnessed by explicit elements of the standard basis $e_0, \dots, e_{15}$,

$$
(e_1 + e_{10})(e_4 - e_{15}) = 0, \qquad N(e_1 + e_{10}) = N(e_4 - e_{15}) = 2 ,
$$

so that $\mathbb{S}$ has zero divisors, and it is not a division algebra. $\square$

## Division Algebras over Other Fields

Over a field $k$, the classification is richer, and the finite-dimensional central simple algebras are organised by a group. A **quaternion algebra over $k$** is a four-dimensional central simple $k$-algebra; it is either a division algebra or is isomorphic to $M_2(k)$. Over $\mathbb{R}$ the two possibilities are $\mathbb{H}$ and $M_2(\mathbb{R})$, so there is exactly one real quaternion division algebra; over a field such as $\mathbb{Q}$ there are infinitely many, given by the symbol algebras $(a,b)_k$ with $a, b \in k^\times$. The **Brauer group** $\operatorname{Br}(k)$ has as its elements the Morita-equivalence classes of finite-dimensional central simple $k$-algebras, with the tensor product as the group operation; a division algebra and each of its matrix algebras represent the same element, and $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2$ is generated by the class of $\mathbb{H}$.

**Example (the two real quaternion algebras).** The general quaternion algebra over a field $k$ with parameters $a, b \in k^\times$ has $k$-basis $1, u, v, w$ with

$$
u^2 = a, \qquad v^2 = b, \qquad uv = w = -vu .
$$

For $k = \mathbb{R}$, $a = b = -1$ this is the division algebra $\mathbb{H}$, with norm form $N = x_0^2 + x_1^2 + x_2^2 + x_3^2$; for $a = b = +1$ the element $1 + u$ is a zero divisor, since $(1+u)(1-u) = 1 - u^2 = 0$, so the algebra is not a division algebra, and as a four-dimensional central simple real algebra it is isomorphic to $M_2(\mathbb{R})$. These are the two elements of $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2$ in their four-dimensional form.

**Theorem (Wedderburn–Artin, standard).** Every finite-dimensional semisimple $k$-algebra is isomorphic to a product $\prod_i M_{n_i}(D_i)$ with the $D_i$ finite-dimensional division algebras over $k$.

This is the theorem for which division algebras exist in the structure theory: they are precisely the simple factors of the semisimple algebras, and the classification of the $D_i$ is the content of the theory beyond the present article.

## The Skolem–Noether Theorem

The structure theory says that the simple algebras are the matrix algebras over division algebras; the next question is how rigid their embeddings are, and the answer is that they are as rigid as possible.

**Theorem (Skolem–Noether, standard).** Let $k$ be a field, let $A$ be a finite-dimensional central simple $k$-algebra, let $B$ be a finite-dimensional simple $k$-subalgebra of $A$, and let $f, g : B \to A$ be two unital $k$-algebra homomorphisms. Then there is a unit $a \in A^\times$ with

$$
g(b) = a\,f(b)\,a^{-1} \qquad \text{for all } b \in B .
$$

*Proof (sketch).* Write $L = Z(B)$ for the centre of $B$. The tensor product $B \otimes_k A^{\mathrm{op}}$ is a finite-dimensional simple ring: it is $B \otimes_L (L \otimes_k A^{\mathrm{op}})$ by the base-change identity $B\otimes_k M \cong B \otimes_L (L \otimes_k M)$, the algebra $L \otimes_k A^{\mathrm{op}}$ is central simple over $L$ because $A^{\mathrm{op}}$ is central simple over $k$, and $B$ is central simple over $L$; a tensor product of central simple algebras being central simple, $B \otimes_k A^{\mathrm{op}}$ is central simple over $L$, hence simple as a ring. Such an algebra has a unique simple module up to isomorphism, because Wedderburn–Artin writes it as $M_n(D)$ for a division algebra $D$ and the unique simple module of $M_n(D)$ is $D^n$. Now $A$ carries two $B \otimes_k A^{\mathrm{op}}$-module structures,

$$
(b \otimes a')\cdot_f x = f(b)\,x\,a', \qquad (b \otimes a')\cdot_g x = g(b)\,x\,a' ,
$$

and each is a direct sum of copies of the unique simple module with the same multiplicity, by dimension count; hence there is a $k$-linear isomorphism $\psi$ of $A$ intertwining $\cdot_f$ with $\cdot_g$. Being a $B \otimes_k A^{\mathrm{op}}$-module isomorphism, $\psi$ is in particular $A^{\mathrm{op}}$-linear, that is $\psi(xa') = \psi(x)a'$, so it is an isomorphism of $A$ as a free right $A$-module of rank one. Therefore $a = \psi(1)$ generates $A$ as a right $A$-module and is a unit, and combining $A^{\mathrm{op}}$-linearity at $x = 1$ with the intertwining relation at $x = 1$ gives

$$
\psi(f(b)) = \psi(1)f(b) = a f(b), \qquad \psi(f(b)) = g(b)\psi(1) = g(b)a ,
$$

whence $g(b)a = af(b)$, that is $g(b) = a f(b)a^{-1}$. $\square$

**Corollary (every automorphism of a central simple algebra is inner).** For a finite-dimensional central simple $k$-algebra $A$ the map $A^\times \to \operatorname{Aut}_k(A)$, $a \mapsto (x \mapsto axa^{-1})$, is surjective with kernel $k^\times$, so

$$
\operatorname{Aut}_k(A) \cong A^\times/k^\times .
$$

For $A = M_n(k)$ this is the projective general linear group $\mathrm{PGL}_n(k) = \mathrm{GL}_n(k)/k^\times$; for $A = M_n(D)$ with $D$ a division algebra it is $\mathrm{PGL}_n(D) = \mathrm{GL}_n(D)/k^\times$, where $\mathrm{GL}_n(D) = M_n(D)^\times$, and in each case the derivations of $A$ are the inner ones, $\delta = \operatorname{ad}_h$, as in *Automorphisms and Derivations of Algebras*.

**Example (the quaternions, and why centrality is needed).** For $A = \mathbb{H}$ over $\mathbb{R}$ the corollary gives $\operatorname{Aut}_\mathbb{R}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times \cong SU(2)/\{\pm1\} \cong SO(3)$, in agreement with the computation of that automorphism group in *Automorphisms and Derivations of Algebras*. The algebra $\mathbb{C}$ viewed over $\mathbb{R}$ is simple but **not** central, its centre being $\mathbb{C}$ itself, and the conclusion fails there: complex conjugation is an $\mathbb{R}$-automorphism of $\mathbb{C}$ that is not inner, and indeed every inner automorphism of the commutative algebra $\mathbb{C}$ is trivial. Centrality is thus exactly what the theorem needs, and the example shows it cannot be dropped.

**Corollary (conjugacy of embeddings of fields).** If $K \subseteq A$ is a subfield of a finite-dimensional central simple $k$-algebra $A$ with $[K : k] < \infty$ and $K$ separable over $k$, then any two $k$-embeddings $K \to A$ are conjugate by an inner automorphism of $A$. This is the form in which the theorem is used to move between splitting fields of a central simple algebra, and it is the algebraic reason the matrix representations attached to two embeddings of such a field are interchangeable.

## Composition of Quadratic Forms

The multiplicativity of the norm is an identity between sums of squares. Writing $N(u) = \sum_i u_i^2$ and $N(v) = \sum_j v_j^2$, the equation $N(uv) = N(u)N(v)$ says that a product of two sums of $n$ squares is again a sum of $n$ squares, with the components of $uv$ bilinear in the $u_i$ and the $v_j$. The smallest cases are classical:

$$
(x_1^2+x_2^2)(y_1^2+y_2^2) = (x_1y_1 - x_2y_2)^2 + (x_1y_2 + x_2y_1)^2,
$$

the two-square identity, which is the multiplicativity of the complex norm;

$$
(x_1^2+x_2^2+x_3^2+x_4^2)(y_1^2+y_2^2+y_3^2+y_4^2) = z_1^2+z_2^2+z_3^2+z_4^2,
$$

the four-square identity, which is the multiplicativity of the quaternion norm, with

$$
z_1 = x_1y_1 - x_2y_2 - x_3y_3 - x_4y_4, \qquad z_2 = x_1y_2 + x_2y_1 + x_3y_4 - x_4y_3,
$$

$$
z_3 = x_1y_3 - x_2y_4 + x_3y_1 + x_4y_2, \qquad z_4 = x_1y_4 + x_2y_3 - x_3y_2 + x_4y_1 .
$$

There is an eight-square identity, giving the multiplicativity of the octonion norm, but no identity for sixteen squares.

**Theorem (Hurwitz, form of the composition problem, standard).** An identity expressing a product of two sums of $n$ squares as a sum of $n$ squares with bilinear components exists if and only if $n \in \{1, 2, 4, 8\}$.

This is the arithmetic face of the classification above: a normed division algebra of dimension $n$ is exactly a composition of the $n$-square quadratic form, and the theorem of Hurwitz is the statement that such a composition exists only in the four stated dimensions. The five- and six-square cases, in particular, are impossible, which is the numerical reason there is no five-dimensional real division algebra with a definite multiplicative norm.

**Proposition (algebraically closed ground fields).** Let $k$ be algebraically closed. Then the only finite-dimensional division algebra over $k$ is $k$ itself.

*Proof.* Let $D$ be a finite-dimensional division algebra over $k$ and let $u \in D$. The powers $1, u, u^2, \dots$ are linearly dependent, so $u$ satisfies a nonzero polynomial $p$ over $k$; the minimal polynomial of $u$ has a root $\lambda \in k$ because $k$ is algebraically closed, and the minimal polynomial is irreducible because $D$ is a division algebra, so it is $t - \lambda$. Hence $u = \lambda \in k$. $\square$

Over an algebraically closed field the quaternion and octonion phenomena therefore disappear entirely: the division algebras of the classification are exactly the algebras left over when the ground field fails to contain the roots of the relevant polynomials.

## Why the Chain Stops

The chain of normed division algebras stops at dimension $8$ and no further doubling produces a division algebra, so the sequence $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ of dimensions $1, 2, 4, 8$ is complete.

**Theorem (dimension restriction, standard).** If a positive definite quadratic form $N$ on $\mathbb{R}^n$ admits a bilinear multiplication with $N(uv) = N(u)N(v)$ and a two-sided identity, then $n \in \{1, 2, 4, 8\}$.

*Proof (sketch).* The multiplication makes $\mathbb{R}^n\setminus\{0\}$ a loop under the product, translated into a condition on the unit sphere $S^{n-1}$: the identity together with the multiplication give a map $S^{n-1}\times S^{n-1} \to S^{n-1}$ that is nonsingular, and the existence of such a multiplication is equivalent to the existence of $n-1$ linearly independent vector fields on $S^{n-1}$ (Hopf's construction). Adams' theorem on vector fields on spheres computes the maximal number of linearly independent vector fields on $S^{n-1}$: it is $n-1$ only for $n = 1, 2, 4, 8$. Hence the dimension restriction. $\square$

Independently of this topological argument, the Cayley–Dickson computation shows exactly where the algebraic construction breaks down: associativity fails at the octonions and multiplicativity of the norm fails at the sedenions. The two facts agree on the same list, and the chain of normed division algebras therefore has exactly four terms.

## Summary

A **division algebra** is a unital associative algebra in which every nonzero element is a unit; over a field and in finite dimension this is equivalent to the absence of zero divisors, and a division algebra is simple with only the two trivial left ideals. **Frobenius' theorem** classifies the finite-dimensional associative real division algebras as $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, the commutative ones being $\mathbb{R}$ and $\mathbb{C}$ over their own ground fields, so no three-dimensional real division algebra exists. **Wedderburn's little theorem** makes every finite division ring a field. **Hurwitz' theorem** classifies the normed division algebras — those with a positive definite multiplicative norm form — as $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and the non-associative octonions $\mathbb{O}$, of dimensions $1, 2, 4$ and $8$. These four are the successive doubles of the **Cayley–Dickson construction**, $\mathbb{R}\to\mathbb{C}\to\mathbb{H}\to\mathbb{O}\to\mathbb{S}$, each step losing one property: order at $\mathbb{C}$, commutativity at $\mathbb{H}$, associativity at $\mathbb{O}$, and the multiplicative norm at the sedenions $\mathbb{S}$, which have zero divisors. The dimension restriction to $1, 2, 4, 8$ is also a theorem about vector fields on spheres. Over a general field the central division algebras are classified up to Morita equivalence by the **Brauer group**, and by **Wedderburn–Artin** they are the simple factors of the semisimple algebras; the **Skolem–Noether theorem** adds that any two embeddings of a finite-dimensional simple algebra into a central simple algebra are conjugate by an inner automorphism, so $\operatorname{Aut}_k(A) \cong A^\times/k^\times$ for $A$ central simple — for instance $\mathrm{PGL}_n(k)$ for $M_n(k)$ and $SO(3)$ for $\mathbb{H}$ over $\mathbb{R}$ — while centrality cannot be dropped, complex conjugation being a non-inner automorphism of $\mathbb{C}$ over $\mathbb{R}$. The multiplicativity of the norm is equivalent to a **composition of quadratic forms**, a product of two sums of $n$ squares being a sum of $n$ squares; such an identity exists only for $n \in \{1,2,4,8\}$, and over an algebraically closed field the only finite-dimensional division algebra is the field itself.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | Ground field |
| $D$ | Division algebra |
| $D^\times = D\setminus\{0\}$ | Units of a division algebra |
| $\mathbb{R}, \mathbb{C}, \mathbb{H}$ | Real, complex, quaternion division algebras |
| $\mathbb{O}$ | Octonions, $\dim_\mathbb{R} = 8$, non-associative |
| $\mathbb{S}$ | Sedenions, $\dim_\mathbb{R} = 16$, zero divisors |
| $N(u)$ | Multiplicative norm form |
| $Z(D)$ | Centre of $D$ |
| $[u,v,w] = (uv)w - u(vw)$ | Associator |
| $(a,b)_k$ | Quaternion (symbol) algebra over $k$, generators $u, v$ with $u^2=a$, $v^2=b$ |
| $\operatorname{Br}(k)$ | Brauer group |
| $M_n(D)$ | Matrix algebra over $D$ |
| $A^{\mathrm{op}}$ | Opposite algebra, $a\cdot b = ba$ |
| $\operatorname{Aut}_k(A) \cong A^\times/k^\times$ | Automorphisms of $A$, all inner for $A$ central simple |
| $\mathrm{PGL}_n(k)$ | Projective general linear group $\mathrm{GL}_n(k)/k^\times$ |
| $z_i$ | Components in the composition of quadratic forms |



## Further Reading

- Ferdinand G. Frobenius, "Über lineare Substitutionen und bilineare Formen", *Journal für die reine und angewandte Mathematik* **84** (1878), 1–63, for the classification of the finite-dimensional real division algebras.
- Joseph H. M. Wedderburn, "On hypercomplex numbers", *Proceedings of the London Mathematical Society* **6** (1908), 77–118, for the little theorem and the structure of semisimple algebras.
- Adolf Hurwitz, "Über die Composition der quadratischen Formen von beliebig vielen Variabeln", *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1898), 309–316, for the classification of the normed division algebras.
- John F. Adams, "Vector fields on spheres", *Annals of Mathematics* **75** (1962), 603–632, for the dimension restriction $1, 2, 4, 8$.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory, the Brauer group, the quaternion algebras and the Skolem–Noether theorem.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the Cayley–Dickson construction and the octonions and sedenions.
