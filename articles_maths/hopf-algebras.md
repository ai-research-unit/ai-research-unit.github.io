
# __Hopf Algebras__

## Introduction

A Hopf algebra is an algebra and a coalgebra at once, tied together by the requirement that the comultiplication and the counit be algebra homomorphisms, and equipped with a single extra map — the **antipode** — that plays the role of inversion. The definition is the smallest algebraic structure in which one can add, multiply, and also split elements apart and read off a constant term, in a way that is compatible with the multiplication. Group algebras and universal enveloping algebras are the two primordial examples, and most of the constructions that look like "algebra plus a symmetry operation" — convolution algebras, the dual of a finite group algebra, quantum groups, and the combinatorics of the shuffle and quasi-shuffle products — are Hopf algebras.

This article is the fifth of the category. It follows *Frobenius Algebras*, whose coalgebraic side it takes up and completes: a finite-dimensional Hopf algebra is Frobenius, and the Frobenius functional is precisely an integral. It precedeswhere the construction of this article is deformed by a parameter, and it is the algebraic theory of the quantum groups of Part II: the locally compact quantum groups, the von Neumann algebraic and $C^*$-algebraic versions, are a different subject, defined with a topology that this Part does not have, and they are deferred there.

The article develops coalgebras and bialgebras first, so that the definition of a Hopf algebra can be stated coherently; then the antipode and its properties; then the examples, of which the group algebra and the enveloping algebra are the two that generate the theory; then integrals, the Hopf-algebraic Maschke theorem and the Frobenius structure; and finally the fundamental theorem of Hopf modules. Everything is over a field, and no notion of convergence, completion or topology is used: a formal power series algebra appears only as the algebraic object.

Throughout, $k$ is a field, all tensor products are over $k$, $H$ is a $k$-vector space, and we use **Sweedler notation**

$$
\Delta(h) = \sum h_{(1)} \otimes h_{(2)} = h_{(1)} \otimes h_{(2)} ,
$$

with the summation sign suppressed, for the comultiplication; iterated comultiplications are written $h_{(1)}\otimes h_{(2)} \otimes h_{(3)}$ and are unambiguous by coassociativity.

## Coalgebras and Bialgebras

### Coalgebras

**Definition.** A **coalgebra** over $k$ is a $k$-vector space $C$ with $k$-linear maps

$$
\Delta : C \to C \otimes_k C \quad \text{(comultiplication)}, \qquad \varepsilon : C \to k \quad \text{(counit)}
$$

satisfying coassociativity and the counit axioms,

$$
(\mathrm{id}\otimes\Delta)\circ\Delta = (\Delta\otimes\mathrm{id})\circ\Delta, \qquad (\varepsilon\otimes\mathrm{id})\circ\Delta = \mathrm{id} = (\mathrm{id}\otimes\varepsilon)\circ\Delta .
$$

In Sweedler notation these read

$$
h_{(1)(1)}\otimes h_{(1)(2)}\otimes h_{(2)} = h_{(1)}\otimes h_{(2)(1)}\otimes h_{(2)(2)}, \qquad \varepsilon(h_{(1)})h_{(2)} = h = h_{(1)}\varepsilon(h_{(2)}) .
$$

A **coalgebra homomorphism** is a $k$-linear map $f : C \to D$ with $\Delta_D \circ f = (f\otimes f)\circ\Delta_C$ and $\varepsilon_D\circ f = \varepsilon_C$. The definitions are the formal duals of those of an algebra: the diagrams are the algebra diagrams with the arrows reversed.

**Example.** For any set $S$, the vector space $kS$ with basis $S$ and

$$
\Delta(s) = s\otimes s, \qquad \varepsilon(s) = 1
$$

is a coalgebra, the **group-like coalgebra**; it is commutative and cocommutative as a coalgebra. Its dual $k^S = \operatorname{Hom}_k(kS,k)$ is the algebra of functions on $S$ with pointwise multiplication.

