# __The Quaternionic Structure of the Module: Why $V_{3/2}$ Admits Real Forms__

## Introduction

**The subject.** The module $V_{3/2}$ is a complex vector space of dimension four carrying an irreducible unitary action of $SU(2)$. It also carries an anti-linear map $T$ that commutes with the action up to complex conjugation, and the square of that map is a scalar. The scalar is $-1$, so the module is quaternionic and not real.

**The order of the article.** The first section constructs $T$ and proves the intertwining relation. The second computes $T^{2}$ and the Frobenius–Schur indicator. The third draws the consequences for the half-integer and the integer carriers. The fourth locates the real spaces of dimension four inside the module. The fifth passes to the algebra of order two and explains why the biquaternion row is a real algebra. The sixth separates the two kinds of real structure.

**It assumes** *The Four Weights of the Module and the Half Angle at $n=4$* for the weight basis. The general theory of the indicator is quoted from the representation theory of compact groups; the row at order two is *The Spin-Half Bispinor Spaces*.

**The result in one line.** $T^{2}=(-1)^{2j}$, so the carriers of half-integer label are quaternionic and the carriers of integer label are real; $V_{3/2}$ is quaternionic, and a quaternionic line inside it has real dimension four.

**A word on the title.** The phrase *real forms* in the title is read in the sense of real subspaces of the module, and the largest of them are the quaternionic lines of real dimension four. The module itself has no real form, since $T^{2}=-\mathrm I$; the real spaces it contains are the quaternionic lines, and they are the subject of the fourth section. The distinction between the two readings is drawn once and for all in the last section.

**Boundaries.** The article does not construct the real algebra of quaternions inside the matrix algebra; that is *The Two Base Fields $M_4(\mathbb{R})$ inside $M_4(\mathbb{C})$* and the biquaternion articles. It does not treat the reality of the algebra action, which is *The Spin Content of $M_4(\mathbb{C})$*.

## The Anti-Linear Intertwiner

**Definition.** Let $v_m$ be the orthonormal weight vector of weight $m$ and put

$$
T\Bigl(\sum_m c_m v_m\Bigr)=\sum_m (-1)^{j-m}\,\overline{c_m}\,v_{-m}.
$$

