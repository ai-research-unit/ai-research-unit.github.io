# __The Peirce Basis of the Biquaternion Algebra__

## Introduction

A root of one gives the Peirce decomposition of the biquaternion algebra $\mathbb{B}$: the four lines are fixed by the root. A **Peirce basis** is more. It is a choice of one nonzero element in each line, with the multiplication rule of the lines. The two diagonal elements are forced by the idempotents. The two mixed elements are not: the root fixes each mixed line as a set, but it does not choose a point in it.

The extra datum is a nonzero element of one mixed line. Once it is chosen, the element of the other mixed line is forced by the product normalization. The remaining freedom is a nonzero complex scale, the **gauge**. So a basis is a root together with a gauge, and the gauge is not a property of the root.

The article proves that every root admits a basis, gives the construction from a root and a transverse vector, computes the coordinates and their product, states the gauge as a torsor, its stabiliser and its gauge fixings, proves that every basis of a fixed family is conjugate to the constructed one, and counts the real dimensions. The second root is treated in a remark at the end. No family is preferred. An example is given at the end.

## Definition

Let $\tilde\Pi_{+},\tilde\Pi_{-}$ be a nondegenerate complete family, with root $\tilde\Xi=\tilde\Pi_{+}-\tilde\Pi_{-}$, and let $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$.

**Definition.** A **Peirce basis** relative to the family is a family $E_{st}\in\mathbb{B}_{st}$, one element for each pair $s,t\in\{+,-\}$, such that
$$
E_{st}E_{uv}=\delta_{tu}E_{sv},\qquad E_{ss}=\tilde\Pi_{s}.
$$
The diagonal elements are therefore $E_{++}=\tilde\Pi_{+}$ and $E_{--}=\tilde\Pi_{-}$. The mixed elements are nonzero, and they satisfy
$$
E_{+-}E_{-+}=\tilde\Pi_{+},\qquad E_{-+}E_{+-}=\tilde\Pi_{-},\qquad
E_{+-}^{2}=E_{-+}^{2}=0.
$$

## From the Root to a Basis

**Theorem.** Let $\tilde\Xi=i\vec u$ with $\vec u\cdot\vec u=1$. Let $\vec v$ be a complex vector with
$$
\vec u\cdot\vec v=0,\qquad q=\vec v\cdot\vec v\ne0.
$$
Put
$$
\vec\Upsilon_{+-}=\vec v+i\,\vec u\times\vec v,\qquad
\vec\Upsilon_{-+}=\frac{-\vec v+i\,\vec u\times\vec v}{4q}.
$$
Then
$$
E_{++}=\tilde\Pi_{+},\quad E_{+-}=\vec\Upsilon_{+-},\quad
E_{-+}=\vec\Upsilon_{-+},\quad E_{--}=\tilde\Pi_{-}
$$
is a Peirce basis. Such a $\vec v$ exists: the transverse plane is two-dimensional, and its isotropic vectors form two complex lines, so any other vector works.

**Proof.** Let $T=\vec u\times\vec v$. Since $\vec u\cdot\vec v=0$ and $\vec u\cdot\vec u=1$,
$$
\vec u\cdot T=0,\qquad \vec v\cdot T=0,\qquad T\cdot T=q,
$$
$$
\vec v\,T=q\vec u,\qquad T\vec v=-q\vec u,\qquad
\vec u\,T=-\vec v,\qquad T\vec u=\vec v.
$$
Then
$$
\vec\Upsilon_{+-}^{2}=(\vec v+iT)^{2}
=\vec v^{2}-T^{2}+i(\vec vT+T\vec v)=-q+q+0=0,
$$
and similarly $\vec\Upsilon_{-+}^{2}=0$. For the product,
$$
\vec\Upsilon_{+-}\vec\Upsilon_{-+}
=\frac{(\vec v+iT)(-\vec v+iT)}{4q}
=\frac{-\vec v^{2}+i(\vec vT-T\vec v)-T^{2}}{4q}
=\frac{2q+2i q\vec u}{4q}
=\tilde\Pi_{+},
$$
and the same computation with the signs exchanged gives $\vec\Upsilon_{-+}\vec\Upsilon_{+-}=\tilde\Pi_{-}$. A direct computation with the same relations gives the corner conditions
$$
\tilde\Pi_{+}\vec\Upsilon_{+-}=\vec\Upsilon_{+-}=\vec\Upsilon_{+-}\tilde\Pi_{-},\qquad
\tilde\Pi_{-}\vec\Upsilon_{-+}=\vec\Upsilon_{-+}=\vec\Upsilon_{-+}\tilde\Pi_{+}.
$$
All other products vanish by the product rule of the lines. Hence the four elements form a Peirce basis.

