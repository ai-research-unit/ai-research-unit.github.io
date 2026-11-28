# __The Fermion–Connection Pieces Above $M_C$: One Lorentz Structure, Two Blocks and One Untouched Index__

## Introduction

**The question.** Row $2$ is $\bar\xi\,i\gamma^{\imath}D_{\imath}\xi$ for sixteen Weyl fields. **What interaction does it produce, how many group components does that interaction have, and what does it leave alone?**

**The answer.** One Lorentz structure, two representation blocks, and the copy index untouched.

$$
\boxed{\;\bar\xi A\xi:\ \text{one }\gamma^{\imath},\ 15\ \text{generators},\ \text{two blocks},\ \text{copy index inert}.\;}
$$

**The vertex is fixed by the representation and carries no free number.** Its strength is $g_{4}$, which is row $1$'s constant, **and not a second coupling.**

## The Kinetic Term and Its Blocks

**The covariant derivative splits by representation, and the two blocks differ by a sign and a transpose.**

$$
D_{\imath}\xi_{i}=\partial_{\imath}\xi_{i}-ig_{4}A_{a,\imath}(t_{a})_{i}{}^{j}\xi_{j},
\qquad
D_{\imath}\bar\xi^{i}=\partial_{\imath}\bar\xi^{i}+ig_{4}A_{a,\imath}\bar\xi^{j}(t_{a})_{j}{}^{i}.
$$

**One carries the index up and the other down, which is the whole of the sign difference.** For $\xi\in\bar{\mathbf4}$ the generator matrices are $-t_{a}^{T}$, **the conjugate representation's matrices**, and the count of them is the same fifteen.

**The same $g_{4}$ in both blocks is the statement that this is one force.** A theory with different couplings for $\mathbf4$ and $\bar{\mathbf4}$ would not be a gauge theory of the connection it writes; **the identity of the coupling across representations is what makes the sector a sector.**

## One Lorentz Structure

**At dimension four the fermion bilinear has exactly one gamma structure.**

| candidate | verdict | reason |
|---|---|---|
| $\gamma^{\imath}$ | **admitted** | vector, dimension four |
| $\sigma^{\imath\jmath}=\tfrac{i}{2}[\gamma^{\imath},\gamma^{\jmath}]$ | excluded | the Pauli term is dimension five |
| $\gamma^{\imath}\gamma_{5}$ | excluded | parity-odd and equivalent to the vector up to a total derivative, or axial with no partner |
| $\mathbb 1$ | excluded | would be a scalar density with a fermion bilinear and no derivative, dimension four but not a current |

**So the vertex is one shape and not four.** The axial current is a member of the same $\gamma^{\imath}$ structure for a massless field, **and the corpus does not write it separately** because for a Weyl field the vector and axial combinations are the same bilinear.

## The Two Blocks and One Hundred and Twenty-Eight Entries

**Each block is a $4\times4$ matrix of gamma structures times a $4\times4$ matrix of generators.**

$$
\text{entries per block}=4\times4\times4\times2=128,
$$

**counting the four gamma components, the four-by-four generator matrix, and the two chiralities of the Weyl field.** Two blocks give a doubled structure, **and the doubling is the representation's and not a second vertex.**

**The fifteen generators act on each field and the copy index does not appear.** The vertex is $\bar\xi_{f}\gamma_{\imath}t_{a}\xi_{f}$, **with $f$ summed and $\alpha$ nowhere**: the copy index is a commutant, and [its article](the-scalars-two-indices-and-the-count-sixteen.html) proves $[X\otimes\mathbb1_{2},\mathbb1_{4}\otimes M]=0$.

## The Copy Index Is Inert, and Why That Matters

**No generator sees $\alpha$.** The gauge action is $X\otimes\mathbb1_{2}$ on the sixteen-dimensional space, **so a rotation mixing the two copies commutes with every generator** and is not gauged.

**Three consequences follow, and they are the article's real content.**

