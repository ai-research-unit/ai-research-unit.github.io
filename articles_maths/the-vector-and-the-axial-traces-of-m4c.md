# __The Vector and the Axial Traces of $M_4(\mathbb{C})$__

## Introduction

A biquaternion has one complex trace, $4b_0$, in its left regular representation. The Dirac module sees two traces instead: the **vector trace** and the **axial trace**. The regular trace is their sum, and this is the exact sense in which the Dirac module carries more information than the regular one. The anomaly articles need the pair, not the sum; using the regular trace as if it were the axial trace adds the vector part to the axial part.

The distinction is a consequence of a fact that is easy to miss: the Clifford embedding
$$
\mathsf{M}_4:\mathbb{B}\longrightarrow \mathrm{Cl}^{+}(1,3)\subset M_4(\mathbb{C})
$$
is **real-linear, not complex-linear**. The central imaginary $i$ of $\mathbb{B}$ maps to the pseudoscalar cell $T_{tz}=L_tR_z$, not to $iI$:
$$
\mathsf{M}_4(ib)=\mathsf{M}_4(i)\mathsf{M}_4(b)=T_{tz}\,\mathsf{M}_4(b).
$$
Hence $\operatorname{tr}\mathsf{M}_4(ib)\ne i\operatorname{tr}\mathsf{M}_4(b)$ in general, and the complex trace of the matrix is not the complex-linear regular trace. The vector and axial traces are the two traces that recover the regular one.

This article computes the two traces, proves the identity
$$
\operatorname{Tr}_{\mathrm{reg}}=\operatorname{Tr}_{\Delta}+\operatorname{Tr}_{\Delta,5},
$$
identifies the two coordinates of the two-sided basis that carry them, and states the vanishing on the odd sector. The five frame cells, written $iT_{tx},iT_{xy},iT_{yy},iT_{zy}$ with the pseudoscalar $T_{tz}$, and the $\mathsf{M}_4$ map are those of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$* and *Matrix Representations Conventions*; the two-sided basis is *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*; the chirality is *The Two Chiralities of $M_4(\mathbb{C})$*.

## The Real-Linear Embedding

**The element.** Write the biquaternion as
$$
b=a+i a',\qquad a=a_0e_t+a_1e_x+a_2e_y+a_3e_z,\quad a_\mu\in\mathbb{R},
$$
with $a'$ real quaternion coefficients. The complex coefficient is $b_\mu=a_\mu+ia'_\mu$, and the scalar coordinate is $b_0=a_0+ia'_0$.

