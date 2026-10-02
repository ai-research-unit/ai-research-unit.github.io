
# __Hermitian Forms on a Lie Algebra__

## Introduction

A **Hermitian form** on a complex Lie algebra is a sesquilinear form that is conjugate-symmetric; it is **invariant** when the adjoint action is skew with respect to it, and the invariance is the single condition that makes the form the infinitesimal counterpart of a unitary structure. A positive definite invariant Hermitian form turns the Lie algebra into a space whose adjoint operators are skew-adjoint, so its representations by skew-adjoint operators are the unitary ones; and the existence of such a form is the compactness of the algebra. The form is thus the bridge from the algebra to its unitary representations, and it is the object from which the star of the enveloping algebra and the Casimir element are read.

This article treats Hermitian forms on a Lie algebra, their invariance and the unitary representations they define. It is the first article of the `- * Operator Theory` group of the category; the real forms and the compact real form are *Real Forms of a Complex Lie Group and the Cartan Involution*, the Cartan decomposition and the compact type are *The Cartan Decomposition and the Cartan Involution*, the star structure of the enveloping algebra is *The Involution on the Enveloping Algebra of a Lie Group*, and the operators built from the adjoint with respect to the form are *Unitary Representations and the Adjoint Operator*, *The Signed Adjoint Sandwich on a Lie Algebra*, *The Signed Adjoint of the Reflection on a Lie Algebra*, *The Signed Adjoint of the Left Multiplication on a Lie Algebra* and *The Graded Adjoint Action on a Module over a Lie Algebra*, all below in this group.

The article assumes the complex and the real Lie algebra, the Killing form and the semisimple structure from *Structure of Lie Algebras*, the compact real form and the Cartan involution from *Real Forms of a Complex Lie Group and the Cartan Involution*, the Hermitian form on a complex vector space and its definite and indefinite cases from *Involutive Linear Spaces* and *Self-Adjoint Operators and the Spectral Theorem*, the star of an involutive algebra from *Involutive Rings*, and the Hilbert space and the adjoint operator from *Hilbert Spaces* and *Bounded Operators on a Hilbert Space*. The unitary representations are cited from *Unitary Representations of a Lie Group*; the analytic theory of their decomposition is not developed here.

## Hermitian Forms

### The Definition

**Definition.** Let $\mathrm{G}$ be a complex Lie algebra. A **Hermitian form** on $\mathrm{G}$ is a map $H : \mathrm{G}\times\mathrm{G}\to\mathbb{C}$ that is linear in the first argument, conjugate-linear in the second, and conjugate-symmetric,

$$
H(\lambda X + \mu Y, Z) = \lambda H(X,Z) + \mu H(Y,Z), \qquad H(X,Y) = \overline{H(Y,X)} ,
$$

so that in particular $H(X,X)\in\mathbb{R}$. It is **non-degenerate** when $H(X,Y) = 0$ for all $Y$ forces $X = 0$, **positive definite** when $H(X,X) > 0$ for $X\neq0$, and **indefinite** otherwise.

**Definition.** The **associated antilinear map** is

$$
\flat : \mathrm{G}\to\mathrm{G}^{*}, \qquad \flat(X)(Y) = H(X,Y) ,
$$

which is conjugate-linear and is a bijection exactly when $H$ is non-degenerate; a Hermitian form is then the same datum as a non-degenerate Hermitian form on $\mathrm{G}^{*}$ by the inverse of $\flat$.

**Proposition.** The non-degenerate Hermitian forms on $\mathrm{G}$ are classified by their signature: over a complex vector space there is a basis in which $H$ has the form

$$
H(X,Y) = \sum_{i=1}^{p}X_i\overline{Y_i} - \sum_{j=p+1}^{n}X_j\overline{Y_j} ,
$$

and the absolute value of the signature is the only invariant of the form up to linear isomorphism.

*Proof.* This is the diagonalisation of a Hermitian form, which is the spectral theorem of *Self-Adjoint Operators and the Spectral Theorem*; the change of basis preserves the Hermitian character and the number of positive and negative squares is invariant by Sylvester's law.

### The Invariance

**Definition.** A Hermitian form $H$ is **invariant** under the bracket when

$$
H([X,Y], Z) = H(X,[Y,Z]) \qquad (X,Y,Z\in\mathrm{G}) .
$$

**Proposition.** The two conditions

$$
H([X,Y],Z) = H(X,[Y,Z]), \qquad H([X,Y],Z) + H(Y,[X,Z]) = 0
$$

are equivalent, and under either of them the adjoint operator of $\operatorname{ad}_X$ with respect to $H$ is $-\operatorname{ad}_X$,

$$
H(\operatorname{ad}_X Y, Z) = -H(Y,\operatorname{ad}_X Z) ,
$$