**First, the Yukawa matrix can live on $\alpha$ and nowhere else.** It cannot carry a quartet index (invariance), it cannot carry a momentum (locality), **and it can carry $\alpha$ because $\alpha$ is the one label the group does not touch.** That is why the Yukawa block is a $2\times2$ matrix and not a $16\times16$ one.

**Second, flavour has no gauge quantum number above $M_C$.** The two copies are degenerate in every gauge interaction, **so the fermion–connection vertex is diagonal in $\alpha$** and the only place flavour appears is the Yukawa.

**Third, the copy basis is unobservable.** A $\mathrm{U}(2)$ acting on $\alpha$ is a symmetry of the whole Lagrangian except the Yukawa, **and it is what removes six of a Yukawa matrix's eight entries.** [The coefficients article](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html) does that subtraction.

## The Current and Its Divergence

$$
j^{\xi}_{a,\imath}=\sum_{f=1}^{16}\bar\xi_{f}\gamma_{\imath}t_{a}\xi_{f},
\qquad
\partial^{\imath}j^{\xi}_{a,\imath}\neq0,
\qquad
D^{\imath}j^{\xi}_{a,\imath}=0 .
$$

**The ordinary divergence is not zero and the covariant one is.** So **no conserved charge exists in this phase**: a conserved current requires a global symmetry of the full Lagrangian, and the only global symmetry here is the copy $\mathrm{U}(2)$, which acts on $\alpha$ and not on the connection.

**This is the phase's sharpest difference from the Standard Model.** There, flavour currents are conserved at tree level and the charges are physical; **here the gauge current is covariantly conserved and its charge is not**, because the connection itself carries the charge.

## Checks

1. The blocks. $\mathbf4$ with $t_{a}$; $\bar{\mathbf4}$ with $-t_{a}^{T}$; fifteen each.
2. The Lorentz structures. One admitted, three excluded, each with a reason.
3. The entry count. $4\times4\times4\times2=128$ per block.
4. The copy index. $[X\otimes\mathbb1_{2},\mathbb1_{4}\otimes M]=0$, so $\alpha$ is inert.
5. The coupling. The same $g_{4}$ in both blocks.
6. The current. Ordinary divergence nonzero, covariant divergence zero.
7. The consequence. The Yukawa matrix lives on $\alpha$ and nowhere else.

## Summary

**Row $2$ produces one vertex: $\bar\xi A\xi$, with one Lorentz structure, two representation blocks and the coupling $g_{4}$ in both.** The fifteen generators act on the quartet index; **the copy index $\alpha$ is a commutant that no generator sees.**

**That inertness is what the rest of the category rests on.** It is why the Yukawa matrix is $2\times2$, why flavour has no gauge quantum number above $M_C$, **and why six of a Yukawa matrix's eight entries are removable.**

**The current is covariantly conserved and not ordinarily conserved**, so this phase has no conserved gauge charge — the difference from the Standard Model that follows from having one connection and no residual group.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\xi_{i}$, $\bar\xi^{i}$ | the Weyl fields in $\mathbf4$ and $\bar{\mathbf4}$ |
| $t_{a}$, $-t_{a}^{T}$ | the generators in the two representations |
| $\alpha$ | the copy index; inert under the gauge action |
| $j^{\xi}_{a,\imath}$ | the fermion current |

## Further Reading

- [The Fermion–Connection Vertex in the Quartet Basis](the-fermion-connection-vertex-in-the-quartet-basis-the-fifteen-read-on-the-sixteen.html). The same vertex read component by component.
- [The Lagrangian and the Sixteen](the-lagrangian-and-the-sixteen-kinetic-term-and-yukawa-coupling.html). The kinetic term and the Yukawa operator.
- [The Scalars, Two Indices and the Count Sixteen](the-scalars-two-indices-and-the-count-sixteen.html). Why the copy index is a commutant.
- [The Coefficients Above $M_C$](the-coefficients-above-m-c-fifteen-constants-one-gauge-parameter-and-one-angle-without-a-row.html). The six removed entries.
- [The Content Above $M_C$](the-content-above-m-c-fifteen-connections-sixteen-weyl-fields-and-one-hermitian-scalar.html). The sixteen fields themselves.
