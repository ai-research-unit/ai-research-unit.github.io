# __The Hermitian Pair of Operators Acting on One Side in $M_2(\mathbb{C})$__

## Introduction

**The question.** An operator is read together with its adjoint. When the adjoint is asked to stay on the same side, both members of the pair multiply on the left, and the pair is $(L_{\tilde Q},L_{\tilde Q^{\natural}})$. This article asks what that pair is as two $4\times4$ arrays, what its composite array is, what pair of equations it writes on the carrier, and why the placement does not preserve the two Hermitian sectors.

**Why it is the same statement.** This is the in-depth matrix reading of [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html). The source writes the pair, its pair of equations, the rewriting of the right actor into a left one and the closure of the pair to the norm; the display turns each statement into a statement about the arrays $\mathrm I_2\otimes A$ and $\mathrm I_2\otimes A^{\natural}$ and their product $\det(A)\,\mathrm I_4$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The two actors have the arrays $\mathrm I_2\otimes A$ and $A^{\mathsf T}\otimes\mathrm I_2$, and the three adjoints that stay on one side are the three operations on the parameter. The pair of equations $AX=Y$ and $XA^{\dagger}=Z$ is consistent exactly when $YA^{\dagger}=AZ$. The right actor is a left one in the dagger frame, $XA^{\dagger}=(AX^{\dagger})^{\dagger}$. The one-side pair composes to $\det(A)$ times the identity, $A^{\natural}=\det(A)A^{-1}$, and the composite is degenerate exactly on the singular cone. The two-component operator $\begin{pmatrix}0&\mathrm I_2\otimes A\\ \mathrm I_2\otimes A^{\natural}&0\end{pmatrix}$ squares to $\det(A)$ on $\mathbb{C}^8$, and its eigenvalues are $\pm\sqrt{\det A}$. The pair does not preserve the Hermitian sectors.

