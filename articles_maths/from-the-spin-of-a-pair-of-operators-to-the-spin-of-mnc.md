# __From the Spin of a Pair of Operators to the Spin of $M_n(\mathbb{C})$__

## Introduction

**The question.** In the biquaternion series the spin content of the algebra was reached from a pair of rotors acting on the two sides. What is the general-$n$ form of that passage, and what does it produce?

**The answer in one line.** The pair $(L_g,R_h)$ is a pair of commuting copies of the principal $SU(2)$, the diagonal is the conjugation action, and the Clebsch–Gordan rule applied to $V_j\boxtimes V_j$ with $j=\tfrac{n-1}{2}$ gives $M_n=\bigoplus_{k=0}^{n-1}V_k$.

**Why the article is needed.** The biquaternion passage begins with the pair of rotors and ends with the three labels $0,\tfrac12,1$. At general $n$ the same passage begins with a pair and ends with a list of $n$ integer labels. The step that produces the list must be separated from the step that produces the pair, and the separation is what this article records.

**Boundaries.** The theorem about the decomposition is *The Spin Decomposition of $M_n(\mathbb{C})$* and is quoted, not reproved, here. The operators themselves are *The One-Sided Operators of $M_n(\mathbb{C})$* and *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*. The biquaternion original is *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*.

**Conventions.** $L_A(X)=AX$, $R_B(X)=XB$, $T_{A,B}=L_AR_B$. The principal copy is the image of $\operatorname{Sym}^{n-1}$, and $j=\tfrac{n-1}{2}$ throughout. The weights of the module are $m_a=j-a$ for $a=0,\dots,n-1$.

## The Pair

**Proposition.** The left and right copies commute, $[L_X,R_Y]=0$ for all $X,Y$, and $X\mapsto L_X-R_X$ is the adjoint action of $\mathfrak{gl}_n$ on itself.

*Proof.* $L_XR_Y(Z)=XZY=R_YL_X(Z)$, and $L_X-R_X$ sends $Z$ to $XZ-ZX$. $\square$

**The two copies.** $X\mapsto L_X$ is a Lie algebra isomorphism onto its image, and $Y\mapsto-R_Y$ is one too, since $[R_Y,R_Z]=R_{[Z,Y]}$. So the pair spans $\mathfrak{gl}_n\oplus\mathfrak{gl}_n$ of dimension $2n^2$, and the diagonal is the adjoint copy.

**The diagonal is the principal copy.** Restricting the diagonal to the principal $\mathfrak{su}_2\subset\mathfrak{gl}_n$ gives the conjugation action whose carrier structure is the theorem of *The Spin Decomposition of $M_n(\mathbb{C})$*.

**The consequence.** The passage from a pair to a single action is restriction to the diagonal. Statements about the spin of the algebra are statements about the diagonal; statements about the pair are statements about two independent labels.

## The Pair's Content

**Proposition.** Under the left and right copies of the principal $SU(2)$ the algebra is the external tensor product $M_n\cong V_j\boxtimes V_j$, of dimension $(2j+1)^2=n^2$.

*Proof.* The left copy acts on the first factor of $M_n=\mathbb{C}^n\otimes(\mathbb{C}^n)^{*}$, the right copy on the second, and both factors are $V_j$. $\square$

**The weights of the pair.** The matrix unit $E_{ab}$ carries the pair of weights $(m_a,-m_b)$: it is raised by $L$ in the first index and lowered by $R$ in the second.

*Proof.* $J_zE_{ab}=m_aE_{ab}$ and $-E_{ab}J_z=-m_bE_{ab}$. $\square$

**The diagonal weights.** Restricting to the diagonal adds the two labels, giving $d=m_a-m_b$, the difference set of the module's weights.

**The multiplicity.** The difference $d$ occurs $n-\lvert d\rvert$ times, which is the weight multiset of $\bigoplus_{k=0}^{n-1}V_k$.

## The Passage to the Algebra

