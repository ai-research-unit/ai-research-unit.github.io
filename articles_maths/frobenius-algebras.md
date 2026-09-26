
# __Frobenius Algebras__

## Introduction

A finite-dimensional algebra over a field is **Frobenius** when it carries a linear functional whose associated pairing with the product is non-degenerate, or equivalently when the algebra is isomorphic, as a module over itself, to its own linear dual. The condition is a duality condition on the algebra, and it is the abstract form of the statement that an algebra has a trace: the trace of a matrix algebra, the coefficient of the identity in a group algebra, and the coefficient of the top power in a truncated polynomial algebra are all instances of a single construction. Frobenius algebras are the algebras over which the regular module is injective as well as projective, and they are the class of algebras on which the duality theory of the symmetric algebra and of the homology of a manifold is modelled.

The article is the first of the representation-theoretic layer of the category. It follows the structure-theoretic articles *Central Simple Algebras and the Brauer Group*, *Crossed Products* and *Separable Algebras*, and it prepares the ground, where the existence of an integral is exactly the Frobenius condition, where the Frobenius property of the algebra makes its dual a coalgebra. The two central objects of the article are the Frobenius functional and its Nakayama automorphism; the symmetric algebras are the case in which the automorphism is the identity, and that is where the comparison is made.

The article is algebraic. The language of a non-degenerate pairing is used only as a device for expressing a duality between an algebra and its dual; the theory of bilinear and quadratic forms — symmetry and skew-symmetry as a classification, diagonalisation, orthogonal groups, and the geometric reading of a pairing — belongs to Part II, and the topological Poincaré duality that a Frobenius algebra models belongs there as well. Everything asserted here is an isomorphism of modules or an identity between elements.

Throughout, $k$ is a field, $A$ is a finite-dimensional unital associative $k$-algebra, and $A^* = \operatorname{Hom}_k(A,k)$ is its linear dual. We write $A^{\mathrm{op}}$ for the opposite algebra and $\operatorname{soc}(A)$ for the socle of the regular module.

## The Frobenius Functional

### Definition and the duality with the dual

**Definition.** A **Frobenius functional** on $A$ is a nonzero $k$-linear map $\lambda : A \to k$ such that the bilinear pairing

$$
A \times A \to k, \qquad (a,b) \mapsto \lambda(ab),
$$

is non-degenerate: if $\lambda(ab) = 0$ for all $b$ then $a = 0$, and if $\lambda(ab) = 0$ for all $a$ then $b = 0$. The algebra $A$ is a **Frobenius algebra** if it carries a Frobenius functional.

The two non-degeneracy conditions are the injectivity of the two maps

$$
\ell_\lambda : A \to A^*, \quad \ell_\lambda(a)(b) = \lambda(ab), \qquad r_\lambda : A \to A^*, \quad r_\lambda(a)(b) = \lambda(ba),
$$

and since $A$ and $A^*$ have the same finite dimension, each of them is injective exactly when it is an isomorphism.

**Theorem (equivalent formulations).** For a finite-dimensional unital $k$-algebra $A$ the following are equivalent:

1. $A$ is a Frobenius algebra;
2. $A \cong A^*$ as left $A$-modules;
3. $A \cong A^*$ as right $A$-modules;
4. there is a nonzero functional $\lambda \in A^*$ whose left and right annihilators in $A$ are zero.

*Proof.* The equivalence of 1 and 2 is the identification of $\ell_\lambda$ as a left $A$-module map: for $a, x, b \in A$,

$$
\ell_\lambda(ax)(b) = \lambda(axb) = \ell_\lambda(x)(ba) = (a \cdot \ell_\lambda(x))(b),
$$

where the left $A$-module structure on $A^*$ is $(a\cdot f)(b) = f(ba)$; so a Frobenius functional gives an isomorphism ${}_A A \to {}_A A^*$, and conversely any isomorphism is $\ell_\lambda$ for $\lambda = \varphi(1)$. The right-hand statement is identical with the opposite module structure, so 3 is equivalent to 1 and 2. Statement 4 is the non-degeneracy condition rewritten, since $\ell_\lambda$ is injective exactly when the left annihilator of $\lambda$ is zero. $\square$

**Corollary (self-injectivity).** A Frobenius algebra $A$ is **quasi-Frobenius**: every projective left $A$-module is injective, and every injective left $A$-module is projective, so a left $A$-module is projective if and only if it is injective.