**What the article does not do.** It does not treat the two-side placement, which is [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html); it does not classify the four adjoints, which is [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html); and it does not treat the transposition rule itself, which is [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, with $N(\tilde Q)=\det A$. The arrays are the axis-free arrays $\mathrm I_2\otimes A$ and $A^{\mathsf T}\otimes\mathrm I_2$, by the canonical privilege of [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html); the Pauli arrays of [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html) are a translation. The conjugate $\natural$ is $A^{\natural}=\det(A)A^{-1}$ on invertible elements and $q\mapsto\mathrm E q$ on coefficients.

**Boundaries.** The two actors alone are [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html). The rotor action that the pair generates is [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $A=\mathsf M_2(\tilde Q)$ and $A^{\natural}=\mathsf M_2(\tilde Q^{\natural})$. The unknown is $X=\mathsf M_2(\tilde X)$ and the data are $Y=\mathsf M_2(\tilde Y)$ and $Z=\mathsf M_2(\tilde Z)$. The pair of equations is written $\mathcal P_A=(L_A,L_{A^{\natural}})$.

## The Two Actors

**The arrays.** For $A=\mathsf M_2(\tilde Q)$,

$$
L_A=\mathrm I_2\otimes A,\qquad R_A=A^{\mathsf T}\otimes\mathrm I_2 ,
$$

and they are the two families of [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html).

**The laws.** $L_AL_B=L_{AB}$ and $R_AR_B=R_{BA}$, and the two families commute, $L_AR_B=R_BL_A$, because both are $Y\mapsto AYB$. In arrays this is the Kronecker rule $(\mathrm I\otimes A)(\mathrm I\otimes B)=\mathrm I\otimes AB$ and $(A^{\mathsf T}\otimes\mathrm I)(B^{\mathsf T}\otimes\mathrm I)=(BA)^{\mathsf T}\otimes\mathrm I$.

**The adjoints that stay on one side.** Of the four adjoints only the quaternionic one and the Hermitian one keep the side:

$$
(L_A)^{\natural}=L_{A^{\natural}},\qquad (L_A)^{\ast}=L_{A^{\dagger}},\qquad (L_A)^{\natural\ast}=R_{\bar A},\qquad (L_A)^{\approx}=R_A .
$$

The first two replace the parameter and keep the side; the last two exchange the side. The Hermitian pair written on one side uses the first of them.

**The injectivity.** Each actor is injective, by the probe at the identity: $L_A(\mathrm I_2)=A$ and $R_A(\mathrm I_2)=A^{\mathsf T}$. In arrays, $\mathrm I_2\otimes A\neq0$ for $A\neq0$ and $A^{\mathsf T}\otimes\mathrm I_2\neq0$ for $A\neq0$.

## The Pair of Equations

**The system.** With one unknown $X$ and two data $Y,Z$,

$$
L_AX=Y,\qquad R_{A^{\dagger}}X=Z,
$$

that is $AX=Y$ and $XA^{\dagger}=Z$. The second parameter is tied to the first: it is the dagger and not an independent matrix.

**The consistency condition.** Multiplying the first equation on the right by $A^{\dagger}$ and the second on the left by $A$ gives the same left-hand side, so a solution requires

$$
YA^{\dagger}=AZ .
$$

**The solution.** For invertible $A$ the first equation gives $X=A^{-1}Y$, and the second holds exactly when $A^{-1}YA^{\dagger}=Z$, which is the condition. The solution is then unique.

**The singular case.** For singular $A$ the condition is necessary and not sufficient, because neither actor is surjective: the pair has either no solution or a solution set equal to one solution plus the left annihilator of $A$, which is the two-dimensional space $\{X:AX=0\}$ for $A$ of rank one.

**The product of the two members.** $L_AR_{A^{\dagger}}=\mathrm{Sd}_A$, the two-side member of [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), with the array $A^{\dagger\mathsf T}\otimes A$.

## Replacing the Right Actor by Its Transpose

**The identity.** The dagger is an anti-automorphism, so it interchanges the two actors:

$$
R_{A^{\dagger}}=(-)^{\dagger}\,L_A\,(-)^{\dagger},
$$

that is $XA^{\dagger}=(AX^{\dagger})^{\dagger}$.

*Proof.* $(AX^{\dagger})^{\dagger}=XA^{\dagger}$ by the antimultiplicativity of the dagger, and the dagger is an involution on matrices.

**The rewritten pair.** Substituting in the second equation,

$$
AX=Y,\qquad AX^{\dagger}=Z^{\dagger}.
$$

Both members now multiply on the left by the **same** matrix $A$. The rewriting costs two things: the second equation constrains $X^{\dagger}$ and not $X$, so it is conjugate linear in the unknown, and the datum $Z$ has been replaced by $Z^{\dagger}$.

**The product of the rewritten pair.** Composing the two members returns the two-side operator,
$$
L_A\bigl((-)^{\dagger}L_A(-)^{\dagger}\bigr)=L_AR_{A^{\dagger}}=\mathrm{Sd}_A ,
$$
which is the exact sense in which the two placements are one pair: the same composite, read once with one actor of each family and once with two left actors and one dagger between them.

**The singular warning.** Dropping either dagger in the rewriting gives an equation that is false for every non-central parameter. The pair $AX=Y$ and $AX=Z$ is a different system, consistent only when $Y=Z$.

## The One-Side Pair

**The definition.** The one-side Hermitian pair is
$$
\mathcal P_A=\bigl(L_A,\,L_{A^{\natural}}\bigr),\qquad A^{\natural}=\det(A)A^{-1},
$$
and the family is complex-linear in $A$: it is a complex space of complex dimension four.

**The closure.** For every $A$,

$$
L_AL_{A^{\natural}}=L_{A^{\natural}}L_A=\det(A)\,\mathrm I_4 .
$$

*Proof.* $A^{\natural}$ is the cofactor matrix, so $AA^{\natural}=A^{\natural}A=\det(A)\mathrm I_2$, and the Kronecker product gives $\mathrm I_2\otimes\det(A)\mathrm I_2=\det(A)\mathrm I_4$. The residual on a hundred random $A$ is $4\cdot10^{-15}$.

**The pair of equations.** $AX=Y$ and $A^{\natural}X=Z$. Both are linear in $X$ and both multiply on the left, and the pair composes to the scalar $\det(A)$. The consistency condition is $Z=\det(A)A^{-2}Y$ for invertible $A$, and the solution is $X=A^{-1}Y$.

**The second order and the mass.** A single left multiplication is first order. The composite of the pair is the scalar $\det(A)$, which is the norm $N(\tilde Q)$, so the pair of two first-order conditions is one second-order operator with mass $\det(A)$. The norm is invariant under $\natural$, so the two members compose to the same scalar in either order.

**The degeneracy.** $\det(A)=0$ exactly on the singular cone, which is the zero-divisor cone of the algebra under the display. There the composite is the zero operator, the pair degenerates and the two equations are solved one at a time. The pair is non-degenerate exactly on $\mathrm{GL}_2(\mathbb{C})$.

**The other tie.** The pair $(L_A,L_{A^{\dagger}})$ is a different object: its composite is $L_{AA^{\dagger}}$, whose array $\mathrm I_2\otimes AA^{\dagger}$ is a positive definite Hermitian operator and not a scalar. The $\natural$-pair composes to the centre and the $\dagger$-pair composes to the Hermitian sector, and that difference is the reason the corpus writes the first here and the second in the two-side operator.

## The Two-Component Reading

**The operator.** On $\mathbb{C}^4\oplus\mathbb{C}^4$ the pair acts by $(X_1,X_2)\mapsto(L_AX_2,L_{A^{\natural}}X_1)$, with the array

$$
\mathcal B_A=\begin{pmatrix}0&\mathrm I_2\otimes A\\[2pt]\mathrm I_2\otimes A^{\natural}&0\end{pmatrix},
\qquad \mathcal B_A\in M_8(\mathbb{C}).
$$

**The square.** $\mathcal B_A^2=\det(A)\,\mathrm I_8$, with residual $4\cdot10^{-15}$ on a hundred random $A$.

**The eigenvalue problem.** $\mathcal B_A\Xi=\lambda\Xi$ reads $AX_2=\lambda X_1$ and $A^{\natural}X_1=\lambda X_2$, and its square gives

$$
\bigl(\det(A)-\lambda^2\bigr)X_1=0,\qquad \bigl(\det(A)-\lambda^2\bigr)X_2=0 .
$$

So the second-order equation for each component is a consequence of the first-order pair, and the eigenvalues are $\lambda=\pm\sqrt{\det A}$, each with multiplicity four. The square root is a square root of the complex number $\det A$ and not of a modulus.

**The reading.** Two first-order conditions, one second-order consequence, one central scalar. The eigenvalue $\pm\sqrt{\det A}$ is the mass of the pair written as a spectral value.

**The limit of the identification.** The tie $\natural$ is an adjoint on the algebra and not on a space of fields, so the eigenvalue problem is an element-level statement and carries no claim about an adjoint on fields.

## What the Placement Does Not Give

**The proposition.** $L_A$ maps the skew-Hermitian sector $\mathfrak{K}$ into itself exactly when $A$ is a real scalar, and the same holds for $R_A$.

*Proof.* For $X^{\dagger}=-X$ the image $AX$ has dagger $X^{\dagger}A^{\dagger}=-XA^{\dagger}$, so the image is skew exactly when $XA^{\dagger}=AX$ for every skew $X$. At $X=i\mathrm I_2$ this gives $A^{\dagger}=A$. At $X=\sigma_1,\sigma_2,\sigma_3$ it then gives $\sigma_kA=A\sigma_k$, so $A$ commutes with a spanning set and is central. A Hermitian central matrix is a real multiple of the identity, and a real multiple of the identity preserves $\mathfrak{K}$.

**The reading.** Neither member of the one-side pair preserves a sector except at a real scalar parameter, so the pair as a whole does not preserve one either. Sector stability belongs to the two-side placement, where the conjugate linearity occurs once in each slot and cancels, by [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html).

**What the placement does give.** The pair is complex-linear in its parameter, so parameters superpose; its composite is central, so two first-order conditions give one scalar second-order operator; and both members act on the left, so a computation uses one anti-automorphism at most.

## Where $n=2$ Differs

**The arrays.** At $n=2$ the pair is two $4\times4$ arrays and the two-component operator is $8\times8$. At order $n$ the pair is two $n^2\times n^2$ arrays and the two-component operator is $2n^2\times2n^2$. Nothing in the closure changes: $L_AL_{A^{\natural}}=\det(A)\mathrm I_{n^2}$.

**The eigenvalues.** At $n=2$ the spectrum of $\mathcal B_A$ is $\pm\sqrt{\det A}$ with multiplicity four, that is $n^2$ copies of each sign. At order $n$ it is the same with multiplicity $n^2$.

**The singular cone.** At $n=2$ the cone is the singular $2\times2$ matrices, of complex dimension two. At order $n$ it is the singular $n\times n$ matrices, of complex dimension $n^2-1$.

**Nothing else differs.** The two actors, the pair of equations, the rewriting and the closure hold at every order with the same proofs.

## Summary

The one-side Hermitian pair of the display is the pair of arrays $\mathrm I_2\otimes A$ and $\mathrm I_2\otimes A^{\natural}$, with $A^{\natural}=\det(A)A^{-1}$. The pair writes the equations $AX=Y$ and $A^{\natural}X=Z$, both linear in the unknown, and it is consistent exactly when $Z=\det(A)A^{-2}Y$ for invertible $A$.

The pair composes to the scalar $\det(A)$, which is the norm of the element, so two first-order conditions give one second-order operator with mass $\det(A)$. The composite vanishes exactly on the singular cone, which is the zero-divisor cone of the algebra.

The two-component operator $\mathcal B_A$ squares to $\det(A)\mathrm I_8$, its eigenvalues are $\pm\sqrt{\det A}$ each with multiplicity four, and the second-order equation for each component is a consequence of the pair. The right member of the pair is the left member in the dagger frame, $XA^{\dagger}=(AX^{\dagger})^{\dagger}$, at the price of a conjugate-linear unknown.

The placement does not preserve the Hermitian sectors: a single left multiplication preserves a sector only at a real scalar parameter. Sector stability is the warrant of the two-side placement.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_A,R_A$ | the left and right actors, $\mathrm I_2\otimes A$ and $A^{\mathsf T}\otimes\mathrm I_2$ |
| $A^{\natural}=\det(A)A^{-1}$ | the natural conjugate |
| $\mathcal P_A=(L_A,L_{A^{\natural}})$ | the one-side Hermitian pair |
| $\mathcal B_A$ | the two-component operator on $\mathbb{C}^8$ |
| $\mathfrak{K}$ | the skew-Hermitian sector |
| $\det(A)=N(\tilde Q)$ | the norm, the mass of the pair |

## Further Reading

- [The Hermitian Pair of Operators Acting on One Side](the-hermitian-pair-of-operators-acting-on-one-side.html), for the source pair, its equations and the rewriting.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), for the placement that preserves the sectors.
- [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html), for the two actors and their laws.
- [Adjoint Pair of $L$ and $R$ Operators in $M_2(\mathbb{C})$](adjoint-pair-of-l-and-r-operators-in-m2c.html), for the four adjoints.
- [The Transposition of the Two Sides in $M_2(\mathbb{C})$](the-transposition-of-the-two-sides-in-m2c.html), for the anti-automorphism rule.
