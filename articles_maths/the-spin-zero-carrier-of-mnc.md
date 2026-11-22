# __The Spin-Zero Carrier of $M_n(\mathbb{C})$: the Scalars__

## Introduction

**The question.** The decomposition $M_n=\bigoplus_{k=0}^{n-1}V_k$ has one summand of dimension one. What is it, why is it unique, and what is its role?

**The answer in one line.** $V_0=\mathbb{C}\mathrm I$ is the line of scalars; it is the unique invariant line; it is the line removed to form $\mathfrak{sl}_n$; and it is unique at every $n$ because the centre of $M_n$ is one-dimensional.

**Why the article is needed.** In the biquaternion series the spin-zero carrier is the centre $\mathbb{C}e_t$, and its uniqueness is proved by a computation with the rotors. At general $n$ the same statement follows from the simplicity of $M_n$, and the proof is shorter and stronger: a family of invariant lines would give a centre of dimension greater than one.

**Boundaries.** The whole decomposition is *The Spin Decomposition of $M_n(\mathbb{C})$*; the centre and the simplicity are *The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$*; the biquaternion original is *Introduction to the Spin-Zero Centre Subspace*.

**Conventions.** $V_0$ is the carrier of spin zero, of complex dimension $2\cdot0+1=1$. The principal copy acts by $X\mapsto gXg^{-1}$.

## The Carrier

**Proposition.** $V_0=\mathbb{C}\mathrm I$, and it is the fixed space of the principal copy.

*Proof.* The scalars are fixed by every conjugation. Conversely an element fixed by the whole copy commutes with the generators $J_x,J_y,J_z$, which generate $M_n$ as an algebra, hence is central, hence is a scalar. $\square$

**The dimension.** $\dim V_0=1$ at every $n$.

**The Casimir.** The operator $-\sum_i\operatorname{ad}_{J_i}^2$ (the $J_i$ anti-Hermitian) vanishes on $V_0$ and has the eigenvalue $k(k+1)$ on $V_k$; since $k(k+1)=0$ only for $k=0$, the zero eigenspace is exactly $V_0$.

*Proof.* $\operatorname{ad}_{J_i}$ annihilates the scalars, and $k\mapsto k(k+1)$ is injective on the nonnegative integers. $\square$

**The projection.** The orthogonal projection onto $V_0$ for the Hilbert–Schmidt form is $X\mapsto\frac{\operatorname{tr}X}{n}\mathrm I$.

*Proof.* $\langle X,\mathrm I\rangle=\operatorname{tr}X$ and $\lVert\mathrm I\rVert^2=n$. $\square$

## Why There Is Exactly One

**Theorem.** The invariant lines of $M_n$ under the principal copy form a single point of the projective space, the line $\mathbb{C}\mathrm I$.

*Proof.* An invariant line lies in some carrier. The carriers are $V_0,\dots,V_{n-1}$, with $V_0$ one-dimensional and the others of dimension $2k+1\ge3$. A line inside $V_k$ with $k\ge1$ would be a one-dimensional submodule of an irreducible module of dimension at least three, which is impossible. So the line is $V_0$. $\square$

**The centre argument.** The same conclusion follows from the centre: two invariant lines would give an invariant plane, hence two independent central elements, contradicting $\dim Z(M_n)=1$.

**The consequence.** There is no family of spin-zero carriers at any $n$. The multiplicity of $V_0$ is one, for a structural reason and not by a numerical accident.

## The Line Removed

**Proposition.** $\mathfrak{sl}_n=\bigoplus_{k=1}^{n-1}V_k$ and $M_n=\mathfrak{sl}_n\oplus V_0$ as modules.

*Proof.* $\mathfrak{sl}_n$ is the kernel of the trace, the scalars are its orthogonal complement for the Hilbert–Schmidt form, and the traceless part is the sum of the carriers with $k\ge1$. $\square$

**The dimension check.** $n^2-1=\sum_{k=1}^{n-1}(2k+1)$, both sides equal to $(n-1)(n+1)$.

**The reading.** Removing the spin-zero carrier is the same as removing the trace, and removing the trace is the same as passing to the simple algebra.

## The Operators on the Line

**The correct statement.** The diagonal operators $T_{g,g^{-1}}$ preserve $V_0$ and act on it trivially. The adjoint action annihilates it.

**The correction.** The statement that every $L_A$ preserves $V_0$ is false: $L_A(\mathrm I)=A$, which lies in the line only when $A$ is scalar. The one-sided families preserve the line only for scalar parameters.

**The reason.** $V_0$ is the carrier of the trivial representation, and only the operators that act by an algebra automorphism or a derivation respect a trivial submodule.

## The Comparison with the Biquaternion Algebra

**The same statement.** In $\mathbb{B}$ the spin-zero carrier is the centre, of complex dimension one, and it is the fixed line of the rotor action.

**The two proofs.** The biquaternion proof identifies the fixed space by a computation with the three carriers; the general proof uses that the generators generate the algebra. The second proof applies at $n=2$ as well, and it is the same argument in a shorter form.

**The difference in real dimension.** The centre of $M_n$ is one complex line, hence two real dimensions, at every $n$. The biquaternion centre is also a line over $\mathbb{C}$; the apparent difference of "a plane" in some real readings is a difference of the real form chosen, not of the carrier.

## The Finite Check

