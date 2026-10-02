# __The General Spectral Theorem on a Krein Space__

## Introduction

A Krein space is a Hilbert space carrying a second, indefinite inner product $[x,y]=\langle Jx,y\rangle$ given by a fundamental symmetry $J$. Self-adjointness is read with respect to the indefinite form, and the operator that satisfies it, the $J$-self-adjoint operator, need not have real spectrum: the indefiniteness admits non-real eigenvalues, and the classical spectral theorem fails in the form in which it holds for a Hilbert space. The general spectral theorem repairs the failure by two complementary statements. If the indefiniteness has finite rank — a Pontryagin space — then the non-real spectrum is finite, of total multiplicity no larger than the rank, and a projection-valued **spectral function** on the real line still integrates the operator; the source of the finitely many exceptional points is the negative part of the form. If instead the operator is definite, meaning its quadratic form $[Ax,x]$ is bounded below by a positive multiple of the fundamental form, then the indefinite metric is equivalent to the definite one and the operator is similar to a self-adjoint operator on the Hilbert space, so the classical spectral theorem returns through the similarity. This article states both faces of the theorem, the finite-rank case and the definite case, together with the resolvent and the invariants.

This article fixes the Krein space with its fundamental decomposition and symmetry, $J$-self-adjoint and self-adjoint operators, the general spectral theorem in a Pontryagin space, the definite case and the similarity theorem, and the invariants that the theorem produces. The Krein space, its fundamental symmetry and its $J$-unitary group are *Krein Spaces*; the Hilbert-space spectral theory is *Self-Adjoint Operators and the Spectral Theorem* and *The Spectral Operator*; the self-adjointness in the indefinite metric of the sandwich is *The Signed Sandwich on a Krein Space*; the projections and the invariance are *Projections and the Fundamental Decomposition of a Krein Space*, where the geometry of the negative part is developed.

Throughout, $K=K_+\oplus K_-$ is a Krein space over $\mathbb{C}$ with fundamental decomposition, $J=P_+-P_-$ is the **fundamental symmetry**, $[x,y]=\langle Jx,y\rangle$ is the indefinite inner product, and the underlying Hilbert space is the completion $H=K_+\oplus K_-$; the space is a **Pontryagin space** $\Pi_\kappa$ when $\kappa=\dim K_-$ is finite. The adjoint in the indefinite metric is $A^{[*]}=JA^*J$, and $A$ is **self-adjoint in the Krein space**, or $J$-self-adjoint, if $A^{[*]}=A$, equivalently $[Ax,y]=[x,Ay]$ for all $x,y$; the $J$-unitary group is $\mathcal{U}_J=\{U:U^{[*]}U=UU^{[*]}=I\}$.

## The Krein Space and the Indefinite Adjoint

**Proposition (the fundamental symmetry).** $J$ is a bounded self-adjoint unitary of $H$ with $J^2=I$ and $J=J^*=J^{-1}$, the form $[\cdot,\cdot]$ is Hermitian and nondegenerate but not definite, $[x,x]$ is positive on $K_+$ and negative on $K_-$, and a different choice of fundamental decomposition replaces $J$ by $VJV^{-1}$ for a bounded invertible $V$, so the pair $(H,J)$ is determined up to similarity.

*Proof.* $P_\pm$ are orthogonal projections with $P_+P_-=0$ and $P_++P_-=I$, so $J^2=P_++P_-=I$ and $J=J^*$; the form is Hermitian because $J$ is self-adjoint, nondegenerate because $J$ is invertible, and the signs are the definitions of the two pieces; the change of decomposition is the usual change of fundamental symmetry by an invertible operator.

**Definition.** For $A\in B(K)$ the **indefinite adjoint** is $A^{[*]}=JA^*J$, and the operator $A$ is **self-adjoint in the Krein space** if $A^{[*]}=A$; it is **$J$-unitary** if $A^{[*]}A=AA^{[*]}=I$.

**Proposition (the indefinite adjoint).** The operation $A\mapsto A^{[*]}$ is a conjugate-linear involution of $B(K)$, it satisfies $(AB)^{[*]}=B^{[*]}A^{[*]}$ and $(A^{[*]})^{[*]}=A$, and $A$ is self-adjoint in the Krein space exactly when $JA$ is self-adjoint in the Hilbert space; the spectrum of a self-adjoint operator is symmetric with respect to the real axis, $\sigma(A^{[*]})=\overline{\sigma(A)}=\sigma(A)$, and the Jordan structure at a non-real eigenvalue mirrors its conjugate.

*Proof.* The identities are the corresponding identities for the Hilbert-space adjoint conjugated by $J$; the self-adjointness criterion is $JA^*J=A$, that is $(JA)^*=JA$; the spectral symmetry is the adjoint spectral identity $\sigma(A^*)=\overline{\sigma(A)}$ together with $A^*=J A J^{-1}$, which makes $A$ similar to its own adjoint.

**Remark (the bounded representative).** Writing the operator of a Pontryagin space in blocks $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $a:K_+\to K_+$ and so on, the indefinite adjoint is

