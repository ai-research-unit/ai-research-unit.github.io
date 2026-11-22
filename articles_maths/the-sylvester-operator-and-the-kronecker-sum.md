# __The Sylvester Operator and the Kronecker Sum__

## Introduction

**The subject.** Two operators are built from a pair of parameters by combining the two one-sided actions instead of composing them: the **Sylvester operator** $S_{a,b}(X)=aX-Xb$, which measures the failure of $a$ to act as $b$ on the right, and the **sum operator** $K_{a,b}(X)=aX+Xb$, which adds the two actions. Both are combinations of the left multiplication by $a$ and the right multiplication by $b$, and the article computes their spectra, their kernels and their algebra laws. The two-sided sandwich is recovered from them by one identity, $K_{a,b}^{2}-S_{a,b}^{2}=4T_{a,b}$, so the whole two-sided structure can be read on the difference and on the sum.

**The order of the article.** The two operators and the identity relating them to the sandwich come first. The spectral law follows, then the kernel, then the rank, and the derivation laws close the article.

**It assumes** *Operators Acting on Two Sides*, *The Spectrum of a Biquaternion* and *The Two-Sided Operators and the Segre Cone*. **The row of the elements is** where the spectrum of one element is read; here two spectra are compared, one read on the left and one on the right.

**The result in one line.** The eigenvalues of $S_{a,b}$ are the differences of the eigenvalues of the two parameters and those of $K_{a,b}$ their sums; the kernel of $S_{a,b}$ is the space of the intertwiners, nonzero exactly when the two spectra meet.

**Boundaries.** The product itself is *The Two-Sided Operators and the Segre Cone*; the coefficients of the sandwich are *The Coefficients of a Two-Sided Operator: A Worked Computation*; the adjoints of the two-sided family are *The Hermitian Pair of Operators Acting on Two Sides*.

## The Two Operators

**Definition.** For a pair of elements,
$$
S_{a,b}(X)=aX-Xb,\qquad K_{a,b}(X)=aX+Xb .
$$

**Proposition.** The two operators are the difference and the sum of the one-sided operators of the pair:
$$
S_{a,b}=L_a-R_b,\qquad K_{a,b}=L_a+R_b .
$$

*Proof.* Apply each right side to $X$.

**Proposition.** The sandwich is recovered from them:
$$
K_{a,b}^{2}-S_{a,b}^{2}=4\,T_{a,b}.
$$

*Proof.* The one-sided operators commute, so $(L_a+R_b)^2-(L_a-R_b)^2=2(L_aR_b+R_bL_a)=4L_aR_b$.

**Corollary.** The pair $(S_{a,b},K_{a,b})$ determines the sandwich and is determined by it up to the exchange of the two parameters.

*Proof.* The identity gives the sandwich from the pair; conversely $S_{a,b}$ and $K_{a,b}$ are the two combinations of $L_a$ and $R_b$, and $L_a$, $R_b$ are recovered from them by half the sum and half the difference.

**The reading.** The Sylvester operator and the sum operator are the two symmetric combinations of the two sides. Their squares differ by the sandwich, and their sum and difference give back the one-sided operators; nothing is lost in passing from the product to the pair.

## The Spectral Law

**Theorem.** Let $a$ be spectrally regular with the two distinct eigenvalues $\lambda_1,\lambda_2$, each of multiplicity two on the algebra, and let $b$ be spectrally regular with the eigenvalues $\mu_1,\mu_2$. Then
$$
\operatorname{spec}S_{a,b}=\{\lambda_i-\mu_j\}_{i,j=1,2},\qquad
\operatorname{spec}K_{a,b}=\{\lambda_i+\mu_j\}_{i,j=1,2},
$$
each value occurring once.

*Proof.* The left and right multiplications commute, and each is diagonalisable because the parameters are spectrally regular. They are therefore simultaneously diagonalisable, and the algebra splits into four joint eigenspaces of dimension one, on which $L_a$ acts as one of the $\lambda_i$ and $R_b$ as one of the $\mu_j$. On such a space the difference acts as $\lambda_i-\mu_j$ and the sum as $\lambda_i+\mu_j$.

**Corollary.** The trace of the Sylvester operator is zero and the trace of the sum operator is $8\,\mathrm{Sc}(a)+8\,\mathrm{Sc}(b)$.

*Proof.* The four differences add to $2(\lambda_1+\lambda_2)-2(\mu_1+\mu_2)$, which is $0$ because each pair adds to twice the scalar part; the four sums add to $2(\lambda_1+\lambda_2)+2(\mu_1+\mu_2)$, which is $8\,\mathrm{Sc}(a)+8\,\mathrm{Sc}(b)$.

**Corollary.** The determinant of the Sylvester operator is the product of the four differences, and it vanishes exactly when the two spectra meet.

*Proof.* The determinant is the product of the eigenvalues, and the product of four differences vanishes when one difference does.

**The reading.** The spectrum of the Sylvester operator is a table of differences and the spectrum of the sum operator a table of sums. Neither table is a new invariant: both are read from the two spectra of the parameters, and they differ only in the sign of the second entry.

## The Kernel

