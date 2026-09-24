# __Commutative Algebras__

## Introduction

A **commutative algebra** is an associative algebra whose product is commutative. The base structure is a **commutative ring** $R$ with identity $1 \neq 0$, and algebras are $R$-algebras, associative and unital unless stated; the broad sense of "algebra" of *Algebras*, a module with a bilinear product not assumed associative, applies here with both extra hypotheses imposed. This article treats the commutative case as a category: the free objects, the tensor product that serves as coproduct, and the contravariant functor to spectra that makes the algebra geometric.

The commutative algebras over $R$ are the algebras that arise from the symmetric algebra of *The Symmetric Algebra*, since the symmetric algebra is the free commutative algebra on a module. The category is closed under tensor product, and this closure is the structural fact that distinguishes it: for commutative algebras the tensor product is a coproduct, so it is both a construction inside the category and the way to combine two algebras freely. For non-commutative algebras the tensor product is still defined but is not a coproduct, and that failure is exactly the asymmetry that the symmetric algebra removes.

The article defines commutative algebras, identifies the free ones with polynomial algebras, proves that the tensor product is the coproduct, and then passes to the prime spectrum, its topology and its functoriality. The exterior and antisymmetric analogues belong to category 07 and are not used here.

## Commutative Algebras

### Definition

Let $R$ be a commutative ring with $1 \neq 0$. A **commutative $R$-algebra** is an $R$-module $A$ with an $R$-bilinear product $A \times A \to A$, $(a,b)\mapsto ab$, that is

$$
(ab)c = a(bc), \qquad ab = ba, \qquad \exists\, 1_A,\ a 1_A = 1_A a = a ,
$$

for all $a, b, c \in A$. The unit is required unless stated; it is unique, and the map $R \to A$, $r \mapsto r1_A$, is a ring homomorphism whose image is the subalgebra of scalars $R\cdot1_A \subseteq A$, which is central. Thus a commutative $R$-algebra is the same thing as a ring homomorphism $R \to A$ with central image; the structure map makes $A$ an $R$-module.

The **category** of commutative $R$-algebras has as morphisms the $R$-linear ring homomorphisms preserving the unit; it is written $\mathsf{CAlg}_R$.

**Example.** $R$ itself, with $r\cdot s = rs$, is the initial object. The zero ring is not admitted as an algebra, since $1 \neq 0$ is required of the base and preserved by homomorphisms.

**Example.** The polynomial algebra $R[x_1, \ldots, x_n]$, the quotient $R[x]/(f)$ for a polynomial $f$, and any quotient of a commutative algebra by an ideal are commutative $R$-algebras. The group algebra $R[G]$ of a finite abelian group $G$ is commutative, with basis $G$; the matrix algebra $M_n(R)$ for $n \geq 2$ is the standard non-commutative contrast treated in *Algebras*.

### The Free Commutative Algebra

A commutative $R$-algebra $A$ is **free on a set $X$** if there is a map $\iota : X \to A$ such that every map $X \to B$ into a commutative $R$-algebra $B$ extends uniquely to an $R$-algebra homomorphism $A \to B$. The free commutative algebra on $X$ exists and is the polynomial algebra.

**Theorem.** The polynomial algebra $R[X] = R[x_s : s \in X]$ is the free commutative $R$-algebra on $X$. If $X$ is finite of cardinality $n$, then $R[X] = R[x_1, \ldots, x_n]$.

*Proof.* Given $\phi : X \to B$, define the homomorphism on monomials by $x_{i_1}^{a_1}\cdots x_{i_k}^{a_k} \mapsto \phi(x_{i_1})^{a_1}\cdots \phi(x_{i_k})^{a_k}$ and extend $R$-linearly. This is well defined because the commutative law makes monomials a basis indexed by finitely supported families of exponents and the order of factors irrelevant; it is a homomorphism because $B$ is commutative and associative; and it is unique because $X$ generates $R[X]$ as an algebra. $\square$

By *The Symmetric Algebra*, the symmetric algebra of a free module of rank $n$ is $R[x_1, \ldots, x_n]$; more generally $\operatorname{Sym}(M) = \bigoplus_{n\geq0}\operatorname{Sym}^n(M)$ is the free commutative algebra on a basis of $M$ when $M$ is free. The free commutative algebra is therefore not a new object but the symmetric algebra.

