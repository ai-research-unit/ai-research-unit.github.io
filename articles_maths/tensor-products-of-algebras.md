
# __Tensor Products of Algebras__

## Introduction

The tensor product of two $R$-algebras $A$ and $B$ is the module $A \otimes_R B$ equipped with the product $(a \otimes b)(a' \otimes b') = aa' \otimes bb'$. It is the construction that combines two algebras without forcing their elements to commute, and it is the operation that produces the biquaternions from the complex numbers and the quaternions, matrix algebras from smaller ones, and the scalar extension of every algebra by a ring homomorphism.

This article develops the algebra tensor product: the product and its well-definedness, the universal property that characterises it, the functorial and exactness properties, base change, tensor powers of an algebra, and the behaviour of central simple algebras. The underlying tensor product of modules is assumed from *Modules*, §13, and the tensor algebra of a module from *Tensor Powers and the Free Algebra*; the two tensor constructions are different and the article keeps them apart. A subtler construction, the **free product**, is the coproduct of not-necessarily-commutative algebras and appears only as a comparison; the detailed study of the quotients that specialise $T(V)$ — the symmetric and alternating quotients in particular — belongs to categories 06 and 07.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, and $A$, $B$, $C$ are $R$-algebras. Unitality and associativity are stated where they are used.

## The Algebra Structure

**Definition.** Let $A$ and $B$ be $R$-algebras. The **tensor product** $A \otimes_R B$ is the tensor product of the underlying $R$-modules, equipped with the product

$$
(a \otimes b)(a' \otimes b') = aa' \otimes bb', \qquad a, a' \in A, \quad b, b' \in B,
$$

extended to all of $A \otimes_R B$ by bilinearity.

The definition presumes that the displayed values on elementary tensors extend, and that is the content of the next proposition. The product of two arbitrary elements is defined by expanding both as finite sums of elementary tensors and applying the formula term by term.

**Proposition (well-definedness).** The product above is well defined, and with it $A \otimes_R B$ is an $R$-algebra.

*Proof.* By the universal property of the tensor product of modules, an $R$-bilinear map $A \times B \to M$ into an $R$-module $M$ induces an $R$-linear map $A \otimes B \to M$. Fix $a' \in A$ and $b' \in B$ and consider the map

$$
A \times B \to A \otimes_R B, \qquad (a,b) \mapsto aa' \otimes bb'.
$$

It is $R$-bilinear, since the product of $A$ and that of $B$ are; hence it induces an $R$-linear map $L_{a',b'} : A \otimes B \to A \otimes B$ with $L_{a',b'}(a \otimes b) = aa' \otimes bb'$. Now fix $x = \sum_i a_i \otimes b_i \in A \otimes B$ and consider the map

$$
A \times B \to A \otimes_R B, \qquad (a', b') \mapsto L_{a',b'}(x) = \sum_i a_i a' \otimes b_i b'.
$$

This is again $R$-bilinear, so it induces an $R$-linear map $R_{x} : A \otimes B \to A \otimes B$ with $R_x(a' \otimes b') = \sum_i a_i a' \otimes b_i b'$. Setting $x \cdot y = R_x(y)$ gives a product, well defined because $R_x$ depends only on $x$ and not on its expression as a sum, and bilinear because $R_{x + x'} = R_x + R_{x'}$ and $R_{rx} = r R_x$. $\square$

**Proposition (algebra axioms).** The tensor product $A \otimes_R B$ inherits the following properties:

1. if $A$ and $B$ are associative, then so is $A \otimes_R B$;
2. if $A$ and $B$ are unital, then so is $A \otimes_R B$, with unit $1_A \otimes 1_B$;
3. if $A$ and $B$ are commutative, then so is $A \otimes_R B$;
4. the products of $A$ and $B$ are recovered on the images of $A$ and $B$: $a \otimes 1_B$ and $1_A \otimes b$.

*Proof.* Associativity on elementary tensors is $(aa')a'' \otimes (bb')b'' = a(a'a'') \otimes b(b'b'')$, and both sides extend by bilinearity. Unitality is $(a \otimes b)(1 \otimes 1) = a \otimes b = (1 \otimes 1)(a \otimes b)$. Commutativity is $(a \otimes b)(a' \otimes b') = aa' \otimes bb' = a'a \otimes b'b = (a' \otimes b')(a \otimes b)$. The last statement is the case $b' = 1_B$ or $a' = 1_A$ of the product formula. $\square$