**What the construction uses.** The root $\vec u$ fixes the two mixed lines. The vector $\vec v$ chooses a point in $\mathbb{B}_{+-}$ and, through the normalization, a point in $\mathbb{B}_{-+}$. The conditions are: $\vec v$ is transverse to $\vec u$, and $\vec v$ is not isotropic, $q\ne0$. These are conditions on the extra datum, not on the root. The root has a transverse plane, but it chooses no vector in it.

**The gauge is the scale of $\vec v$.** For $\lambda\in\mathbb{C}^{\times}$, replace $\vec v$ by $\lambda\vec v$. Then
$$
\vec\Upsilon_{+-}\mapsto\lambda\,\vec\Upsilon_{+-},\qquad
\vec\Upsilon_{-+}\mapsto\lambda^{-1}\vec\Upsilon_{-+}.
$$
So the same root and the same family carry a one-parameter family of bases. The parameter $\lambda$ is the gauge. The basis is determined by the root and by $\vec v$, modulo this scale. If $\vec v$ is normalized by $\vec v\cdot\vec v=1$, the scale is reduced to $\lambda=\pm1$; the unnormalized $\vec v$ is the object that carries the full gauge.

## Coordinates

For $\tilde Q\in\mathbb{B}$ write
$$
\tilde Q=Q_{++}\tilde\Pi_{+}+Q_{+-}E_{+-}+Q_{-+}E_{-+}+Q_{--}\tilde\Pi_{-}.
$$
The four coefficients are the **Peirce coordinates** of $\tilde Q$. They are complex numbers, and they depend on the basis.

**The product.** If $\tilde Q'$ has coordinates $Q'_{st}$, the coordinates of $\tilde Q\tilde Q'$ are
$$
\begin{aligned}
Q''_{++}&=Q_{++}Q'_{++}+Q_{+-}Q'_{-+},\\
Q''_{+-}&=Q_{++}Q'_{+-}+Q_{+-}Q'_{--},\\
Q''_{-+}&=Q_{-+}Q'_{++}+Q_{--}Q'_{-+},\\
Q''_{--}&=Q_{-+}Q'_{+-}+Q_{--}Q'_{--}.
\end{aligned}
$$
This is the product rule of the lines written in coordinates.

**The norm.** A direct expansion gives
$$
Q_{++}Q_{--}-Q_{+-}Q_{-+}=Q_{t}^{2}+Q_{x}^{2}+Q_{y}^{2}+Q_{z}^{2},
$$
where $\tilde Q=Q_{t}e_{t}+Q_{x}\vec e_{x}+Q_{y}\vec e_{y}+Q_{z}\vec e_{z}$. The left side is therefore independent of the basis, as it must be.

## The Gauge

**A change of basis of the same family.** Let $E_{st}$ and $F_{st}$ be two bases of the same family. Each line is one-dimensional and the diagonal elements are fixed, so
$$
F_{st}=c_{st}E_{st},\qquad c_{++}=c_{--}=1.
$$
The product $F_{+-}F_{-+}=\tilde\Pi_{+}$ gives $c_{+-}c_{-+}=1$. Put $t=c_{-+}$. Then
$$
F_{+-}=t^{-1}E_{+-},\qquad F_{-+}=tE_{-+},\qquad t\in\mathbb{C}^{\times}.
$$
This is the **gauge transformation**. In the construction above, $t=\lambda^{-1}$.

