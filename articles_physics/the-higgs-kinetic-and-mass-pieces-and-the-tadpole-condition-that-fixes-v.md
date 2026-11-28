# __The Higgs Kinetic and Mass Pieces, and the Tadpole Condition That Fixes $v$__

## Introduction

**The claim.** The scalar contributes two quadratic pieces to the list,

$$
\mathcal{L}_{h}=\tfrac12\partial_\mu h\,\partial^\mu h-\tfrac12m_h^2h^2 ,
$$

and a condition that is not a piece: the coefficient of the term linear in $h$ vanishes. That condition is what fixes $v$, and it is why $v$ is derived from the potential's two parameters rather than added to them.

**The answer.**

$$
\boxed{\;\tfrac12\partial_\mu h\partial^\mu h-\tfrac12m_h^2h^2,\qquad m_h^2=2\varpi_{\mathrm{cpl}}v^2,\qquad v\Bigl(\varpi_{\mathrm{cpl}}v^2-\mu^2\Bigr)=0\;}
$$

**Why a condition and not a piece.** A term linear in $h$ is a dimension-three invariant and would be in the list if it were present. It is absent, and its absence is not an accident of the potential: it is the statement that the expansion point is the minimum. A reader who expands about a point that is not the minimum gets a tadpole piece and a different mass, and [The Lagrangian and the Higgs Field](the-lagrangian-and-the-higgs-field.html) shows the same statement in the corpus's own variables.

**The standing.** Both pieces and the condition are standard. The corpus's treatment is [The Lagrangian and the Higgs Field](the-lagrangian-and-the-higgs-field.html) for the potential and the radial variable, and [Electroweak Symmetry Breaking](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html) for the expansion that gives the vectors their masses.

## The Two Pieces

**The kinetic piece.**

$$
\tfrac12\partial_\mu h\,\partial^\mu h
$$

with the coefficient fixed by the canonical commutator. The field $h$ is the one real component of the doublet that survives the gauge choice $G^\pm=G^0=0$, and its normalisation is the one that makes this coefficient $\tfrac12$.

**The mass piece.**

$$
-\tfrac12m_h^2h^2
$$

with $m_h^2=2\varpi_{\mathrm{cpl}}v^2$. The factor $\tfrac12$ is the reality of $h$: one real field, one half. The $Z$ mass piece carries the same fraction for the same reason, and the $W$ mass piece does not, because the charged field is complex.

**Why the scalar has no partner.** The doublet's other three components are the Goldstones. They have no kinetic piece in the list because they are set to zero, and their degrees of freedom are the longitudinal polarisations of the three massive vectors. The scalar sector contributes two rows and not eight.

## The Tadpole Condition

**One expansion, three pieces and one constant.**

$$
V(v+h)=-\frac{\varpi_{\mathrm{cpl}}v^4}{4}+\varpi_{\mathrm{cpl}}v^2h^2+\varpi_{\mathrm{cpl}}vh^3+\frac{\varpi_{\mathrm{cpl}}}{4}h^4 .
$$

**The linear term is zero by construction.** With $V=-\mu^2H^\dagger H+\varpi_{\mathrm{cpl}}(H^\dagger H)^2$ and $H^\dagger H=\tfrac12(v+h)^2$, the coefficient of $h$ is $v(\varpi_{\mathrm{cpl}}v^2-\mu^2)$, and it vanishes exactly when

$$
v^2=\frac{\mu^2}{\varpi_{\mathrm{cpl}}} .
$$

**What the condition does.** It converts two parameters of the potential into one parameter and one derived scale. The two parameters are $\mu^2$ and $\varpi_{\mathrm{cpl}}$; the derived scale is $v$; and the mass is $m_h^2=2\varpi_{\mathrm{cpl}}v^2=2\mu^2$.

**What the condition is not.** It is not a piece of the list and it is not a prediction. It is the statement that the vacuum is the minimum, and a theory expanded about any other point would have a tadpole piece and a wrong mass. The condition holds by the definition of the expansion point.

**The constant term is the one row with no fields.** $-\frac{\varpi_{\mathrm{cpl}}v^4}{4}$ is the vacuum energy density. It has dimension zero, changes no vertex, and is excluded from the list by [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html) as the only candidate with no field content. Its exclusion is the reason the scalar contributes two pieces and not three.

## Why $v$ Is Derived

**Two parameters, one scale, one mass.** The potential has two numbers. The condition removes one combination, leaving $v$; the curvature at the minimum is the other, leaving $m_h$. The count is two in and two out, and [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) states the map: $(v,m_h)\leftrightarrow(\mu^2,\varpi_{\mathrm{cpl}})$, invertible.