**Proposition (centre).** For unital associative $A$ and $B$, the inclusion

$$
Z(A) \otimes_R Z(B) \subseteq Z(A \otimes_R B), \qquad z \otimes w \mapsto z \otimes w,
$$

realises $Z(A) \otimes_R Z(B)$ as a subalgebra of the centre of the tensor product.

*Proof.* This is the computation $(z \otimes w)(a \otimes b) = za \otimes wb = az \otimes bw = (a\otimes b)(z\otimes w)$, extended bilinearly. $\square$

Over a field the inclusion is an equality.

**Proposition (centre over a field).** Let $k$ be a field and let $A$, $B$ be $k$-algebras. Then

$$
Z(A \otimes_k B) = Z(A) \otimes_k Z(B).
$$

*Proof.* The inclusion $\supseteq$ is the proposition above. For the reverse, let $z = \sum_{i=1}^{n} a_i \otimes b_i$ be an expression with $n$ minimal; then $\{a_i\}$ and $\{b_i\}$ are each linearly independent over $k$. Commuting $z$ with $a \otimes 1_B$ gives $\sum_i (a_i a - a a_i) \otimes b_i = 0$, so $a_i a = a a_i$ for every $i$ by linear independence of the $b_i$; hence each $a_i \in Z(A)$. Commuting $z$ with $1_A \otimes b$ then gives $\sum_i a_i \otimes (b_i b - b b_i) = 0$, so $b_i b = b b_i$ for every $i$ by linear independence of the $a_i$; hence each $b_i \in Z(B)$. Therefore $z \in Z(A)\otimes_k Z(B)$. $\square$

Over a general commutative ring only the inclusion is asserted here, because the minimal expression need not have linearly independent coefficients.

## The Universal Property

**Theorem (universal property of $A \otimes_R B$).** Let $A$, $B$, $C$ be $R$-algebras, with $A$, $B$, $C$ associative and unital. There is a natural bijection between

- algebra homomorphisms $\Phi : A \otimes_R B \to C$, and
- pairs of algebra homomorphisms $f : A \to C$, $g : B \to C$ whose images commute elementwise: $f(a)g(b) = g(b)f(a)$ for all $a \in A$, $b \in B$.

The pair recovered from $\Phi$ is $f(a) = \Phi(a \otimes 1_B)$, $g(b) = \Phi(1_A \otimes b)$, and the homomorphism recovered from $(f,g)$ is $\Phi(a \otimes b) = f(a)g(b)$.

*Proof.* Given $\Phi$, the maps $f$ and $g$ are algebra homomorphisms, and their images commute because $(a\otimes 1)(1\otimes b) = a \otimes b = (1 \otimes b)(a \otimes 1)$. Conversely, given $f$ and $g$ with commuting images, the map $A \times B \to C$, $(a,b) \mapsto f(a)g(b)$, is $R$-bilinear because $f$ and $g$ are linear and the product of $C$ is bilinear; it induces an $R$-linear $\Phi : A \otimes B \to C$. Multiplicativity is

$$
\Phi\bigl((a\otimes b)(a'\otimes b')\bigr) = f(aa')g(bb') = f(a)f(a')g(b)g(b') = f(a)g(b)f(a')g(b') = \Phi(a\otimes b)\Phi(a'\otimes b'),
$$

where the third equality uses that the images of $f$ and $g$ commute; unitality is $\Phi(1 \otimes 1) = 1_C$. The two constructions are inverse. $\square$

**Corollary (coproduct of commutative algebras).** If $A$, $B$, $C$ are commutative, the commuting condition is automatic, and the theorem reads

$$
\operatorname{Hom}_{R\text{-alg}}(A \otimes_R B, C) \;\cong\; \operatorname{Hom}_{R\text{-alg}}(A, C) \times \operatorname{Hom}_{R\text{-alg}}(B, C).
$$