**Proposition.** Every commutative $R$-algebra is a quotient of a polynomial algebra; that is, $A \cong R[x_s : s \in X]/\mathfrak{a}$ for some set $X$ and some ideal $\mathfrak{a}$.

*Proof.* Choose a generating set $X$ of $A$ as an $R$-algebra, for instance a set of module generators; the universal property gives a surjection $R[X] \to A$, and its kernel is an ideal. $\square$

## The Coproduct: Tensor Product

### The Tensor Product as a Coproduct

Recall from *Modules*, §13, that the tensor product $A \otimes_R B$ of two $R$-modules exists with its universal property for bilinear maps. For algebras, the product on the tensor product is the one induced by

$$
(a \otimes b)(a' \otimes b') = aa' \otimes bb',
$$

extended bilinearly. Commutativity is used twice: it makes $A \otimes_R B$ a commutative algebra, so that it is an object of the category, and it makes the images of $A$ and of $B$ commute in any commutative target, which is what the universal property of a coproduct demands.

**Theorem.** For commutative $R$-algebras $A$ and $B$, the tensor product $A\otimes_R B$ with the product above is the **coproduct** in $\mathsf{CAlg}_R$: the maps

$$
\iota_A : A \longrightarrow A\otimes_R B, \quad a \mapsto a\otimes 1, \qquad \iota_B : B \longrightarrow A\otimes_R B, \quad b \mapsto 1\otimes b
$$

are algebra homomorphisms, and for every commutative $R$-algebra $C$ and pair of homomorphisms $f : A \to C$, $h : B \to C$ there is a unique homomorphism $A \otimes_R B \to C$ with $f$ and $h$ as its composites with $\iota_A$ and $\iota_B$.

*Proof.* The prescribed composites force $a \otimes b \mapsto f(a)h(b)$; since the elementary tensors span $A\otimes_R B$ this determines the map, so uniqueness is clear. For existence, the map $(a, b) \mapsto f(a) h(b)$ is $R$-bilinear, so it factors through the tensor product; it carries $1\otimes1$ to $1$, respects addition, and respects multiplication because

$$
f(aa')h(bb') = f(a)f(a')h(b)h(b') = \bigl(f(a)h(b)\bigr)\bigl(f(a')h(b')\bigr),
$$

using the commutativity of $C$ to reorder. $\square$

**Corollary.** $R$ is the initial object and $R\otimes_R A \cong A$, so the tensor product has the unit properties expected of a coproduct. The tensor product is associative and commutative up to canonical isomorphism, $(A\otimes_R B)\otimes_R C \cong A\otimes_R(B\otimes_R C)$ and $A\otimes_R B \cong B\otimes_R A$.

### The Failure Without Commutativity

For associative algebras that are not commutative the tensor product is still an associative algebra with the product $(a\otimes b)(a'\otimes b') = aa'\otimes bb'$, but it is not a coproduct. The obstruction is visible in the proof above: the verification that the induced map respects multiplication used $f(a')h(b) = h(b)f(a')$, which fails if $C$ is non-commutative and the images overlap. The coproduct in the category of all associative algebras is instead the **free product** $A * B$, the quotient of the free algebra on the disjoint union of the underlying sets by the relations of $A$ and of $B$, which is generally much larger than $A\otimes_R B$. The commutative hypothesis therefore converts the tensor product from a mere construction into the universal combination of two algebras.

**Example.** For $A = R[x]$ and $B = R[y]$ one has $R[x]\otimes_R R[y] \cong R[x,y]$: the coproduct of two polynomial algebras in one variable is the polynomial algebra in two variables. More generally

$$
\operatorname{Sym}(M) \otimes_R \operatorname{Sym}(N) \cong \operatorname{Sym}(M \oplus N),
$$

which is the compatibility of the symmetric algebra with direct sums noted in *The Symmetric Algebra*, now read as the statement that $\operatorname{Sym}$ takes direct sums to coproducts.

## The Polynomial Algebra Revisited

### Generators and Relations