**The gauge group.** The same transformation reads
$$
E_{st}\longmapsto d_{s}d_{t}^{-1}E_{st},\qquad d_{+},d_{-}\in\mathbb{C}^{\times}.
$$
The pairs $(d_{+},d_{-})$ and $(\mu d_{+},\mu d_{-})$ agree on every line, because $(\mu d_{s})(\mu d_{t})^{-1}=d_{s}d_{t}^{-1}$. The **gauge group** is therefore
$$
G=(\mathbb{C}^{\times})^{2}/\mathbb{C}^{\times}\cong\mathbb{C}^{\times},\qquad t=d_{-}d_{+}^{-1}.
$$
The quotient is by the scalars, which act trivially. The same definition applies to a system of matrix units for $n$ orthogonal idempotents in $M_{n}(\mathbb{C})$:
$$
G=(\mathbb{C}^{\times})^{n}/\mathbb{C}^{\times}\cong(\mathbb{C}^{\times})^{n-1},\qquad
E_{ij}\longmapsto d_{i}d_{j}^{-1}E_{ij},
$$
and for $n=2$ this is the group above. The dimension $n-1$ is the number of independent rescalings of the lines.

**The bases form a torsor.** Fix the family $F$ and let $\mathcal{B}(F)$ be the set of its Peirce bases. Then $\mathcal{B}(F)$ is a $G$-torsor: the action is free and transitive.

*Free.* If $d_{s}d_{t}^{-1}=1$ for all $s,t$, then $d_{+}=d_{-}$, and the pair is the diagonal class, the identity of $G$.

*Transitive.* For bases $E$ and $F$, write $F_{st}=c_{st}E_{st}$ as above and take $d_{+}=c_{+-}$, $d_{-}=1$. Then $d_{+}d_{-}^{-1}=c_{+-}$ and $d_{-}d_{+}^{-1}=c_{+-}^{-1}=c_{-+}$, so the action carries $E$ to $F$.

A torsor is not a group: it has no identity, because no basis is distinguished. **The group $G$ is the gauge group; a choice of basis is a point of $\mathcal{B}(F)$.** The root fixes the family and hence the torsor, but no point of it.

**The stabiliser.** The action is free, so the stabiliser of a basis in $G$ is trivial. In the unit group the same fact reads as follows. The units that fix the two idempotents are
$$
\tilde U=a\tilde\Pi_{+}+b\tilde\Pi_{-},\qquad a,b\in\mathbb{C}^{\times},
$$
and conjugation by $\tilde U$ acts on the basis by
$$
E_{+-}\longmapsto\frac{b}{a}E_{+-},\qquad E_{-+}\longmapsto\frac{a}{b}E_{-+}.
$$
The map $\tilde U\mapsto(a,b)$ is an isomorphism $U(F)\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, and the centre is the diagonal $a=b$, so
$$
G\cong U(F)/Z(\mathbb{B}^{\times}),
$$
and the stabiliser of a basis in $U(F)$ is the centre. Two bases are therefore conjugate by a unit, with $t=a/b$, and the conjugating unit is unique up to the centre. This is the inner form of the torsor statement.

**Coordinates under the gauge.** The element is fixed, so
$$
Q'_{st}=Q_{st}\,d_{t}d_{s}^{-1},
$$
that is,
$$
Q'_{++}=Q_{++},\qquad Q'_{+-}=tQ_{+-},\qquad
Q'_{-+}=t^{-1}Q_{-+},\qquad Q'_{--}=Q_{--}.
$$
The product and the norm above are unchanged.

**Gauge fixing.** A **gauge fixing** is a section of the torsor: a rule that selects one basis in each family. Two remarks separate a condition on a basis from a choice of one.

- The nonvanishing of the mixed elements and the product normalization $E_{+-}E_{-+}=\tilde\Pi_{+}$ are part of the definition of a basis. They do not fix $t$: the rescaled pair $(t^{-1}E_{+-},tE_{-+})$ is again a basis.
- The Hermitian condition $E_{+-}^{*}=E_{-+}$, when the root is Hermitian, reduces the orbit to $|t|=1$. It restricts the gauge but does not fix it: a circle remains.