This is an anti-linear map of $V$ to itself: $T(c\,w)=\bar c\,Tw$ and $T(w+w')=Tw+Tw'$.

*Proof.* The definition is a sum of terms each anti-linear in the coefficient, and the coefficients $(-1)^{j-m}$ are real.

**Proposition.** $T$ is a bijection, and $T\rho(q)=\overline{\rho(q)}\,T$ for every $q$ in the copy, where the bar is the entrywise complex conjugate.

*Proof.* The map sends the orthonormal basis to an orthonormal basis up to signs, so it is invertible. For the relation, both sides are anti-linear in the vector and it suffices to check on the weight vectors. The conjugate representation $\overline{\rho}$ has the weights $-m$ on the conjugate of $v_m$, and the signs $(-1)^{j-m}$ are exactly the signs of the standard intertwiner between the representation and its conjugate; the two sides agree on each weight vector.

**Proposition (uniqueness).** Every anti-linear map $S$ with $S\rho(q)=\overline{\rho(q)}S$ is a real multiple of $T$.

*Proof.* The composite $T^{-1}S$ is complex-linear and commutes with every $\rho(q)$; the module is irreducible and the complex numbers are the only operators commuting with an irreducible complex representation, by Schur's lemma. Hence $T^{-1}S=\lambda\mathrm I$ for a real $\lambda$, since both maps are anti-linear.

**Corollary.** The structure is canonical up to a positive real scalar, and the sign of its square is an invariant of the representation.

*Proof.* The scalar $\lambda$ changes $S^{2}$ by $\lambda^{2}$, which is positive for real $\lambda$; the sign of the square is therefore unchanged.

## The Square and the Indicator

**Proposition.** $T^{2}=(-1)^{2j}\mathrm I$. At $j=\tfrac32$ this is $-\mathrm I$.

*Proof.* On a weight vector, $T^{2}v_m=(-1)^{j-m}(-1)^{j+m}v_m=(-1)^{2j}v_m$, since the conjugate of a real coefficient is itself and the two applications reverse the weight twice. At $j=\tfrac32$ the exponent $2j=3$ is odd.

**Definition.** The **Frobenius–Schur indicator** of the irreducible representation is the sign of $T^{2}$, that is, $(-1)^{2j}$.

**Corollary.** The indicator is $-1$, and the representation is quaternionic, for $j=\tfrac12$ and $j=\tfrac32$; it is $+1$, and the representation is real, for $j=1$, $j=2$ and $j=3$.

*Proof.* The exponent $2j$ is odd exactly for the two half-integer labels among these five.

**The table.**

| carrier | $2j$ | $T^{2}$ | type | real dimension of the form |
|---|---|---|---|---|
| $V_{1/2}$ | $1$ | $-1$ | quaternionic | none |
| $V_1$ | $2$ | $+1$ | real | $3$ |
| $V_{3/2}$ | $3$ | $-1$ | quaternionic | none |
| $V_2$ | $4$ | $+1$ | real | $5$ |
| $V_3$ | $6$ | $+1$ | real | $7$ |

**Corollary.** The four carriers of the algebra and the module split into two quaternionic and three real representations, and the module is one of the quaternionic two.

*Proof.* The table.

## The Consequences for the Carriers

**Proposition.** For an integer label $k$ the fixed points of $T$ form a real subspace of real dimension $2k+1$, whose complexification is $V_k$.

*Proof.* $T^{2}=\mathrm I$ makes $T$ a real structure; the fixed points of an anti-linear involution on a complex space of dimension $2k+1$ have real dimension $2k+1$, and the complexification is the whole space.

**Corollary.** The real form of $V_1$ has dimension three, of $V_2$ dimension five, of $V_3$ dimension seven.

*Proof.* The proposition with $k=1,2,3$.

**Proposition.** For a half-integer label the map $T$ is a quaternionic structure: $T^{2}=-\mathrm I$, and the module becomes a vector space over the quaternions, with the imaginary unit $i$ acting as multiplication by $i$ and the unit $j$ acting as $T$.

*Proof.* The relations $i^{2}=j^{2}=-1$ and $ij=-ji$ are the complex structure of the vector space and the anti-linearity of $T$.

**Corollary.** $V_{3/2}$ has complex dimension four, real dimension eight and quaternionic dimension two, and it admits no real subspace $W$ with $W\otimes_{\mathbb{R}}\mathbb{C}=V_{3/2}$.

*Proof.* The real dimension of a quaternionic vector space is four times its quaternionic dimension, so the quaternionic dimension is two. A real form would be the fixed space of an anti-linear involution; $T^{2}=-\mathrm I$ has no nonzero fixed vector, since $Tv=v$ would give $T^{2}v=v$ and also $T^{2}v=-v$.

## Real Spaces of Dimension Four Inside the Module

**Proposition.** The complex span of the two weight vectors $v_{3/2}$ and $v_{-3/2}$ is stable under $T$, and as a real space of dimension four it is a quaternionic line.

*Proof.* $Tv_{3/2}=v_{-3/2}$ and $Tv_{-3/2}=(-1)^{3}v_{3/2}=-v_{3/2}$, both inside the span; the span has complex dimension two and real dimension four, and it is stable under multiplication by $i$ and by $T$, hence under the quaternions.

**Corollary.** The module is a direct sum of two quaternionic lines, for instance the line spanned by the extreme weights and the line spanned by the two middle weights.

*Proof.* The two spans are $T$-stable, of complex dimension two each, and their sum is the whole module.

**Corollary.** Every quaternionic line has real dimension four, and the module contains a two-parameter family of them, since a quaternionic line is determined by a point of the quaternionic projective line.

*Proof.* The dimension count and the definition of the quaternionic projective line.

**The reading.** The phrase "a real form of dimension four" is correct for a quaternionic line and incorrect for the module: the module has real dimension eight. The distinction is the whole content of the sign of $T^{2}$.

## The Passage to Order Two

**Proposition.** At $n=2$ the module is $V_{1/2}$, of complex dimension two and real dimension four, and $T^{2}=-\mathrm I$; the module is a single quaternionic line.

*Proof.* The weights are $\pm\tfrac12$, and the computation of the square gives $-1$; a quaternionic space of real dimension four has quaternionic dimension one.

**Corollary.** The real algebra of the quaternions acts on $V_{1/2}$ by complex-linear maps, and the algebra of all such maps is $M_2(\mathbb{C})$, the biquaternion algebra.

*Proof.* The quaternions act by $i$ and $T$, and the real dimension of $M_2(\mathbb{C})$ is eight, which is the real dimension of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$.

**Proposition.** There is no eight-dimensional real division algebra, by the theorem of Frobenius, and the biquaternion algebra is not one: it is $M_2(\mathbb{C})$ and it has zero divisors.

*Proof.* Frobenius classifies the finite-dimensional real division algebras as $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, of dimensions one, two and four. The biquaternion algebra contains the rank-one matrix $E_{00}$, which is a zero divisor.

**Corollary.** The enlargement from $n=2$ to $n=4$ does not produce a division algebra of dimension eight: it produces the matrix algebra of order four, which has zero divisors of every rank.

*Proof.* The proposition, and the rank-one elements of $M_4(\mathbb{C})$.

## The Two Kinds of Real Structure

**The distinction.** A real structure is an anti-linear involution; a quaternionic structure is an anti-linear map whose square is minus the identity. The first produces a real form and the second produces a quaternionic structure, and the two are distinguished by the sign of $T^{2}$ alone.

*Proof.* The definitions and the two propositions above.

**Corollary.** The half-integer carriers are the ones on which the sign is negative, and the biquaternion row consists exactly of such carriers: $V_{1/2}$ at $n=2$, and the module $V_{3/2}$ at $n=4$.

*Proof.* The table of indicators.

**The reading.** The biquaternion algebra is a real algebra because the module of its spin group is quaternionic, and the module of order four is quaternionic for the same reason: the parity of $2j$. The integer carriers of the algebra of order four are real, and that is why the algebra carries real forms of dimensions three, five and seven and the module carries none.

*Proof.* The two preceding corollaries.

## Summary

The module carries an anti-linear intertwiner $T$ with $T\rho=\overline{\rho}T$, unique up to a real scalar, and $T^{2}=(-1)^{2j}\mathrm I$. At $j=\tfrac32$ the square is $-1$: the module is quaternionic, of quaternionic dimension two and real dimension eight, and it contains no real form. A quaternionic line inside it has real dimension four, and the module is a sum of two such lines.

The integer carriers $V_1,V_2,V_3$ have $T^{2}=+1$ and therefore carry real forms of dimensions three, five and seven. At $n=2$ the module $V_{1/2}$ is a single quaternionic line, the quaternions act on it, and the algebra of all complex-linear maps is $M_2(\mathbb{C})$, the biquaternion algebra, which is not a division algebra and is not of dimension eight as a division algebra.

The distinction between the two kinds of real structure is the sign of $T^{2}$, and the sign is the parity of $2j$. Half-integer carriers are quaternionic, integer carriers are real, and the module of order four belongs to the first class.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T$ | the anti-linear intertwiner |
| $T^{2}=(-1)^{2j}\mathrm I$ | the Frobenius–Schur indicator |
| quaternionic | $T^{2}=-\mathrm I$ |
| real | $T^{2}=+\mathrm I$ |
| $V_{3/2}$ | the module, quaternionic, real dimension eight |
| quaternionic line | a $T$-stable complex line pair, real dimension four |
| $\mathbb{H}$ | the quaternions, real dimension four |

## Further Reading

- [The Four Weights of the Module and the Half Angle at $n=4$](the-four-weights-of-the-module-and-the-half-angle-at-n-4.html), for the weight basis used in the definition of $T$.
- [The Spin Group at $n=4$: the Principal Copy, $\operatorname{Sym}^3$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-at-n-4-the-principal-copy-and-its-kernel.html), for the action that $T$ intertwines.
- [The Spin-Half Bispinor Spaces](the-spin-half-bispinor-spaces.html), for the row at order two.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the four carriers and their labels.
- [The Two Base Fields $M_4(\mathbb{R})$ inside $M_4(\mathbb{C})$](the-two-base-fields-m4r-inside-m4c.html), for the real slices of the matrix algebra.