A **presentation** of a commutative $R$-algebra is an isomorphism $A \cong R[x_s : s \in X]/(f_j)$ for a set of generators $x_s$ and a set of relations $f_j \in R[x_s : s\in X]$. The category admits presentations freely: every algebra has one, by the proposition above, and a homomorphism out of a presented algebra is a map of generators satisfying the relations. This is the practical meaning of freeness: homomorphisms are determined by images of generators, and only the relations must be checked.

**Example.** $R[x]/(f)$ for $f \in R[x]$ monic of degree $n$ is a free $R$-module of rank $n$ with basis $1, x, \ldots, x^{n-1}$; this is the division-algorithm description inherited from *Rings*. For $f$ not monic the quotient need not be free: $\mathbb{Z}[x]/(2x-1) \cong \mathbb{Z}[\tfrac12]$ is not a free $\mathbb{Z}$-module.

### Grading and the Symmetric Algebra

$\operatorname{Sym}(M)$ is graded, $\operatorname{Sym}(M) = \bigoplus_{n\geq0}\operatorname{Sym}^n(M)$ with $\operatorname{Sym}^n$ the symmetric powers of *Symmetric Powers*, and the product maps $\operatorname{Sym}^m \times \operatorname{Sym}^n \to \operatorname{Sym}^{m+n}$. The polynomial algebra is the free graded commutative algebra in the sense that homomorphisms of algebras respect the grading when the generators are assigned degrees; for degree-one generators $x_1, \ldots, x_n$ the component $\operatorname{Sym}^k$ of total degree $k$ has rank $\binom{n+k-1}{k}$, the number of monomials of degree $k$.

**Proposition.** $\operatorname{rank}_R \operatorname{Sym}^k(R^n) = \binom{n+k-1}{k}$, the dimension when $R$ is a field.

*Proof.* A monomial $x_1^{a_1}\cdots x_n^{a_n}$ of total degree $k$ corresponds to a weak composition $a_1 + \cdots + a_n = k$ with $a_i \geq 0$; the number of such compositions is the number of ways to place $n - 1$ separators among $k$ identical objects, namely $\binom{n+k-1}{n-1} = \binom{n+k-1}{k}$. $\square$

## Constructions

### Quotients and Ideals

An **ideal** $\mathfrak{a} \subseteq A$ of a commutative algebra is an $R$-submodule with $A\mathfrak{a} \subseteq \mathfrak{a}$; the quotient $A/\mathfrak{a}$ is again a commutative $R$-algebra, and the pair $(A/\mathfrak{a}, A \to A/\mathfrak{a})$ is universal among homomorphisms out of $A$ that vanish on $\mathfrak{a}$. Ideals are exactly the kernels, so the correspondence between ideals and quotients is bijective on isomorphism classes, and it is order reversing: $\mathfrak{a} \subseteq \mathfrak{b}$ gives a surjection $A/\mathfrak{b}\twoheadrightarrow A/\mathfrak{a}$.

**Example.** $\mathbb{Z}[x]/(x^2 - 2) \cong \mathbb{Z}[\sqrt2]$ and $\mathbb{R}[x]/(x^2 + 1) \cong \mathbb{C}$; in both cases the quotient by a principal ideal is described as adjoining a formal root of the polynomial.

### Localisation

Let $S \subseteq A$ be a **multiplicative subset**: $1 \in S$ and $s, t \in S \Rightarrow st \in S$. The **localisation** $S^{-1}A$ is the algebra of fractions $a/s$ with respect to the equivalence $a/s = a'/s' \Leftrightarrow \exists u \in S,\ u(as' - a's) = 0$, with the evident operations.

**Proposition (universal property).** Every homomorphism $\phi : A \to B$ with $\phi(S) \subseteq B^{\times}$ factors uniquely through the canonical map $A \to S^{-1}A$.

