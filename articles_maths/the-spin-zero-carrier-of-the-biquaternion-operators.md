# __The Spin-Zero Carrier: the Scalars__

## Introduction

**The subject.** The carrier of label zero in the operator space is the line of the scalar multiples of the identity. The article computes its dimension over the two fields, splits it into its real and imaginary halves, identifies the trace as the functional that reads it off up to a normalising factor, proves that it is the unique line fixed by the whole copy, and locates it as the intersection of the two one-sided families.

**The order of the article.** The carrier comes first; the two real halves second. The invariance follows, then the trace, then the intersection with the one-sided families, and the reading closes.

**It assumes** *The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$*, *The One-Sided Operators* and *The Transposition of the Two Sides*. **The row of the spin-zero carrier is** where the scalars of the algebra form the analogous line, of real dimension one and complex dimension one.

**The result in one line.** The carrier $V_0$ is the complex line $\mathbb{C}\,\mathrm I$, of complex dimension one and real dimension two, fixed by every action of the copy and equal to the intersection $L_{\mathbb{B}}\cap R_{\mathbb{B}}$.

**Boundaries.** The determinant on the carrier is *The Spin-Zero Carrier and the Determinant*; the spectra are *The Spin-Zero Carrier and the Spectral Strata*; the rank is *The Spin-Zero Carrier and the Rank Strata*.

## The Carrier

**Definition.** The carrier $V_0$ is the set of the operators commuting with every element of the copy.

**Theorem.** The carrier is the complex line of the multiples of the identity, of complex dimension one.

*Proof.* An operator commuting with every $\xi$ in the copy is an intertwiner of the module with itself. The module is irreducible, so every such intertwiner is a scalar multiple of the identity.

**Corollary.** The carrier contributes one dimension to the decomposition $16=7+5+3+1$.

*Proof.* The dimension of the trivial module is $2\cdot0+1=1$.

**Corollary.** The carrier is contained in every sum of carriers, and its intersection with each of the other three is the origin.

*Proof.* The decomposition of the space into the four carriers is direct.

**The reading.** One line, of dimension one, labelled zero. The smallest carrier is the one that carries no weight, and its triviality is what makes it central.

## The Two Real Halves

**Proposition.** As a real space of operators the carrier has dimension two, and it splits into the real line spanned by the identity and the imaginary line spanned by the multiplication by $i$.

*Proof.* A multiple $\lambda\mathrm I$ with $\lambda=\mu+i\nu$ is $\mu\mathrm I+\nu(i\mathrm I)$, and the two real operators are independent over the reals and dependent over the complex numbers.

**Corollary.** The real line is the carrier of the real scalars and the imaginary line is the carrier of the purely imaginary scalars, and the two are exchanged by the multiplication by $i$.

*Proof.* The multiplication by $i$ is an operator of square minus the identity on the carrier, and it exchanges the two lines.

**Corollary.** The complex structure of the carrier is the restriction of the complex structure of the whole space, and the real form it defines is the real line.

*Proof.* The two halves and their complexification.

**The reading.** Two real dimensions, two halves, one complex dimension. The carrier is the smallest place where the real and the complex readings of the space can be compared, and the comparison is exact: the complexification of the real line is the whole carrier.

## The Invariance

**Theorem.** The carrier is fixed pointwise by the conjugation action of the whole unit group, by the transposition, and by the multiplication by central elements.

*Proof.* A scalar is central, so $a\lambda\mathrm I a^{-1}=\lambda\mathrm I$; the transposition fixes the central elements; and the product of a central element with a scalar is a scalar.

**Corollary.** The carrier is the unique line of the space fixed pointwise by the conjugation action of the copy.

*Proof.* An operator fixed by the conjugation with every element of the copy commutes with the copy, and the commutant is the line of the scalars.

**Corollary.** The left action of the copy does not fix the carrier: it carries the identity to the element $\xi$, and the orbit of the identity is the sphere of the elements of norm one.

*Proof.* $\xi\,\mathrm I=\xi$ for every $\xi$.

**The reading.** The invariance of the carrier is an invariance under similarity and not under left multiplication. The two groups act on the same space, one fixing the line pointwise and the other sweeping it onto the sphere; the carrier is the fixed line of the first and a point of the orbit of the second.

## The Trace as the Projector

**Proposition.** The trace of a scalar operator is four times its multiplier, and the trace of the map of the sixteen-dimensional space given by left composition with a scalar operator is sixteen times its multiplier.

*Proof.* The identity of the algebra has trace four as a map of the four-dimensional module, and left composition with $S$ acts on the four copies of the module in the space of the operators, so its trace is $4\operatorname{tr}(S)=16\lambda$.

**Corollary.** The normalised functional $\tfrac{1}{16}\operatorname{tr}$ reads off the scalar coordinate of the carrier, and the functional $\tfrac14\operatorname{tr}$ reads it off on the algebra.

*Proof.* Both functionals take the value $\lambda$ on $\lambda\mathrm I$ and vanish on the traceless hyperplane.

**Corollary.** The trace is the only linear functional of the space that is invariant under the conjugation and normalised on the identity.

*Proof.* The invariant functionals are the multiples of the trace, since the conjugation acts irreducibly on the traceless hyperplane.

**The reading.** The trace is the projector onto the carrier up to the factor sixteen, in the reading where the carrier acts on the space by composition. It is a projection followed by a scalar, and the scalar is the price of the two levels: the algebra and the space of the operators on it.

## The Intersection of the One-Sided Families

**Theorem.** The intersection of the two one-sided families is the carrier:
$$
L_{\mathbb{B}}\cap R_{\mathbb{B}}=\mathbb{C}\,\mathrm I .
$$

*Proof.* An operator which is both a left multiplication $L_a$ and a right multiplication $R_b$ satisfies $aX=Xb$ for every $X$; setting $X=\mathrm I$ gives $a=b$, and then $a$ commutes with every $X$, so it is central and the operator is a scalar multiple of the identity. Conversely a scalar multiple of the identity is both.

**Corollary.** The intersection has dimension one, the sum has dimension seven, and the complement has dimension nine, so $16=1+3+3+9$.

*Proof.* The two families have dimension four each and intersection one, so the sum has dimension seven; the complement of a seven in a sixteen has dimension nine.

**Corollary.** The carrier is the only operator that is one-sided in both senses, and every other one-sided operator is one-sided in exactly one sense.

*Proof.* The computation of the intersection and the dimensions of the two families.

**The reading.** The centre is the one carrier that no choice of copy can move. It is the fixed line of the conjugation, the intersection of the two one-sided families, the kernel of the traceless projection and the home of the multiplicative invariant.

## Further Reading

- [The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$](the-clebsch-gordan-decomposition-of-the-biquaternion-operators.html), for the four carriers.
- [The One-Sided Operators](the-one-sided-operators-of-the-biquaternion-algebra.html), for the two families whose intersection is the carrier.
- [The Spin-Zero Carrier and the Determinant](the-spin-zero-carrier-and-the-determinant.html), for the multiplicative invariant on the carrier.
- [The Copy Acting on Sixteen Dimensions](the-copy-acting-on-sixteen-dimensions.html), for the two actions that fix or move the carrier.