Thus $A \otimes_R B$, with the maps $a \mapsto a \otimes 1_B$ and $b \mapsto 1_A \otimes b$, is the **coproduct** in the category of commutative unital $R$-algebras. It is not the product: the product of $A$ and $B$ in that category is the direct product $A \times B$, with its coordinatewise operations.

**Corollary (pushout).** Let $C$ be a commutative unital $R$-algebra and let $A$ and $B$ be commutative unital $C$-algebras. Then $A \otimes_C B$, with the maps $a \mapsto a \otimes 1_B$ and $b \mapsto 1_A \otimes b$, is the **pushout** of the diagram $A \leftarrow C \rightarrow B$ in the category of commutative unital $R$-algebras: for every commutative unital $R$-algebra $D$ and every pair of $R$-algebra homomorphisms $A \to D$, $B \to D$ whose restrictions to $C$ agree, there is a unique $R$-algebra homomorphism $A \otimes_C B \to D$ through which both factor. The case $C = R$ is the coproduct above, and the case of two quotients $E/I$ and $E/J$ of a commutative unital $C$-algebra $E$ is the identification $(E/I) \otimes_E (E/J) \cong E/(I+J)$ obtained from the proposition on tensor products of ideals.

**Corollary (the tensor product is a quotient of the free product).** For unital associative $A$ and $B$, let $A \sqcup B$ denote their free product, the coproduct in the category of unital associative $R$-algebras, which is the algebra with no relation imposed between $A$ and $B$. Then

$$
A \otimes_R B \;\cong\; (A \sqcup B)\big/\bigl(ab - ba : a \in A, \ b \in B\bigr),
$$

the quotient in which every element of $A$ is forced to commute with every element of $B$.

*Proof.* The free product satisfies the universal property of pairs of homomorphisms with no commuting condition, and imposing the relations $ab = ba$ adds exactly that condition; the universal property of the quotient then matches the theorem above. $\square$

The distinction between the tensor product and the free product is the distinction between allowing and forbidding commutativity between the two factors; it parallels the distinction between the polynomial algebra and the free algebra in *Tensor Powers and the Free Algebra*.

## Examples and Computations

**Example (the biquaternions).** Let $A = \mathbb{C}$ and $B = \mathbb{H}$, both over $R = \mathbb{R}$. The tensor product is the biquaternion algebra

$$
\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H},
$$

of real dimension $2 \cdot 4 = 8$. The copy of $\mathbb{C}$ given by $\mathbb{C} \otimes 1$ is the central scalar imaginary $i$ with $i^2 = -1$, and it commutes with the quaternion units $1 \otimes e_k$. This is the definition of $\mathbb{B}$ used in *Biquaternion Algebra ($\mathbb{B}$)*.

**Example (the split biquaternions).** With $A = \mathbb{D}$ and $B = \mathbb{H}$ over $R = \mathbb{R}$,

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H},
$$

the split biquaternion algebra, of real dimension $2 \cdot 4 = 8$. The central unit $j \in \mathbb{D}$ has $j^2 = +1$ and commutes with the quaternion units, so the element $1 + j$ is a zero divisor: $(1 + j)(1 - j) = 1 - j^2 = 0$. The two split-complex idempotents $e_\pm = \tfrac{1}{2}(1 \pm j)$ act as central idempotents, so the algebra decomposes as a direct sum of two ideals; the details are.

**Example (matrix algebras).** For a commutative ring $R$ and positive integers $m, n$, there is an isomorphism of $R$-algebras

$$
M_m(R) \otimes_R M_n(R) \;\cong\; M_{mn}(R),
$$

given on matrix units by $E_{ij} \otimes E_{kl} \mapsto E_{(i,k),(j,l)}$, the **Kronecker product** of matrices. The product formula is verified on elementary tensors and extends by additivity.

**Example (polynomial algebras).** For $R$ commutative,

$$
R[x] \otimes_R R[y] \;\cong\; R[x,y],
$$

by $x \mapsto x \otimes 1$, $y \mapsto 1 \otimes y$; both sides are the free commutative $R$-algebra on two generators, and the isomorphism is the universal property in the commutative case. In $R[x] \otimes_R R[x]$ the two copies of $x$ have been made into commuting independent variables $x \otimes 1$ and $1 \otimes x$, so the result is $R[x,y]$, not $R[x]$.