*Proof.* The formula $\phi(a/s) = \phi(a)\phi(s)^{-1}$ is forced; it is well defined because $as' = a's$ gives $\phi(a)\phi(s') = \phi(a')\phi(s)$, and $\phi(s)$, $\phi(s')$ are units; it is a homomorphism by the usual rules of fractions. $\square$

The localisations $A_f$ for $f \in A$ ($S = \{f^n\}$) and $A_{\mathfrak{p}}$ for a prime ideal $\mathfrak{p}$ ($S = A \setminus \mathfrak{p}$) are the principal and local cases. The primes of $S^{-1}A$ correspond bijectively to the primes of $A$ disjoint from $S$; in particular $\operatorname{Spec} A_f = D(f)$ as sets.

### Polynomial Extensions and Base Change

For any commutative algebra $B$, the polynomial algebra $B[x_1, \ldots, x_n] = B \otimes_R R[x_1, \ldots, x_n]$ is the coproduct of $B$ with the free algebra, by the coproduct theorem. More generally a ring homomorphism $R \to B$ gives a **base-change** functor $A \mapsto A\otimes_R B$ from $\mathsf{CAlg}_R$ to $\mathsf{CAlg}_B$, left adjoint to the forgetful functor, and this is the coproduct construction read in a moving base.

**Example.** $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C} \cong \mathbb{C} \times \mathbb{C}$, by the Chinese remainder theorem applied to $\mathbb{C}[x]/(x^2+1) \cong \mathbb{C}[x]/(x-i)\times\mathbb{C}[x]/(x+i)$. This shows that the coproduct of a field with itself can have zero divisors; coproducts of domains need not be domains.

## Finiteness Conditions

### Finite Type and Finite

A commutative $R$-algebra $A$ is **of finite type** if it is generated as an $R$-algebra by finitely many elements, that is, $A \cong R[x_1, \ldots, x_n]/\mathfrak{a}$ for some $n$ and ideal $\mathfrak{a}$; it is **finite** if it is finitely generated as an $R$-module. Finite implies finite type, because module generators generate the algebra. The converse fails: $R[x]$ is of finite type but not finite.

**Theorem (Hilbert basis theorem).** If $R$ is Noetherian, then every commutative $R$-algebra of finite type is Noetherian; in particular $R[x_1, \ldots, x_n]$ is Noetherian.

The theorem is standard and is proved by induction on $n$ from the case of one variable. Its consequence here is that the geometric objects of the next section are built from finitely presented data whenever the base and the presentation are finite.

### Integral Elements

An element $a \in A$ is **integral** over a subalgebra $R \subseteq A$ if it satisfies a monic polynomial equation $a^n + r_{n-1}a^{n-1} + \cdots + r_0 = 0$ with $r_i \in R$. The following are equivalent, and the equivalences are standard:

1. $a$ is integral over $R$;
2. the subalgebra $R[a]$ is a finite $R$-module;
3. there is a subalgebra $B$ with $R \subseteq B \subseteq A$, $a \in B$ and $B$ finite over $R$.

The set of integral elements is a subalgebra, the **integral closure** of $R$ in $A$; when it is all of $A$ the extension is **integral**. The connection with the polynomial algebra is direct: an algebra of finite type is finite over a subalgebra exactly when every generator is integral, which is the algebraic form of the statement that finiteness of a morphism of spectra is checked on generators, and it is what makes a finite morphism have finite fibres.

## The Functor of Points

The spectrum construction is complemented by a functorial description of an algebra by its points in other algebras. For a commutative $R$-algebra $A$ put

$$
h_A : \mathsf{CAlg}_R \longrightarrow \mathsf{Set}, \qquad h_A(B) = \operatorname{Hom}_{\mathsf{CAlg}_R}(A, B),
$$

functorial by post-composition.

**Theorem (Yoneda).** The assignment $A \mapsto h_A$ is a fully faithful functor: for all $A, A'$,

$$
\operatorname{Hom}_{\mathsf{CAlg}_R}(A, A') \cong \operatorname{Nat}(h_A, h_{A'}),
$$

so $A$ is determined up to canonical isomorphism by the functor $h_A$, and by its values $h_A(B)$ on the "test algebras" $B$.

The elements of $h_A(B)$ are the **$B$-valued points** of the object represented by $A$. For $A = R[x_1, \ldots, x_n]/(f_1, \ldots, f_m)$ the set $h_A(B)$ is the set of $n$-tuples $(b_1, \ldots, b_n) \in B^n$ satisfying $f_j(b) = 0$ for all $j$: solving equations in an arbitrary commutative algebra $B$ is the same as mapping out of the presented algebra. This is the operational content of freeness and of the coproduct theorem, and it is the reason the tensor product, which computes the coproduct, computes intersections of solution sets.

