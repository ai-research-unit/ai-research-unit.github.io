
# __Division Algebras__

## Introduction

A division algebra is an algebra with identity in which every nonzero element is invertible. The examples of the corpus — the real numbers, the complex numbers and the quaternions, together with the finite-dimensional algebras over other fields — are the building blocks of the structure theory, because the Wedderburn–Artin theorem writes every finite-dimensional semisimple algebra as a product of matrix algebras over division algebras. This article develops the definition and its elementary consequences, the classification of the finite-dimensional associative division algebras over $\mathbb{R}$ (Frobenius), the theorem that every finite division ring is a field (Wedderburn), together with the structure theory and the classification over a general field (Wedderburn–Artin, the Brauer group and Skolem–Noether), and the question of when a product of two quaternion algebras over a general field is itself a division algebra, which is arithmetic and which is answered over a rational function field.

The ground ring is a field $k$ unless stated otherwise.

## Definition and Elementary Properties

**Definition.** A **division algebra** over $k$ is an associative $k$-algebra $D$ with unit $1 \neq 0$ such that every nonzero element is a unit; that is, $D^\times = D\setminus\{0\}$.

For a finite-dimensional $D$ this is equivalent to the absence of zero divisors, as the next proposition shows; a division algebra is also simple, its only two-sided ideals being $0$ and $D$, and a commutative division algebra is a **field**.

**Proposition (finite-dimensional criterion).** Let $A$ be a finite-dimensional unital $k$-algebra. Then $A$ is a division algebra if and only if $A$ has no zero divisors.

*Proof.* A division algebra has no zero divisors, since $ab = 0$ with $a \neq 0$ implies $b = a^{-1}(ab) = 0$. Conversely, suppose $A$ has no zero divisors and let $a \neq 0$. The linear map $L_a : A \to A$, $L_a(x) = ax$, is injective: if $ax = 0$ then $x = 0$. An injective linear map of a finite-dimensional space is bijective, so there is $b$ with $ab = 1$. Applying the same argument to the right multiplication $R_a$ gives $c$ with $ca = 1$, and then $c = c(ab) = (ca)b = b$, so $a$ has the two-sided inverse $b$.

**Proposition (ideals and quotients).** A division algebra has exactly two left ideals and exactly two right ideals, namely $0$ and the whole algebra; hence it is simple, and every nonzero algebra homomorphism from a division algebra is injective. A finite-dimensional simple algebra over $k$ is, by Wedderburn–Artin, of the form $M_n(D)$ for a division algebra $D$ and an integer $n \geq 1$, and it is a division algebra exactly when $n = 1$.

*Proof.* If $I \neq 0$ is a left ideal and $0 \neq a \in I$, then $1 = a^{-1}a \in I$, so $I = A$. Injectivity of a homomorphism $\varphi$ follows because $\ker\varphi$ is a proper two-sided ideal, hence $0$. The last statement is Wedderburn–Artin: a simple finite-dimensional algebra is $M_n(D)$ for a division algebra $D$, and $M_n(D)$ is a division algebra only for $n = 1$.

**Example.** $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and every field are division algebras. The algebras $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$, $M_n(k)$ for $n \geq 2$, $k[x]$ and $k[G]$ for nontrivial finite $G$ are not, by the zero divisors listed in *Examples of Algebras*. The pattern is instructive: $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ are the division algebras among the number systems.

## Finite-Dimensional Division Algebras over $\mathbb{R}$: Frobenius

**Theorem (Frobenius, standard).** Every finite-dimensional associative division algebra over $\mathbb{R}$ is isomorphic to one of

$$
\mathbb{R}, \qquad \mathbb{C}, \qquad \mathbb{H}.
$$

*Proof (outline).* Let $D$ be such an algebra, of dimension $n$ over $\mathbb{R}$, and let $Z$ be its centre.

