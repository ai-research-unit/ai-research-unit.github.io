
# __Split-Quaternion Representations__

## Introduction

This article classifies the finite-dimensional real representations of the split-quaternion algebra, proves that the algebra is semisimple and has exactly one irreducible representation up to equivalence, computes its representation ring, relates the algebra's representations to the representations of the Lie algebra $\mathfrak{sl}_2(\mathbb{R})$ and to the double cover of the Lorentz group of signature $(2,1)$, and compares the result with the quaternion case.

The split-quaternion algebra, its matrix model $\Phi$, its idempotents $u_\pm$, its vector subspace $V$ and its simplicity are assumed from *Split-Quaternion Algebra*. The defining module and the irreducibility of the defining representation are assumed from *Split-Quaternion Matrix Representations*, §*The Defining Module*. The matrix algebra $M_2(\mathbb{R})$, its matrix units and its modules are assumed from *Matrix Algebras*; the highest-weight classification of the finite-dimensional $\mathfrak{sl}_2$-modules is assumed from *Representations of Lie Algebras*, and the tensor conventions of this category for the comparison come from *Quaternion Representations*. The double cover is stated here and proved in *Split-Quaternion Rotations and the Lorentz Group*; the homogeneous spaces are treated in *Split-Quaternions and Hyperbolic Geometry*. Nothing physical is invoked.

## Representations of $\mathbb{H}_{\mathrm{s}}$

### Definition

A **representation** of $\mathbb{H}_{\mathrm{s}}$ is a real vector space $V$ with a bilinear map $\mathbb{H}_{\mathrm{s}} \times V \to V$, $(x,v) \mapsto x \cdot v$, such that

$$
x \cdot (y \cdot v) = (xy) \cdot v, \qquad 1 \cdot v = v
$$

for all $x,y \in \mathbb{H}_{\mathrm{s}}$ and $v \in V$. Equivalently, a representation is a unital algebra homomorphism $\rho : \mathbb{H}_{\mathrm{s}} \to \operatorname{End}_{\mathbb{R}}(V)$. A **module** is a representation; the two words are used interchangeably, and a module is **simple** or **irreducible** when it has no submodule other than $0$ and itself. The representation is **finite-dimensional** when $V$ is.

By (*Split-Quaternion Algebra*, §*The Centre and Simplicity*) the algebra is simple and non-commutative, so the kernel of a unital homomorphism $\rho$ is a two-sided ideal, hence $0$ or all of $\mathbb{H}_{\mathrm{s}}$; it is not all, because $\rho(1) = \mathrm{id}$. Every representation of a nonzero module is therefore faithful.

### The Regular Representation

The **left regular representation** is the algebra acting on itself by left multiplication:

$$
\lambda(x) y = x y .
$$

It is the representation on the four-dimensional space $\mathbb{H}_{\mathrm{s}}$, and its image is the four-dimensional subalgebra of $\operatorname{End}_{\mathbb{R}}(\mathbb{H}_{\mathrm{s}})$ isomorphic to $\mathbb{H}_{\mathrm{s}}$. The **right regular representation** $\rho(x) y = yx$ is an algebra anti-homomorphism, and composing it with the conjugation makes it a left representation isomorphic to the left regular one, exactly as in the quaternion case of *Quaternion Representations*, §*The Left and Right Regular Representations*.

### The Idempotent Decomposition

The idempotents give a decomposition of every representation.

**Theorem (The Idempotent Splitting).** Let $V$ be a representation and let $u_\pm = \tfrac12(1 \pm e_2)$ be the non-central idempotents. Then

$$
V = u_+ V \oplus u_- V
$$

as real vector spaces. In the case of the simple module the summands are the eigenspaces of $\Phi(e_2)$ on $\mathbb{R}^2$, the lines $\mathbb{R}(1,1)$ and $\mathbb{R}(1,-1)$, and in the algebra the corresponding objects are the minimal ideals $\mathbb{H}_{\mathrm{s}}u_\pm$.