## Spectra

### Prime and Maximal Ideals

Let $A$ be a commutative $R$-algebra. A **prime ideal** is an ideal $\mathfrak{p} \subsetneq A$ such that $ab \in \mathfrak{p}$ implies $a \in \mathfrak{p}$ or $b \in \mathfrak{p}$; equivalently, $A/\mathfrak{p}$ is a domain. A **maximal ideal** is an ideal $\mathfrak{m}$ maximal under inclusion among proper ideals; equivalently, $A/\mathfrak{m}$ is a field. Every maximal ideal is prime; the converse fails, as in $A = \mathbb{Z}[x]$ where $(x)$ is prime but not maximal.

The **spectrum** is the set of prime ideals,

$$
\operatorname{Spec} A = \{\mathfrak{p} \subseteq A : \mathfrak{p} \text{ prime}\},
$$

and the **maximal spectrum** is the set of maximal ideals, $\operatorname{MaxSpec} A = \{\mathfrak{m}\}$. For $A = k[x_1,\ldots,x_n]$ over an algebraically closed field $k$ the maximal ideals are exactly the $(x_1 - a_1, \ldots, x_n - a_n)$, so $\operatorname{MaxSpec} A$ is the affine $n$-space $k^n$; this is the classical content of the Nullstellensatz, and its proof belongs to commutative algebra rather than to this article.

### The Zariski Topology

For an ideal $\mathfrak{a} \subseteq A$ put

$$
V(\mathfrak{a}) = \{\mathfrak{p} \in \operatorname{Spec} A : \mathfrak{a} \subseteq \mathfrak{p}\}.
$$

**Proposition.** The sets $V(\mathfrak{a})$ are the closed sets of a topology, the **Zariski topology**, on $\operatorname{Spec} A$.

*Proof.* $V(0) = \operatorname{Spec} A$ and $V(A) = \varnothing$. Intersections: $V(\mathfrak{a}) \cap V(\mathfrak{b}) = V(\mathfrak{a} + \mathfrak{b})$, because a prime containing both $\mathfrak{a}$ and $\mathfrak{b}$ contains their sum, and conversely. Unions: $V(\mathfrak{a}) \cup V(\mathfrak{b}) = V(\mathfrak{a}\mathfrak{b})$, because a prime containing $\mathfrak{a}\mathfrak{b}$ contains $\mathfrak{a}$ or $\mathfrak{b}$ by primality. The same argument with an arbitrary family of ideals gives $\bigcap_i V(\mathfrak{a}_i) = V(\sum_i \mathfrak{a}_i)$, using that every prime is proper, so the collection is closed under arbitrary intersections and finite unions; that is a topology. $\square$

The sets $D(f) = \operatorname{Spec} A \setminus V((f)) = \{\mathfrak{p} : f \notin \mathfrak{p}\}$ for $f \in A$ are the **principal open sets**, a basis of the topology. A point $\mathfrak{p}$ is closed exactly when $\mathfrak{p}$ is maximal, so $\operatorname{MaxSpec} A$ is the subspace of closed points.

### Functoriality

A homomorphism $\phi : A \to B$ of commutative $R$-algebras induces a map on spectra,

$$
\phi^* : \operatorname{Spec} B \longrightarrow \operatorname{Spec} A, \qquad \phi^*(\mathfrak{q}) = \phi^{-1}(\mathfrak{q}),
$$

which is well defined because the preimage of a prime ideal is prime, and continuous because $(\phi^*)^{-1}V(\mathfrak{a}) = V(B\phi(\mathfrak{a}))$. The assignment is contravariant: $(\psi \circ \phi)^* = \phi^* \circ \psi^*$, and $(\mathrm{id})^* = \mathrm{id}$. Thus

$$
\operatorname{Spec} : \mathsf{CAlg}_R^{\mathrm{op}} \longrightarrow \mathsf{Top}
$$

is a functor from the opposite category of commutative $R$-algebras to topological spaces.

