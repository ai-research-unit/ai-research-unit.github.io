# __The Adjoint of the Left Multiplication on a Linear Space__

## Introduction

The endomorphism algebra $E = \operatorname{End}_F(V)$ carries a pairing of its own, the **trace pairing** $\langle X,Y\rangle = \operatorname{tr}(XY)$, which needs no form and no choice: it is non-degenerate, symmetric and associative with respect to the multiplication of $E$, and it is the natural pairing of the category. With respect to it the left multiplication $L_A$ and the right multiplication $R_A$ are adjoint to one another, $(L_A)^{\dagger} = R_A$ and $(R_A)^{\dagger} = L_A$, which is the operator-level statement of the fact that the transpose of a matrix is the matrix of the transposed map. When $E$ also carries a pairing-based involution, the two operations relate by $(L_A)^{\dagger} = R_A$ and $L_A^{*} = R_{A^{*}}$, so the trace-adjoint and the involution differ by the involution of the parameter. This article develops the trace pairing, the adjointness of the left and right multiplications, and the compatibility with the involution.

The left and right multiplications on a group are *Left and Right Multiplication in a Group*; their analogues on an algebra are used in *Algebras of Endomorphisms*, where the commutant is built from them. The adjoint of a single endomorphism with respect to a pairing is *The Adjoint of an Endomorphism*, the unitary elements are *Unitary Endomorphisms*, and the pairing-based involution on $E$ is *Involutions of the Endomorphism Algebra*. The signed version of the left multiplication is *The Signed Left Multiplication on a Linear Space*, and its adjoint is *The Signed Adjoint of the Left Multiplication on a Linear Space*. The forms are Part II.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space of dimension $n$, $E = \operatorname{End}_F(V)$, and for $A \in E$ the left and right multiplications are

$$
L_A(X) = AX, \qquad R_A(X) = XA .
$$

The **trace pairing** is $\langle X,Y\rangle = \operatorname{tr}(XY)$, and the adjoint of an operator on $E$ with respect to it is written ${}^{\dagger}$. When $E$ carries a pairing-based involution the element involution is written ${}^{*}$, and the induced operator involution on $\operatorname{End}_F(E)$ is $S^{*}(X) = S(X^{*})^{*}$.

## The Trace Pairing

**Proposition.** The trace pairing on $E$ is bilinear, symmetric and non-degenerate:

$$
\langle X,Y\rangle = \langle Y,X\rangle, \qquad
\langle X,Y\rangle = 0 \ \text{for all } Y \implies X = 0 ,
$$

and it is associative with respect to the multiplication, $\langle XY,Z\rangle = \langle X,YZ\rangle$.

**Proof.** Symmetry is $\operatorname{tr}(XY) = \operatorname{tr}(YX)$; associativity is $\operatorname{tr}(XYZ)$, which is invariant under cyclic permutation of the factors. For non-degeneracy, if $X \neq 0$ choose $v$ with $Xv \neq 0$ and a functional $\varphi$ with $\varphi(Xv) = 1$; the endomorphism $Y = v\varphi$, $Y(w) = \varphi(w)v$, satisfies $\operatorname{tr}(XY) = \varphi(Xv) = 1$, so $X$ pairs nontrivially.

**Remark (the natural pairing of the category).** The trace pairing is the pairing that the category of endomorphisms carries without any further structure: it is defined for every finite-dimensional $V$, it is invariant under the isomorphism of $E$ with its opposite, and the adjointness it produces is the abstract form of transposition. The pairing-based adjoint articles use an extra form on $V$; this article uses none.

## The Left and Right Multiplications

**Proposition.** For $A,B \in E$,

$$
L_AL_B = L_{AB}, \qquad R_AR_B = R_{BA}, \qquad L_AR_B = R_BL_A , \qquad L_A + L_B = L_{A+B}, \qquad R_A+R_B = R_{A+B}.
$$

**Proof.** $(L_AL_B)(X) = A(BX) = (AB)X$; $(R_AR_B)(X) = (XA)B = X(AB) = R_{BA}(X)$; $L_AR_B(X) = A(XB) = (AX)B = R_BL_A(X)$; the additive statements are immediate. The identities exhibit $E$ acting on itself by left and right multiplication with the two actions commuting.

**Proposition (the trace-adjointness).** For every $A \in E$,

$$
(L_A)^{\dagger} = R_A, \qquad (R_A)^{\dagger} = L_A ,
$$

where ${}^{\dagger}$ is the adjoint with respect to the trace pairing.

**Proof.** $\langle L_AX,Y\rangle = \operatorname{tr}(AXY) = \operatorname{tr}(XYA) = \langle X, R_AY\rangle$ by the cyclic invariance of the trace; the uniqueness of the adjoint with respect to a non-degenerate pairing gives $(L_A)^{\dagger}=R_A$, and the second identity is the same computation read the other way.