If $D$ is commutative, then $D$ is a field extension of $\mathbb{R}$ of finite degree $n$. Every element of $D$ has a minimal polynomial over $\mathbb{R}$, which is irreducible because $D$ is a field; over $\mathbb{R}$ the irreducible polynomials have degree $1$ or $2$, since every real polynomial of odd degree has a real root. Hence $n \leq 2$ and $D$ is $\mathbb{R}$ or $\mathbb{C}$.

Suppose $D$ is not commutative. Its centre $Z$ is a field extension of $\mathbb{R}$ of finite degree, hence $\mathbb{R}$ or $\mathbb{C}$ by the previous paragraph; and $Z = \mathbb{C}$ is impossible, because then every element $u \in D$ has $u - \lambda$ non-invertible for some $\lambda \in \mathbb{C}$ — the $\mathbb{C}$-linear map $x \mapsto ux$ has an eigenvalue — and a non-invertible element of a division algebra is zero, so every element would be central and $D$ commutative. Hence $Z = \mathbb{R}$, and $D$ is central over $\mathbb{R}$. Choose $u \in D\setminus\mathbb{R}$; then $\mathbb{R}[u]$ is a proper field extension of $\mathbb{R}$, hence $\mathbb{R}[u] \cong \mathbb{C}$. Now $D$ is a left module over this copy $C$ of $\mathbb{C}$, so $\dim_\mathbb{R}D = 2\dim_C D$. The inner automorphisms of $D$ preserve $C$ and act on it by the only nontrivial possibility, complex conjugation; analysing the conjugation action shows $\dim_C D \leq 2$, so $\dim_\mathbb{R}D \leq 4$. The case $\dim_\mathbb{R}D = 2$ is commutative, and the case $\dim_\mathbb{R}D = 4$ forces $D \cong \mathbb{H}$: the subalgebra generated by two independent anticommuting square roots of $-1$ is quaternion, and the dimension count leaves no room for anything more.

**Corollary.** The only commutative finite-dimensional real division algebras are $\mathbb{R}$ and $\mathbb{C}$; the only non-commutative one is $\mathbb{H}$. In particular there is no three-dimensional real division algebra, which is the obstruction met.

**Remark (the hypotheses are sharp).** Frobenius' theorem concerns associative algebras. Dropping associativity admits the octonions, of dimension $8$; keeping associativity but dropping the requirement that the ground field be $\mathbb{R}$ admits the division rings of the next section; and dropping finite dimension admits the field of rational functions $\mathbb{R}(x)$.

## Wedderburn's Little Theorem

**Theorem (Wedderburn, standard).** Every finite division ring is a field: if $D$ is a division ring with finitely many elements, then $D$ is commutative.

*Proof (sketch).* The centre $Z$ of $D$ is a finite field $\mathbb{F}_q$, and $D$ is a finite-dimensional $Z$-vector space of dimension $n$, so $|D| = q^n$. Counting the conjugacy classes of the multiplicative group $D^\times$ and using the class equation, together with the fact that the size of every conjugacy class is the index of a centraliser and hence of the form $(q^n-1)/(q^d-1)$, one shows that the cyclotomic polynomial $\Phi_n(q)$ divides $q - 1$ whenever $n \geq 2$. Since $\Phi_n(q) > q - 1$ for $n \geq 2$ and $q \geq 2$, this is impossible, so $n = 1$ and $D = Z$ is a field.

The theorem is the boundary case of the structure theory over finite fields: because there are no finite non-commutative division rings, every finite simple ring is a matrix algebra over a finite field, by Wedderburn–Artin. It also shows that the construction of $\mathbb{H}$ genuinely needs an infinite ground field.

## Division Algebras over Other Fields