**Theorem (quoted).** $M_n=\bigoplus_{k=0}^{n-1}V_k$ under the diagonal principal copy, each carrier once, and $\mathfrak{sl}_n=\bigoplus_{k=1}^{n-1}V_k$.

**Two readings of one list.** The list $0,1,\dots,n-1$ is the Clebsch–Gordan content of $V_j\otimes V_j$, and it is also the list of multiplicities of the differences of weights. The theorem says the two readings agree, and either can serve as the definition.

**The maximal label.** The maximal diagonal label is $2j=n-1$, twice the module's label. This is the arithmetic reason a module of spin $j$ produces an algebra with a top carrier of spin $2j$.

**What the pair adds.** The pair distinguishes the two tensor factors; the diagonal forgets the distinction and keeps the sum. The information lost is the second label, and with it the possibility of separating the two sides.

## What the Biquaternion Case Is

**The values.** At $n=2$ one has $j=\tfrac12$, and the pair content is $V_{1/2}\boxtimes V_{1/2}=V_1\oplus V_0$, the list $1,0$ of the biquaternion algebra.

**The coincidence.** At $n=2$ the module's label is $\tfrac12$ and the diagonal's list is $1,0$: three numbers, the three labels of the biquaternion algebra. The pair's two labels both equal the module's label, so one half-integer describes the whole structure.

**The failure of the identification.** The diagonal's top label is $2j=n-1$ and the module's label is $j$, and these differ for every $n\ge2$. Identifying the spin of the module with the spin of the algebra is an error of a factor two even at $n=2$, where the module has label $\tfrac12$ and the top carrier has label $1$.

## The Real Reading

**The pair over $\mathbb{R}$.** At $n=2$ the biquaternion algebra is real of dimension four and the pair of rotors acts by real maps. At general $n$ the algebra is complex of dimension $n^2$, real of dimension $2n^2$, and the pair acts by complex linear maps, hence by real maps of twice the dimension.

**The consequence.** The real dimension of the carrier does not change the carriers: the complex decomposition $M_n=\bigoplus V_k$ is the same over $\mathbb{C}$ and over $\mathbb{R}$. What the biquaternion case emphasises is the pair of labels, not the real dimension.

**The honest statement.** The passage from a pair to the algebra is the same at every $n$. What changes is the length of the resulting list, which is $n$ rather than $3$.

## The Finite Check

Checked for $n=2,3,4,5$: the commutator $[L_X,R_Y]$ vanishes to $10^{-15}$ for random $X,Y$; the diagonal operator $L_{J_z}-R_{J_z}$ has the eigenvalues $d$ with multiplicity $n-\lvert d\rvert$, matching the difference multiset to $10^{-14}$; the identity $\sum_{k=0}^{n-1}(2k+1)=n^2$ holds at every $n$.

The pair's Lie algebra was checked by dimensions: the left copy is $n^2$-dimensional, the right copy is $n^2$-dimensional, and their intersection is the scalars, so the pair spans $2n^2-1$ dimensions, as $\mathfrak{gl}_n\oplus\mathfrak{gl}_n$ modulo the diagonal scalar requires.

## The Pair in Coordinates

**The difference.** $L_A-R_A=\operatorname{ad}_A$: the difference of the two sides is the bracket with the parameter.

**The sum.** $L_A+R_A$ is the anticommutator map $X\mapsto AX+XA$.

**The kernel.** $L_A+R_B=0$ for all arguments exactly when $B=-A$ and $A$ is scalar, so the pair is injective on the quotient of $M_n\oplus M_n$ by the diagonal line of scalars.

**The reading.** The pair contains the bracket and the anticommutator, and those two generate the whole algebra of the principal copy. That is the structural reason the passage to the algebra loses no spin content.

## The Casimir of the Pair

**The statement.** The Casimir $-\sum_i\operatorname{ad}_{J_i}^2$ (the $J_i$ anti-Hermitian) computed from the pair is the Casimir of the algebra, because the pair generates the algebra.

**The values.** $0,2,6,\dots,n(n-1)$, with multiplicities $1,3,\dots,2n-1$.

**The table.**