*Proof.* The dual $A^*$ of the regular module is injective as a left $A$-module, since $A^* = \operatorname{Hom}_k(A,k)$ is the injective cogenerator of the category of $k$-vector spaces, and $A \cong A^*$ by the theorem; hence ${}_AA$ is injective. A direct summand of an injective module is injective and a direct sum of injectives is injective, so every projective module is injective. Applying the same argument to $A^{\mathrm{op}}$ and dualising gives the converse. $\square$

The converse of the corollary fails in general: a self-injective algebra need not satisfy $A \cong A^*$ as modules on either side, and such algebras are precisely the quasi-Frobenius non-Frobenius algebras. The extra condition that upgrades quasi-Frobenius to Frobenius is that the left socle and the right socle of the regular module coincide, a condition of Nakayama's.

### The Nakayama automorphism

**Definition.** Let $\lambda$ be a Frobenius functional and let $\nu : A \to A$ be the $k$-linear map determined by

$$
\lambda(ab) = \lambda\bigl(b\,\nu(a)\bigr) \qquad \text{for all } a, b \in A .
$$

The map $\nu$ is the **Nakayama automorphism** of $(A,\lambda)$.

**Proposition.** The map $\nu$ is a $k$-algebra automorphism of $A$, and it depends on $\lambda$ only up to composition with an inner automorphism: if $\lambda' = \lambda \circ \iota_u$ for a unit $u$, then $\nu' = \iota_u^{-1}\circ\nu\circ\iota_u$ where $\iota_u(x) = uxu^{-1}$.

*Proof.* For the multiplicativity, compute

$$
\lambda\bigl(b\,\nu(ac)\bigr) = \lambda(acb) = \lambda\bigl((cb)\nu(a)\bigr) = \lambda\bigl(b\,\nu(a)\nu(c)\bigr)
$$

using the defining property twice, so $\nu(ac) = \nu(a)\nu(c)$ by non-degeneracy. For the unit, $\lambda(b) = \lambda(b\,\nu(1))$ gives $\nu(1)=1$. Injectivity follows because $\lambda(b\nu(a))=0$ for all $b$ forces $\nu(a)=0$. The dependence on $\lambda$ is a direct calculation: $\lambda'(ab) = \lambda(uabu^{-1}) = \lambda(bu^{-1}\nu(a)u) = \lambda'(b\,u^{-1}\nu(a)u)$. $\square$

An algebra is called **symmetric** if it admits a Frobenius functional with $\nu = \mathrm{id}$, that is, one satisfying $\lambda(ab) = \lambda(ba)$ for all $a,b$. Every commutative Frobenius algebra is symmetric, and so is every matrix algebra and every group algebra; the exterior algebra, when its dimension is even, is Frobenius but not symmetric, and its Nakayama automorphism is the parity automorphism.

### Self-injectivity and the cogenerator property

**Corollary.** A Frobenius algebra $A$ is self-injective: every projective left $A$-module is injective, and every injective left $A$-module is projective. Consequently a left $A$-module is projective if and only if it is injective, and the projective indecomposable modules are the injective indecomposable modules.

*Proof.* The regular module is injective by the theorem, and a direct summand of an injective module is injective, so every projective module, being a summand of a free module, is injective. The converse is the dual statement, obtained by applying the same argument to the opposite algebra and using that a module is injective over $A$ exactly when its dual is projective over $A^{\mathrm{op}}$. $\square$

**Corollary.** For a Frobenius algebra $A$ the socle of the left regular module is isomorphic to the dual of the top, $\operatorname{soc}({}_AA) \cong (A/J(A))^*$, and in particular $\operatorname{soc}({}_AA)$ is simple exactly when $A$ is a local algebra, that is, exactly when $A$ has a unique simple module up to isomorphism. Every finite-dimensional semisimple $k$-algebra is Frobenius, and a local Frobenius algebra is the basic example with a simple socle.

*Proof.* The dual of the top is $\operatorname{Hom}_k(A/J(A),k) \cong \operatorname{ann}_A(J(A))$, the annihilator of the radical; and $A/J(A)$ is generated by the simple modules, so its dual is the largest semisimple submodule of $A^*$. Under $A \cong A^*$ this is $\operatorname{soc}(A)$. The socle is simple exactly when there is one summand in its decomposition, which happens exactly for a local algebra. $\square$

The mutual injectivity and projectivity of the modules over a Frobenius algebra is what makes the algebra its own dual in the strongest sense, and it is the algebraic shadow of Poincaré duality, whose geometric statement requires the topological notions of a later Part and is therefore deferred there.

