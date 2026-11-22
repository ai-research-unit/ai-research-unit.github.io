# __The Spin-Two Carrier and the Rank Strata__

## Introduction

**The subject.** Every element of the quintet satisfies a quadratic equation, $X^{2}=c\,\mathrm I$ with $c=\tfrac14\operatorname{tr}(X^{2})$. The article draws the consequences: the spectrum is $\{s,s,-s,-s\}$, the rank takes the values zero, two and four and never one or three, the determinant is $c^{2}$, and the singular elements form a quadric cone of dimension four.

**The order of the article.** The rank is defined and its parity proved first. The quadratic law follows, then the two strata and their dimensions, the alternating form that explains the parity, and the singular locus as the set of the zero divisors of the operator algebra.

**It assumes** *The Spin-Two Carrier and the Trace Form* and *Introduction to the Spin-Two Carrier: the Alternating Square*. **The row of the elements is** where the same count is made on the algebra; there a left multiplication has rank four, two or zero, according as the element is invertible, a zero divisor or zero.

**The result in one line.** The rank of an element of $V_2$ is four when $\operatorname{tr}(X^{2})\neq0$, two when that trace vanishes at a nonzero element, and zero at the origin; the two strata have dimensions five and four.

**Boundaries.** The form whose isotropic cone is the singular locus is computed in *The Spin-Two Carrier and the Trace Form*; the spectral stratification of the row is *The Spin-Three Carrier and the Spectral Strata*; the rank law for products of elements is *The Four Ranks of the Two-Sided Operators*.

## The Rank

**Definition.** The **rank** of an operator of the sixteen is the dimension of its image in the algebra, equivalently four minus the dimension of its kernel. It is the rank of a complex-linear map of a four-dimensional space, and it is invariant under conjugation by an invertible element.

**Proposition.** The rank of an element of $V_2$ is even. It takes the values four, two and zero, and it never takes the values one or three.

*Proof.* The spectrum of an element of the quintet is symmetric and has multiplicity two at each value, as the next section proves; a spectrum $\{s,s,-s,-s\}$ has four nonzero entries at $s\neq0$ and none at $s=0$. A rank-one element would have the spectrum $\{\mu,0,0,0\}$ and a rank-three element a spectrum with a single zero; neither shape is symmetric with multiplicity two.

**Corollary.** The set of elements of rank at most two is the set on which the determinant vanishes, and it is a proper subset of the carrier.

*Proof.* The determinant is the product of the eigenvalues, which is $s^{4}$; it vanishes exactly at $s=0$. The set is proper because the element of weight zero has four nonzero eigenvalues.

**The reading.** The parity of the rank is the first trace of the alternating square. Odd ranks would need an eigenvalue of odd multiplicity, and the construction of the carrier forbids it.

## The Quadratic Law

**Theorem.** Every element of the quintet satisfies
$$
X^{2}=\frac{\operatorname{tr}(X^{2})}{4}\,\mathrm I ,
$$
so the characteristic polynomial is $\left(\lambda^{2}-\tfrac14\operatorname{tr}(X^{2})\right)^{2}$ and the spectrum is $\{s,s,-s,-s\}$ with $s^{2}=\tfrac14\operatorname{tr}(X^{2})$.

*Proof.* The carrier is the traceless part of the alternating square of the module, so its elements correspond to alternating forms on the module, and an alternating form on a four-dimensional space with the invariant form removed defines an endomorphism whose square is a multiple of the identity: the square is self-adjoint, it commutes with the form, and it is moreover a scalar because the only symmetric endomorphisms commuting with the whole alternating square are the scalars. The scalar is read by taking the trace, which gives $4c=\operatorname{tr}(X^{2})$. The spectrum follows from the quadratic equation, and the multiplicity two from the degree of the minimal polynomial.

**Corollary.** The determinant and the trace of the square are related by $\det X=\left(\tfrac14\operatorname{tr}(X^{2})\right)^{2}$, and the trace of $X$ itself vanishes.

*Proof.* The eigenvalues are $s,s,-s,-s$, so the product is $s^{4}=c^{2}$ and the sum is zero. The trace vanishes identically on the carrier because the trace is the invariant linear functional of the trivial summand, and $V_2$ has label two.

**Corollary.** The cube of an element of the carrier is a multiple of the element itself, and the carrier is closed under the formation of odd powers up to a scalar.

*Proof.* Multiplying the quadratic law by $X$ gives $X^{3}=cX$.

**The reading.** One invariant controls the whole spectral picture. The element is invertible exactly when $c$ is nonzero, its inverse is $c^{-1}X$, and the two eigenvalues are exchanged by multiplication by $-1$, which is the action of the element of the copy that implements the half-turn.

## The Two Strata