**Example (quotients, and the pushout).** Let $I, J$ be ideals of a commutative ring $A$. Then

$$
(A/I) \otimes_A (A/J) \;\cong\; A/(I + J),
$$

the two quotients being $A$-algebras. This is the composite of the quotient description of the tensor product with the coproduct property: a pair of $A$-algebra maps out of $A/I$ and $A/J$ is a map out of $A$ killing both ideals. Read in the category of commutative $A$-algebras, the same statement says that $A/I \otimes_A A/J$ is the **pushout** of the diagram $A/I \leftarrow A \rightarrow A/J$: it receives $A/I$ and $A/J$ by $A$-algebra maps that agree on the images of $A$, and any other such pair of maps factors uniquely through it. In particular, for integers $m, n \geq 1$,

$$
\mathbb{Z}/m\mathbb{Z} \otimes_{\mathbb{Z}} \mathbb{Z}/n\mathbb{Z} \;\cong\; \mathbb{Z}/\gcd(m,n)\mathbb{Z}.
$$

**Example (a tensor product of fields that is not a field).** Over $R = \mathbb{R}$,

$$
\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \;\cong\; \mathbb{C} \times \mathbb{C},
$$

of real dimension four. The idempotents are $\tfrac12(1 \otimes 1 \pm i \otimes i)$, and the two components correspond to the two $\mathbb{R}$-algebra homomorphisms $\mathbb{C} \to \mathbb{C}$, namely the identity and complex conjugation. In particular the tensor product of fields need not be a field; over an algebraically closed field $k$ the analogous product $k \otimes_k k \cong k$ is a field, because the only $k$-algebra structure on $k$ is the identity.

**Example (quaternion algebras).** For a field $F$ and $a, b \in F^\times$, the **quaternion algebra** $(a,b)_F$ is

$$
(a,b)_F = F\langle i,j\rangle\big/\bigl(i^2 - a,\; j^2 - b,\; ij + ji\bigr),
$$

so that $k = ij$ satisfies $k^2 = -ab$ and $i,j,k$ anticommute pairwise. The division algebra $\mathbb{H}$ is $(-1,-1)_{\mathbb{R}}$, and the split biquaternions of the example above are the tensor product $\mathbb{D} \otimes_\mathbb{R} \mathbb{H}$, in which $1 \otimes e_k$ play the role of $i, j, k$ over the split complex base. Tensoring two quaternion algebras over $F$ gives a central simple algebra of dimension $16$ over $F$, and its class in the Brauer group is the sum of the two classes, as the closing section of the article explains.

## Functoriality and Base Change

**Functoriality.** A pair of algebra homomorphisms $f : A \to A'$, $g : B \to B'$ induces

$$
f \otimes g : A \otimes_R B \to A' \otimes_R B', \qquad (f\otimes g)(a \otimes b) = f(a) \otimes g(b),
$$

which is an algebra homomorphism by the universal property, because $(a,b)\mapsto f(a)\otimes g(b)$ is bilinear. Composition and identities are preserved, so $\otimes_R$ is a functor of two variables.

**Extension of scalars.** Let $R \to S$ be a homomorphism of commutative rings and regard $S$ as an $R$-algebra. For an $R$-algebra $A$, the **base change** of $A$ to $S$ is

$$
A_S = A \otimes_R S,
$$

an $S$-algebra with product $(a \otimes s)(a' \otimes s') = aa' \otimes ss'$. Every $R$-algebra homomorphism $A \to B$ induces an $S$-algebra homomorphism $A \otimes_R S \to B \otimes_R S$, so base change is a functor from $R$-algebras to $S$-algebras. It is left adjoint to the functor from $S$-algebras to $R$-algebras that regards an $S$-algebra as an $R$-algebra along $R \to S$.

**Example.** Over $\mathbb{R}$, complexification sends $\mathbb{H}$ to $\mathbb{B} = \mathbb{H} \otimes_\mathbb{R} \mathbb{C}$ and $\mathbb{D}$ to $\mathbb{D} \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$; the second is a splitting of the split complex numbers into two copies of $\mathbb{C}$, and it is the complex analogue of $\mathbb{D} \cong \mathbb{R} \times \mathbb{R}$.