## Symmetric Algebras

### Definition and the trace property

**Definition.** A Frobenius algebra $(A,\lambda)$ is **symmetric** if $\lambda(ab) = \lambda(ba)$ for all $a, b \in A$. Equivalently the **trace** functional $\lambda$ vanishes on commutators, $\lambda([a,b]) = 0$, and the Nakayama automorphism is the identity.

The functional of a symmetric algebra is what is usually called a **trace**, and the tensor product and the direct product of symmetric algebras are symmetric with the product functionals.

### The Casimir element

**Definition.** Let $\lambda$ be a Frobenius functional with Nakayama automorphism $\nu$, and let $\{a_i\}$ be a $k$-basis of $A$ with dual basis $\{a^i\}$ defined by $\lambda(a_i a^j) = \delta_i^j$. The **Casimir element** of $(A,\lambda)$ is

$$
C = \sum_i a_i \otimes a^i \in A \otimes_k A .
$$

**Proposition.** Let $\{a_i\}$ be a $k$-basis of $A$ and let $\{a^i\}$ be the basis dual to it with respect to the Frobenius pairing, $\lambda(a_i a^j) = \delta_i^j$.

1. $\lambda\bigl(\mu(C)\bigr) = \dim_k A$, where $\mu$ is the multiplication of $A$.
2. For every $a \in A$ the trace of the left multiplication $L_a$ is
$$
\operatorname{Tr}(L_a) \;=\; \lambda\Bigl(\sum_i a\,a_i\,a^i\Bigr),
$$
so the trace is computed by contracting the Casimir element with $a$ in the first tensor factor.
3. If $A$ is symmetric, then $C$ is fixed by the flip $\tau(x\otimes y) = y\otimes x$; if $A$ is Frobenius but not symmetric then $C$ is not flip-fixed, and the failure is measured by $\nu$.

*Proof.* 1: $\lambda\bigl(\sum_i a_i a^i\bigr) = \sum_i \lambda(a_i a^i) = \sum_i \delta_i^i = \dim_k A$. For 2, let $c_{ij}$ be the matrix of $L_a$ in the basis $\{a_i\}$, so that $a\,a_i = \sum_j c_{ij}a_j$. Multiplying on the right by $a^i$ and applying $\lambda$ gives, by associativity and $\lambda(a_k a^i) = \delta_{ki}$,

$$
\lambda\bigl(a\,a_i\,a^i\bigr) = \sum_j c_{ij}\lambda\bigl(a_j a^i\bigr) = c_{ii},
$$

and summing over $i$ gives $\lambda\bigl(\sum_i a\,a_i\,a^i\bigr) = \sum_i c_{ii} = \operatorname{Tr}(L_a)$. For 3, the flip sends $C$ to $\sum_i a^i\otimes a_i$; when $\lambda(ab) = \lambda(ba)$ the pairing is invariant under the flip and the metric-dual bases may be interchanged, so the two sums agree, while for a general $\nu$ they differ, the defect being the twist $\nu$ of the pairing. $\square$

### Examples

**Example (matrix algebras).** $A = M_n(k)$ with $\lambda = \operatorname{Tr}$, the matrix trace. The pairing $(X,Y)\mapsto\operatorname{Tr}(XY)$ is non-degenerate because the trace form is non-degenerate on $M_n(k)$; and $\operatorname{Tr}(XY) = \operatorname{Tr}(YX)$, so $M_n(k)$ is symmetric. The Casimir element is $\sum_{i,j}E_{ij}\otimes E_{ji}$.

**Example (truncated polynomial algebras).** $A = k[x]/(x^n)$ with basis $1, x, \dots, x^{n-1}$ and $\lambda$ the coefficient of $x^{n-1}$. Then $\lambda(x^ix^j) \neq 0$ exactly when $i+j=n-1$, and $\lambda(x^ix^j) = \lambda(x^jx^i)$, so $A$ is symmetric. The Casimir element is $\sum_{i=0}^{n-1} x^i \otimes x^{n-1-i}$, and $A$ is a local Frobenius algebra with socle spanned by $x^{n-1}$, the unique simple module being $k$.