| $n$ | the values | the weighted sum |
|---|---|---|
| $2$ | $0,2$ | $8$ |
| $3$ | $0,2,6$ | $36$ |
| $4$ | $0,2,6,12$ | $96$ |
| $5$ | $0,2,6,12,20$ | $200$ |

**The reading.** The weighted sum is $\tfrac{n^2(n^2-1)}{2}$ in every row, and it is computed from the pair alone. The pair is therefore sufficient to recover the carrier structure, which is the claim of the article in one line.

## The Image and the Span

**The fibre.** $T_{A,B}=T_{A',B'}$ exactly when $A'=\lambda A$ and $B'=\lambda^{-1}B$ for some nonzero scalar $\lambda$.

**The dimension.** The map $(A,B)\mapsto T_{A,B}$ therefore has one-dimensional fibres, so its image has dimension $2n^2-1$, the same dimension as the span of the two copies.

**The span.** The linear span of the image is all of $\operatorname{End}(M_n)$, of dimension $n^4$: the family spans a space five times larger than itself at $n=2$ and twenty-five times larger at $n=4$.

**The reading.** The family of two-sided products is a cone of dimension $2n^2-1$ that spans an $n^4$-dimensional space. The pair is small, and the space it spans is large. The passage from the pair to the algebra is a passage from the cone to its span.

**The check.** The image's dimension was verified by the scalar fibre, and the span was verified by computing the rank of the $n^4\times 2n^2$ matrix of all matrix-unit products: the rank is $16,81,256,625$ for $n=2,3,4,5$.

## What the Pair Sees

**The algebra.** The pair determines the algebra it generates, and the algebra is $M_n$; the carrier structure is therefore determined by the pair.

**The parameters.** The pair does not determine its parameters, since $(A,B)$ and $(\lambda A,\lambda^{-1}B)$ give the same operator for every nonzero $\lambda$.

**The reading.** The pair sees the algebra and not the parameters. That is enough for the spin, because the spin is a property of the algebra and not of the parametrisation.

## The Notation

| symbol | meaning |
|---|---|
| $L_A$ | $X\mapsto AX$ |
| $R_B$ | $X\mapsto XB$ |
| $T_{A,B}$ | $X\mapsto AXB$ |
| $C$ | the Casimir $-\sum_i\operatorname{ad}_{J_i}^2$ |

**The use.** The argument uses $L$ and $R$ only through the algebra they generate, and that algebra is $M_n$. The Casimir is the invariant that makes the carriers visible, and it is computed from the pair without using anything else.

## Summary

The pair $(L,R)$ is two commuting copies of the principal copy, with the diagonal equal to the adjoint action. The pair's content is $V_j\boxtimes V_j$ and the diagonal's content is $\bigoplus_{k=0}^{n-1}V_k$. The maximal label doubles from $j$ to $2j=n-1$. At $n=2$ the three labels coincide with the biquaternion list; at $n\ge3$ they do not, and the pair keeps information the diagonal discards.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A,R_B$ | the left and right multiplications |
| $\mathfrak{gl}_n\oplus\mathfrak{gl}_n$ | the Lie algebra spanned by the pair |
| $V_j\boxtimes V_j$ | the external tensor product of the two copies |
| $m_a=j-a$ | the weights of the module |
| $d=m_a-m_b$ | the weights of the diagonal |

## Further Reading
- [The Spin Decomposition of $M_n(\mathbb{C})$: $n$ Carriers, One for Each Spin from $0$ to $n-1$](the-spin-decomposition-of-mnc.html), for the theorem quoted here.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the case $n=2$.
- [The One-Sided Operators of $M_n(\mathbb{C})$](the-one-sided-operators-of-mnc.html), for the left copy.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the two-sided family.
- [The Enveloping Operator Algebra of $M_n(\mathbb{C})$ and the Bi-module Structure](the-enveloping-operator-algebra-of-mnc.html), for the pair as an algebra.
- [The Spin Content of $M_4(\mathbb{C})$](the-spin-content-of-m4c.html), for the case $n=4$ in four readings.