**Example.** The inclusion $\phi : R \to A$ induces $\phi^* : \operatorname{Spec} A \to \operatorname{Spec} R$, the **structure map**, whose fibres are the spectra of the geometric fibres $A\otimes_R\kappa(\mathfrak{p})$ over residue fields $\kappa(\mathfrak{p}) = \operatorname{Frac}(R/\mathfrak{p})$. The spectrum of a coproduct computes a fibre product: for finitely presented algebras over an algebraically closed field, $\operatorname{Spec}(A\otimes_k B)$ is the fibre product $\operatorname{Spec} A \times_{\operatorname{Spec} k} \operatorname{Spec} B$. This is the geometric meaning of the coproduct theorem.

### The Coordinate Algebra and its Functions

An element $f \in A$ is a **function** on $\operatorname{Spec} A$: its value at $\mathfrak{p}$ is the image of $f$ in the residue field $\kappa(\mathfrak{p})$. The function $f$ vanishes at $\mathfrak{p}$ exactly when $f \in \mathfrak{p}$, so the ideal of functions vanishing on the closed set $V(\mathfrak{a})$ is the radical $\sqrt{\mathfrak{a}} = \{f : f^n \in \mathfrak{a} \text{ for some } n\}$, by the definition of the radical; this is the **radical** or nilradical theorem, and it says that $\operatorname{Spec}$ sees exactly the radical ideals.

**Proposition.** For a commutative $R$-algebra $A$, the nilradical $\sqrt{0}$ is the intersection of all prime ideals, and $A$ is reduced, that is $\sqrt{0} = 0$, if and only if $A$ embeds in a product of domains.

*Proof.* If $f$ is nilpotent then $f \in \mathfrak{p}$ for every prime $\mathfrak{p}$, since $f^n = 0 \in \mathfrak{p}$ forces $f \in \mathfrak{p}$. Conversely, if $f$ is not nilpotent, the localisation $A_f$ is nonzero and has a maximal ideal $\mathfrak{m}$, whose contraction to $A$ is a prime ideal not containing $f$. The second statement follows by embedding $A$ into the product of the domains $A/\mathfrak{p}$ over primes. $\square$

### The Structure Sheaf

The localisations of $A$ assemble into a sheaf of algebras on $\operatorname{Spec} A$. On a principal open set $D(f)$ put

$$
\mathcal{O}(D(f)) = A_f ,
$$

and on a general open set $U$ let $\mathcal{O}(U)$ be the set of compatible families of elements of the $A_f$ over principal opens $D(f) \subseteq U$, with the restriction maps coming from the localisations $A_f \to A_{fg}$. Then $\mathcal{O}$ is a sheaf of commutative $R$-algebras, the **structure sheaf**, and its stalk at a prime $\mathfrak{p}$ is the local ring

$$
\mathcal{O}_{\mathfrak{p}} = \varinjlim_{f \notin \mathfrak{p}} A_f = A_{\mathfrak{p}} .
$$

The global sections recover the algebra, $\mathcal{O}(\operatorname{Spec} A) = A$; this is the precise sense in which the spectrum is a geometric model of $A$. The pair $(\operatorname{Spec} A, \mathcal{O})$ is an affine scheme, and the construction is the starting point of algebraic geometry; only the sheaf-theoretic organisation of the localisations is used here.

### Idempotents and Connected Components

The idempotents of a commutative algebra encode the decompositions of its spectrum.

**Proposition.** Let $A$ be a commutative $R$-algebra and let $e \in A$ with $e^2 = e$. Put $f = 1 - e$, so that $ef = 0$ and $e + f = 1$. Then there is a canonical isomorphism $A \cong Ae \times Af$ of commutative $R$-algebras, and $\operatorname{Spec} A$ is the disjoint union of the open sets $D(e)$ and $D(f)$.

*Proof.* Every $a \in A$ has the decomposition $a = ae + af$ with $ae \in Ae$, $af \in Af$; the components satisfy $(ae)(af) = a^2ef = 0$, so the product in $A$ agrees with the coordinatewise product, and $e$, $f$ are the coordinate units. The open sets $D(e)$ and $D(f)$ are disjoint because $ef = 0$ lies in every prime, and they cover $\operatorname{Spec} A$ because $e + f = 1$ lies in no prime. $\square$