Over a field $k$, the classification is richer, and the finite-dimensional central simple algebras are organised by a group. A **quaternion algebra over $k$** is a four-dimensional central simple $k$-algebra; it is either a division algebra or is isomorphic to $M_2(k)$. Over $\mathbb{R}$ the two possibilities are $\mathbb{H}$ and $M_2(\mathbb{R})$, so there is exactly one real quaternion division algebra; over a field such as $\mathbb{Q}$ there are infinitely many, given by the symbol algebras $(a,b)_k$ with $a, b \in k^\times$. The **Brauer group** $\operatorname{Br}(k)$ has as its elements the Morita-equivalence classes of finite-dimensional central simple $k$-algebras, with the tensor product as the group operation; a division algebra and each of its matrix algebras represent the same element, and $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2$ is generated by the class of $\mathbb{H}$.

**Example (the two real quaternion algebras).** The general quaternion algebra over a field $k$ with parameters $a, b \in k^\times$ has $k$-basis $1, u, v, w$ with

$$
u^2 = a, \qquad v^2 = b, \qquad uv = w = -vu .
$$

For $k = \mathbb{R}$, $a = b = -1$ this is the division algebra $\mathbb{H}$; for $a = b = +1$ the element $1 + u$ is a zero divisor, since $(1+u)(1-u) = 1 - u^2 = 0$, so the algebra is not a division algebra, and as a four-dimensional central simple real algebra it is isomorphic to $M_2(\mathbb{R})$. These are the two elements of $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2$ in their four-dimensional form.

**Theorem (Wedderburn–Artin, standard).** Every finite-dimensional semisimple $k$-algebra is isomorphic to a product $\prod_i M_{n_i}(D_i)$ with the $D_i$ finite-dimensional division algebras over $k$.

This is the theorem for which division algebras exist in the structure theory: they are precisely the simple factors of the semisimple algebras, and the classification of the $D_i$ is the content of the theory beyond the present article.

## Biquaternion Algebras and the Division Question

### The Algebra and the Criterion

An algebra isomorphic to $Q \otimes_k Q'$ for two $k$-quaternion algebras $Q$ and $Q'$ is a **$k$-biquaternion algebra**. It is central simple of degree $4$ and dimension $16$ over $k$; its class in the Brauer group is the sum of the classes of its two factors, and its exponent divides $2$, so its index is $1$, $2$ or $4$. The phrase is the algebraists' one, over a general field, and it is not the corpus's algebra: a biquaternion algebra here is a **product of two quaternion algebras over the same field**, sixteen-dimensional over that field, whereas $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ is a four-dimensional complex algebra. The two share the factor $\mathbb{H}$ when $k = \mathbb{R}$ and nothing else, and the collision of the two names is worth recording once: a reader who carries the corpus's sense of the word into the arithmetic literature will misread every statement there.

The class of $Q \otimes_k Q'$ is the sum of the symbols of the two factors in the mod-2 Milnor $K$-group $k_2(k) = k_2^M(k)/2$ of *Higher Algebraic K-Theory*, the group that is the quaternion layer of the Brauer group by Merkurjev's theorem. Write $\{a,b\}$ for the symbol of the quaternion algebra $(a,b)_k$, so that $\{a,b\} = 0$ exactly when $(a,b)_k$ is split; the criterion then reads as follows.

**Criterion.** Let $B = (a, b)_k \otimes_k (c, d)_k$. Then $B$ has zero divisors exactly when its class is itself the class of a quaternion algebra, that is, exactly when

$$
\{a,b\} + \{c,d\} = \{e,f\} \qquad \text{for some } e, f \in k^\times ,
$$

and $B$ is a division algebra exactly when its class is **not** represented by a single symbol. The three cases are the index: index $1$, that is $B \cong M_4(k)$; index $2$, that is $B \cong M_2(Q'')$ for a $k$-quaternion algebra $Q''$; and index $4$, which is the division case. The criterion is what makes the question an arithmetic one: a biquaternion algebra is a division algebra when a sum of two symbols fails to be a symbol, so the answer depends on the field and not on the algebra alone. The criterion has a form-theoretic face: for $B = (a, b)_k \otimes_k (c, d)_k$, the class is that of a quaternion algebra — equivalently $B$ has zero divisors — exactly when the six-dimensional **Albert form** $\langle a, b, -ab, -c, -d, cd\rangle$ of $B$ is isotropic, and $B$ is a division algebra exactly when that form is anisotropic. The Albert form, its trivial signed discriminant and its index trichotomy are in *The Witt Group and the Grothendieck–Witt Ring*, and the criterion by which its anisotropy is decided over a local field is Springer's theorem, in *Local Fields*.