so the adjoint operators of the algebra are skew-Hermitian.

*Proof.* The bracket is alternating, so $H([X,Y],Z) = -H([Y,X],Z)$; substituting the first identity and using conjugate symmetry gives the second, and conversely. Reading either identity as the definition of the adjoint of $\operatorname{ad}_X$ gives the skew-Hermitian statement.

## The Unitary Structure

### The Definite Case

**Theorem.** Let $\mathrm{G}$ be a complex Lie algebra with a positive definite invariant Hermitian form $H$. Then the real Lie algebra $\mathrm{G}_{\mathbb{R}}$ of the Hermitian operators of $H$ is compact, its adjoint operators are skew-Hermitian, and $H$ is the negative of a compact form; conversely a compact real form $\mathrm{K}$ of a complex semisimple Lie algebra carries a positive definite invariant form, and the algebra is identified with a space of skew-Hermitian operators.

*Proof.* The algebra of the skew-Hermitian operators of a positive definite Hermitian form on $\mathbb{C}^n$ is $\mathrm{u}(n)$, which is compact, and the invariance of $H$ says exactly that $\operatorname{ad}_X$ is skew-Hermitian, so the image of $\mathrm{G}$ lies in $\mathrm{u}(n)$ for a faithful representation and $\mathrm{G}$ is compact; the Killing form of a compact algebra is negative definite by *Structure of Lie Algebras*, hence $-B$ is positive definite and invariant. The converse is the same argument read for $\mathrm{K}$ acting on the complexification.

**Corollary.** A complex semisimple Lie algebra carries a positive definite invariant Hermitian form exactly when it has a compact real form, and then the form is unique up to a positive scalar; the form is the negative of the Killing form of the compact form.

*Proof.* The uniqueness up to scalar is Schur's lemma applied to the irreducible adjoint representation, whose endomorphisms commuting with the action are the scalars on each simple summand; the identification with $-B$ is the previous theorem.

### The Indefinite Case

**Proposition.** Let $H$ be a non-degenerate invariant Hermitian form of signature $(p,q)$ on a real Lie algebra $\mathrm{G}$. Then the operators $\operatorname{ad}_X$ are in the Lie algebra $\mathrm{u}(p,q)$ of the form, the isometry algebra of $H$ is a real form of the complex algebra preserving the form, and the Cartan involution of $\mathrm{G}$ with respect to the compact part of the form is the map $+\mathrm{id}$ on the maximal compact subalgebra and $-\mathrm{id}$ on its complement.

*Proof.* The invariance is the statement that the adjoint action preserves $H$, so the image of $\mathrm{G}$ lies in the isometry algebra $\mathrm{u}(p,q)$; the isometry algebra of the complexification contains the compact part $\mathrm{u}(p)\oplus\mathrm{u}(q)$, whose fixed algebra is the maximal compact subalgebra of the real form, and the Cartan involution is the conjugation of the form. This connects the form with *Real Forms of a Complex Lie Group and the Cartan Involution*.

## The Forms and the Representations

### The Form Defines the Star

**Theorem.** Let $\mathrm{G}$ be a real Lie algebra with an invariant Hermitian form $H$, and let $\sigma$ be the principal anti-automorphism of $U(\mathrm{G})$. Then the adjoint operation for $H$ on the operators coincides with the star,

$$
\operatorname{ad}_X^{\dagger} = -\operatorname{ad}_X = \operatorname{ad}_{\sigma(X)} \qquad (X\in\mathrm{G}),
$$

and a representation of $\mathrm{G}$ by skew-Hermitian operators with respect to $H$ is a star-representation of $U(\mathrm{G})$; conversely a star-representation of $U(\mathrm{G})$ whose operators are skew-Hermitian for $H$ is unitarisable.

*Proof.* The identity is the invariance of $H$; the equivalence of the two formulations on the enveloping algebra is that both are generated on the first order, by the universality of $U(\mathrm{G})$. This is the content of *The Involution on the Enveloping Algebra of a Lie Group*, read with the form as the geometric datum.

### The Casimir and Positivity

**Theorem.** Let $H$ be a positive definite invariant Hermitian form on a real semisimple Lie algebra $\mathrm{G}$, let $(X_i)$ be an orthonormal basis, and let $\Omega = -\sum_i X_i^2$. Then $\Omega$ is a positive Hermitian element of $U(\mathrm{G})$, it is central, and its image in every star-representation is a positive self-adjoint operator; the scalars by which it acts are the quadratic invariants of the irreducible summands.

*Proof.* The element is Hermitian because the $X_i$ are skew under the star, and it is positive because $-\sum X_i^2 = \sum X_i^{\star}X_i$; the centrality is the invariance of the form; the positivity of the image is the positivity of the sum of the squares of skew-adjoint operators, and the eigenvalue statement is *The Casimir Operator of a Lie Group*.