It follows that $\operatorname{Spec} A$ is disconnected if and only if $A$ has a nontrivial idempotent, and that the decomposition of a spectrum into connected components corresponds to the decomposition of the algebra into a product of algebras. For a reduced algebra of finite type over a field, the idempotents of $A$ are exactly the characteristic functions of the clopen subsets of $\operatorname{MaxSpec} A$. This is the algebraic counterpart of the fact that the polynomial algebra $k[x]$ has no idempotents other than $0$ and $1$, hence connected spectrum, while $k[x]/(x^2 - x) \cong k\times k$ has two.

## Summary

A **commutative $R$-algebra** is an associative, commutative, unital $R$-algebra, and the category $\mathsf{CAlg}_R$ has the polynomial algebras as its free objects: $R[x_s : s \in X]$ is free on $X$, and every algebra is a quotient of a polynomial algebra. The symmetric algebra of a module is the free commutative algebra on that module, so the polynomial algebra and the symmetric algebra are the same construction. The **tensor product** $A\otimes_R B$ with the product $(a\otimes b)(a'\otimes b') = aa'\otimes bb'$ is the **coproduct** in $\mathsf{CAlg}_R$; it is the universal algebra receiving both $A$ and $B$, and the proof uses the commutativity of the target. Without commutativity the tensor product is not a coproduct, and the coproduct is the free product instead. The **prime spectrum** $\operatorname{Spec} A$ with the Zariski topology is the set of prime ideals, functorial and contravariant, $\operatorname{Spec} : \mathsf{CAlg}_R^{\mathrm{op}}\to\mathsf{Top}$; the closed points are the maximal ideals, and the closed sets detect radical ideals, the nilradical being the intersection of the primes. The coproduct theorem reads geometrically as the statement that the spectrum of a tensor product of finitely presented algebras is the fibre product of the spectra over $\operatorname{Spec} R$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $\mathsf{CAlg}_R$ | Category of commutative $R$-algebras |
| $A \otimes_R B$ | Tensor product, the coproduct in $\mathsf{CAlg}_R$ |
| $R[X] = R[x_s : s \in X]$ | Free commutative algebra on $X$ |
| $\operatorname{Sym}(M)$ | Symmetric algebra, free commutative algebra on $M$ |
| $\operatorname{Sym}^k(M)$ | $k$-th symmetric power |
| $\mathfrak{p}$, $\mathfrak{m}$ | Prime ideal, maximal ideal |
| $\operatorname{Spec} A$ | Spectrum: set of prime ideals |
| $\operatorname{MaxSpec} A$ | Set of maximal ideals (closed points) |
| $V(\mathfrak{a})$ | Zariski-closed set of primes containing $\mathfrak{a}$ |
| $D(f)$ | Principal open set $\{\mathfrak{p} : f \notin \mathfrak{p}\}$ |
| $\phi^*(\mathfrak{q}) = \phi^{-1}(\mathfrak{q})$ | Contravariant map on spectra |
| $\sqrt{\mathfrak{a}}$, $\sqrt{0}$ | Radical of $\mathfrak{a}$; nilradical |
| $\kappa(\mathfrak{p})$ | Residue field at a prime $\mathfrak{p}$, $\operatorname{Frac}(A/\mathfrak{p})$ |
| $S^{-1}A$, $A_f$, $A_{\mathfrak{p}}$ | Localisations of $A$ |
| $\mathcal{O}$ | Structure sheaf on $\operatorname{Spec} A$, $\mathcal{O}(D(f)) = A_f$ |
| $h_A(B) = \operatorname{Hom}(A,B)$ | Functor of points of $A$ |

## Further Reading

- Michael F. Atiyah and Ian G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for spectra, the Zariski topology and the nilradical.
- Nicolas Bourbaki, *Algebra II: Chapters 4–7* (Springer, 1990), for the tensor product, free algebras and coproducts.
- Robin Hartshorne, *Algebraic Geometry* (Springer, 1977), for the functoriality of $\operatorname{Spec}$ and fibre products.
- Saunders Mac Lane, *Categories for the Working Mathematician* (Springer, 2nd ed. 1998), for coproducts and free objects.
- David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry* (Springer, 1995), for the Nullstellensatz and the structure of spectra.