Three consequences follow immediately, and they locate the phenomenon. Over $\mathbb{R}$ the group is $\operatorname{Br}(\mathbb{R}) \cong \mathbb{Z}/2$, the sum of the two symbols is $0$, and every real biquaternion algebra is therefore split, that is $M_4(\mathbb{R})$; the instance $\mathbb{H} \otimes_\mathbb{R} \mathbb{H} \cong M_4(\mathbb{R})$ already recorded above is the general case. Over a finite field the group is $0$, and again every biquaternion algebra has zero divisors. Over a number field or a local field the index of a central simple algebra equals its exponent, so a class of exponent dividing $2$ has index $1$ or $2$, is a quaternion class, and no biquaternion algebra over such a field is a division algebra. Division biquaternion algebras are therefore a phenomenon of the function fields.

### Division Biquaternion Algebras over a Rational Function Field

Let $E$ be a field of characteristic different from $2$ and let $E(t)$ be the rational function field over $E$. A quaternion division algebra over $E(t)$ exists if and only if $E$ has some field extension of even degree, and this is the easy half of the theory; the biquaternion question is finer.

The valuations of $E(t)$ trivial on $E$ are the monic irreducible polynomials of $E[t]$, with residue field $E_p = E[t]/(p)$, together with the place at infinity, with residue field $E$. At such a place $v$ the **tame symbol** is the homomorphism $\partial_v : k_2(E(t)) \to k_1(\kappa_v)$ given on symbols by

$$
\partial_v(\{f,g\}) = (-1)^{v(f)v(g)}\, u_f^{-v(g)}\, u_g^{v(f)} \qquad \text{in } k_1(\kappa_v) ,
$$

where $u_f, u_g$ are the unit parts of $f$ and $g$, as in *Higher Algebraic K-Theory*; the sum of the tame symbols over the places is the **ramification map** $\partial$. Milnor's exact sequence

$$
0 \to k_2(E) \to k_2(E(t)) \xrightarrow{\ \partial\ } \bigoplus_{p} k_1(E_p) \xrightarrow{\ N\ } k_1(E) \to 0
$$

identifies its image, the kernel of the norm map $N$, as the group $R_2(E)$ of **ramification sequences**. A sequence is **represented by a symbol** when it is $\partial(\sigma)$ for a symbol $\sigma = \{f,g\}$ of $k_2(E(t))$, and in these terms the criterion above reads: a biquaternion algebra over $E(t)$ is a division algebra exactly when the ramification sequence of its class is not represented by any symbol.

The passage from ramification sequences to quadratic forms is made by the **Bezoutian form** $q_{f,g}$ of a pair of polynomials, defined in *Quadratic Forms and Polarisation*: a quadratic form on $E[t]/(g)$ formed from $f$ modulo the monic $g$, non-degenerate exactly when $\gcd(f,g) = 1$. Its computation rules — linearity in $f$, and a determinant equal to the resultant up to an explicit sign — make a non-trivial Bezoutian an obstruction to the representability of a ramification sequence by a symbol, which is the criterion of Becher and Raczek. The Witt classes of these forms belong to *The Witt Group and the Grothendieck–Witt Ring*; only the vocabulary is used here.

**Theorem (Becher).** Let $E$ be a field of characteristic different from $2$ which is not real euclidean and over which some quaternion algebra is not split. Then there exists a biquaternion division algebra over $E(t)$ which contains no quaternion algebra defined over $E$.