**Corollary.** The set of operators on $E$ that are adjoint to a left multiplication is the set of right multiplications and conversely; a left multiplication is self-adjoint with respect to the trace pairing exactly when $A$ is central, and then $L_A = R_A$.

**Proof.** The first statement is the proposition; $L_A = R_A$ means $AX = XA$ for all $X$, that is $A$ central.

## The Compatibility with the Involution

**Proposition (the two operations).** Suppose $E$ carries a pairing-based involution $A \mapsto A^{*}$ as in *Involutions of the Endomorphism Algebra*. Then on $\operatorname{End}_F(E)$ the induced operator involution $S^{*}(X) = S(X^{*})^{*}$ satisfies

$$
L_A^{*} = R_{A^{*}}, \qquad R_A^{*} = L_{A^{*}} ,
$$

and the trace-adjoint and the operator involution are related by

$$
(L_A)^{\dagger} = R_A, \qquad L_A^{*} = R_{A^{*}} = (L_{A^{*}})^{\dagger} .
$$

**Proof.** $L_A^{*}(X) = L_A(X^{*})^{*} = (AX^{*})^{*} = XA^{*} = R_{A^{*}}(X)$, using the anti-multiplicativity of the involution; the second identity is the same computation for $R_A$. The last display collects the first with the trace-adjointness of $L_{A^{*}}$.

**Proposition (the trace pairing is compatible with the involution).** If the involution is the adjoint with respect to a pairing on $V$, then

$$
\langle X^{*},Y\rangle = \varsigma\bigl(\langle Y^{*},X\rangle\bigr) ,
$$

so the trace pairing is $\varsigma$-compatible with the involution; in the bilinear symmetric case it satisfies $\langle X^{*},Y\rangle = \langle X,Y^{*}\rangle$.

**Proof.** $\operatorname{tr}(X^{*}Y) = \operatorname{tr}((Y^{*}X)^{*}) = \varsigma(\operatorname{tr}(Y^{*}X))$, since the involution is $\varsigma$-semilinear and applies to the trace; when $\varsigma=\mathrm{id}$ this is $\langle Y^{*},X\rangle$, and applying the same identity to $Y^{*},X$ gives $\langle X^{*},Y\rangle=\langle X,Y^{*}\rangle$.

**Example.** With the standard pairing on $F^n$ the element involution is transposition, and $L_A^{*} = R_{A^{\mathsf{T}}}$: the operator involution sends the left multiplication by $A$ to the right multiplication by the transpose, which is the abstract form of $(AXY)^{\mathsf{T}} = Y^{\mathsf{T}}X^{\mathsf{T}}A^{\mathsf{T}}$.

## Summary

The endomorphism algebra $E = \operatorname{End}_F(V)$ carries the trace pairing $\langle X,Y\rangle=\operatorname{tr}(XY)$, which is bilinear, symmetric, non-degenerate and associative, and which needs no form on $V$; it is the natural pairing of the category. The left and right multiplications satisfy $L_AL_B=L_{AB}$, $R_AR_B=R_{BA}$ and $L_AR_B=R_BL_A$, and with respect to the trace pairing they are adjoint to one another: $(L_A)^{\dagger}=R_A$ and $(R_A)^{\dagger}=L_A$, a left multiplication being self-adjoint exactly for central $A$. When $E$ carries a pairing-based involution, the induced operator involution satisfies $L_A^{*}=R_{A^{*}}$ and $R_A^{*}=L_{A^{*}}$, so the trace-adjoint and the operator involution differ by the involution of the parameter, $(L_A)^{\dagger}=R_A$ against $L_A^{*}=(L_{A^{*}})^{\dagger}$; and the trace pairing is compatible with the involution, $\langle X^{*},Y\rangle=\varsigma(\langle Y^{*},X\rangle)$, becoming $\langle X^{*},Y\rangle=\langle X,Y^{*}\rangle$ in the bilinear symmetric case. The signed versions of these statements are *The Signed Adjoint of the Left Multiplication on a Linear Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $n$ | the field, the space and its dimension |
| $E=\operatorname{End}_F(V)$ | the endomorphism algebra |
| $L_A(X)=AX$, $R_A(X)=XA$ | left and right multiplication |
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace pairing |
| ${}^{\dagger}$ | the adjoint with respect to the trace pairing |
| $(L_A)^{\dagger}=R_A$ | the adjointness |
| $A^{*}$ | the pairing-based element involution |
| $S^{*}(X)=S(X^{*})^{*}$ | the induced operator involution |
| $L_A^{*}=R_{A^{*}}$, $R_A^{*}=L_{A^{*}}$ | the compatibility with the involution |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the left and right multiplications and the trace pairing on an endomorphism ring.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the trace, the trace form and the adjoint.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the structure of endomorphism rings and the centraliser of the left multiplications.
- Joseph J. Rotman, *Advanced Modern Algebra* (American Mathematical Society, 3rd ed. 2015), for the trace form and the adjoint of a multiplication operator.
