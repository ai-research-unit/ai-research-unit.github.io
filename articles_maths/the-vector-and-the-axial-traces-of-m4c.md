# __The Vector and the Axial Traces of $M_4(\mathbb{C})$__

## Introduction

A biquaternion has one complex trace, $4b_0$, in its left regular representation. The Dirac module sees two traces instead: the **vector trace** and the **axial trace**. The regular trace is their sum, and this is the exact sense in which the Dirac module carries more information than the regular one. The anomaly articles need the pair, not the sum; using the regular trace as if it were the axial trace adds the vector part to the axial part.

The distinction is a consequence of a fact that is easy to miss: the Clifford embedding
$$
\mathsf{M}_4:\mathbb{B}\longrightarrow \mathrm{Cl}^{+}(1,3)\subset M_4(\mathbb{C})
$$
is **real-linear, not complex-linear**. The central imaginary $i$ of $\mathbb{B}$ maps to the pseudoscalar cell $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, not to $iI$:
$$
\mathsf{M}_4(ib)=\mathsf{M}_4(i)\mathsf{M}_4(b)=L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\,\mathsf{M}_4(b).
$$
Hence $\operatorname{tr}\mathsf{M}_4(ib)\ne i\operatorname{tr}\mathsf{M}_4(b)$ in general, and the complex trace of the matrix is not the complex-linear regular trace. The vector and axial traces are the two traces that recover the regular one.

This article computes the two traces, proves the identity
$$
\operatorname{Tr}^{\mathrm{reg}}=\operatorname{Tr}_{\Delta}+\operatorname{Tr}_{\Delta,5},
$$
identifies the two coordinates of the two-sided basis that carry them, and states the vanishing on the odd sector. The five frame cells $iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and the pseudoscalar cell $-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, and the $\mathsf{M}_4$ map, are those of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$* and *Matrix Representations Conventions*; the two-sided basis is *The Two-Sided Operators Method to Build $M_4(\mathbb{C})$*; the chirality is *The Two Chiralities of $M_4(\mathbb{C})$*.

## The Real-Linear Embedding

**The element.** Write the biquaternion as
$$
b=a+i a',\qquad a=a_0e_t+a_1\vec e_x+a_2\vec e_y+a_3\vec e_z,\quad a_\mu\in\mathbb{R},
$$
with $a'$ real quaternion coefficients. The complex coefficient is $b_\mu=a_\mu+ia'_\mu$, and the scalar coordinate is $b_0=a_0+ia'_0$.

**The embedding.** On the real basis,
$$
\mathsf{M}_4(e_t)=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I,\qquad
\mathsf{M}_4(\vec e_x)=L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
\mathsf{M}_4(\vec e_y)=L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
\mathsf{M}_4(\vec e_z)=L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},
$$
and
$$
\mathsf{M}_4(i)=-\omega=L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},\qquad \omega=(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})(iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})(iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})(iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})=-L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},\quad -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=i\omega .
$$
The map is real-linear:
$$
\mathsf{M}_4(b)=\mathsf{M}_4(a)+\mathsf{M}_4(i)\mathsf{M}_4(a')
=\mathsf{M}_4(a)+L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\,\mathsf{M}_4(a').
$$
It is an isomorphism of real algebras onto $\mathrm{Cl}^{+}(1,3)$; it is not complex-linear, because $\mathsf{M}_4(i)\ne iI$.

**The real quaternion part.** For a real quaternion $a$, the matrix $\mathsf{M}_4(a)$ is a real linear combination of $I$ and the six bivectors:
$$
\mathsf{M}_4(a)=a_0I+a_1L_{\vec e_x}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}+a_2L_{\vec e_y}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}+a_3L_{\vec e_z}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}} .
$$
It has no pseudoscalar component. Hence
$$
\operatorname{tr}\mathsf{M}_4(a)=4a_0,\qquad
\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(a)\bigr)=0,
$$
because the trace pairing is orthogonal on the sixteen cells, $\operatorname{tr}(L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}} L_{e_\rho}^{\mathrm{pau}}R_{e_\tau}^{\mathrm{pau}})=4\,g_{\mu\mu}g_{\nu\nu}\delta_{\mu\rho}\delta_{\nu\tau}$, so the functional $\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\,\cdot\bigr)$ reads only the $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ coordinate, and $\mathsf{M}_4(a)$ has none.