$$
A^{[*]}=\begin{pmatrix}a^*&-c^*\\-b^*&d^*\end{pmatrix},
$$

so self-adjointness in the Krein space is the pair of conditions $a=a^*$, $d=d^*$, $c=-b^*$; the off-diagonal pair is skew rather than symmetric, and this skewness is the entire difference from the Hilbert-space case.

## The General Spectral Theorem in a Pontryagin Space

**Theorem (Pontryagin's theorem).** Let $A$ be a bounded self-adjoint operator in a Pontryagin space $\Pi_\kappa$ with finite $\kappa=\dim K_-$. Then $\sigma(A)\cap(\mathbb{C}\setminus\mathbb{R})$ is finite, it consists of at most $\kappa$ eigenvalues counted with algebraic multiplicity, the operator has $A$-invariant subspaces $K_\pm$ of dimensions $\dim K_\pm$ on which the form is definite, and the real spectrum is invariant under the reflection splitting the operator into a self-adjoint part on a Hilbert space and a finite-dimensional indefinite part.

*Proof.* The negative part $K_-$ has dimension $\kappa$, and the restriction of $A$ to the $A$-invariant negative subspace is the source of the non-real eigenvalues, whose number is bounded by $\kappa$ by the defect formula for the resolvent; the existence of the invariant maximal definite subspaces is Pontryagin's isotropic subspace theorem, and the splitting of the real spectrum follows from the decomposition of the space into a Hilbert part and a finite-dimensional part.

**Theorem (the general spectral theorem).** Let $A$ be a bounded self-adjoint operator in $\Pi_\kappa$. Then there is a **spectral function** $E$, defined on the Borel subsets of $\mathbb{R}\setminus\overline{W_0}$ for a finite exceptional set $W_0$ containing the non-real eigenvalues and their closures, with values in the self-adjoint projections of the Krein space, satisfying

$$
E(\varnothing)=0,\qquad E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2),\qquad E(\Delta)^{[*]}=E(\Delta),
$$

and the operator is the strong integral

$$
A=\int_{\mathbb{R}}\lambda\,dE(\lambda)+\text{a finite-dimensional correction on }\operatorname{span}(W_0),
$$

the integral converging in the strong operator topology; on each of the two definite parts the spectral function is that of a self-adjoint operator on a Hilbert space, and on the finite-dimensional part it is the spectral resolution of the finite matrix.

*Proof.* The space splits into a Hilbert part and a finite-dimensional part as in the previous theorem; the spectral theorem on the Hilbert part is the classical one of *Self-Adjoint Operators and the Spectral Theorem*, the finite-dimensional part has its Jordan resolution, and the two assemble into the spectral function of the statement. The multiplicativity and the indefinite self-adjointness of $E$ are the corresponding properties on each piece, and the integral is the sum of the two integrals.

**Corollary (the resolvent and the eigenvalues).** The resolvent $(A-z)^{-1}$ is analytic off $\sigma(A)$, the non-real spectrum consists of the finitely many exceptional points, and the real spectrum is the support of the spectral function; a point $\lambda\in\mathbb{R}$ is an eigenvalue exactly when $E(\{\lambda\})\neq0$, and the algebraic multiplicity of a non-real eigenvalue is at most $\kappa$.

*Proof.* Analyticity is the resolvent identity; the support statement is the definition of the spectral function; the eigenvalue criterion and the multiplicity bound are the finite-dimensional and Pontryagin statements.

## The Definite Case

**Definition.** A self-adjoint operator $A$ in the Krein space is **definite** if its quadratic form dominates the indefinite form,

$$
[Ax,x]\ge c\,[x,x]\quad\text{or}\quad [Ax,x]\le c\,[x,x]\quad(x\in K),
$$

for a constant $c$, with a fixed sign; it is **uniformly positive** if $[Ax,x]\ge \varepsilon[x,x]$ for some $\varepsilon>0$ and all $x$.