The two hypotheses are not redundant. $E$ is **real euclidean** when its set of squares is an ordering of $E$; in that case every quaternion algebra over $E(t)$ is of the form $(-1, f)$ with $f \in E[t]$, the sum of two such symbols is again a symbol, and by the criterion every $E(t)$-biquaternion algebra has zero divisors — so the first hypothesis cannot be dropped. The second hypothesis is that $k_2(E) \neq 0$, equivalently that not every $E$-quaternion algebra is split. The conclusion is stronger than the existence of a division algebra: the algebra constructed contains no quaternion algebra **defined over $E$**, by which is meant none of the form $Q_0 \otimes_E E(t)$ with $Q_0$ an $E$-quaternion algebra, although it contains $E(t)$-quaternion algebras by construction.

*The construction.* For $a, b \in E^\times$ with $a \notin E^{\times 2}$ and $b \notin aE^{\times 2} \cup (a-4)E^{\times 2}$, set $g_1 = t^2 + (a+1)t + a$ and $g_2 = t^2 + at + a$, so that $g_1 = (t+1)(t+a)$, that $g_2(0) = a$, that the discriminant of $g_2$ is $a(a-4)$, and that $g_1 t \equiv t^2$ modulo $g_2$. The algebra

$$
B = \big(t^2 + (a+1)t + a,\ a\big) \otimes_{E(t)} \big(t^2 + at + a,\ ab\big)
$$

has ramification sequence supported on the divisors of $g_1 g_2$, of degree $4$. Its class is the sum of the two symbols $\{g_1, a\}$ and $\{g_2, ab\}$, and the criterion of the previous subsection translates the theorem into the statement that this sum is represented by a symbol exactly when $\{a,b\} = 0$ in $k_2(E)$. So when $\{a,b\} \neq 0$ the sequence is not representable, and $B$ is a division algebra — the Faddeev index of the class is $4$ in the terminology of the arithmetic literature. A field with $k_2(E) \neq 0$ and not real euclidean always supplies such a pair $a, b$.

Among the standard fields of this article, the rational function field is the one over which a biquaternion algebra can fail to have zero divisors, and the reason is visible in the sequence above: there are ramification sequences that are not the ramification of any symbol, so the symbol relations of $k_2(E)$ need not lift to $k_2(E(t))$. The converse of the theorem fails, and the failure is informative: a field of cohomological dimension $1$ — over which every quaternion algebra is split, so that $k_2(E) = 0$ — can still have biquaternion division algebras over $E(t)$. The local case was known earlier, with $E$ a local number field and the division algebras over $E(t)$ constructed by other means; the theorem above is what removes the arithmetic hypothesis on $E$.

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

whence $g(b)a = af(b)$, that is $g(b) = a f(b)a^{-1}$.

**Corollary (every automorphism of a central simple algebra is inner).** For a finite-dimensional central simple $k$-algebra $A$ the map $A^\times \to \operatorname{Aut}_k(A)$, $a \mapsto (x \mapsto axa^{-1})$, is surjective with kernel $k^\times$, so

$$
\operatorname{Aut}_k(A) \cong A^\times/k^\times .
$$

For $A = M_n(k)$ this is the projective general linear group $\mathrm{PGL}_n(k) = \mathrm{GL}_n(k)/k^\times$; for $A = M_n(D)$ with $D$ a division algebra it is $\mathrm{PGL}_n(D) = \mathrm{GL}_n(D)/k^\times$, where $\mathrm{GL}_n(D) = M_n(D)^\times$, and in each case the derivations of $A$ are the inner ones, $\delta = \operatorname{ad}_h$, as in *Automorphisms and Derivations of Algebras*.