**Proposition (base change commutes with quotients).** Let $I \subseteq A$ be a two-sided ideal and let $R \to S$ be a ring homomorphism. Then the image of $I \otimes_R S$ in $A \otimes_R S$ is a two-sided ideal, and

$$
(A/I) \otimes_R S \;\cong\; (A \otimes_R S)\big/\operatorname{im}\bigl(I \otimes_R S \to A \otimes_R S\bigr).
$$

*Proof.* The tensor product is right exact in each variable (*Modules*, §13), so the quotient exact sequence $0 \to I \to A \to A/I \to 0$ yields an exact sequence $I \otimes_R S \to A \otimes_R S \to (A/I)\otimes_R S \to 0$; the kernel of the second map is therefore the image of the first, which is a two-sided ideal because $I$ is two-sided and $S$ is central. $\square$

The image is written $I\cdot(A\otimes_R S)$ when one wants to emphasise that it need not be isomorphic to $I \otimes_R S$, since the map $I\otimes_R S \to A\otimes_R S$ need not be injective. For $R = \mathbb{Z}$, $A = \mathbb{Z}$, $I = 2\mathbb{Z}$ and $S = \mathbb{Z}/2\mathbb{Z}$: the source $I\otimes_R S = 2\mathbb{Z}\otimes_\mathbb{Z}\mathbb{Z}/2\mathbb{Z} \cong \mathbb{Z}/2\mathbb{Z}$ is spanned by $2 \otimes \bar 1$, and $2\otimes\bar 1 $ maps to $2\otimes\bar 1 = 1\otimes 2\bar 1 = 0$ in $A \otimes_R S = \mathbb{Z}\otimes_\mathbb{Z}\mathbb{Z}/2\mathbb{Z}$, so the image is $0$ and the displayed quotient is $\mathbb{Z}/2\mathbb{Z}$, equal to $(A/I)\otimes_R S$. Thus the ideal is genuinely the image of $I \otimes_R S$ and not $I\otimes_R S$ itself.

## Tensor Products of Ideals and Quotients

**Proposition.** Let $I \subseteq A$ and $J \subseteq B$ be two-sided ideals, and let $\bar I$ and $\bar J$ be the images of $I \otimes_R B$ and $A \otimes_R J$ in $A \otimes_R B$. Then $\bar I + \bar J$ is a two-sided ideal of $A \otimes_R B$ and

$$
(A \otimes_R B)\big/\bigl(\bar I + \bar J\bigr) \;\cong\; (A/I) \otimes_R (B/J).
$$

*Proof.* The quotient maps $A \to A/I$ and $B \to B/J$ induce a surjection $A \otimes B \to (A/I) \otimes (B/J)$, and its kernel is spanned by the tensors with a factor in $I$ or in $J$; that span is $\bar I + \bar J$, since $\bar I$ is spanned by the tensors with first factor in $I$ and $\bar J$ by those with second factor in $J$. Each of $\bar I$ and $\bar J$ is a two-sided ideal, being the image of a two-sided ideal under an algebra homomorphism, so their sum is a two-sided ideal and the first isomorphism theorem applies. $\square$

**Corollary.** If $I$ is a two-sided ideal of $A$ with image $\bar I$ in $A \otimes_R B$, then $(A/I) \otimes_R B \cong (A \otimes_R B)/\bar I$.

**Example.** The general statement gives, for $m, n \geq 1$,

$$
\mathbb{Z}/m\mathbb{Z} \otimes_\mathbb{Z} \mathbb{Z}/n\mathbb{Z} \;\cong\; \mathbb{Z}/\gcd(m,n)\mathbb{Z},
$$

recovering the computation of the example above.

## Central Simple Algebras

**Definition.** Let $F$ be a field. A finite-dimensional $F$-algebra $A$ is **central simple** if $Z(A) = F \cdot 1_A$ and $A$ has no two-sided ideal other than $0$ and $A$ (with $A^2 \neq 0$).

**Theorem (tensor product of central simple algebras).** Let $A$ and $B$ be finite-dimensional central simple $F$-algebras. Then $A \otimes_F B$ is central simple, with $\dim_F (A \otimes_F B) = (\dim_F A)(\dim_F B)$.