**Proof.** The identities $u_+ + u_- = 1$ and $u_+u_- = 0$ give $v = u_+v + u_-v$ for every $v$, so the sum is all of $V$; and if $v \in u_+V \cap u_-V$, say $v = u_+v'$, then $v = u_+v$ because $u_+^2 = u_+$, while $v = u_-v''$ gives $u_+v = u_+u_-v'' = 0$; hence $v = 0$ and the sum is direct. Both summands are invariant under $u_+$ and $u_-$, since $u_\pm^2 = u_\pm$ and $u_+u_- = 0$. For the last statement, $\Phi(u_+)$ and $\Phi(u_-)$ are the rank-one projections of (*Split-Quaternion Matrix Representations*, §*The Image as a Linear Subspace*), with images $\mathbb{R}(1,1)$ and $\mathbb{R}(1,-1)$. $\square$

## Classification

**Theorem (The Classification of Representations).** Let $V$ be a finite-dimensional representation of $\mathbb{H}_{\mathrm{s}}$, and let $S = \mathbb{R}^2$ be the defining module with the action $x \cdot v = \Phi(x)v$. Then there is a unique integer $d \geq 0$ with

$$
V \cong S^{\oplus d},
$$

so $\dim_{\mathbb{R}} V = 2d$, every module has even dimension, and the isomorphism class of $V$ is determined by its dimension alone.

**Proof.** Let $e = E_{11} = \Phi\big(\tfrac12(1 - e_3)\big)$ and $f = E_{22} = 1 - e$ be the two complementary rank-one idempotents. Since $e + f = 1$, every $v$ is $ev + fv$ with $ev \in eV$ and $fv \in fV$, so $V = eV + fV$; applying $e$ to a relation $v_1 + v_2 = 0$ with $v_1 \in eV$ gives $v_1 = 0$, so the sum is direct. The maps

$$
eV \longrightarrow fV, \quad w \longmapsto E_{21}w, \qquad fV \longrightarrow eV, \quad z \longmapsto E_{12}z
$$

are mutually inverse, because $E_{12}E_{21} = E_{11} = e$ and $E_{21}E_{12} = E_{22} = f$. Choose a basis $w_1,\dots,w_d$ of $eV$; then $E_{21}w_1,\dots,E_{21}w_d$ is a basis of $fV$, and the two families together form a basis of $V$.

Now define, for $s = (s_1,s_2) \in S = \mathbb{R}^2$, the matrix $E(s)$ whose first column is $s$ and whose second column is $0$, and let

$$
\varphi : S^{\oplus d} \longrightarrow V, \qquad \varphi(s^{(1)}, \dots, s^{(d)}) = \sum_{k=1}^{d} E(s^{(k)}) w_k .
$$

The map is $M_2(\mathbb{R})$-linear: $E(As) = A E(s)$ for every matrix $A$, because both sides have first column $As$ and second column $0$. It carries the standard basis vectors of the $k$-th copy of $S$ to $w_k$ and $E_{21}w_k$, since $E(1,0) = E_{11}$ and $E(0,1) = E_{21}$, so it is bijective. Hence $V \cong S^{\oplus d}$ as a module. $\square$

**Corollary (No Odd-Dimensional Representations).** There is no representation of dimension $1$, and therefore no one-dimensional representation exists in this category at all. In particular the algebra has no **trivial** representation: a unital homomorphism $\mathbb{H}_{\mathrm{s}} \to \mathbb{R}$ would be an algebra homomorphism from a non-commutative simple algebra onto a commutative field, and its kernel would be a proper two-sided ideal.

**Proof.** The dimension of $S^{\oplus d}$ is $2d$, and the algebra is non-commutative, so $M_1(\mathbb{R})$ is excluded. $\square$

## Semisimplicity and the Irreducible Representation

**Theorem (Semisimplicity).** The algebra $\mathbb{H}_{\mathrm{s}}$ is semisimple: every finite-dimensional representation is a direct sum of simple representations, and every submodule of a representation is a direct summand.