**Example (group algebras).** $A = k[G]$ for a finite group $G$, with $\lambda$ the coefficient of the identity: $\lambda\bigl(\sum_g c_g g\bigr) = c_1$. Then $\lambda(gh) = 1$ if $gh = 1$ and $0$ otherwise, so $\lambda(gh) = \lambda(hg)$ and $k[G]$ is symmetric. The socle of $k[G]$ is spanned by the sum of the elements of a Sylow $p$-subgroup when $\operatorname{char}k = p$ divides $\lvert G\rvert$, and $k[G]$ is semisimple exactly when it is separable, that is, when $p \nmid \lvert G\rvert$.

**Example (exterior algebras).** $A = \Lambda(V)$ with $\dim_k V = n$, with $\lambda$ the coefficient of the top class $e_1\wedge\cdots\wedge e_n$. For homogeneous $u$ of degree $i$ and $v$ of degree $n-i$ the two products $uv$ and $vu$ differ by the sign $(-1)^{i(n-i)}$; that sign equals $(-1)^i$ when $n$ is even, and it equals $1$ for every $i$ when $n$ is odd. The exterior algebra is therefore symmetric in an odd number of variables and is the standard example of a Frobenius algebra that is not symmetric in an even number of variables: for $n \geq 2$ even the Nakayama automorphism is the parity automorphism

$$
\nu(u) = (-1)^{\deg u}\,u ,
$$

which is the algebra automorphism; it is not inner, because the odd part generates $\Lambda(V)$ as an algebra and a unit conjugating an odd element to its negative would have to be a scalar, while the scalars act trivially. The exterior algebra in an even number of variables is therefore the basic example of a Frobenius algebra whose Nakayama automorphism is not inner, and its sign rule is the Koszul sign rule.

**Example (semisimple algebras).** Every finite-dimensional semisimple $k$-algebra is symmetric Frobenius. If $A = \prod_i M_{n_i}(D_i)$ with the $D_i$ division algebras, take $\lambda$ to be the sum of the reduced traces of the components; each reduced trace satisfies $\operatorname{Trd}(xy) = \operatorname{Trd}(yx)$ and is non-degenerate, so their sum is a symmetric Frobenius functional. Hencedescribes a subclass of the Frobenius algebras, and the Frobenius condition is the weakening of semisimplicity that keeps the duality of the regular module but drops complete reducibility.

## The Dual and the Coalgebra Structure

### The dual as a bimodule

The isomorphism $\ell_\lambda : A \to A^*$, $a \mapsto \lambda(a\,\cdot\,)$, transports the natural $A$-bimodule structure of $A^*$ to a new bimodule structure on $A$. Explicitly, for $f \in A^*$ and $a,b \in A$,

$$
(a \cdot f)(b) = f(ba), \qquad (f\cdot a)(b) = f(ab),
$$

and writing $a \rightharpoonup x$ and $x \leftharpoonup a$ for the resulting actions on $x = \ell_\lambda^{-1}(f)$, the second is the ordinary right multiplication, $x \leftharpoonup a = xa$, while the first is the **twisted left action**

$$
a \rightharpoonup x = \nu(a)\, x .
$$

Thus the Nakayama automorphism exactly measures the failure of the transported dual action to agree with the ordinary left multiplication on $A$. When $A$ is symmetric the two structures coincide, and then the $A$-bimodule $A$ is isomorphic to its own dual as a bimodule; this is the cleanest formulation of symmetry.

### The comultiplication

Because $A^*$ is the dual of an algebra, it is a coalgebra with comultiplication the transpose of the multiplication: $\Delta = {}^t\mu : A^* \to (A\otimes_k A)^* \cong A^*\otimes_k A^*$ and counit $\varepsilon = {}^t\eta : A^* \to k$; the axioms of the coalgebra are the transposes of those of the algebra. Under the Frobenius isomorphism $A \cong A^*$ this gives $A$ the structure of a coalgebra with

$$
\Delta(a) = \sum_i a a_i \otimes a^i, \qquad \varepsilon(a) = \lambda(a),
$$

for a basis $\{a_i\}$ and its $\lambda$-dual $\{a^i\}$; the counit identity is $\sum_i \varepsilon(a a_i)a^i = \sum_i \lambda(aa_i)a^i = a$, which is the definition of the dual basis. The coalgebra is coassociative because $\Delta$ is the transpose of an associative multiplication, and its comultiplication is compatible with the left action of $A$ in the sense that $\Delta$ is a homomorphism of $A$-bimodules with respect to the twisted structure:

$$
\Delta(ab) = \sum_i ab\,a_i\otimes a^i
$$