**The imaginary part.** For the imaginary quaternion $ia'$,
$$
\mathsf{M}_4(ia')=L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\,\mathsf{M}_4(a'),
$$
so
$$
\operatorname{tr}\mathsf{M}_4(ia')=\operatorname{tr}\bigl(L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\mathsf{M}_4(a')\bigr)=0,
$$
and
$$
\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(ia')\bigr)
=i\operatorname{tr}\mathsf{M}_4(a')=4i a'_0 ,
$$
because $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ squares to $-I$.

**The two traces.** Adding the two pieces,
$$
\boxed{\;
\operatorname{Tr}_{\Delta}(b):=\operatorname{tr}\mathsf{M}_4(b)=4a_0=4\operatorname{Re}b_0,
\qquad
\operatorname{Tr}_{\Delta,5}(b):=\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(b)\bigr)=4i a'_0=4i\operatorname{Im}b_0 .
\;}
$$
The vector trace is real; the axial trace is purely imaginary. Together they are the real and imaginary parts of the complex scalar coordinate, multiplied by four.

## The Identity

**The regular trace.** The left regular representation of $\mathbb{B}$ on itself has trace
$$
\operatorname{Tr}^{\mathrm{reg}}(b)=4b_0 .
$$
This is the complex-linear trace: $\operatorname{Tr}^{\mathrm{reg}}(ib)=i\operatorname{Tr}^{\mathrm{reg}}(b)$.

**Theorem (the trace identity).** For every $b\in\mathbb{B}$,
$$
\boxed{\;\operatorname{Tr}^{\mathrm{reg}}(b)
=\operatorname{Tr}_{\Delta}(b)+\operatorname{Tr}_{\Delta,5}(b)\; } .
$$

**Proof.** The two displayed values are $4a_0$ and $4ia'_0$, and $b_0=a_0+ia'_0$.

**The reading.** The identity is not a decomposition of the trace of an arbitrary $4\times4$ matrix. It holds on the image of $\mathbb{B}$, where the two traces are the real and imaginary parts of one complex number. For a general $A\in M_4(\mathbb{C})$, $\operatorname{tr}A$ and $\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})A\bigr)$ are two independent complex functionals, and their sum is not $\operatorname{tr}A$. The identity is a statement about the **even Clifford subalgebra** and its real-linear parametrisation by $\mathbb{B}$.

**The central imaginary.** For $b=i$,
$$
\operatorname{Tr}_{\Delta}(i)=0,\qquad
\operatorname{Tr}_{\Delta,5}(i)=4i,\qquad
\operatorname{Tr}^{\mathrm{reg}}(i)=4i .
$$
The vector trace does not see the central imaginary; the axial trace sees only the central imaginary. This is the sharpest illustration of the pair.

**The chiral traces.** With $P_{\pm}=\tfrac12(I\mp iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})$,
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
\operatorname{tr}(L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}})=4\delta_{\mu t}\delta_{\nu t},
\qquad
\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}\bigr)=4i\,\delta_{\mu t}\delta_{\nu z},
$$
because $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I$, $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ is the pseudoscalar cell, and every other $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ is a vector, bivector or trivector product.

**Proof.** The table of *The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$* gives $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I$, the pseudoscalar $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, and the other fourteen as vectors, bivectors or trivectors. The trace of every graded cell other than $I$ and $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ is zero, and $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ times a vector, bivector or trivector is again one of those. Only $I$ and $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ survive: $\operatorname{tr}I=4$ and $\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}\bigr)=4i$.

**The reading on the basis.** For
$$
A=\sum_{\mu,\nu}c_{\mu\nu}L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}},
$$
the two traces are
$$
\operatorname{tr}A=4c_{tt},\qquad
\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})A\bigr)=4i\,c_{tz}.
$$
The vector trace reads the coefficient of $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I$; the axial trace reads the coefficient of $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, the pseudoscalar cell. The other fourteen coordinates are invisible to both. This is the exact content of the statement that the traces see only the scalar and the pseudoscalar.

**The biquaternion coordinates.** For $A=\mathsf{M}_4(b)$,
$$
c_{tt}=\operatorname{Re}b_0,\qquad c_{tz}=\operatorname{Im}b_0,
$$
so the two traces are
$$
\operatorname{tr}\mathsf{M}_4(b)=4c_{tt},\qquad
\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(b)\bigr)=4i\,c_{tz}.
$$
The identity $\operatorname{Tr}^{\mathrm{reg}}=4(c_{tt}+ic_{tz})$ is the coordinate form of the trace identity.

## The Odd Sector

**Proposition (the odd traces vanish).** Let $X\in\mathrm{Cl}(1,3)$ be odd. Then
$$
\operatorname{tr}\mathsf{M}_4(X)=0,\qquad
\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(X)\bigr)=0 .
$$

**Proof.** In the chiral basis the pseudoscalar cell reads $-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\operatorname{diag}(I_2,-I_2)$; an odd element is off-diagonal, so its trace is zero. The product $(-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})X$ is also off-diagonal, so its trace is zero.

**The reading.** The odd sector is invisible to both traces. The vector and axial traces see the even part only, and within the even part they see only the scalar and the pseudoscalar. This is why a trace cannot detect the odd generator: the odd generator is not an element of the biquaternion algebra but an operation on the module, and its contribution to a closed trace vanishes.

**The anomaly.** The chiral anomaly is a statement about the pair $(\operatorname{Tr}_{\Delta},\operatorname{Tr}_{\Delta,5})$, not about $\operatorname{Tr}^{\mathrm{reg}}$. The regular trace is their sum; using it as the axial trace adds the vector part $4\operatorname{Re}b_0$ to the axial part $4i\operatorname{Im}b_0$. The anomaly computation needs the two separately, and the odd operators have zero trace in either. The replacement of the Clifford layer by the biquaternion calculus therefore preserves the trace pair; it does not preserve a single regular trace as a substitute for the pair.