**Proof.** The classification gives $V \cong S^{\oplus d}$, and $S$ is simple by (*Split-Quaternion Matrix Representations*, §*The Defining Module*); hence $V$ is a direct sum of simples. For a submodule $W \subseteq V$, the standard argument of complete reducibility applies: the inclusion splits because $W$, being a submodule of a semisimple module, is a direct sum of simples and the remaining simples of $V$ provide a complement; equivalently, $\mathbb{H}_{\mathrm{s}} \cong M_2(\mathbb{R})$ is a matrix algebra, and matrix algebras over fields are semisimple by *Matrix Algebras*. $\square$

**Theorem (The Unique Irreducible Representation).** Up to isomorphism there is exactly one simple representation of $\mathbb{H}_{\mathrm{s}}$, namely $S = \mathbb{R}^2$ with the action of the defining representation. It has dimension $2$.

**Proof.** Every nonzero module is $S^{\oplus d}$ with $d \geq 1$, and such a module is simple exactly when $d = 1$, since $d \geq 2$ exhibits a proper direct summand. The dimension of $S$ is $2$. $\square$

**Theorem (Schur's Lemma and the Endomorphism Ring).** The endomorphism ring of the simple module is $\mathbb{R}$:

$$
\operatorname{End}_{\mathbb{H}_{\mathrm{s}}}(S) = \mathbb{R} \cdot \mathrm{id} .
$$

**Proof.** Schur's lemma gives that every $M_2(\mathbb{R})$-linear endomorphism of $S = \mathbb{R}^2$ is scalar, since a matrix commuting with every matrix is a scalar matrix by (*Matrix Algebras*, §*Ideals and Simplicity*). $\square$

The endomorphism ring of the simple module being $\mathbb{R}$ rather than a division algebra over $\mathbb{R}$ larger than $\mathbb{R}$ is the algebraic expression of the fact that the algebra is **split**: by Schur's lemma the endomorphism ring of a simple module is a division algebra, and here that division algebra is $\mathbb{R}$ itself. In the quaternion case it is $\mathbb{H}$, by *Quaternion Representations*, §*Schur's Lemma*, and the two situations differ in exactly this invariant.

## The Representation Ring

**Definition.** The **representation ring** $R(\mathbb{H}_{\mathrm{s}})$ is the Grothendieck ring of finite-dimensional representations, with addition from direct sums and multiplication from tensor products, the algebra acting on the first factor of a tensor product.

**Theorem (The Additive Group).** As an abelian group,

$$
R(\mathbb{H}_{\mathrm{s}}) \cong \mathbb{Z},
$$

freely generated by the class $[S]$ of the simple module. Indeed the classification gives $[S^{\oplus d}] = d\,[S]$.

**Proof.** The isomorphism classes of finite-dimensional representations are the classes of $S^{\oplus d}$ for $d \geq 0$, and direct sum corresponds to addition of the integers $d$. $\square$

**Theorem (The Ring Structure).** The product in $R(\mathbb{H}_{\mathrm{s}})$ satisfies

$$
[S^{\oplus a}] \cdot [S^{\oplus b}] = [S^{\oplus 2ab}],
$$

so $R(\mathbb{H}_{\mathrm{s}})$ is $\mathbb{Z}$ with the multiplication $m \cdot n = 2mn$. This multiplication is associative and commutative, and it has no identity element: $2 e n = n$ for all $n$ would force $e = \tfrac12$, which is not an integer.

**Proof.** Let the algebra act on the first factor of the tensor product. Then

$$
S \otimes_{\mathbb{R}} S \cong \mathbb{R}^4 \cong S^{\oplus 2},
$$

because $S \otimes S$ has dimension $4$ and every four-dimensional module is $S^{\oplus 2}$ by the classification; the tensor product of $S^{\oplus a}$ with $S^{\oplus b}$ is therefore $S^{\oplus 2ab}$. A ring with product $m\cdot n = 2mn$ on $\mathbb{Z}$ is associative and commutative, and an identity $e$ would satisfy $2en = n$ for all $n$, in particular $2e = 1$. $\square$

The absence of an identity is the same phenomenon as in the quaternion case, where the product is $m\cdot n = 4mn$ by *Quaternion Representations*, §*The Representation Ring*; the factor is the dimension of the simple module, $2$ here and $4$ there. The tensor of representations is not a ring with unit because the algebra is not a bialgebra, and no trivial representation exists to serve as the unit.

## The Category of Representations

**Theorem (Morita Triviality).** The category of finite-dimensional representations of $\mathbb{H}_{\mathrm{s}}$ is equivalent, as an abelian category, to the category of finite-dimensional real vector spaces:

$$
\mathbb{H}_{\mathrm{s}}\text{-}\mathbf{mod} \;\simeq\; \mathbf{Vect}_{\mathbb{R}} .
$$

The equivalence sends a vector space $W$ to $S \otimes_{\mathbb{R}} W$ and a module $V$ to $\operatorname{Hom}_{\mathbb{H}_{\mathrm{s}}}(S, V)$. Under it the simple module corresponds to $\mathbb{R}$, direct sums to direct sums, and tensor products to tensor products with the algebra acting on the first factor.

**Proof.** This is the standard equivalence of module categories induced by $M_2(\mathbb{R}) = \operatorname{End}_{\mathbb{R}}(\mathbb{R}^2)$, treated in *Matrix Algebras*: a module $V$ is recovered from $\operatorname{Hom}_{\mathbb{H}_{\mathrm{s}}}(S,V) \otimes_{\mathbb{R}} S$ by evaluation, and the classification theorem is precisely the statement that the evaluation map is an isomorphism. $\square$

**Corollary (Finite-Dimensional Representations Are Free).** Every finite-dimensional representation is a free module of rank $d$ over the algebra, in the sense of the isomorphism $V \cong S^{\oplus d}$, and the rank is half the real dimension.

## The Relation to the Representations of $\mathfrak{sl}_2(\mathbb{R})$

The vector subspace $V$, with the commutator bracket, is a Lie algebra isomorphic to $\mathfrak{sl}_2(\mathbb{R})$, by (*Split-Quaternion Algebra*, §*The Lie Algebra Structure*). Every representation of the associative algebra is a representation of this Lie algebra: the forgetful functor

$$
\mathbb{H}_{\mathrm{s}}\text{-}\mathbf{mod} \longrightarrow \mathfrak{sl}_2(\mathbb{R})\text{-}\mathbf{mod}
$$

sends a module $V$ to the same space with the action $u \cdot v = [u, v]$ extended bilinearly, and it is exact and faithful. The two theories are not the same, and the difference is sharp.

**Theorem (The Lie Irreducibles Do Not Lift).** The finite-dimensional irreducible $\mathfrak{sl}_2(\mathbb{R})$-modules are the symmetric powers $\operatorname{Sym}^n(S)$ of the standard module, of dimension $n+1$ for $n \geq 0$, by *Representations of Lie Algebras*, §*The Example of $\mathfrak{sl}(2)$*. Among them exactly one carries the structure of a representation of the associative algebra $\mathbb{H}_{\mathrm{s}}$, namely $\operatorname{Sym}^1(S) = S$. Consequently the representation theory of the Lie algebra is strictly larger than that of the algebra.

**Proof.** Every $\mathbb{H}_{\mathrm{s}}$-module is isomorphic to $S^{\oplus d}$ by the classification, so every irreducible $\mathbb{H}_{\mathrm{s}}$-module has dimension $2$. If $\operatorname{Sym}^n(S)$ carried an $\mathbb{H}_{\mathrm{s}}$-module structure whose associated Lie action is the given one, then as an $\mathbb{H}_{\mathrm{s}}$-module it would be $S^{\oplus d}$ with $2d = n+1$, so $n$ would be odd and $d = (n+1)/2$. The submodules of $\operatorname{Sym}^n(S)$ over the associative algebra are submodules over the Lie algebra, since the Lie action is derived from the associative one; so if $d \geq 2$ the Lie module would have a proper nonzero submodule, contradicting its irreducibility. Hence $d = 1$, that is $n = 1$, and then $\operatorname{Sym}^1(S) = S$ is indeed a module. $\square$

**Corollary (The Trivial Lie Module Does Not Lift).** The one-dimensional trivial $\mathfrak{sl}_2(\mathbb{R})$-module is not a representation of $\mathbb{H}_{\mathrm{s}}$, in accordance with the corollary of the classification that the algebra has no one-dimensional representation.

**Remark.** The relation between the two representation theories is the usual one for an enveloping algebra: $\mathbb{H}_{\mathrm{s}}$ is the quotient of the universal enveloping algebra $U(\mathfrak{sl}_2(\mathbb{R}))$ by the annihilator of its two-dimensional irreducible module, so a $U(\mathfrak{sl}_2)$-module descends to $\mathbb{H}_{\mathrm{s}}$ exactly when it is a sum of copies of that module. The enveloping algebra itself is infinite-dimensional, by *Universal Enveloping Algebras*, and its representation theory is strictly richer.

## The Double Cover of the Lorentz Group of Signature $(2,1)$

**Theorem (The Double Cover).** The group of norm-one split-quaternions is

$$
U = \{x \in \mathbb{H}_{\mathrm{s}} : N(x) = 1\} \cong \mathrm{SL}_2(\mathbb{R}),
$$

and the adjoint action $x \mapsto (u \mapsto uxu^{-1})$ on the vector subspace $V$ defines a surjective group homomorphism

$$
\mathrm{SL}_2(\mathbb{R}) \longrightarrow \mathrm{SO}^{+}(2,1)
$$

onto the identity component of the Lorentz group of the signature-$(2,1)$ form, with kernel $\{\pm 1\}$; the map is therefore a double cover.

**Proof.** The identification of $U$ with $\mathrm{SL}_2(\mathbb{R})$ is (*Split-Quaternion Norm and Invertibility*, §*The Group of Units*); the adjoint action preserves the form $N$ on $V$ by multiplicativity, and the remaining statements are proved in *Split-Quaternion Rotations and the Lorentz Group*, §*The Double Cover of $\mathrm{SO}^{+}(2,1)$*. $\square$

**Corollary (Group Representations and Algebra Representations Are Different).** The representations of the group $\mathrm{SL}_2(\mathbb{R})$ and the representations of the algebra $\mathbb{H}_{\mathrm{s}}$ are not the same objects: the algebra has a single finite-dimensional irreducible module, whereas $\mathrm{SL}_2(\mathbb{R})$ has infinite-dimensional irreducible unitary representations and its finite-dimensional representations are the symmetric powers of the standard two-dimensional one. The algebra's module $S$ exponentiates to the standard representation of the group, which is the first member of the group's family and the only member that also carries an algebra action by the preceding theorem.

**Proof.** The finite-dimensional representations of $\mathrm{SL}_2(\mathbb{R})$ are the symmetric powers of $S$ by *Representations of Lie Algebras*, §*The Example of $\mathfrak{sl}(2)$*, applied to the Lie algebra; by the preceding theorem only the first of them is a module for the associative algebra. $\square$

## Comparison with the Quaternion Case

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| algebra | division | $M_2(\mathbb{R})$, simple with zero divisors |
| simple module | $\mathbb{H}$ itself, dimension $4$ | $S = \mathbb{R}^2$, dimension $2$ |
| number of simples | one | one |
| general module | $\mathbb{H}^{\oplus d}$, dimension $4d$ | $S^{\oplus d}$, dimension $2d$ |
| endomorphism ring of the simple | $\mathbb{H}$ | $\mathbb{R}$ |
| representation ring | $\mathbb{Z}$, product $m\cdot n = 4mn$ | $\mathbb{Z}$, product $m\cdot n = 2mn$ |
| trivial representation | none | none |
| module category | free modules over a division algebra | equivalent to $\mathbf{Vect}_{\mathbb{R}}$ |

The quaternion column is that of *Quaternion Representations*; the two theories have the same shape, one simple module, free modules, and a representation ring without identity, and they differ in the dimension of the simple module and in the endomorphism ring, which measures how far the algebra is from being split. In both cases there is no one-dimensional representation, since a unital homomorphism from a simple non-commutative algebra to a field would have a proper kernel.

## Summary

A representation of the split-quaternion algebra is a module over $M_2(\mathbb{R})$. The algebra is simple and semisimple; every finite-dimensional representation is isomorphic to a direct sum of copies of the single simple module $S = \mathbb{R}^2$, so the dimension of a representation is even and determines it up to isomorphism, and there is no odd-dimensional or one-dimensional representation.

The endomorphism ring of the simple module is $\mathbb{R}$, by Schur's lemma, so the algebra is split. The representation ring is $\mathbb{Z}$ with the product $m \cdot n = 2mn$, generated by the class of $S$; it has no identity element, because the algebra is not a bialgebra and has no trivial representation to serve as a unit. The category of finite-dimensional representations is equivalent to the category of finite-dimensional real vector spaces, so every module is free.

The Lie algebra $\mathfrak{sl}_2(\mathbb{R}) = V$ with the commutator has a strictly larger representation theory: its finite-dimensional irreducibles are the symmetric powers $\operatorname{Sym}^n(S)$ of dimension $n+1$, and only $\operatorname{Sym}^1(S) = S$ carries the structure of an associative-algebra module. The norm-one group acts by conjugation on the vector subspace with kernel $\{\pm 1\}$, giving the double cover $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$; the representations of that group are not the representations of the algebra. In the quaternion case the single simple module has dimension $4$, its endomorphism ring is $\mathbb{H}$, and the representation ring has product $m\cdot n = 4mn$; otherwise the shape is the same.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| representation, module | a real vector space with an action of $\mathbb{H}_{\mathrm{s}}$ | this article |
| simple, irreducible | a module with no nontrivial submodule | this article |
| $S = \mathbb{R}^2$ | the unique simple module, of dimension $2$ | *Split-Quaternion Matrix Representations* |
| $S^{\oplus d}$ | the general finite-dimensional representation | this article |
| $\lambda$, $\rho$ | the left and right regular representations | this article |
| $u_\pm$ | the non-central idempotents and their splitting | *Split-Quaternion Algebra* |
| $\operatorname{End}_{\mathbb{H}_{\mathrm{s}}}(S) = \mathbb{R}$ | Schur's lemma; the algebra is split | this article |
| $R(\mathbb{H}_{\mathrm{s}}) \cong \mathbb{Z}$ | the representation ring, product $m\cdot n = 2mn$ | this article |
| $\mathbb{H}_{\mathrm{s}}\text{-}\mathbf{mod} \simeq \mathbf{Vect}_{\mathbb{R}}$ | Morita equivalence | this article |
| $\operatorname{Sym}^n(S)$ | the irreducible $\mathfrak{sl}_2(\mathbb{R})$-modules | *Representations of Lie Algebras* |
| $U \cong \mathrm{SL}_2(\mathbb{R})$ | the norm-one group | *Split-Quaternion Norm and Invertibility* |
| $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$ | the double cover | *Split-Quaternion Rotations and the Lorentz Group* |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for semisimple algebras, matrix algebras and the Morita equivalence between modules over $M_n(k)$ and vector spaces.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for Schur's lemma, the endomorphism ring of a simple module and the density theorem.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the highest-weight classification of the $\mathfrak{sl}_2$-modules and the symmetric powers.
- Serge Lang, *$\mathrm{SL}_2(\mathbb{R})$* (Addison-Wesley, 1975), for the group $\mathrm{SL}_2(\mathbb{R})$, its double cover and the comparison between the group and the algebra.