**Theorem (Krein's similarity theorem).** Let $A$ be a bounded self-adjoint operator in a Krein space and suppose $[Ax,x]\ge\varepsilon[x,x]$ for all $x$ and some $\varepsilon>0$. Then there is a bounded invertible operator $V$ and a self-adjoint operator $B$ on the Hilbert space $H$ with

$$
A=V^{-1}BV,
$$

and $A$ has a spectral function whose integral represents $A$; consequently the spectral theorem in the form of the existence of a resolution of the identity holds for $A$ on the whole real line and the non-real spectrum is empty.

*Proof.* The inequality makes the form $[Ax,\cdot]$ a positive definite inner product equivalent to $\langle\cdot,\cdot\rangle$, and the representing operator $V$ of this inner product is bounded and invertible by the equivalence; conjugating by $V$ replaces $A$ by the Hilbert-space self-adjoint operator $B=VAV^{-1}$, whose spectral theorem is classical. The spectral function of $B$ is transported back by $V$ and is self-adjoint in the indefinite metric; the absence of non-real spectrum is the reality of the spectrum of $B$ together with the similarity.

**Corollary (the uniformly positive case).** A uniformly positive self-adjoint operator in a Krein space has a spectral function $E$ on the real line with

$$
A=\int_{\mathbb{R}}\lambda\,dE(\lambda),\qquad E(\Delta)^{[*]}=E(\Delta),
$$

and the $J$-orthogonal projections $E(\Delta)$ form a resolution of the identity in the indefinite metric; the operator generates a bounded group $e^{itA}$ for $t\in\mathbb{R}$ and the group is $J$-unitary exactly when $A$ is self-adjoint in the Krein space.

*Proof.* The spectral function is the transported one of the previous theorem; the group statement follows from the functional calculus in the definite metric, and the $J$-unitarity of $e^{itA}$ is the computation $e^{itA}e^{-itA}=I$ with the indefinite adjoint $(e^{itA})^{[*]}=e^{itA^{[*]}}=e^{itA}$.

**Example (the finite-dimensional metric).** On $\mathbb{C}^2$ with the form $[x,y]=x_1\bar y_1-x_2\bar y_2$ the diagonal matrix $\operatorname{diag}(2,1)$ is self-adjoint in the Krein space and uniformly positive, since $[Ax,x]=2|x_1|^2-|x_2|^2\ge|x_1|^2-|x_2|^2=[x,x]$; its eigenvalues $2$ and $1$ are real and positive, and it is the definite case in its simplest form. The matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ is self-adjoint in the Krein space, since $c=-1=-b^*$, and its eigenvalues are $\pm i$; it is the simplest indefinite self-adjoint operator with non-real spectrum, and it shows that the general spectral theorem must exclude the non-real points.

**Example (the Pontryagin space $\Pi_1$).** In a Pontryagin space of rank one at most one non-real eigenvalue of a self-adjoint operator occurs, counting algebraic multiplicity; the spectral function is defined on the real line minus that point, and the rank-one exceptional set is the smallest instance of the general theorem, illustrating that the failure of the Hilbert-space spectral theory is confined to the negative directions.

## Summary

A Krein space is a Hilbert space with a fundamental symmetry $J=J^*=J^{-1}$ and indefinite form $[x,y]=\langle Jx,y\rangle$; the indefinite adjoint is $A^{[*]}=JA^*J$ and self-adjointness in the Krein space is $A^{[*]}=A$, equivalently the self-adjointness of $JA$ in the Hilbert space, so the spectrum of such an operator is symmetric with respect to the real axis and the operators are those whose blocks satisfy $a=a^*$, $d=d^*$, $c=-b^*$. The general spectral theorem states that a bounded self-adjoint operator in a Pontryagin space $\Pi_\kappa$ has at most $\kappa$ non-real eigenvalues counted with multiplicity, admits a projection-valued spectral function $E$ on the real line outside the finite exceptional set, self-adjoint in the indefinite metric with $E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2)$, and is represented by the strong integral of $\lambda\,dE(\lambda)$ together with a finite-dimensional correction. If instead the operator is uniformly positive, $[Ax,x]\ge\varepsilon[x,x]$, then by Krein's similarity theorem it is $V^{-1}BV$ for a Hilbert-space self-adjoint $B$, the non-real spectrum is empty, the spectral function exists on the whole real line and generates a $J$-unitary group $e^{itA}$; so the general theorem has the finite-rank face, in which the indefinite metric costs finitely many exceptional points, and the definite face, in which the indefinite metric costs only a similarity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $J=P_+-P_-$ | fundamental symmetry, $J^2=I$, $J=J^*$ |
| $[x,y]=\langle Jx,y\rangle$ | indefinite inner product |
| $\Pi_\kappa$ | Pontryagin space with $\kappa=\dim K_-<\infty$ |
| $A^{[*]}=JA^*J$ | the indefinite adjoint |
| $A^{[*]}=A$ | self-adjoint in the Krein space |
| $c=-b^*$ | the skew off-diagonal condition |
| $E(\Delta)$ | spectral function, $E(\Delta_1\cap\Delta_2)=E(\Delta_1)E(\Delta_2)$ |
| $A=\int\lambda\,dE(\lambda)$ | general spectral theorem, up to a finite correction |
| at most $\kappa$ non-real eigenvalues | Pontryagin's theorem |
| $A=V^{-1}BV$ | Krein's similarity in the definite case |

## Further Reading

- Mark G. Krein and Heinz Langer, "On the Spectral Function of a Self-Adjoint Operator in a Space with Indefinite Metric", *Soviet Mathematics Doklady* **3** (1962), 404–406, for the general spectral theorem.
- Mark G. Krein and Yurii L. Shmulyan, "On Linear-Fractional Transformations with Operator Coefficients", *American Mathematical Society Translations* **103** (1974), 1–26, for the similarity theorem and the definite case.
- Heinz Langer, "Spectral Functions of Definitizable Operators in Krein Spaces", in *Functional Analysis*, Lecture Notes in Mathematics 948 (Springer, 1982), 1–46, for the spectral function and the definite operators.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the geometry, the Pontryagin spaces and the spectral theory.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the finite-dimensional theory and the examples.