*Proof (sketch).* The centre is computed by the proposition on centres: extending scalars to an algebraic closure, where $A$ and $B$ become matrix algebras, the tensor product becomes a matrix algebra and is central simple. Descent along the finite Galois extension then gives the result in general. $\square$

**Wedderburn's structure theorem.** Every finite-dimensional central simple $F$-algebra is isomorphic to $M_n(D)$ for a unique positive integer $n$ and a unique central $F$-division algebra $D$.

**Definition (Brauer group).** Two central simple $F$-algebras $A$ and $B$ are **equivalent**, written $A \sim B$, if

$$
A \otimes_F M_m(F) \;\cong\; B \otimes_F M_n(F) \qquad \text{for some } m, n \geq 1;
$$

by Wedderburn's theorem this is the same as requiring that the division algebras underlying $A$ and $B$ be isomorphic. The tensor product respects equivalence and gives the set of equivalence classes the structure of an abelian group, the **Brauer group** $\mathrm{Br}(F)$, with identity the class of $F$ and inverse the opposite algebra $A^{\mathrm{op}}$, because $A \otimes_F A^{\mathrm{op}} \cong M_{n^2}(F)$ when $\dim_F A = n^2$.

**Example.** Over $F = \mathbb{R}$ the division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ (Frobenius), so the Brauer group is generated by the class of $\mathbb{H}$, which has order $2$: $\mathrm{Br}(\mathbb{R}) \cong \mathbb{Z}/2\mathbb{Z}$. Consequently $\mathbb{H} \otimes_\mathbb{R} \mathbb{H}$ has trivial class, so it is a full matrix algebra over $\mathbb{R}$, and the dimension count $16$ forces

$$
\mathbb{H} \otimes_\mathbb{R} \mathbb{H} \;\cong\; M_4(\mathbb{R}).
$$

Similarly $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ is not central over $\mathbb{R}$ — its centre is $\mathbb{C}$ — but over $\mathbb{C}$ it is $M_2(\mathbb{C})$, and $\mathbb{B} \otimes_\mathbb{C} \mathbb{B} \cong M_4(\mathbb{C})$.

**Example.** For a field $F$ of characteristic not $2$, $(a,b)_F \otimes_F (a,b)_F$ is split for every $a,b \in F^\times$, since the class of $(a,b)_F$ has order dividing $2$ in $\mathrm{Br}(F)$. Thus $\mathbb{H} \otimes_\mathbb{R}\mathbb{H} \cong M_4(\mathbb{R})$ is an instance of a general phenomenon.

## Tensor Powers of an Algebra

**Definition.** Let $A$ be a unital associative $R$-algebra. The **tensor powers** of $A$ are

$$
A^{\otimes 0} = R, \qquad A^{\otimes 1} = A, \qquad A^{\otimes n} = \underbrace{A \otimes_R \cdots \otimes_R A}_{n \text{ factors}}, \quad n \geq 2,
$$

each an $R$-algebra by iteration of the tensor product. As a module, $A^{\otimes n}$ is the $n$-th tensor power of the underlying module of $A$, and the direct sum

$$
\bigoplus_{n \geq 0} A^{\otimes n}
$$

with concatenation is exactly the tensor algebra of *Tensor Powers and the Free Algebra* applied to the underlying module of $A$. The point of the present construction is what that construction does not see: each $A^{\otimes n}$ carries in addition the **componentwise product**

$$
(a_1 \otimes \cdots \otimes a_n)(b_1 \otimes \cdots \otimes b_n) = a_1b_1 \otimes \cdots \otimes a_nb_n,
$$

which uses the product of $A$ and is not determined by the module structure of $A$. It is this product, not concatenation, that makes $A^{\otimes n}$ an algebra whose multiplication is internal to each factor.

**The symmetric group action.** For each $n$, the symmetric group $S_n$ acts on $A^{\otimes n}$ by permuting the factors:

$$
\sigma \cdot (a_1 \otimes \cdots \otimes a_n) = a_{\sigma(1)} \otimes \cdots \otimes a_{\sigma(n)}.
$$

Each $\sigma$ acts by an algebra automorphism, because the product is componentwise and permutation preserves componentwise multiplication. The fixed subalgebra $(A^{\otimes n})^{S_n}$ is the algebra of **symmetric tensors**; its study, and the symmetric powers that appear as its degree-$n$ part in the commutative case, belongs to category 06.