## Examples

### The Unitary Algebra

Let $\mathrm{G} = \mathrm{u}(n)$ with $H(X,Y) = \operatorname{tr}(X\overline{Y}^{t}) = -\operatorname{tr}(XY)$ on the skew-Hermitian matrices, using that the conjugate transpose of a skew-Hermitian matrix is its negative. The form is positive definite and invariant under the commutator, the adjoint operators are skew-Hermitian, and the algebra is the model compact case.

### The Special Linear Algebra

Let $\mathrm{G} = \mathrm{su}(n)$ with $H(X,Y) = -\operatorname{tr}(XY)$ on the traceless skew-Hermitian matrices. The form is positive definite and invariant, it is a positive multiple of $-\frac{1}{2n}B$ with $B$ the Killing form, and the Casimir element is positive; the unitary representations of the compact group act by skew-Hermitian operators, which is the Peter--Weyl situation of *Unitary Representations of a Lie Group*.

### An Indefinite Form

Let $\mathrm{G} = \mathrm{u}(p,q)$ with the Hermitian form of signature $(p,q)$ on $\mathbb{C}^{p+q}$. The form on the algebra $H(X,Y) = \operatorname{tr}(X\overline{Y}^{t})$ has the indefinite signature $(p^2+q^2, 2pq)$, the invariance holds, and the Cartan involution is conjugation by the form; the unitary representations are the discrete series and the analytic continuation of *Unitary Representations of a Lie Group*, and the geometry of the associated domain is *Hermitian Lie Groups and the Bounded Domain*.

### The Heisenberg Algebra

Let $\mathrm{G}$ be the Heisenberg algebra with the central element $Z$ and the brackets $[X,Y] = Z$. There is no non-degenerate invariant Hermitian form for which $Z$ acts as a scalar in an irreducible representation other than zero: the invariance forces $H([X,Y],Z) = H(X,[Y,Z]) = 0$, so $H(Z,Z) = 0$ and the form is degenerate exactly at the radical; the unitary representations nonetheless exist, and they are those of *Unitary Representations and the Orbit Method*.

## Summary

A **Hermitian form** on a complex Lie algebra is sesquilinear, conjugate-symmetric and real-valued on the diagonal, and it is **invariant** when $H([X,Y],Z) = H(X,[Y,Z])$, equivalently when $H([X,Y],Z) + H(Y,[X,Z]) = 0$; the two forms of the condition are equivalent and they say that each adjoint operator $\operatorname{ad}_X$ is skew-Hermitian for $H$. A positive definite invariant Hermitian form makes the algebra a compact real form, and conversely every compact form carries such a form, unique up to a positive scalar and equal to the negative of the Killing form; non-degenerate indefinite forms have a signature and put the algebra inside the isometry algebra $\mathrm{u}(p,q)$, whose compact part gives the Cartan involution. The adjoint operation of the form coincides with the star of the principal anti-automorphism of the enveloping algebra, so the unitary representations are exactly the star-representations by skew-Hermitian operators, and the Casimir element $-\sum X_i^2$ of an orthonormal basis is a positive central Hermitian element whose images are positive self-adjoint operators. The definite case is the compact theory, the indefinite case is the theory of the real forms, and the degenerate case — in which the form vanishes on the radical — exhibits the limits of the construction, as the Heisenberg algebra shows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H(X,Y)$ | a Hermitian form, linear in the first and conjugate-linear in the second argument |
| $H(X,Y) = \overline{H(Y,X)}$ | conjugate symmetry |
| $H([X,Y],Z) = H(X,[Y,Z])$ | invariance of the form |
| $\operatorname{ad}_X^{\dagger} = -\operatorname{ad}_X$ | skew-Hermitian adjoint operators |
| $\flat(X)(Y) = H(X,Y)$ | the associated antilinear map to the dual |
| $(p,q)$ | the signature of a non-degenerate form |
| $\mathrm{u}(p,q)$ | the isometry algebra of a form of signature $(p,q)$ |
| $\Omega = -\sum_i X_i^2$ | the Casimir element of an orthonormal basis |
| $\operatorname{ad}_X^{\dagger} = \operatorname{ad}_{\sigma(X)}$ | the agreement of the adjoint with the star |
| positive definite invariant form | the compact case, $-B$ up to a scalar |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the invariant forms, the compact forms and the Cartan involution.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the Hermitian forms on a real Lie algebra and the hermitian structure of the real forms.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the Hermitian forms on a vector space, their signature and Sylvester's law.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, second edition, 2015), for the unitary representations defined by an invariant form and the embedding into the unitary group.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the invariant forms, the star and the positivity of the Casimir element.