A point of the torsor requires an extra datum. In the construction above that datum is the transverse vector $\vec v$; the section is defined over the families together with a chosen transverse direction, not over the root alone. The gauge is not a symmetry of the algebra: it changes the coordinates, not the element and not the lines.

## Dimensions

**The count is $6=4+2$ in real dimensions.**

A basis is a family together with a nonzero element of one mixed line. The family is a root modulo sign; a root is $\tilde\Xi=i\vec u$ with $\vec u\cdot\vec u=1$, which has two complex parameters, that is four real. The nonzero element of a complex line has two real parameters. Hence the bases have
$$
4+2=6
$$
real parameters.

The fiber over a family is the torsor $\mathcal{B}(F)$, whose group $G$ has one complex parameter, that is two real parameters. So
$$
\underbrace{6}_{\text{bases}}=\underbrace{4}_{\text{families}}+\underbrace{2}_{\text{gauge}}.
$$

**A check against the construction.** The root $\vec u$ has four real parameters. The transverse vector $\vec v$ modulo scale is a point of a complex projective line, of two real parameters. The pair $(\vec u,\vec v)$ modulo scale therefore has six real parameters. This is the same count.

## Example: The Root $i\vec e_{z}$

This example is given at the end because it is one point in the four-real-parameter space of roots, not a preferred one.

For $\tilde\Xi=i\vec e_{z}$ take $\vec v=\vec e_{x}$. Then $q=1$ and the construction gives
$$
\vec\Upsilon_{+-}=\vec e_{x}+i\vec e_{y},\qquad
\vec\Upsilon_{-+}=\frac{-\vec e_{x}+i\vec e_{y}}{4}.
$$
The rescalings
$$
\vec\Upsilon_{1}=\frac{i}{2}\vec\Upsilon_{+-}=\frac{i\vec e_{x}-\vec e_{y}}{2},\qquad
\vec\Upsilon_{2}=-2i\,\vec\Upsilon_{-+}=\frac{i\vec e_{x}+\vec e_{y}}{2}
$$
give the pair often written down. It satisfies
$$
\vec\Upsilon_{1}\vec\Upsilon_{2}=\tilde\Pi_{+},\qquad
\vec\Upsilon_{2}\vec\Upsilon_{1}=\tilde\Pi_{-},\qquad
\vec\Upsilon_{1}^{2}=\vec\Upsilon_{2}^{2}=0.
$$
The rescaling is a gauge transformation with $t=-2i$.

## Remark: The Second Root

**A transverse root is a basis, not a second primitive.** Call $\tilde\Xi'$ transverse to $\tilde\Xi$ when
$$
\tilde\Xi\tilde\Xi'+\tilde\Xi'\tilde\Xi=0,\qquad \tilde\Xi'^{2}=e_{t}.
$$
In a basis $E$ of the family of $\tilde\Xi$, every transverse root is
$$
\tilde\Xi'=\tau E_{+-}+\tau^{-1}E_{-+},\qquad \tau\in\mathbb{C}^{\times},
$$
and conversely. The diagonal part of $\tilde\Xi'$ commutes with $\tilde\Xi$ and the mixed part anticommutes, so a transverse element is purely mixed; its square is $\tau\sigma e_{t}$, and $\tau\sigma=1$.

**It is a point of the torsor.** A transverse root determines a basis with no further choice:
$$
E_{+-}=\frac12\left(\tilde\Xi'+\frac12[\tilde\Xi,\tilde\Xi']\right),\qquad
E_{-+}=\frac12\left(\tilde\Xi'-\frac12[\tilde\Xi,\tilde\Xi']\right).
$$
For $\tilde\Xi'=\tau E_{+-}+\tau^{-1}E_{-+}$ one has $\tfrac12[\tilde\Xi,\tilde\Xi']=\tau E_{+-}-\tau^{-1}E_{-+}$, so these give $\tau E_{+-}$ and $\tau^{-1}E_{-+}$, whose product is $\tilde\Pi_{+}$. The inverse map is $\tilde\Xi'=E_{+-}+E_{-+}$. Hence the transverse roots are in canonical bijection with the Peirce bases: a transverse root is exactly a point of the gauge torsor. The root gives the family and the torsor; the transverse root chooses the point, that is, the basis. It produces no new idempotents: those come from $\tilde\Xi$ alone.