**Example.** For $A = \mathbb{H}$, the tensor powers $\mathbb{H}^{\otimes n}$ are algebras of real dimension $4^n$, and $S_n$ permutes the factors. The invariant subalgebra of $\mathbb{H} \otimes_\mathbb{R} \mathbb{H}$ under the swap $a \otimes b \mapsto b \otimes a$ is the fixed space of a linear involution, of real dimension $(16 + 4)/2 = 10$; it is spanned by the four tensors $e_i \otimes e_i$ and the six sums $e_i \otimes e_j + e_j \otimes e_i$ with $0 \leq i < j \leq 3$, and it is a subalgebra because the fixed points of an algebra automorphism always are.

## Summary

The **tensor product of algebras** $A \otimes_R B$ is the module tensor product with the componentwise product $(a\otimes b)(a'\otimes b') = aa' \otimes bb'$. It is associative and unital when its factors are, commutative when its factors are, and its centre contains $Z(A) \otimes_R Z(B)$, with equality when $R$ is a field. Its universal property is that algebra homomorphisms $A \otimes_R B \to C$ correspond to pairs of homomorphisms $A \to C$, $B \to C$ with commuting images; for commutative algebras this makes $\otimes_R$ the coproduct, not the product, and in general $A \otimes B$ is the quotient of the free product $A \sqcup B$ by the relations $ab = ba$. Over a common algebra $A$ the tensor product of two quotients is the pushout of the diagram $A/I \leftarrow A \rightarrow A/J$ in commutative $A$-algebras, with $(A/I) \otimes_A (A/J) \cong A/(I+J)$.

The principal computations are $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ and $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_\mathbb{R} \mathbb{H}$, both of real dimension $8$; $M_m(R) \otimes_R M_n(R) \cong M_{mn}(R)$; $R[x] \otimes_R R[y] \cong R[x,y]$; $(A/I) \otimes_A (A/J) \cong A/(I+J)$ and $\mathbb{Z}/m \otimes_\mathbb{Z} \mathbb{Z}/n \cong \mathbb{Z}/\gcd(m,n)$; and $\mathbb{C} \otimes_\mathbb{R} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$, showing that a tensor product of fields need not be a field. Base change $A \mapsto A \otimes_R S$ is a functor commuting with quotients, and the tensor product of central simple algebras is central simple; the classes of central simple algebras form the Brauer group, whose only nontrivial real element is the class of $\mathbb{H}$, giving $\mathbb{H} \otimes_\mathbb{R} \mathbb{H} \cong M_4(\mathbb{R})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $A$, $B$, $C$ | $R$-algebras |
| $A \otimes_R B$ | Tensor product of algebras |
| $Z(A)$ | Centre of $A$ |
| $A \sqcup B$ | Free product (coproduct of associative algebras) |
| $A \otimes_C B$ | Pushout of $A \leftarrow C \rightarrow B$ in commutative algebras |
| $A \otimes_R S$ | Base change along $R \to S$ |
| $M_n(R)$ | Matrix algebra; $M_m \otimes M_n \cong M_{mn}$ |
| $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$ | Biquaternions |
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_\mathbb{R} \mathbb{H}$ | Split biquaternions |
| $(a,b)_F$ | Quaternion algebra over $F$ |
| $A^{\mathrm{op}}$ | Opposite algebra |
| $\mathrm{Br}(F)$ | Brauer group of $F$ |
| $A^{\otimes n}$ | $n$-th tensor power of the algebra $A$ |
| $S_n$ | Symmetric group acting by permutations of factors |



## Further Reading

- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for tensor products of modules and algebras, base change and the universal property.
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the tensor product of algebras in full generality.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for central simple algebras and Wedderburn's theorem.
- Philippe Gille and Tamás Szamuely, *Central Simple Algebras and Galois Cohomology* (Cambridge, 2nd ed. 2017), for the Brauer group and the tensor product of central simple algebras.
- John Voight, *Quaternion Algebras* (Springer, 2021), for $(a,b)_F$, its tensor products and its splitting behaviour.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for tensor products of algebras over commutative rings.
