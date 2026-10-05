# __Unitary Endomorphisms__

## Introduction

The endomorphisms that preserve a non-degenerate reflexive pairing form a group, the **unitary group** of the pairing, and its algebraic structure is read off the involution that the pairing defines on the endomorphism algebra: the group is the set of $A$ with $A^{*}A=1$, its centre consists of the scalars of the involution's fixed field that have the appropriate multiplier, its determinant is constrained according to the symmetry of the pairing, and its infinitesimal structure is the space of skew-adjoint operators, with the self-adjoint operators forming the complementary Jordan system. This article treats the group, its centre and determinant, the self-adjoint and skew-adjoint operators, and the bracket and anticommutator that organise them.

The unitary elements as a set, the involution they belong to and the preservation criterion are *Involutions of the Endomorphism Algebra*; the adjoint of a single endomorphism is *The Adjoint of an Endomorphism*; this article assumes both and treats the group and the infinitesimal structure. The classification of the groups by the symmetry of the pairing, the orthogonal, the symplectic and the unitary families, and their generation and simplicity, are the business of *Symmetric Bilinear Algebras* and *Anti-symmetric Bilinear Algebras*, later in this Part; the Lie algebra as a structure is *Lie Algebras* and the Jordan algebra is *Jordan Algebras*, also later in this Part, and both are named only as forward references. The forms and the analysis on them are *Hilbert Algebras*, Part II.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, and $B$ is a non-degenerate reflexive pairing with involution $\varsigma$ of the sesquilinear case and sign $\varepsilon$ of the bilinear case. The adjoint is $A^{*}$, and $E^{\pm}$ are the self-adjoint and skew-adjoint parts.

## The Unitary Group

**Definition.** The **unitary group** of $B$ is

$$
U(V,B) = \{A \in E : A^{*}A = AA^{*} = \mathrm{id}_V\} = \{A \in \operatorname{GL}(V) : B(Ax,Ay) = B(x,y) \ \forall x,y\} .
$$

**Proposition.** $U(V,B)$ is a subgroup of $\operatorname{GL}(V)$, and it is exactly the stabiliser of $B$ under the action $A \cdot B = B \circ (A\times A)$ of $\operatorname{GL}(V)$ on the pairings.

**Proof.** The equality of the two descriptions is the preservation criterion of *Involutions of the Endomorphism Algebra*; the product of two unitaries is unitary because $(AB)^{*}AB = B^{*}A^{*}AB = B^{*}B = \mathrm{id}$, and the identity is unitary. The stabiliser statement is the definition of the action.

**Proposition (the centre).** The centre of $U(V,B)$ is the set of scalars $\lambda\,\mathrm{id}_V$ with $\varsigma(\lambda)\lambda = 1$, a subgroup of $F^{\times}$.

**Proof.** A scalar is unitary exactly when $\varsigma(\lambda)\lambda=1$, and it commutes with everything; conversely, a unitary commuting with all unitaries is a scalar by the computation of the centre of $\operatorname{GL}(V)$, in *The General Linear Group*. That a central element of $U(V,B)$ is a scalar follows from the same computation, the unitary group being a subgroup of the general linear group with the same conjugation orbits in the relevant cases.

**Proposition (the determinant).** In the bilinear symmetric case every $A \in U(V,B)$ has $\det(A)^{2}=1$, so $\det(A) = \pm1$ and the determinant is a homomorphism $U(V,B) \to \{\pm1\}$; in the antisymmetric case $\det(A) = 1$ and the determinant is trivial.

**Proof.** $\det(A^{*})=\det(A)$ and $\det(A^{*}A)=\det(A)^{2}=1$ in the symmetric case; the antisymmetric case is the standard determinant-one property of the symplectic group, quoted from the theory of the classical groups.

**Example.** For the standard pairing on $F^n$, $U(V,B)$ is the orthogonal group: the matrices with $A^{\mathsf{T}}A = I$, of determinant $\pm1$. For the pairing $B(x,y) = x_1y_1 - x_2y_2$ on $F^2$, the unitaries are the matrices preserving the two lines spanned by the coordinate vectors together with the diagonal and antidiagonal involutions, and the determinant is $\pm1$.

## The Self-Adjoint and Skew-Adjoint Operators

**Definition.** The bracket and the anticommutator of two endomorphisms are

$$
[X,Y] = XY - YX, \qquad \{X,Y\} = XY + YX .
$$

**Proposition (the bracket table).** With $E^{\pm} = \{X : X^{*} = \pm X\}$,

$$
[E^{+},E^{+}] \subseteq E^{-}, \qquad [E^{+},E^{-}] \subseteq E^{+}, \qquad [E^{-},E^{-}] \subseteq E^{-},
$$

so the skew-adjoint operators form a Lie subalgebra of $E$ under the bracket, and the self-adjoint operators form a subspace closed under the anticommutator, $\{E^{+},E^{+}\} \subseteq E^{+}$.