**Example (the dual of a finite-dimensional algebra).** If $A$ is a finite-dimensional $k$-algebra, then $A^* = \operatorname{Hom}_k(A,k)$ is a coalgebra with

$$
\Delta(f)(a\otimes b) = f(ab), \qquad \varepsilon(f) = f(1),
$$

the transposes of the multiplication and the unit. The finite-dimensionality is used to identify $(A\otimes_k A)^*$ with $A^*\otimes_k A^*$.

### Bialgebras and the convolution algebra

**Definition.** A **bialgebra** is a $k$-vector space $B$ that is simultaneously an algebra $(B, \mu, \eta)$ and a coalgebra $(B,\Delta,\varepsilon)$ such that $\Delta$ and $\varepsilon$ are algebra homomorphisms:

$$
\Delta(ab) = \Delta(a)\Delta(b), \qquad \Delta(1) = 1\otimes 1, \qquad \varepsilon(ab) = \varepsilon(a)\varepsilon(b), \qquad \varepsilon(1) = 1 .
$$

Equivalently, the multiplication and the unit are coalgebra homomorphisms. A **bialgebra homomorphism** is a map that is both an algebra and a coalgebra homomorphism.

**Definition.** For a coalgebra $C$ and an algebra $A$, the **convolution product** on $\operatorname{Hom}_k(C,A)$ is

$$
(f * g)(c) = \mu_A\bigl((f\otimes g)(\Delta(c))\bigr) = f(c_{(1)})\,g(c_{(2)}) .
$$

**Proposition.** With the convolution product $\operatorname{Hom}_k(C,A)$ is an associative $k$-algebra with identity the map $\eta_A\circ\varepsilon_C$. If $C$ is cocommutative or $A$ is commutative, the convolution product is commutative.

*Proof.* Associativity is the coassociativity of $\Delta$ together with the associativity of $\mu_A$: both sides of $(f*g)*h = f*(g*h)$ evaluated at $c$ compute $f(c_{(1)})g(c_{(2)})h(c_{(3)})$. The identity is $\eta\circ\varepsilon$ because $(\eta\varepsilon * f)(c) = \varepsilon(c_{(1)})f(c_{(2)}) = f(c)$ by the counit axiom, and symmetrically. Commutativity in the two stated cases follows because the transposition of the two middle factors does not change the product. $\square$

For a bialgebra $B$ the convolution product makes $\operatorname{End}_k(B) = \operatorname{Hom}_k(B,B)$ an algebra, and the identity map $\mathrm{id}_B$ has a distinguished role: a bialgebra is a Hopf algebra exactly when $\mathrm{id}_B$ is convolution-invertible.

## Hopf Algebras and the Antipode

### Definition

**Definition.** A **Hopf algebra** is a bialgebra $H$ together with a $k$-linear map $S : H \to H$, the **antipode**, that is inverse to $\mathrm{id}_H$ under convolution:

$$
S * \mathrm{id}_H = \eta\circ\varepsilon = \mathrm{id}_H * S ,
$$

that is, in Sweedler notation,

$$
S(h_{(1)})\,h_{(2)} = \varepsilon(h)\,1 = h_{(1)}\,S(h_{(2)}) \qquad \text{for all } h \in H .
$$

A **Hopf algebra homomorphism** is a bialgebra homomorphism commuting with the antipodes.

**Proposition (uniqueness and basic properties of the antipode).** Let $H$ be a Hopf algebra.

1. The antipode is unique.
2. $S$ is an algebra anti-homomorphism and a coalgebra anti-homomorphism:
$$
S(ab) = S(b)S(a), \qquad S(1) = 1, \qquad \Delta(S(h)) = S(h_{(2)})\otimes S(h_{(1)}), \qquad \varepsilon(S(h)) = \varepsilon(h) .
$$