**Example (the quaternions, and why centrality is needed).** For $A = \mathbb{H}$ over $\mathbb{R}$ the corollary gives $\operatorname{Aut}_\mathbb{R}(\mathbb{H}) \cong \mathbb{H}^\times/\mathbb{R}^\times \cong SU(2)/\{\pm1\} \cong SO(3)$, in agreement with the computation of that automorphism group in *Automorphisms and Derivations of Algebras*. The algebra $\mathbb{C}$ viewed over $\mathbb{R}$ is simple but **not** central, its centre being $\mathbb{C}$ itself, and the conclusion fails there: complex conjugation is an $\mathbb{R}$-automorphism of $\mathbb{C}$ that is not inner, and indeed every inner automorphism of the commutative algebra $\mathbb{C}$ is trivial. Centrality is thus exactly what the theorem needs, and the example shows it cannot be dropped.

**Corollary (conjugacy of embeddings of fields).** If $K \subseteq A$ is a subfield of a finite-dimensional central simple $k$-algebra $A$ with $[K : k] < \infty$ and $K$ separable over $k$, then any two $k$-embeddings $K \to A$ are conjugate by an inner automorphism of $A$. This is the form in which the theorem is used to move between splitting fields of a central simple algebra, and it is the algebraic reason the matrix representations attached to two embeddings of such a field are interchangeable.

### Algebraically Closed Ground Fields

**Proposition (algebraically closed ground fields).** Let $k$ be algebraically closed. Then the only finite-dimensional division algebra over $k$ is $k$ itself.

*Proof.* Let $D$ be a finite-dimensional division algebra over $k$ and let $u \in D$. The powers $1, u, u^2, \dots$ are linearly dependent, so $u$ satisfies a nonzero polynomial $p$ over $k$; the minimal polynomial of $u$ has a root $\lambda \in k$ because $k$ is algebraically closed, and the minimal polynomial is irreducible because $D$ is a division algebra, so it is $t - \lambda$. Hence $u = \lambda \in k$.

Over an algebraically closed field the quaternion and octonion phenomena therefore disappear entirely: the division algebras of the classification are exactly the algebras left over when the ground field fails to contain the roots of the relevant polynomials.

## Summary

A **division algebra** is a unital associative algebra in which every nonzero element is a unit; over a field and in finite dimension this is equivalent to the absence of zero divisors, and a division algebra is simple with only the two trivial left ideals. **Frobenius' theorem** classifies the finite-dimensional associative real division algebras as $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, the commutative ones being $\mathbb{R}$ and $\mathbb{C}$ over their own ground fields, so no three-dimensional real division algebra exists. **Wedderburn's little theorem** makes every finite division ring a field. Over a general field the central division algebras are classified up to Morita equivalence by the **Brauer group**, and by **Wedderburn–Artin** they are the simple factors of the semisimple algebras; the **Skolem–Noether theorem** adds that any two embeddings of a finite-dimensional simple algebra into a central simple algebra are conjugate by an inner automorphism, so $\operatorname{Aut}_k(A) \cong A^\times/k^\times$ for $A$ central simple — for instance $\mathrm{PGL}_n(k)$ for $M_n(k)$ and $SO(3)$ for $\mathbb{H}$ over $\mathbb{R}$ — while centrality cannot be dropped, complex conjugation being a non-inner automorphism of $\mathbb{C}$ over $\mathbb{R}$; over an algebraically closed field the only finite-dimensional division algebra is the field itself.