**Proof.** For $X,Y$ and the involution, $(XY)^{*} = Y^{*}X^{*}$; hence $(XY - YX)^{*} = Y^{*}X^{*} - X^{*}Y^{*}$. If $X^{*}=\alpha X$ and $Y^{*}=\beta Y$ with $\alpha,\beta \in \{\pm1\}$ then $(XY-YX)^{*} = \beta\alpha XY - \alpha\beta YX = \alpha\beta(XY-YX)$, giving the three inclusions according to the signs; the anticommutator computation is $(XY+YX)^{*} = \beta\alpha XY + \alpha\beta YX = \alpha\beta(XY+YX)$, which is self-adjoint when $\alpha\beta=1$, that is for two elements of the same parity, giving $\{E^{+},E^{+}\}\subseteq E^{+}$ and $\{E^{-},E^{-}\}\subseteq E^{+}$.

**Proposition (the exponential bridge).** For $X \in E$ the series $\exp(X) = \sum_{j\ge0}X^{j}/j!$ is a unitary exactly when $X$ is skew-adjoint, and it is then an element of $U(V,B)$ of determinant one; on the skew-adjoint part the exponential is a bijection with a neighbourhood of the identity in the classical topology of the field, and the bracket is its infinitesimal law.

**Proof.** For nilpotent or formal $X$ one has $\exp(X)^{*} = \exp(X^{*})$ and hence $\exp(X)^{*}\exp(X) = \exp(X^{*}+X)$, which is the identity exactly when $X^{*}=-X$ and the series converges appropriately; the determinant statement is $\det\exp(X) = \exp(\operatorname{tr}X)$ and $\operatorname{tr}X^{*} = \varsigma(\operatorname{tr}X)$, vanishing on the skew-adjoint part. The statements about the bijection and its domain are the theory of the exponential map, *Lie Algebras* and the analysis of *Hilbert Algebras*.

**Remark (the two names for the same space).** In the sesquilinear case over a field with a conjugation, the skew-adjoint operators are $i$ times the self-adjoint ones, and the space of self-adjoint operators is the standard real form of the Lie algebra; the self-adjoint operators with the anticommutator form a **Jordan algebra**, whose structure is *Jordan Algebras*, and the skew-adjoint operators with the bracket form the Lie algebra of $U(V,B)$, whose structure is *Lie Algebras*. Both are named and deferred; the article uses only the bracket table and the exponential criterion.

## Summary

A non-degenerate reflexive pairing $B$ on a finite-dimensional space defines the unitary group $U(V,B)$, the subgroup of $\operatorname{GL}(V)$ of the endomorphisms with $A^{*}A = AA^{*} = \mathrm{id}$, which is exactly the stabiliser of $B$. Its centre is the group of scalars $\lambda$ with $\varsigma(\lambda)\lambda=1$, its determinant is constrained: $\det(A)^{2}=1$ in the symmetric bilinear case and $\det(A)=1$ in the antisymmetric case. The self-adjoint and skew-adjoint parts $E^{\pm}$ satisfy the bracket table $[E^{+},E^{+}]\subseteq E^{-}$, $[E^{+},E^{-}]\subseteq E^{+}$, $[E^{-},E^{-}]\subseteq E^{-}$ and $\{E^{+},E^{+}\}\subseteq E^{+}$, so the skew-adjoint operators form the Lie algebra of the unitary group under the bracket and the self-adjoint operators form a Jordan system under the anticommutator; the exponential of a skew-adjoint operator is unitary with determinant one. The classification of the classical groups and the analysis on the forms are the subjects of the symmetric and antisymmetric categories of this Part and of *Hilbert Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B$, $\varsigma$, $\varepsilon$ | the pairing, the field involution, the reflexive sign |
| $E=\operatorname{End}_F(V)$ | the endomorphism algebra |
| $A^{*}$ | the adjoint element |
| $U(V,B)$ | the unitary group, $A^{*}A=AA^{*}=\mathrm{id}$ |
| $E^{+},E^{-}$ | self-adjoint and skew-adjoint parts |
| $[X,Y]=XY-YX$ | the commutator (bracket) |
| $\{X,Y\}=XY+YX$ | the anticommutator |
| $\exp(X)=\sum_j X^{j}/j!$ | the exponential, unitary for $X$ skew-adjoint |
| $\det:\ U(V,B)\to\{\pm1\}$ | the determinant in the symmetric case |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the unitary group of a sesquilinear pairing.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the classical groups and their determinants.
- Larry C. Grove, *Classical Groups and Geometric Algebra* (American Mathematical Society, 2002), for the orthogonal, symplectic and unitary groups.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for the Lie algebra of the classical groups and the exponential.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the orthogonal and symplectic groups and the determinant.