**In $M_{n}(\mathbb{C})$.** A transverse root exists only when the two eigenvalues of $\tilde\Xi$ have equal multiplicity, so $n=2m$; for odd $n$ there is none. In blocks,
$$
\tilde\Xi'=\begin{pmatrix}0&A\\A^{-1}&0\end{pmatrix},\qquad A\in GL_{m}(\mathbb{C}),
$$
and the transverse roots have $m^{2}$ complex parameters. For a family of $n$ idempotents the gauge has $n-1=2m-1$ parameters. The two counts agree only for $m=1$, that is $n=2$. For $n>2$ a transverse root does not determine a frame: it identifies the two blocks through $A$ but fixes no basis inside either block. The second root is therefore a phenomenon of dimension two. In higher dimension the torsor and its gauge group are the general notion, and no single element plays its role.

## Summary

A Peirce basis of a nondegenerate family of $\mathbb{B}$ is a choice $E_{st}\in\mathbb{B}_{st}$ with $E_{st}E_{uv}=\delta_{tu}E_{sv}$ and $E_{ss}=\tilde\Pi_{s}$. The root fixes the four lines but not the mixed elements. To build a basis one adds a transverse vector $\vec v$, with $\vec u\cdot\vec v=0$ and $\vec v\cdot\vec v\ne0$; the formulas $\vec\Upsilon_{+-}=\vec v+i\vec u\times\vec v$ and $\vec\Upsilon_{-+}=(-\vec v+i\vec u\times\vec v)/(4\vec v\cdot\vec v)$ give the mixed elements, and the product normalization is then automatic. The scale of $\vec v$ is the gauge, $E'_{+-}=t^{-1}E_{+-}$ and $E'_{-+}=tE_{-+}$. The bases of a fixed family form a torsor under $G\cong\mathbb{C}^{\times}$; the action is free, so the stabiliser of a basis in $G$ is trivial, and in the unit group it is the centre. Nonvanishing and product normalization belong to the definition of a basis and leave $t$ free; the Hermitian condition restricts the gauge to $|t|=1$ but does not fix it. The coordinates multiply by the four-term rule, and the norm is $Q_{++}Q_{--}-Q_{+-}Q_{-+}$. Every basis of a fixed family is conjugate to the constructed one. The dimensions are $6=4+2$: six real for the bases, four for the families, two for the gauge. A second root is a point of the torsor, hence a gauge choice; a single such element exists only in dimension two.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra |
| $\tilde\Xi=i\vec u$ | The root, with $\vec u\cdot\vec u=1$ |
| $\tilde\Pi_{\pm}$ | The complete family of two idempotents |
| $\mathbb{B}_{st}=\tilde\Pi_{s}\mathbb{B}\tilde\Pi_{t}$ | A Peirce line |
| $E_{st}$ | A Peirce basis, with $E_{ss}=\tilde\Pi_{s}$ |
| $\vec\Upsilon_{+-},\vec\Upsilon_{-+}$ | The mixed elements of a basis |
| $Q_{st}$ | The Peirce coordinates of $\tilde Q$ |
| $\mathcal{B}(F)$ | The set of Peirce bases of the family $F$ |
| $G=(\mathbb{C}^{\times})^{2}/\mathbb{C}^{\times}$ | The gauge group, a $\mathbb{C}^{\times}$ |
| $t$ | The gauge parameter, $t=d_{-}d_{+}^{-1}$ |

## Further Reading

- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the four lines and the root.
- [Spinors as Peirce Coordinates in the Biquaternion Algebra](spinors-as-peirce-coordinates-in-the-biquaternion-algebra.html), for the elements of the two spinor spaces.
- [Idempotents](idempotents.html), for the roots and the idempotents.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the units and the centre.