*Proof.* 1: if $S'$ is another convolution inverse of $\mathrm{id}$ then $S = S * \eta\varepsilon = S * (\mathrm{id} * S') = (S*\mathrm{id})*S' = \eta\varepsilon * S' = S'$. 2: consider the convolution algebra $\operatorname{Hom}_k(H\otimes_k H, H)$ and the elements $\alpha = \mu\circ(S\otimes S)\circ\tau$ and $\beta = S\circ\mu$, where $\tau$ is the transposition. Both are convolution-inverses of $\mu$ in $\operatorname{Hom}_k(H\otimes_k H,H)$, since $S$ is a convolution inverse of $\mathrm{id}$ and convolution is compatible with the tensor algebra structure; by uniqueness of inverses in an associative algebra $\alpha = \beta$. The coalgebra statements are proved by the dual argument, or by applying the algebra statement to $H^{\mathrm{op}}$ and $H^{\mathrm{cop}}$. $\square$

### Group-like and primitive elements

**Definition.** An element $g \in H$ is **group-like** if $\Delta(g) = g\otimes g$ and $\varepsilon(g) = 1$; the set $G(H)$ of group-like elements is a group under multiplication, with inverse $S(g)$. An element $x \in H$ is **primitive** if $\Delta(x) = x\otimes 1 + 1\otimes x$; the set $P(H)$ of primitive elements is a Lie subalgebra of $H$ under the commutator bracket $[x,y] = xy - yx$.