A **biquaternion algebra** over a field is the tensor product of two quaternion algebras over that field, a sixteen-dimensional central simple algebra of index $1$, $2$ or $4$, and the word is not the corpus's $\mathbb{C} \otimes_\mathbb{R} \mathbb{H}$. Its class is the sum of the two quaternion symbols, and it has zero divisors exactly when that sum is itself a symbol: it is a **division algebra** exactly when its index is $4$, which is a question about the field and not about the algebra. Over $\mathbb{R}$, over a finite field and over a number field or a local field, where the index equals the exponent, no biquaternion algebra is a division algebra; over the rational function field $E(t)$ of a field not real euclidean with $k_2(E) \neq 0$, one exists, by the theorem of Becher, and the constructed example contains no quaternion algebra defined over $E$. The proof is by the **ramification sequence** of the class, an element of $R_2(E) = \ker N$ read off from the tame symbols at the places of $E(t)$, and by the **Bezoutian forms** of *Quadratic Forms and Polarisation*, which obstruct the representability of that sequence by a single symbol; the class then has **Faddeev index** $4$. The real-euclidean case is exactly the case excluded, since there every $E(t)$-quaternion algebra is $(-1, f)$ and the sum of two such symbols is a symbol.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | Ground field |
| $D$ | Division algebra |
| $D^\times = D\setminus\{0\}$ | Units of a division algebra |
| $\mathbb{R}, \mathbb{C}, \mathbb{H}$ | Real, complex, quaternion division algebras |
| $\mathbb{O}$ | Octonions, $\dim_\mathbb{R} = 8$, non-associative |
| $Z(D)$ | Centre of $D$ |
| $[u,v,w] = (uv)w - u(vw)$ | Associator |
| $(a,b)_k$ | Quaternion (symbol) algebra over $k$, generators $u, v$ with $u^2=a$, $v^2=b$ |
| $\operatorname{Br}(k)$ | Brauer group |
| $M_n(D)$ | Matrix algebra over $D$ |
| $A^{\mathrm{op}}$ | Opposite algebra, $a\cdot b = ba$ |
| $\operatorname{Aut}_k(A) \cong A^\times/k^\times$ | Automorphisms of $A$, all inner for $A$ central simple |
| $\mathrm{PGL}_n(k)$ | Projective general linear group $\mathrm{GL}_n(k)/k^\times$ |
| $Q \otimes_k Q'$ | Biquaternion algebra, central simple of degree $4$, index $1$, $2$ or $4$ |
| $k_2(k) = k_2^M(k)/2$, $\{a,b\}$ | Mod-2 Milnor $K$-group of the ground field (*Higher Algebraic K-Theory*); the symbol of the quaternion algebra $(a,b)_k$ |
| $E(t)$, $E_p$ | Rational function field over $E$; its residue field $E[t]/(p)$ at the prime $p$ |
| $\partial_v$, $\partial$ | Tame symbol at the place $v$; the ramification map $\sum_v \partial_v$ |
| $R_2(E)$ | Ramification sequences, the image of $\partial$ |



## Further Reading

- Ferdinand G. Frobenius, "Über lineare Substitutionen und bilineare Formen", *Journal für die reine und angewandte Mathematik* **84** (1878), 1–63, for the classification of the finite-dimensional real division algebras.
- Joseph H. M. Wedderburn, "On hypercomplex numbers", *Proceedings of the London Mathematical Society* **6** (1908), 77–118, for the little theorem and the structure of semisimple algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory, the Brauer group, the quaternion algebras and the Skolem–Noether theorem.
- Karim Johannes Becher, "Biquaternion division algebras over rational function fields", *Journal of Pure and Applied Algebra* **224** (2020), article 106282, for the existence of biquaternion division algebras over the rational function field and the method of ramification sequences and Bezoutian forms.
- Karim Johannes Becher and Rafał Raczek, "Ramification sequences and Bezoutian forms", *Journal of Algebra* **476** (2017), 26–47, for the ramification criterion and the Bezoutian computations that the proof uses.
- John Milnor, "Algebraic $K$-theory and quadratic forms", *Inventiones Mathematicae* **9** (1970), 318–344, for the Milnor $K$-groups and the exact sequence of the rational function field.
- Jean-Louis Colliot-Thélène and David Madore, "Surfaces de Del Pezzo sans point rationnel sur un corps de dimension cohomologique un", *Journal de l'Institut Mathématique de Jussieu* **3** (2004), 1–16, for the field of cohomological dimension $1$ whose rational function field still carries biquaternion division algebras.