**Why this matters for the whole list.** Every mass in the broken list carries $v$: the two vector masses, the nine fermion masses, and every $hVV$ and $h\bar ff$ coupling. A $v$ that were a free parameter would make the list look as though it had one more number than it does. The tadpole condition is what ties the scale to the potential's parameters and keeps the count at nineteen.

**The two directions of the map.** Given $(\mu^2,\varpi_{\mathrm{cpl}})$, the condition gives $v$ and the curvature gives $m_h$. Given $(v,m_h)$, the relations give $\varpi_{\mathrm{cpl}}=m_h^2/(2v^2)$ and $\mu^2=m_h^2/2$. Neither direction loses information.

## Checks

1. The count. Two rows, the fifth and sixth of the forty-seven.
2. The dimension. $\partial h\partial h$ has dimension four; $m_h^2h^2$ has dimension four.
3. The factor. One real field, so $\tfrac12$ on both pieces.
4. The tadpole. $v(\varpi_{\mathrm{cpl}}v^2-\mu^2)=0$ at $v^2=\mu^2/\varpi_{\mathrm{cpl}}$.
5. The mass. The second derivative of $V$ at the minimum is $2\varpi_{\mathrm{cpl}}v^2$, so $m_h^2=2\varpi_{\mathrm{cpl}}v^2=2\mu^2$.
6. The Taylor coefficients. Comparing $V(v+h)$ with the two pieces and the two self-pieces gives $\varpi_{\mathrm{cpl}}v^2=\tfrac12m_h^2$, $\varpi_{\mathrm{cpl}}v=\lambda_3/3!$ and $\varpi_{\mathrm{cpl}}/4=\lambda_4/4!$, which [The Higgs Self-Pieces](the-higgs-self-pieces-two-couplings-and-one-quartic.html) converts into the two couplings.
7. The constant term. $V(v)=-\varpi_{\mathrm{cpl}}v^4/4$, dimension zero, no vertex, excluded.
8. The Goldstone count. $4-3=1$ component, and the three removed are the longitudinal modes.
9. The invertibility. $(v,m_h)\leftrightarrow(\mu^2,\varpi_{\mathrm{cpl}})$ in both directions.
10. The normalisation's meaning. A rescaling $h\mapsto h/\sqrt{Z}$ moves $Z$ between the kinetic piece and every other $h$ piece, which is why the canonical choice is a convention and not a measurement.

## Summary

The scalar contributes two quadratic pieces, $\tfrac12\partial_\mu h\partial^\mu h$ and $-\tfrac12m_h^2h^2$, and one condition, the vanishing of the coefficient linear in $h$. The two pieces carry the canonical normalisation and the mass $m_h^2=2\varpi_{\mathrm{cpl}}v^2$; the condition fixes $v^2=\mu^2/\varpi_{\mathrm{cpl}}$.

The condition is not a piece and not a prediction. It is the statement that the expansion point is the minimum of the potential, and without it the expansion would produce a tadpole piece and a different mass.

The constant term of the potential, $-\varpi_{\mathrm{cpl}}v^4/4$, is the vacuum energy density. It is dimension zero, changes no vertex, and is the one candidate of dimension at most four that the completeness enumeration excludes for having no field content.

The two pieces are what keeps the count of parameters at nineteen. Every mass and every Higgs coupling carries $v$, and $v$ is derived from the potential's two parameters rather than added as a twentieth.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h$ | The physical scalar, one real component of the doublet |
| $m_h$ | Its mass, $m_h^2=2\varpi_{\mathrm{cpl}}v^2$ |
| $\mu^2$, $\varpi_{\mathrm{cpl}}$ | The two parameters of the potential |
| $V(v+h)$ | The potential expanded about the minimum |
| $-\varpi_{\mathrm{cpl}}v^4/4$ | The vacuum energy density, excluded |

## Further Reading

- [The Lagrangian and the Higgs Field](the-lagrangian-and-the-higgs-field.html). The potential, the radial variable and the unitary chart.
- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Vector-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html). The expansion shared with the vector masses.
- [The Higgs Mechanism in Biquaternionic Form](the-higgs-mechanism-in-biquaternionic-form.html). The abelian case and the eaten field.
- [The Higgs Self-Pieces](the-higgs-self-pieces-two-couplings-and-one-quartic.html). The two non-quadratic rows of the same expansion.
- [Nineteen and Nineteen](nineteen-and-nineteen-the-parameter-count-before-and-after-the-rotation.html). Why $v$ is derived and the count stays at nineteen.
