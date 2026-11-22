# __The Quaternionic Structure of the Module: Why $V_{3/2}$ Admits Real Forms__

## Introduction

**The subject.** The module of the operators carries an anti-linear map that commutes with the copy up to the conjugation of the generator, and the square of that map is a negative scalar. This is a quaternionic structure: the module has no real form of dimension four, but it has a quaternionic structure whose real dimension is eight. The article constructs the map, proves its uniqueness, computes the sign, and separates the three types of module, real, quaternionic and complex, by the labels of the two rows.

**The order of the article.** The anti-linear intertwiner comes first; its uniqueness and its square second. The type of the module follows, then the integer carriers, and the trichotomy closes the article.

**It assumes** *The Four Weights of the Module and the Half Angle*, *The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$* and *The Complex Numbers*. **The row of the elements is** where the same computation gives a quaternionic structure on the two-dimensional spinor space; here it gives one on the four-dimensional module.

**The result in one line.** There is an anti-linear $T$ with $T\rho(\xi)=\rho(\bar\xi)T$, unique up to a scalar, and $T^{2}=-c\,\mathrm I$ with $c>0$: the module admits no real form of dimension four, and the real forms it does admit are quaternionic, of complex dimension four and real dimension eight.

**Boundaries.** The integer carriers and their real dimensions are *The Clebsch–Gordan Decomposition of the Operators*; the conjugation of the labels is *Why the Conjugation Labels Are Integer*; the anti-linear maps in general are *Conjugate-Linear Maps and the Conjugate Dual*.

## The Intertwiner

**Definition.** An **anti-linear intertwiner** is a map $T$ of the module, conjugate-linear in the scalar, with
$$
T\rho(\xi)=\rho(\bar\xi)\,T
$$
for every element $\xi$ of the copy, where $\bar\xi$ is the conjugate generator.

**Theorem.** The module admits an anti-linear intertwiner, and it is unique up to multiplication by a nonzero real scalar.

*Proof.* The conjugate of the module, with the action $\xi\mapsto\rho(\bar\xi)$, is again a module of the copy; its weights are the negatives of the weights of the module, so it is isomorphic to the module itself, since the weight string is symmetric. The space of intertwiners is therefore one-dimensional by the simplicity of the module and the multiplicity-free character of the decomposition.

**Corollary.** The intertwiner is defined up to a scalar, and its square is a scalar.

*Proof.* $T^{2}$ is linear and commutes with the copy, hence is a scalar by uniqueness.

**Corollary.** The intertwiner reverses the weights, $T v_m=\lambda_m v_{-m}$ with scalars of modulus one.

*Proof.* $T$ carries a vector of weight $m$ to one of weight $-m$, and the two strings coincide.

**The reading.** The symmetry of the weight string is the whole reason for the existence of the map. The module and its conjugate are the same object, and the intertwiner is the comparison.

## The Sign of the Square

**Theorem.** Normalise $T$ so that its square is $\pm\mathrm I$ in modulus; then $T^{2}=c\,\mathrm I$ with $c$ real, and for the module of label $\tfrac32$ the sign is negative.

*Proof.* The scalars $\lambda_m$ satisfy $\lambda_m\lambda_{-m}=c$ and $|\lambda_m|=1$, so $c$ is real of modulus one. The value of $c$ is computed on a pair of weight vectors: the composition of the two reflections in the weights gives the factor $(-1)^{2m}$ accumulated over the pairs, and for a half-integer $m$ the product over the four weights is negative.

**Corollary.** The module carries no real structure, that is, no conjugate-linear map with square $+\mathrm I$ commuting with the copy.

*Proof.* A real structure would have square plus one, and the square is minus one up to a positive scalar.

**Corollary.** The module carries a quaternionic structure, and its real dimension is eight.

*Proof.* An anti-linear map of square $-c\,\mathrm I$ with $c>0$ defines the action of the quaternion units $J$ with $J^{2}=-1$; the complex dimension four then gives the real dimension eight.

**The reading.** The sign is the invariant. It is computed on the half-integer label, and it is the same sign that makes the module change sign after a full turn: a half-integer module is quaternionic, and this is one fact and not two.

## The Type of the Module

**Proposition.** The type of a simple module of the copy is decided by its label: half-integer labels are quaternionic, integer labels are real, and the complex type does not occur for this group.

*Proof.* For the label $j$ the sign of the square of the intertwiner is $(-1)^{2j}$; it is negative for half-integer $j$ and positive for integer $j$. The two cases exhaust the possibilities, so no module of complex type occurs.

**Corollary.** The module of the operators is quaternionic and the carriers of the sixteen are real.

*Proof.* The module has label $\tfrac32$, and the four carriers have the integer labels $3,2,1,0$.

**Corollary.** The real dimensions of the carriers are seven, five, three and one, equal to their complex dimensions.

*Proof.* A real module of complex dimension $d$ has real dimension $d$.

**The reading.** The two rows of the theory have different types at the module and the same type at the algebra. The elements act on a quaternionic spinor space; the operators act on a quaternionic module of twice the label; and the carriers, being integer, are real.

## The Integer Carriers

**Theorem.** Each carrier of the sixteen admits a real structure, and the real structure is unique up to sign.

*Proof.* The sign of the square of the intertwiner is positive for an integer label, so the map can be normalised to square $+\mathrm I$; the uniqueness is again the multiplicity one.

**Corollary.** The fixed space of the real structure of a carrier has the dimension of the carrier, and the carrier is the complexification of a real space of that dimension.

*Proof.* A real structure with square $+\mathrm I$ has a fixed space of half the real dimension, that is, of the complex dimension.

**Corollary.** The three carriers of positive label carry real forms of dimensions seven, five and three, and the scalar carrier carries a real form of dimension one.

*Proof.* The dimensions of the carriers, and the theorem.

**The reading.** The integer labels are exactly the labels on which a real form exists. This is why the algebra of the operators can be read over the reals while its module cannot, and the reason is the half-integer of the module.

## The Trichotomy

**Proposition.** Every simple module of the copy is of exactly one of three types: real, quaternionic, or complex, according to the sign of the square of the intertwiner and to the existence of an invariant anti-linear map.

*Proof.* The three cases are the positive sign, the negative sign, and the absence of any anti-linear intertwiner; the last case does not occur here because the module is self-conjugate.

**Corollary.** The five labels of the two rows fall into the trichotomy as follows: the two half-integers are quaternionic, the five integers are real, and none is complex.

*Proof.* The two modules of the rows have labels $\tfrac12$ and $\tfrac32$; the carriers have labels $0,1$ in the first row and $0,1,2,3$ in the second.

**Corollary.** A statement about a real form of the module of the operators is false, while the same statement for a carrier is true, and the two statements differ by the parity of one label.

*Proof.* The parity of the label decides the sign of the square of the intertwiner.

**The reading.** The trichotomy is read on the five labels of the two rows: two half-integers, five integers, three types with one empty. The emptiness is a theorem about this group and not an accident, and it is the reason the module of the operators is quaternionic.

## Further Reading

- [The Four Weights of the Module and the Half Angle](the-four-weights-of-the-module-and-the-half-angle.html), for the half-integer weights.
- [The Spin Group: the Principal Copy, $\operatorname{Sym}^{3}$ and the Kernel $\{\pm\mathrm I\}$](the-spin-group-the-principal-copy-and-the-kernel.html), for the copy and its modules.
- [The Complex Numbers](the-complex-numbers.html), for the conjugation used in the anti-linear maps.
- [Conjugate-Linear Maps and the Conjugate Dual](conjugate-linear-maps-and-the-conjugate-dual.html), for the anti-linear maps of the operator space.