Computed for $n=2,3,4,5$: the Casimir $-\sum_i\operatorname{ad}_{J_i}^2$ has the eigenvalue $0$ with multiplicity exactly $1$, and the other eigenvalues $2,6,12,20$ with multiplicities $3,5,7,9$, so the zero eigenspace is one-dimensional at every $n$.

The fixed space was checked directly: the intersection of the kernels of $X\mapsto[J_x,X]$, $X\mapsto[J_y,X]$ and $X\mapsto[J_z,X]$ is one-dimensional, spanned by $\mathrm I$, at $n=2,3,4,5$.

The projection was checked: the residual of $\langle X-\frac{\operatorname{tr}X}{n}\mathrm I,\mathrm I\rangle=0$ is below $10^{-15}$.

## The Projection

**The formula.** $P_0(X)=\tfrac{\operatorname{tr}X}{n}\mathrm I$.

**The operator form.** As a Hilbert–Schmidt operator, $P_0=\tfrac{1}{n}\lvert\mathrm I\rangle\langle\mathrm I\lvert$, of rank one.

**The properties.** $P_0^2=P_0$, $P_0^{\dagger}=P_0$, and $P_0$ commutes with every $L_A$ and every $R_B$, because the trace is invariant under multiplication on either side.

**The reading.** The projection onto the scalars is the unique invariant projection of rank one, and it is the same at every $n$; no other carrier has a projection of this form.

## The Trace in the Frame

**The statement.** In the frame the projector has the entries $1/n$ in every position, its trace is one, and its Hilbert–Schmidt norm is one.

**The consequence.** The spin-zero carrier is the only carrier whose projector does not depend on the choice of a basis inside the carrier, since the carrier has no basis to choose.

**The reading.** The scalars are the one carrier that the decomposition identifies without any computation, and they are the line removed to form $\mathfrak{sl}_n$.

## The Vanishing Casimir

**The statement.** $-\sum_i\operatorname{ad}_{J_i}^2$ vanishes exactly on the scalars, because $k(k+1)=0$ only at $k=0$ for a nonnegative integer $k$.

**The kernel.** The eigenspace of the Casimir for the eigenvalue zero is one-dimensional at every $n$: $1,1,1,1$ for $n=2,3,4,5$.

**The reading.** The spin-zero carrier is the kernel of the Casimir, and the Casimir is the operator that produces the whole decomposition. The scalar line is the part of the algebra the Casimir cannot see.

## The Exact Sequence

**The statement.** $0\to V_0\to M_n\to\mathfrak{sl}_n\to0$, with the inclusion of the scalars and the trace as the projection, and the sequence splits because the trace gives a canonical section up to a scalar.

**The consequence.** $M_n=V_0\oplus\mathfrak{sl}_n$ as modules, and the splitting is the reason the decomposition of the algebra is the decomposition of the traceless part plus the scalars.

**The reading.** The spin-zero carrier is the one summand that the exact sequence adds, and it is the only summand that is not traceless.

## The Scalar in the Biquaternion Case

**The subspace.** The scalars of $M_2$ are the complex span of the identity, a complex line and a real plane.

**The biquaternion subalgebra.** The real scalars $a+\mathrm I b$ form a real two-dimensional subspace of the four-real-dimensional algebra, and they are the spin-zero carrier of that algebra.

**The reading.** The complex line of $M_2$ and the real plane of $\mathbb{B}$ are the same carrier read over two fields, and the doubling is the doubling of the field, not of the carrier.

## The Four Readings at $n=4$

| reading | position of $V_0$ |
|---|---|
| principal | one summand, dimension one |
| $U(4)$ | the trivial summand of $1\oplus15$ |
| factorised | $(0,0)$, dimension one |
| block | two copies, in $4V_1\oplus4V_0$ |

**The reading.** The scalar carrier survives all four readings with different multiplicities, and it is the only carrier that the block reading sees twice.

## The Count

**The numbers.** $V_0$ has dimension one against the $n^{2}$ of the algebra, and its share falls like $1/n^{2}$.

## Summary

The spin-zero carrier is the line of scalars. It is the fixed space of the principal copy, the unique invariant line, and the orthogonal complement of $\mathfrak{sl}_n$. It is unique at every $n$ because the centre is one-dimensional and because no carrier of dimension at least three contains an invariant line. It is preserved by the diagonal action and killed by the adjoint action; the one-sided families preserve it only for scalar parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_0$ | the carrier of spin zero, equal to $\mathbb{C}\mathrm I$ |
| $\frac{\operatorname{tr}X}{n}\mathrm I$ | the projection onto $V_0$ |
| $Z(M_n)=\mathbb{C}\mathrm I$ | the centre |
| $k(k+1)$ | the Casimir value, zero only at $k=0$ |

## Further Reading
- [The Spin Decomposition of $M_n(\mathbb{C})$: $n$ Carriers, One for Each Spin from $0$ to $n-1$](the-spin-decomposition-of-mnc.html), for the decomposition.
- [The Ideals, the Centre and the Simplicity of $M_n(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-mnc.html), for the centre.
- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the case $n=2$.
- [The Spin-One Carrier of $M_n(\mathbb{C})$: the Three-Dimensional $V_1$](the-spin-one-carrier-of-mnc.html), for the neighbouring carrier.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the trace.
- [Where the Half-Integers Go in $M_n(\mathbb{C})$](where-the-half-integers-go-in-mnc.html), for the labels that are not here.