*Proof (of the group statement).* If $g, g'$ are group-like then $\Delta(gg') = (g\otimes g)(g'\otimes g') = gg'\otimes gg'$ and $\varepsilon(gg')=1$, so $G(H)$ is closed under multiplication; $1$ is group-like; and from $S(g)g = \varepsilon(g)1 = 1$ we get $S(g) = g^{-1}$. For primitives, $\Delta([x,y]) = [\Delta x, \Delta y]$ computed in the tensor algebra, which expands to $[x,y]\otimes1 + 1\otimes[x,y]$, so $P(H)$ is closed under the bracket; the Jacobi identity is inherited from the associativity of $H$. $\square$

For a group algebra $k[G]$ the group-like elements are exactly the elements of $G$; for an enveloping algebra the primitive elements are exactly the Lie algebra, by the Milnor–Moore theorem when $k$ has characteristic $0$.

### Cocommutativity and the dual

**Definition.** A bialgebra is **cocommutative** if $\tau\circ\Delta = \Delta$, where $\tau(x\otimes y) = y\otimes x$, and **commutative** if $ab = ba$. A Hopf algebra is **commutative or cocommutative** accordingly; the group algebra is cocommutative and the algebra of functions on a finite group is commutative.

**Proposition (the dual Hopf algebra).** Let $H$ be a finite-dimensional Hopf algebra. Then $H^* = \operatorname{Hom}_k(H,k)$ is a Hopf algebra with the transposes of the structure maps:

$$
(fg)(h) = (f\otimes g)(\Delta(h)), \qquad \eta(1) = \varepsilon, \qquad \Delta(f)(h\otimes h') = f(hh'), \qquad \varepsilon(f) = f(1), \qquad S(f) = f\circ S .
$$

The dual is commutative exactly when $H$ is cocommutative, and cocommutative exactly when $H$ is commutative.

*Proof.* The algebra axioms for $H^*$ are the coalgebra axioms for $H$ and conversely, since transposition reverses all diagrams and finite-dimensionality makes the double dual identity, so every axiom transfers. The last statement is the observation that commutativity of $H^*$ is cocommutativity of $H$ read through the transposition. $\square$

## Examples

**Example (the group algebra).** For any group $G$, the group algebra $k[G]$ is a Hopf algebra with

$$
\Delta(g) = g\otimes g, \qquad \varepsilon(g) = 1, \qquad S(g) = g^{-1},
$$

extended linearly. Coassociativity and the counit axioms are immediate from the group axioms; the antipode identity is $g^{-1}g = 1$. Thusdescribes a Hopf algebra, and the group-like elements are exactly the elements of $G$. The algebra is cocommutative, and it is commutative exactly when $G$ is abelian; when $G$ is abelian and $k$ contains the $\lvert G\rvert$-th roots of unity, the dual Hopf algebra is the group algebra of the dual group $\widehat G$, by Pontryagin duality for finite abelian groups.

**Example (the universal enveloping algebra).** Let $\mathfrak{g}$ be a Lie algebra over $k$, with bracket $[\cdot,\cdot]$, and let

$$
U(\mathfrak{g}) = T(\mathfrak{g})\big/\bigl(x\otimes y - y\otimes x - [x,y]\bigr)
$$

be its universal enveloping algebra, as in *Quotients of the Tensor Algebra*; the systematic theory of $U(\mathfrak{g})$ and of the Poincaré–Birkhoff–Witt theorem is developed in the anti-symmetric category. Then $U(\mathfrak{g})$ is a Hopf algebra with

$$
\Delta(x) = x\otimes 1 + 1\otimes x, \qquad \varepsilon(x) = 0, \qquad S(x) = -x \qquad (x \in \mathfrak{g}),
$$

extended so that $\Delta$ and $\varepsilon$ are algebra homomorphisms and $S$ is an algebra anti-homomorphism. The primitive elements are exactly $\mathfrak{g}$, which is the statement that the Lie algebra can be recovered from its enveloping algebra. The Hopf algebra $U(\mathfrak{g})$ is cocommutative, and it is commutative exactly when $\mathfrak{g}$ is abelian, in which case $U(\mathfrak{g}) = \operatorname{Sym}(\mathfrak{g})$ as a Hopf algebra.

**Example (functions on a finite group).** Let $G$ be finite and let $k^G = \operatorname{Hom}_k(k[G],k)$ be the dual of the group algebra, with basis the coordinate functions $\delta_g$, $\delta_g(h) = \delta_{gh}$. The product in the dual is pointwise, $(fg)(h) = (f\otimes g)(\Delta h) = f(h)g(h)$, so $\delta_g\delta_h = \delta_{gh}\,\delta_g$ where $\delta_{gh}$ is the Kronecker symbol; the algebra is therefore the product $\prod_{g\in G}k$ of $\lvert G\rvert$ copies of $k$, and it has $\lvert G\rvert$ orthogonal idempotents $\delta_g$. The Hopf structure is

$$
\Delta(\delta_g) = \sum_{h\ell = g}\delta_h\otimes \delta_\ell, \qquad \varepsilon(\delta_g) = \delta_{g,1}, \qquad S(\delta_g) = \delta_{g^{-1}} .
$$

This Hopf algebra is commutative and, for nonabelian $G$, not cocommutative; it is the algebraic model of the functions on the group with convolution as comultiplication, and it is the finite case of the Hopf algebra of functions on an algebraic group.

**Example (the Laurent polynomial algebra).** $H = k[x,x^{-1}]$ with $x$ group-like, $\Delta(x) = x\otimes x$, $\varepsilon(x)=1$, $S(x)=x^{-1}$, is the group algebra $k[\mathbb{Z}]$; it is the simplest Hopf algebra that is neither finite-dimensional nor generated by primitives.

**Example (coordinate Hopf algebras).** Let the coordinate algebra of $n\times n$ matrices be $k[x_{ij}]$, a polynomial algebra in $n^2$ variables, with

$$
\Delta(x_{ij}) = \sum_{\ell=1}^n x_{i\ell}\otimes x_{\ell j}, \qquad \varepsilon(x_{ij}) = \delta_{ij} .
$$

These formulas make $k[x_{ij}]$ a bialgebra, the comultiplication being the transpose of matrix multiplication; it is not a Hopf algebra, because the antipode would have to be built from the inverse of a matrix and a general matrix is not invertible. Inverting the determinant $D = \det(x_{ij})$ gives the algebra $k[x_{ij},D^{-1}]$, which is a Hopf algebra with $S(x_{ij})$ the $(j,i)$ entry of the inverse matrix, computed by the cofactor formula $S(x_{ij}) = (-1)^{i+j}D^{-1}M_{ji}$ where $M_{ji}$ is the complementary minor. This is the standard source of non-cocommutative examples, and it is the algebra that the quantum groups deform. The determinant and the minors are the algebraic constructions.

**Example (tensor products).** If $H_1, H_2$ are Hopf algebras then so is $H_1\otimes_k H_2$, with all structure maps applied componentwise and the product on the tensor product as in *Tensor Products of Algebras*; the antipode is $S_1\otimes S_2$. The dual of a tensor product is the tensor product of the duals when both factors are finite-dimensional.

## Integrals and Semisimplicity

### Integrals

**Definition.** A **left integral** in a Hopf algebra $H$ is an element $\Lambda \in H$ with

$$
h\Lambda = \varepsilon(h)\Lambda \qquad \text{for all } h \in H ;
$$

a **right integral** is an element $\Lambda$ with $\Lambda h = \varepsilon(h)\Lambda$. The subspaces of left and right integrals are written $\int_H^\ell$ and $\int_H^r$.

**Theorem (Larson–Sweedler, standard).** Let $H$ be a finite-dimensional Hopf algebra. Then $\dim_k\int_H^\ell = 1 = \dim_k\int_H^r$, and the antipode induces an isomorphism $\int_H^\ell \to \int_H^r$.

This is the theorem that makes the Hopf algebra Frobenius, and the integral is exactly the Frobenius functional's dual object.

### The Hopf-algebraic Maschke theorem

**Theorem (Larson–Sweedler, standard).** Let $H$ be a finite-dimensional Hopf algebra. Then the following are equivalent:

1. $H$ is semisimple as a left $H$-module;
2. there is a left integral $\Lambda$ with $\varepsilon(\Lambda) \neq 0$;
3. $H$ is separable over $k$.

*Proof (sketch).* If $\varepsilon(\Lambda) \neq 0$ then normalising $\Lambda$ to have $\varepsilon(\Lambda) = 1$ and averaging over $H$ with the aid of the comultiplication produces a projection onto the invariants, which is the Maschke argument: for any surjection $M \to N$ of $H$-modules and any $k$-linear splitting $\sigma$, the averaged map $\tilde\sigma(n) = \Lambda_{(1)}\cdot\sigma(S(\Lambda_{(2)})\cdot n)$ is $H$-linear and still splits. Conversely, if $H$ is semisimple then the counit, which is a nonzero $H$-module map onto the trivial module, splits, and the image of $1$ under a splitting is a left integral with $\varepsilon(\Lambda)=1$. The equivalence with separability is the characterisation of separability by the splitting of the multiplication in *Separable Algebras*, applied to the Hopf algebra whose regular module is semisimple. $\square$

**Corollary.** For a finite group $G$ and a field $k$, the group algebra $k[G]$ is semisimple as a Hopf algebra exactly when $\operatorname{char}k \nmid \lvert G\rvert$; the left integral is $\Lambda = \sum_{g\in G}g$ when $\operatorname{char}k = p \mid \lvert G\rvert$, and $\varepsilon(\Lambda) = \lvert G\rvert = 0$ in that case. This is Maschke's theorem in the form, and the integral is the element that would serve as a normalised average if $\lvert G\rvert$ were invertible. When $\operatorname{char}k = p \mid \lvert G\rvert$ the integral $\sum_g g$ lies in the socle of $k[G]$, which is the module-theoretic form of the failure of semisimplicity.

### The Frobenius structure

**Theorem (standard).** Every finite-dimensional Hopf algebra is a Frobenius algebra, and it is symmetric Frobenius when $S^2 = \mathrm{id}$.

*Proof (sketch).* Let $0 \neq \Lambda \in \int_H^\ell$. Define $\lambda : H \to k$ by $\lambda(h) = \varepsilon(h\Lambda)$; the pairing $(h,h') \mapsto \lambda(hh')$ is non-degenerate because $H$ is a free module over the one-dimensional space of integrals and the composition $H \to \int_H^\ell$, $h \mapsto h\Lambda$ together with the surjectivity of $\varepsilon$ on the integral gives the required splitting. The symmetry statement follows because $\lambda(hh') = \lambda(h'h)$ is equivalent to $S^2 = \mathrm{id}$ for a finite-dimensional Hopf algebra, by the relation between the modular functions. $\square$

This theorem is the precise link between the present article and *Frobenius Algebras*: the Frobenius functional is the counit evaluated against the integral, the Nakayama automorphism is the square of the antipode conjugated by the modular function, and the Frobenius algebra is symmetric exactly when $S^2 = \mathrm{id}$.

## Hopf Modules and the Fundamental Theorem

**Definition.** A **(left-left) Hopf module** over a Hopf algebra $H$ is a $k$-vector space $M$ that is a left $H$-module and a left $H$-comodule, with the action and coaction compatible:

$$
\delta(h\cdot m) = h_{(1)}m_{(-1)}\otimes h_{(2)}\cdot m_{(0)} ,
$$

where $\delta(m) = m_{(-1)}\otimes m_{(0)}$ is the coaction. A Hopf module is **trivial** if the coaction is $\delta(m) = 1\otimes m$.

**Theorem (fundamental theorem of Hopf modules, standard).** Let $H$ be a Hopf algebra with antipode $S$. For a Hopf module $M$ let

$$
M^{\mathrm{co}H} = \{m \in M : \delta(m) = 1\otimes m\}
$$

be its space of **coinvariants**. Then the multiplication map

$$
H\otimes_k M^{\mathrm{co}H} \longrightarrow M, \qquad h\otimes m \longmapsto h\cdot m
$$

is an isomorphism of Hopf modules. Consequently every Hopf module is free over $H$ on its coinvariants.

*Proof.* The map is a Hopf module homomorphism by the compatibility axiom. Its inverse is built from the antipode: $\Phi(m) = m_{(-1)}S(m_{(-2)})\otimes m_{(0)}$, which lands in $H\otimes M^{\mathrm{co}H}$ because the coaction on the first factor is balanced by $S$. Both composites are the identity by the antipode identity and the coassociativity and counit axioms. $\square$

The theorem is the Hopf-algebraic form of the statement that a module over a group algebra is free over the coinvariants, and it is the engine of the **Galois theory** of Hopf algebras: a Hopf algebra $H$ acting on an algebra $A$ gives a Galois extension precisely when the comparison map $A\otimes_{A^H}A \to A\otimes_k H$ is an isomorphism, and the fundamental theorem of Hopf modules is what makes the coinvariants the correct "fixed algebra". This is the algebraic counterpart of the Galois descent of *Group Cohomology*.

## Actions, Smash Products and the Quantum Plane of the Next Article

**Definition.** Let $H$ be a Hopf algebra. An **$H$-module algebra** is an algebra $A$ that is a left $H$-module with

$$
h\cdot(ab) = (h_{(1)}\cdot a)(h_{(2)}\cdot b), \qquad h\cdot 1 = \varepsilon(h)1 ,
$$

and an **$H$-comodule algebra** is defined dually with a coaction $\delta : A \to H\otimes_k A$ that is an algebra homomorphism. An **$H$-module coalgebra** and an **$H$-comodule coalgebra** are defined by the same pattern with the coalgebra structure preserved.

**Proposition (the smash product).** Let $H$ be a Hopf algebra and $A$ an $H$-module algebra. Then the vector space $A\otimes_k H$ carries an associative multiplication

$$
(a\otimes h)(b\otimes g) = a\,(h_{(1)}\cdot b)\otimes h_{(2)}g ,
$$

with unit $1\otimes 1$, called the **smash product** $A\# H$. The maps $a \mapsto a\otimes 1$ and $h \mapsto 1\otimes h$ are algebra homomorphisms from $A$ and $H$, and $A\#H$ is generated by their images.

*Proof.* Associativity is a direct expansion using the module-algebra axiom and the coassociativity and multiplicativity of $\Delta$; the computation of $((a\otimes h)(b\otimes g))(c\otimes \ell)$ and $(a\otimes h)((b\otimes g)(c\otimes \ell))$ both reduce to $a(h_{(1)}\cdot b)(h_{(2)}\cdot c)\otimes h_{(3)}g\ell$. The unit is immediate from $h_{(1)}\varepsilon(h_{(2)}) = h$. $\square$

**Example (the Weyl algebra from a group algebra action).** Let $H = k[\mathbb{Z}] = k[x,x^{-1}]$ act on the polynomial algebra $A = k[y]$ by $x\cdot y = y+1$, extended as an algebra automorphism. Then $A\# H$ has generators $y$ and $x$ with the single relation

$$
xy - yx = x ,
$$

so the smash product is the localisation of the first Weyl algebra, the algebra of operators generated by multiplication by $y$ and the shift $x$. This is the standard illustration that a Hopf algebra action on an algebra can be encoded in a larger algebra with a commutation relation, and it is the pattern that the quantum groups repeat with a parameter $q$.

The **quantum plane** is the algebra $k_q[x,y]$ with the single relation $yx = q\,xy$ for $q \in k^\times$. A group-like element $K$ acting by $K\cdot x = x$ and $K\cdot y = q^{-1}y$ extends to an algebra automorphism of $k_q[x,y]$, so the quantum plane is a module algebra over the group algebra $k[\mathbb{Z}]$, with $\mathbb{Z}$ generated by $K$; the smash product $k_q[x,y]\# k[\mathbb{Z}]$ is then an algebra generated by $x, y, K$ with the relations $yx = qxy$ and $KxK^{-1} = x$, $KyK^{-1} = q^{-1}y$. The general theory of these deformations, of the quantised enveloping algebras $U_q(\mathfrak{g})$ and of the quantum groups at roots of unity is developed, which is not covered here; the present article supplies the undeformed structure that the deformation acts on.

**Boundary note.** The word *quantum group* also names the locally compact quantum groups, which are objects of operator algebra theory defined by a comultiplication on a von Neumann algebra together with left and right Haar weights, and the compact quantum groups defined by Woronowicz with a dense $C^*$-subalgebra and a Haar state. Those theories require a topology, a norm and a completion, and they belong to a later Part; the Hopf algebras of this article and the algebraic quantum groups of the next are the algebraic objects, and no topological statement is made here.

## Summary

A **coalgebra** is the formal dual of an algebra: a space with a coassociative comultiplication $\Delta$ and a counit $\varepsilon$ satisfying $(\varepsilon\otimes\mathrm{id})\Delta = \mathrm{id} = (\mathrm{id}\otimes\varepsilon)\Delta$. A **bialgebra** is an algebra and a coalgebra whose comultiplication and counit are algebra homomorphisms, and the **convolution product** $(f*g)(h) = f(h_{(1)})g(h_{(2)})$ makes $\operatorname{Hom}_k(C,A)$ an algebra with identity $\eta\varepsilon$. A **Hopf algebra** is a bialgebra whose identity map is convolution-invertible; the inverse is the **antipode** $S$, characterised by $S(h_{(1)})h_{(2)} = \varepsilon(h)1 = h_{(1)}S(h_{(2)})$. The antipode is unique, it is an algebra and coalgebra anti-homomorphism, and $\Delta(S(h)) = S(h_{(2)})\otimes S(h_{(1)})$; the **group-like** elements $\Delta(g) = g\otimes g$ form a group, and the **primitive** elements $\Delta(x) = x\otimes 1 + 1\otimes x$ form a Lie algebra.

The group algebra $k[G]$ with $\Delta(g) = g\otimes g$, $\varepsilon(g)=1$, $S(g)=g^{-1}$ and the enveloping algebra $U(\mathfrak{g})$ with $\Delta(x) = x\otimes 1+1\otimes x$, $\varepsilon(x)=0$, $S(x)=-x$ are the two primordial examples, cocommutative and generating the theory; the dual $H^*$ of a finite-dimensional Hopf algebra is a Hopf algebra with the transposed structure maps, so $k^G = (k[G])^*$ is the commutative Hopf algebra of functions on a finite group. A finite-dimensional Hopf algebra has a one-dimensional space of left integrals and a one-dimensional space of right integrals, the **Larson–Sweedler theorem**; it is semisimple exactly when some left integral has $\varepsilon(\Lambda) \neq 0$, which is the Hopf-algebraic **Maschke theorem** and specialises to the classical one for $k[G]$; and it is a **Frobenius algebra** in the sense of the preceding article, with the Frobenius functional built from the integral and the counit, symmetric exactly when $S^2 = \mathrm{id}$. The **fundamental theorem of Hopf modules** identifies every Hopf module with $H\otimes_k M^{\mathrm{co}H}$, making the coinvariants the correct fixed objects and providing the algebraic engine of Hopf–Galois theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | ground field |
| $H$, $C$, $B$ | Hopf algebra, coalgebra, bialgebra |
| $\mu$, $\eta$ | multiplication and unit of an algebra |
| $\Delta$, $\varepsilon$ | comultiplication and counit of a coalgebra |
| $h_{(1)}\otimes h_{(2)}$ | Sweedler notation for $\Delta(h)$ |
| $S$ | antipode, $\mathrm{id}$-inverse under convolution |
| $(f*g)(c) = f(c_{(1)})g(c_{(2)})$ | convolution product |
| $G(H)$ | group-like elements, $\Delta(g)=g\otimes g$ |
| $P(H)$ | primitive elements, $\Delta(x)=x\otimes1+1\otimes x$ |
| $H^*$ | dual Hopf algebra for $\dim_k H < \infty$ |
| $k[G]$ | group algebra, $S(g)=g^{-1}$ |
| $U(\mathfrak{g})$ | enveloping algebra, $S(x)=-x$ |
| $k^G = (k[G])^*$ | Hopf algebra of functions on a finite group |
| $\int_H^\ell$, $\int_H^r$ | left and right integrals, one-dimensional |
| $\varepsilon(\Lambda)\neq0$ | Maschke condition for semisimplicity |
| $M^{\mathrm{co}H}$ | coinvariants of a Hopf module |
| $m_{(-1)}\otimes m_{(0)}$ | coaction |
| $\tau(x\otimes y) = y\otimes x$ | transposition; cocommutativity |
| $A\# H$ | smash product, $(a\otimes h)(b\otimes g) = a(h_{(1)}\cdot b)\otimes h_{(2)}g$ |
| $H$-module algebra | $h\cdot(ab) = (h_{(1)}\cdot a)(h_{(2)}\cdot b)$, $h\cdot 1 = \varepsilon(h)1$ |
| $k_q[x,y]$ | quantum plane, $yx = q\,xy$ |





## Further Reading

- Moss E. Sweedler, *Hopf Algebras* (Benjamin, 1969), for the foundational theory, integrals and the fundamental theorem of Hopf modules.
- Susan Montgomery, *Hopf Algebras and Their Actions on Rings* (American Mathematical Society, 1993), for integrals, the Hopf-algebraic Maschke theorem and Hopf–Galois theory.
- Eiichi Abe, *Hopf Algebras* (Cambridge, 1980), for the structure theory and the relation to algebraic groups.
- Richard G. Larson and Moss E. Sweedler, "An associative orthogonal bilinear form for Hopf algebras", *American Journal of Mathematics* **91** (1969), 75–94, for the Frobenius structure of a finite-dimensional Hopf algebra.
- Christian Kassel, *Quantum Groups* (Springer, 1995), for the deformation theory that begins with the Hopf algebras of this article.
- Sorin Dăscălescu, Constantin Năstăsescu and Șerban Raianu, *Hopf Algebras: An Introduction* (Marcel Dekker, 2001), for a modern systematic treatment with the categorical constructions.