**Theorem.** The carrier splits into two strata and the origin:
$$
V_2=\{0\}\ \cup\ \{X:c(X)\neq0,\ \operatorname{rank}X=4\}\ \cup\ \{X\neq0:c(X)=0,\ \operatorname{rank}X=2\},
$$
of dimensions $0$, $5$ and $4$.

*Proof.* The first set is a point. The second is the complement of the zero set of the polynomial $c$, which is a nonzero homogeneous polynomial of degree two on a five-dimensional space, so the complement is open and of dimension five. The third is the zero set itself with the origin removed; it is a quadric cone, of dimension four, and its nonzero elements are the nilpotents of the carrier, of rank two by the quadratic law.

**Corollary.** The singular locus of the carrier is a quadric cone of dimension four, and it is the cone over a quadric surface in the projective space of dimension four.

*Proof.* The cone is the zero set of one quadratic form; its projectivisation is the quadric defined by that form, of dimension three in the projective four-space.

**Corollary.** The rank and the vanishing of the determinant cut the same locus on the carrier.

*Proof.* The determinant vanishes exactly where $c$ does, by the identity $\det X=c^{2}$, and $c$ vanishes exactly where the rank drops.

**The reading.** The quintet is the smallest carrier on which the rank and the determinant cut the same locus, because it is the smallest carrier on which the determinant is a power of the single invariant that the quadratic law supplies. On the triplet the rank drops along a cone of dimension two, and on the septet the determinant is not a power of any one invariant.

## The Alternating Form

**Proposition.** An element of the quintet corresponds to an alternating form $\beta_X$ on the module, and the rank of the operator equals the rank of that form.

*Proof.* The carrier is the traceless part of the alternating square, whose elements are the alternating forms; the invariant form of the module identifies a form with an endomorphism, and an identification by a nondegenerate form preserves the rank.

**Corollary.** The elements of rank two are the decomposable alternating forms, and they are exactly the nonzero elements of the cone $c=0$.

*Proof.* An alternating form on a four-dimensional space has even rank; rank two means that the form is the product of two linear forms, which is decomposability. The square of the corresponding endomorphism vanishes exactly in that case.

**Corollary.** The carrier realises the ranks zero, two and four and no other, and the word rank in the name of the strata refers to the same number read on the form and on the operator.

*Proof.* The two readings agree by the proposition, and the possible ranks of an alternating form on a four-dimensional space are $0,2,4$.

**The reading.** The alternating square is not only the space in which the carrier lives; it is the reason for the parity of the rank. A symmetric rank-two tensor would give every rank from one to four, and the alternating one gives only the even ranks.

## The Zero Divisors

**Proposition.** The singular locus of the carrier is the set of its elements that are not invertible as operators, and in the operator algebra these elements are zero divisors.

*Proof.* An operator of rank less than four has a nonzero kernel, so some nonzero element of the algebra is annihilated by it and the operator is a zero divisor of the operator algebra. The converse holds as well, since an operator with trivial kernel is injective on a space of finite dimension and therefore invertible.

**Corollary.** The algebra of biquaternions has no zero divisors, and the operator algebra has a singular locus of dimension four inside the quintet.

*Proof.* Every element of nonvanishing norm is invertible, and its left and right multiplications are bijections; a nonzero element of vanishing norm is a zero divisor, and its multiplications have rank two. The two-sided products built from two degenerate elements have rank one, by the law $\operatorname{rank}T_{a,b}=\operatorname{rank}L_a\operatorname{rank}R_b/4$, so the four values zero, one, two and four all occur on the space. The operator algebra is the endomorphism algebra of a four-dimensional space, which has singular elements, and the quintet meets them in the quadric cone.

**Corollary.** The intersection of the carrier with the singular set of the whole operator space is the cone $c=0$, and the two-sided operators of the row meet that set only at the origin.

*Proof.* A two-sided operator with two nonzero parameters is a product of two bijections and therefore invertible; the carrier, by contrast, contains nilpotents of rank two.

**The reading.** The word singular means two different things in the two rows. In the row of the elements nothing is singular except zero; in the row of the operators the singular set is a hypersurface, and the quintet meets it in a quadric cone.

## Further Reading

- [The Spin-Two Carrier and the Trace Form](the-spin-two-carrier-and-the-trace-form.html), for the quadratic form that cuts the cone.
- [Introduction to the Spin-Two Carrier: the Alternating Square](introduction-to-the-spin-two-carrier-the-alternating-square.html), for the construction of the carrier.
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the rank law of products.
- [Zero Divisors and Invertibles in the Biquaternion Algebra](zero-divisors-and-invertibles-in-the-biquaternion-algebra.html), for the zero divisors and the invertibles.
- [The Spin-Three Carrier and the Rank Strata](the-spin-three-carrier-and-the-rank-strata.html), for the carrier where every rank occurs.