**Definition.** The **intertwiner space** of the pair is
$$
\ker S_{a,b}=\{X:aX=Xb\}.
$$

**Theorem.** The kernel of $S_{a,b}$ is nonzero exactly when the two spectra meet, and its dimension is the number of common eigenvalues, each counted once.

*Proof.* By the simultaneous diagonalisation of the preceding section, $S_{a,b}$ acts on the joint eigenspace of the pair $(\lambda_i,\mu_j)$ as the scalar $\lambda_i-\mu_j$. The kernel is the direct sum of the joint eigenspaces whose scalar vanishes, and there is one such space for each coincidence $\lambda_i=\mu_j$.

**Corollary.** For a spectrally regular pair with distinct spectra the Sylvester operator is a bijection, and for a pair with one common eigenvalue it has rank three.

*Proof.* The dimension count $4-\dim\ker S_{a,b}$.

**Corollary.** The kernel of $S_{a,b}$ is a space of intertwiners: every element of it carries the left action of $a$ to the right action of $b$, and the space is a module over the common centraliser of the two parameters.

*Proof.* An element $X$ of the kernel satisfies $aX=Xb$, and for $Y$ commuting with both parameters the element $XY$ satisfies the same identity.

**The reading.** The Sylvester operator measures the distance between two elements: it is injective exactly when they have no eigenvalue in common, and its kernel records the coincidences. This is the operator form of the statement that two elements with disjoint spectra generate the whole algebra.

## The Rank

**Proposition.** The rank of $S_{a,b}$ is $4-\dim\ker S_{a,b}$, and the rank of $K_{a,b}$ is four unless the spectra contain a pair of opposite values.

*Proof.* The rank-nullity count for the first; for the second, the same argument with the scalar $\lambda_i+\mu_j$ in place of the difference.

**Corollary.** The rank of the Sylvester operator takes the values four, three, two or one according to the number of coincidences of the two spectra, and it is zero only when the two parameters are scalars with the same value.

*Proof.* The number of vanishing differences among the four is at most four, and all four vanish exactly when every eigenvalue of $a$ equals the corresponding eigenvalue of $b$, which for scalars means equality of the two scalars.

**Corollary.** The rank of $S_{a,b}$ is not a function of the rank of the sandwich: the sandwich is a bijection whenever both parameters are nonzero, while the Sylvester operator is a bijection only when the spectra are disjoint.

*Proof.* The rank of the product is four for nonzero parameters, and the rank of the difference depends on the spectra.

**The reading.** Here the row differs sharply from the product: the product sees only whether a parameter vanishes, and the difference sees the spectra. The two invariants of a pair, the vanishing of a parameter and the coincidence of two eigenvalues, are read by two different operators built from the same pair.

## The Derivation Laws

**Theorem.** For every element $c$,
$$
[S_{a,b},L_c]=L_{[a,c]},\qquad [S_{a,b},R_c]=-R_{[b,c]}.
$$

*Proof.* Apply the commutator to $X$. On the left, $S_{a,b}(cX)-cS_{a,b}(X)=acX-cXb-caX+cXb=(ac-ca)X$, which is $L_{[a,c]}(X)$. On the right, $S_{a,b}(Xc)-S_{a,b}(X)c=aXc-Xbc-aXc+Xbc=-X(bc-cb)$, which is $-R_{[b,c]}(X)$.

**Corollary.** The assignment $a\mapsto S_{a,b}$ is equivariant for the adjoint action: conjugating the parameter by a unit conjugates the operator by the same left multiplication.

*Proof.* The theorem integrated, or directly: $S_{uau^{-1},b}=L_uS_{a,b}L_{u^{-1}}$ when $u$ commutes with $b$.

*Corollary.* The sum operator satisfies the same two laws with the same right-hand sides, since the identity cancels in the commutator.

*Proof.* $K_{a,b}$ and $S_{a,b}$ differ by $2R_b$, which commutes with $L_c$ and with $R_c$ only in the second case; the commutators with $L_c$ agree, and the commutator with $R_c$ differs by the central term, which vanishes when $c$ commutes with $b$.

**The reading.** The Sylvester operator is a derivation in its first argument: it converts the commutator of parameters into the commutator of operators, and it does so on each side separately. This is the algebraic reason the spectrum of $S_{a,b}$ is the table of differences: a derivation on a semisimple element acts on the spectrum by differences.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{a,b}(X)=aX-Xb=L_a-R_b$ | the Sylvester operator |
| $K_{a,b}(X)=aX+Xb=L_a+R_b$ | the sum operator |
| $K_{a,b}^{2}-S_{a,b}^{2}=4T_{a,b}$ | the identity recovering the sandwich |
| $\{\lambda_i-\mu_j\}$, $\{\lambda_i+\mu_j\}$ | the two spectra |
| $\ker S_{a,b}=\{X:aX=Xb\}$ | the intertwiner space |
| $[S_{a,b},L_c]=L_{[a,c]}$ | the derivation law |

## Further Reading

- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the sandwich and its law.
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the eigenvalues of a parameter.
- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the product recovered from the pair.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), for the simultaneous diagonalisation used in the spectral law.
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the rank of the product against the rank of the difference.