## The Sign Conventions

**The pseudoscalar cell.** The article uses
$$
-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=i\,(iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}})(iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})(iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})(iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}),\qquad
(-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})^2=I,\qquad
P_{\pm}=\tfrac12(I\mp iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}),
$$
and the embedding $\mathsf{M}_4(i)=L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$. The opposite sign of $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ exchanges $P_+$ and $P_-$ and changes the sign of the axial trace; the identity $\operatorname{Tr}^{\mathrm{reg}}=\operatorname{Tr}_{\Delta}+\operatorname{Tr}_{\Delta,5}$ is invariant under the exchange, because both the axial trace and the chiral difference change sign. The absolute statement is the pair, not the sign of either member.

**The trace of the pseudoscalar cell.** Its trace is zero:
$$
\operatorname{tr}L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=0 .
$$
The axial trace of an element $b$ is not the trace of $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$; it is the trace of the product $(-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(b)$. For $b=I$ it vanishes; for $b=i$ it is $4i$. The distinction is the reason the axial trace can be nonzero while the trace of the chirality is zero.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The Clifford embedding $\mathsf{M}_4:\mathbb{B}\to M_4(\mathbb{C})$ is real-linear, not complex-linear: $\mathsf{M}_4(i)=L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$. The vector trace and the axial trace of $b=a+ia'$ are
$$
\operatorname{Tr}_{\Delta}(b)=\operatorname{tr}\mathsf{M}_4(b)=4a_0=4\operatorname{Re}b_0,
\qquad
\operatorname{Tr}_{\Delta,5}(b)=\operatorname{tr}\bigl((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(b)\bigr)=4ia'_0=4i\operatorname{Im}b_0 .
$$
Their sum is the regular trace $4b_0$. The chiral traces are $2b_0$ and $2\bar b_0$. On the two-sided basis the vector trace reads the coefficient of $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I$ and the axial trace reads the coefficient of the pseudoscalar cell $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$; the other fourteen coordinates are invisible. The odd elements have zero trace in both. The pair is the data the anomaly needs; the regular trace is their sum and cannot replace either member.

| quantity | value on $b=a+ia'$ | value on the basis |
|---|---|---|
| $\operatorname{Tr}_{\Delta}(b)$ | $4a_0$ | $4c_{tt}$ |
| $\operatorname{Tr}_{\Delta,5}(b)$ | $4ia'_0$ | $4i\,c_{tz}$ |
| $\operatorname{Tr}^{\mathrm{reg}}(b)$ | $4(a_0+ia'_0)$ | $4(c_{tt}+ic_{tz})$ |
| $\operatorname{tr}(P_+\mathsf{M}_4(b))$ | $2b_0$ | — |
| $\operatorname{tr}(P_-\mathsf{M}_4(b))$ | $2\bar b_0$ | — |
| odd $X$ | $0,0$ | — |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathsf{M}_4$ | the real-linear Clifford embedding $\mathbb{B}\to\mathrm{Cl}^{+}(1,3)$ |
| $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ | the two-sided cells $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$; $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I$ and $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ the pseudoscalar cell |
| $P_\pm$ | the chiral projectors $\tfrac12(I\mp iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})$ |
| $\operatorname{Tr}_{\Delta}$ | the vector trace $\operatorname{tr}\mathsf{M}_4(\cdot)$ |
| $\operatorname{Tr}_{\Delta,5}$ | the axial trace $\operatorname{tr}((-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}})\mathsf{M}_4(\cdot))$ |
| $\operatorname{Tr}^{\mathrm{reg}}$ | the regular trace $4b_0$ |
| $c_{\mu\nu}$ | the coordinates in the two-sided basis |

## Further Reading

- [The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$](the-gamma-frame-and-the-complexified-dirac-algebra-of-m4c.html), for the five frame cells and the Clifford basis.
- [The Two-Sided Operators Method to Build $M_4(\mathbb{C})$](the-two-sided-operators-method-to-build-m4c.html), for the sixteen $L_{e_\mu}^{\mathrm{pau}}R_{e_\nu}^{\mathrm{pau}}$ and their product table.
- [The $\mathbb{Z}$-Grading and the Odd Slot of $M_4(\mathbb{C})$](the-z-grading-and-the-odd-slot-of-m4c.html), for the table $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}=I$, the pseudoscalar cell $L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ and the grades of the other fourteen.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the projectors $P_\pm$ and the chiral blocks.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the trace form and the Hermitian structure.
- [Conventions of the Matrix Models](../articles_physics/matrix-representations-conventions.html), for the real-linear embedding and the explicit matrices, §*The Clifford Structure and the Frame*.
- [The Star and the Conjugate-Linear Operators of $M_4(\mathbb{C})$](the-star-and-the-conjugate-linear-operators-of-m4c.html), for the bar, the star and the two Clifford dictionaries.