**The embedding.** On the real basis,
$$
\mathsf{M}_4(e_t)=T_{tt}=I,\qquad
\mathsf{M}_4(e_x)=T_{xt},\qquad
\mathsf{M}_4(e_y)=T_{yt},\qquad
\mathsf{M}_4(e_z)=T_{zt},
$$
and
$$
\mathsf{M}_4(i)=-\omega=T_{tz},\qquad \omega=(iT_{tx})(iT_{xy})(iT_{yy})(iT_{zy})=-T_{tz},\quad -iT_{tz}=i\omega .
$$
The map is real-linear:
$$
\mathsf{M}_4(b)=\mathsf{M}_4(a)+\mathsf{M}_4(i)\mathsf{M}_4(a')
=\mathsf{M}_4(a)+T_{tz}\,\mathsf{M}_4(a').
$$
It is an isomorphism of real algebras onto $\mathrm{Cl}^{+}(1,3)$; it is not complex-linear, because $\mathsf{M}_4(i)\ne iI$.

**The real quaternion part.** For a real quaternion $a$, the matrix $\mathsf{M}_4(a)$ is a real linear combination of $I$ and the six bivectors:
$$
\mathsf{M}_4(a)=a_0I+a_1T_{xt}+a_2T_{yt}+a_3T_{zt} .
$$
It has no pseudoscalar component. Hence
$$
\operatorname{tr}\mathsf{M}_4(a)=4a_0,\qquad
\operatorname{tr}\bigl((-iT_{tz})\mathsf{M}_4(a)\bigr)=0,
$$
because the trace of every graded cell other than $I$ and $T_{tz}$ is zero, and $(-iT_{tz})$ times a bivector product is again a bivector product, also traceless.

**The imaginary part.** For the imaginary quaternion $ia'$,
$$
\mathsf{M}_4(ia')=T_{tz}\,\mathsf{M}_4(a'),
$$
so
$$
\operatorname{tr}\mathsf{M}_4(ia')=\operatorname{tr}\bigl(T_{tz}\mathsf{M}_4(a')\bigr)=0,
$$
and
$$
\operatorname{tr}\bigl((-iT_{tz})\mathsf{M}_4(ia')\bigr)
=i\operatorname{tr}\mathsf{M}_4(a')=4i a'_0 ,
$$
because $T_{tz}$ squares to $-I$.

**The two traces.** Adding the two pieces,
$$
\boxed{\;
\operatorname{Tr}_{\Delta}(b):=\operatorname{tr}\mathsf{M}_4(b)=4a_0=4\operatorname{Re}b_0,
\qquad
\operatorname{Tr}_{\Delta,5}(b):=\operatorname{tr}\bigl((-iT_{tz})\mathsf{M}_4(b)\bigr)=4i a'_0=4i\operatorname{Im}b_0 .
\;}
$$
The vector trace is real; the axial trace is purely imaginary. Together they are the real and imaginary parts of the complex scalar coordinate, multiplied by four.

## The Identity

**The regular trace.** The left regular representation of $\mathbb{B}$ on itself has trace
$$
\operatorname{Tr}_{\mathrm{reg}}(b)=4b_0 .
$$
This is the complex-linear trace: $\operatorname{Tr}_{\mathrm{reg}}(ib)=i\operatorname{Tr}_{\mathrm{reg}}(b)$.

**Theorem (the trace identity).** For every $b\in\mathbb{B}$,
$$
\boxed{\;\operatorname{Tr}_{\mathrm{reg}}(b)
=\operatorname{Tr}_{\Delta}(b)+\operatorname{Tr}_{\Delta,5}(b)\; } .
$$

**Proof.** The two displayed values are $4a_0$ and $4ia'_0$, and $b_0=a_0+ia'_0$. $\square$

**The reading.** The identity is not a decomposition of the trace of an arbitrary $4\times4$ matrix. It holds on the image of $\mathbb{B}$, where the two traces are the real and imaginary parts of one complex number. For a general $A\in M_4(\mathbb{C})$, $\operatorname{tr}A$ and $\operatorname{tr}\bigl((-iT_{tz})A\bigr)$ are two independent complex functionals, and their sum is not $\operatorname{tr}A$. The identity is a statement about the **even Clifford subalgebra** and its real-linear parametrisation by $\mathbb{B}$.

**The central imaginary.** For $b=i$,
$$
\operatorname{Tr}_{\Delta}(i)=0,\qquad
\operatorname{Tr}_{\Delta,5}(i)=4i,\qquad
\operatorname{Tr}_{\mathrm{reg}}(i)=4i .
$$
The vector trace does not see the central imaginary; the axial trace sees only the central imaginary. This is the sharpest illustration of the pair.

**The chiral traces.** With $P_{\pm}=\tfrac12(I\mp iT_{tz})$,
$$
\operatorname{tr}\bigl(P_+\mathsf{M}_4(b)\bigr)=\tfrac12\bigl(\operatorname{Tr}_{\Delta}(b)+\operatorname{Tr}_{\Delta,5}(b)\bigr)=2b_0,
$$
$$
\operatorname{tr}\bigl(P_-\mathsf{M}_4(b)\bigr)=\tfrac12\bigl(\operatorname{Tr}_{\Delta}(b)-\operatorname{Tr}_{\Delta,5}(b)\bigr)=2\bar b_0 .
$$
The two chiral traces are twice the element and twice its coefficient conjugate. The vector trace is their sum, the axial trace their difference:
$$
\operatorname{Tr}_{\Delta}=\operatorname{tr}P_++\operatorname{tr}P_-,
\qquad
\operatorname{Tr}_{\Delta,5}=\operatorname{tr}P_+-\operatorname{tr}P_- .
$$

## The Two Coordinates of the Two-Sided Basis

**The trace functionals on $M_4(\mathbb{C})$.** On the two-sided basis,
$$
\operatorname{tr}(T_{\mu\nu})=4\delta_{\mu t}\delta_{\nu t},
\qquad
\operatorname{tr}\bigl((-iT_{tz})T_{\mu\nu}\bigr)=4i\,\delta_{\mu t}\delta_{\nu z},
$$
because $T_{tt}=I$, $T_{tz}$ is the pseudoscalar cell, and every other $T_{\mu\nu}$ is a vector, bivector or trivector product.

**Proof.** The table of *The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$* gives $T_{tt}=I$, the pseudoscalar $T_{tz}$, and the other fourteen as vectors, bivectors or trivectors. The trace of every graded cell other than $I$ and $T_{tz}$ is zero, and $T_{tz}$ times a vector, bivector or trivector is again one of those. Only $I$ and $T_{tz}$ survive: $\operatorname{tr}I=4$ and $\operatorname{tr}\bigl((-iT_{tz})T_{tz}\bigr)=4i$. $\square$

**The reading on the basis.** For
$$
A=\sum_{\mu,\nu}c_{\mu\nu}T_{\mu\nu},
$$
the two traces are
$$
\operatorname{tr}A=4c_{tt},\qquad
\operatorname{tr}\bigl((-iT_{tz})A\bigr)=4i\,c_{tz}.
$$
The vector trace reads the coefficient of $T_{tt}=I$; the axial trace reads the coefficient of $T_{tz}$, the pseudoscalar cell. The other fourteen coordinates are invisible to both. This is the exact content of the statement that the traces see only the scalar and the pseudoscalar.

**The biquaternion coordinates.** For $A=\mathsf{M}_4(b)$,
$$
c_{tt}=\operatorname{Re}b_0,\qquad c_{tz}=\operatorname{Im}b_0,
$$
so the two traces are
$$
\operatorname{tr}\mathsf{M}_4(b)=4c_{tt},\qquad
\operatorname{tr}\bigl((-iT_{tz})\mathsf{M}_4(b)\bigr)=4i\,c_{tz}.
$$
The identity $\operatorname{Tr}_{\mathrm{reg}}=4(c_{tt}+ic_{tz})$ is the coordinate form of the trace identity.

## The Odd Sector

**Proposition (the odd traces vanish).** Let $X\in\mathrm{Cl}(1,3)$ be odd. Then
$$
\operatorname{tr}\mathsf{M}_4(X)=0,\qquad
\operatorname{tr}\bigl((-iT_{tz})\mathsf{M}_4(X)\bigr)=0 .
$$

**Proof.** In the chiral basis the pseudoscalar cell reads $-iT_{tz}=\operatorname{diag}(I_2,-I_2)$; an odd element is off-diagonal, so its trace is zero. The product $(-iT_{tz})X$ is also off-diagonal, so its trace is zero. $\square$

**The reading.** The odd sector is invisible to both traces. The vector and axial traces see the even part only, and within the even part they see only the scalar and the pseudoscalar. This is why a trace cannot detect the odd generator: the odd generator is not an element of the biquaternion algebra but an operation on the module, and its contribution to a closed trace vanishes.

**The anomaly.** The chiral anomaly is a statement about the pair $(\operatorname{Tr}_{\Delta},\operatorname{Tr}_{\Delta,5})$, not about $\operatorname{Tr}_{\mathrm{reg}}$. The regular trace is their sum; using it as the axial trace adds the vector part $4\operatorname{Re}b_0$ to the axial part $4i\operatorname{Im}b_0$. The anomaly computation needs the two separately, and the odd operators have zero trace in either. The replacement of the Clifford layer by the biquaternion calculus therefore preserves the trace pair; it does not preserve a single regular trace as a substitute for the pair.

## The Sign Conventions

**The pseudoscalar cell.** The article uses
$$
-iT_{tz}=i\,(iT_{tx})(iT_{xy})(iT_{yy})(iT_{zy}),\qquad
(-iT_{tz})^2=I,\qquad
P_{\pm}=\tfrac12(I\mp iT_{tz}),
$$
and the embedding $\mathsf{M}_4(i)=T_{tz}$. The opposite sign of $T_{tz}$ exchanges $P_+$ and $P_-$ and changes the sign of the axial trace; the identity $\operatorname{Tr}_{\mathrm{reg}}=\operatorname{Tr}_{\Delta}+\operatorname{Tr}_{\Delta,5}$ is invariant under the exchange, because both the axial trace and the chiral difference change sign. The absolute statement is the pair, not the sign of either member.

**The trace of the pseudoscalar cell.** Its trace is zero:
$$
\operatorname{tr}T_{tz}=0 .
$$
The axial trace of an element $b$ is not the trace of $T_{tz}$; it is the trace of the product $(-iT_{tz})\mathsf{M}_4(b)$. For $b=I$ it vanishes; for $b=i$ it is $4i$. The distinction is the reason the axial trace can be nonzero while the trace of the chirality is zero.

## Summary

The Clifford embedding $\mathsf{M}_4:\mathbb{B}\to M_4(\mathbb{C})$ is real-linear, not complex-linear: $\mathsf{M}_4(i)=T_{tz}$. The vector trace and the axial trace of $b=a+ia'$ are
$$
\operatorname{Tr}_{\Delta}(b)=\operatorname{tr}\mathsf{M}_4(b)=4a_0=4\operatorname{Re}b_0,
\qquad
\operatorname{Tr}_{\Delta,5}(b)=\operatorname{tr}\bigl((-iT_{tz})\mathsf{M}_4(b)\bigr)=4ia'_0=4i\operatorname{Im}b_0 .
$$
Their sum is the regular trace $4b_0$. The chiral traces are $2b_0$ and $2\bar b_0$. On the two-sided basis the vector trace reads the coefficient of $T_{tt}=I$ and the axial trace reads the coefficient of the pseudoscalar cell $T_{tz}$; the other fourteen coordinates are invisible. The odd elements have zero trace in both. The pair is the data the anomaly needs; the regular trace is their sum and cannot replace either member.

| quantity | value on $b=a+ia'$ | value on the basis |
|---|---|---|
| $\operatorname{Tr}_{\Delta}(b)$ | $4a_0$ | $4c_{tt}$ |
| $\operatorname{Tr}_{\Delta,5}(b)$ | $4ia'_0$ | $4i\,c_{tz}$ |
| $\operatorname{Tr}_{\mathrm{reg}}(b)$ | $4(a_0+ia'_0)$ | $4(c_{tt}+ic_{tz})$ |
| $\operatorname{tr}(P_+\mathsf{M}_4(b))$ | $2b_0$ | — |
| $\operatorname{tr}(P_-\mathsf{M}_4(b))$ | $2\bar b_0$ | — |
| odd $X$ | $0,0$ | — |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathsf{M}_4$ | the real-linear Clifford embedding $\mathbb{B}\to\mathrm{Cl}^{+}(1,3)$ |
| $T_{\mu\nu}$ | the two-sided cells $L_\mu R_\nu$; $T_{tt}=I$ and $T_{tz}$ the pseudoscalar cell |
| $P_\pm$ | the chiral projectors $\tfrac12(I\mp iT_{tz})$ |
| $\operatorname{Tr}_{\Delta}$ | the vector trace $\operatorname{tr}\mathsf{M}_4(\cdot)$ |
| $\operatorname{Tr}_{\Delta,5}$ | the axial trace $\operatorname{tr}((-iT_{tz})\mathsf{M}_4(\cdot))$ |
| $\operatorname{Tr}_{\mathrm{reg}}$ | the regular trace $4b_0$ |
| $c_{\mu\nu}$ | the coordinates in the two-sided basis |

## Further Reading

- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five frame cells and the Clifford basis.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen $T_{\mu\nu}$ and their product table.
- [The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$](the-z-grading-and-the-odd-slot-of-m4c.html), for the table $T_{tt}=I$, the pseudoscalar cell $T_{tz}$ and the grades of the other fourteen.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the projectors $P_\pm$ and the chiral blocks.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the trace form and the Hermitian structure.
- [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html), for the real-linear embedding and the explicit matrices, §*The Clifford Structure and the Frame*.
- [The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$](the-star-and-the-conjugate-linear-operators-of-m4c.html), for the bar, the star and the two Clifford dictionaries.

## Appendix — The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\gamma_0=iL_tR_x,\quad \gamma_1=iL_xR_y,\quad \gamma_2=iL_yR_y,\quad \gamma_3=iL_zR_y,\quad \gamma_5=-iL_tR_z .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.