and the twist by $\nu$ is what makes the two sides agree. The Frobenius algebra is thus simultaneously an algebra and a coalgebra; when the two structures are compatible, the result is a Hopf algebra, and this is one route to the theorem that a finite-dimensional Hopf algebra is Frobenius.

## Constructions

**Proposition (products and tensor products).** If $A$ and $B$ are Frobenius over $k$, then:

1. $A \times B$ is Frobenius, with functional $\lambda_{A\times B}(a,b) = \lambda_A(a) + \lambda_B(b)$;
2. $A \otimes_k B$ is Frobenius, with functional $\lambda_A \otimes \lambda_B$, that is, $\lambda(a\otimes b) = \lambda_A(a)\lambda_B(b)$.

If $A$ and $B$ are symmetric then so are $A\times B$ and $A\otimes_k B$. The Nakayama automorphisms multiply in the second case: $\nu_{A\otimes B} = \nu_A \otimes \nu_B$.

*Proof.* For the product, the pairing $(a,b)\cdot(a',b') \mapsto \lambda_A(aa') + \lambda_B(bb')$ is non-degenerate because a component with $\lambda_A(aa')=0$ for all $a'$ has $a=0$, and similarly for $B$; this is the direct sum of the two pairings, hence non-degenerate. For the tensor product, use bases $\{a_i\},\{b_j\}$ and their dual bases; the non-degeneracy of a tensor product of two non-degenerate pairings follows from the identity $\lambda\bigl((a\otimes b)(a'\otimes b')\bigr) = \lambda_A(aa')\lambda_B(bb')$ and the fact that a tensor product of non-degenerate pairings is non-degenerate when the factors have bases. The trace identities pass through the tensor product because $\lambda_A(aa')= \lambda_A(a'a)$ and $\lambda_B(bb')=\lambda_B(b'b)$. $\square$

**Theorem (finite-dimensional Hopf algebras are Frobenius, standard).** Every finite-dimensional Hopf algebra over a field is a Frobenius algebra; more precisely, it possesses a nonzero left integral and a nonzero right integral, and the space of left integrals is one-dimensional.

The theorem belongs; it is recorded here as the structural reason the representation theory of a finite-dimensional Hopf algebra has the same duality as that of a Frobenius algebra. The same statement with "Hopf algebra" replaced by "finite-dimensional $k$-algebra with an augmentation and a comultiplication" is false, so both structures are needed.

## Frobenius Algebras and the Symmetric Algebra

The Frobenius condition is a finiteness condition, and it is not satisfied by the polynomial algebra. For $A = k[x_1,\dots,x_n]$ there is no nonzero linear functional vanishing on no nonzero ideal on both sides, and indeed the regular module is not injective; the symmetric algebra $\operatorname{Sym}(V)$ is not a Frobenius algebra unless it is finite-dimensional, which for a nonzero $V$ never happens. What is true is that the **finite-dimensional quotients** of the symmetric algebra by sufficiently many relations are Frobenius, and they are the standard examples.

**Theorem (complete intersections, standard).** Let $f_1,\dots,f_n \in k[x_1,\dots,x_n]$ be a regular sequence and let $A = k[x_1,\dots,x_n]/(f_1,\dots,f_n)$. Then $A$ is a Frobenius algebra, and it is a symmetric Frobenius algebra when the sequence is a regular sequence of homogeneous polynomials. In the hypersurface case $n = 1$ and $A = k[x]/(f)$ with $\deg f = m$, the Frobenius functional is the coefficient of $x^{m-1}$, and $A$ is symmetric.

*Proof (sketch).* A regular sequence is a sequence whose successive quotients have the expected dimension, and the resulting algebra is a finite-dimensional **complete intersection**; the dualising module of a complete intersection is free of rank one, which is the Frobenius property. In the hypersurface case the computation is explicit: the pairing $\lambda(pq)$ with $\lambda$ the coefficient of $x^{m-1}$ is non-degenerate because for every nonzero $p$ of degree $<m$ the product $p x^{m-1-\deg p}$ has nonzero top coefficient in the monomial basis. $\square$

The connection with the symmetric algebra is that $k[x_1,\dots,x_n]/(f_1,\dots,f_n)$ is a quotient of $\operatorname{Sym}(V)$ for $V$ of dimension $n$, so the Frobenius algebras of this kind are the finite-dimensional quotients of the symmetric algebra by a regular sequence. The corresponding statement for the exterior algebra is that $\Lambda(V)$ is Frobenius with the top-degree functional, which is the anti-symmetric analogue; the two families are the commutative and the alternating edge of the same construction, and the Frobenius property is what they have in common.

## Summary

A finite-dimensional $k$-algebra $A$ is **Frobenius** when it carries a linear functional $\lambda$ whose associated pairing $(a,b) \mapsto \lambda(ab)$ is non-degenerate; equivalently $A \cong A^*$ as left (or right) $A$-modules, equivalently the regular module is injective. The **Nakayama automorphism** $\nu$ of $(A,\lambda)$ is defined by $\lambda(ab) = \lambda(b\nu(a))$, it is an algebra automorphism, and it is determined up to inner automorphisms. The algebra is **symmetric** when $\nu = \mathrm{id}$, that is, when $\lambda(ab) = \lambda(ba)$, and then $\lambda$ is a trace; matrix algebras with the trace, group algebras with the coefficient functional, truncated polynomial algebras $k[x]/(x^n)$, and all finite-dimensional semisimple algebras are symmetric, while the exterior algebra $\Lambda(V)$ is Frobenius with Nakayama automorphism the parity automorphism when $\dim V$ is even. Frobenius algebras are self-injective and quasi-Frobenius, so projectivity and injectivity of modules coincide over them; the **Casimir element** $C = \sum_i a_i\otimes a^i$ built from a basis and its $\lambda$-dual satisfies $\mu(C)=1$ and is invariant under the twisted diagonal action, and its contraction with an element gives the trace of left multiplication.

A Frobenius algebra is at once an algebra and a coalgebra, with comultiplication the transpose of the multiplication transported across $A \cong A^*$ and counit $\lambda$; the Nakayama automorphism measures the twist needed to make the two structures compatible, and this is the point of departure, where the existence of an integral makes every finite-dimensional Hopf algebra Frobenius. The Frobenius property is closed under products and tensor products, and the finite-dimensional quotients of the symmetric algebra by a regular sequence are Frobenius complete intersections, with the hypersurface $k[x]/(f)$ as the basic example; the symmetric algebra itself is not Frobenius because it is infinite-dimensional. The topological statement that a Frobenius algebra models, Poincaré duality, and the form theory that a non-degenerate pairing evokes belong to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$ | ground field |
| $A$ | finite-dimensional unital associative $k$-algebra |
| $A^* = \operatorname{Hom}_k(A,k)$ | linear dual |
| $\lambda : A \to k$ | Frobenius functional |
| $\ell_\lambda(a)(b) = \lambda(ab)$ | left dualising isomorphism $A \to A^*$ |
| $(a,b)\mapsto\lambda(ab)$ | Frobenius pairing, non-degenerate |
| $\nu$ | Nakayama automorphism, $\lambda(ab)=\lambda(b\nu(a))$ |
| symmetric | Frobenius with $\nu=\mathrm{id}$, $\lambda(ab)=\lambda(ba)$ |
| $C = \sum_i a_i\otimes a^i$ | Casimir element, $\lambda(a_i a^j)=\delta_i^j$ |
| $\mu : A\otimes_k A \to A$ | multiplication |
| $\Delta$, $\varepsilon = \lambda$ | comultiplication and counit of the dual coalgebra |
| $\iota_u(x) = uxu^{-1}$ | inner automorphism |
| $\operatorname{soc}(A)$, $J(A)$ | socle and Jacobson radical |
| $\operatorname{Tr}$, $\operatorname{Trd}$ | matrix trace, reduced trace |
| $M_n(k)$, $k[G]$, $k[x]/(x^n)$, $\Lambda(V)$ | standard Frobenius examples |
| $k[x_1,\dots,x_n]/(f_1,\dots,f_n)$ | complete intersection, Frobenius for a regular sequence |





## Further Reading

- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for Frobenius algebras, the Nakayama automorphism and quasi-Frobenius algebras.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for self-injectivity, the cogenerator property and the duality between projective and injective modules.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of finite-dimensional algebras and the role of the dualising module.
- Andrei V. Zelevinsky, *Representations of Finite Classical Groups* (Springer, 1981), for Frobenius algebras as the algebras with a duality and their applications to representations.
- David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry* (Springer, 1995), for regular sequences, complete intersections and Gorenstein rings.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the tensor algebra, the exterior algebra and the duality of finite-dimensional algebras.
- Bruce Sagan, *The Symmetric Group: Representations, Combinatorial Algorithms, and Symmetric Functions* (Springer, 2nd ed. 2001), for the symmetric group algebra as a symmetric Frobenius algebra.
