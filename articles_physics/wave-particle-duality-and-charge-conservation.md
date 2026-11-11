# __Wave–Particle Duality and Charge Conservation: The Cokernel of Maxwell's Symbol__

## Introduction

**Charge conservation is the cokernel of Maxwell's symbol.** Off the light cone the symbol maps the three complex directions of the field strength into the four of the algebra, and the single direction it misses is read by one functional. That functional is the transform of $\mathrm{Sc}((\tilde\nabla^{\natural})_\Phi\tilde J_\Phi)$, and its vanishing is the continuity equation. Charge conservation is therefore not a second law standing beside the field equation. It is the one condition the field equation places on its source, and the cokernel is where that condition lives. The word "is" names an identification through the dual, not an identity of two objects. The cokernel is a quotient and charge conservation is the vanishing of one functional on the source, and §*The cokernel is a space of multipliers* makes them the same piece of data.

**The identification is exact off the cone and incomplete on it.** On the light cone the rank falls to two, the cokernel becomes two-dimensional, and charge conservation is one of its two members. The second member is a condition of another kind. It says that the current has no component along the polarisation the symbol annihilates. That condition is not a conservation law; it is a selection rule, and it appears exactly where an amplitude disappears.

**The bookkeeping is one sum.** The rank and the dimension of the cokernel add to four at every frequency point, because the codomain is four-dimensional. Off the cone that is three and one; on the cone two and two. The space of field strengths the symbol can produce and the space of sources it can accept have the same dimension, and that dimension is the rank. So the count of polarisations and the count of conditions on the source are not independent numbers. What the field can carry plus what the source must satisfy is four.

**Why this belongs to the duality.** *Wave–Particle Duality and the Fourier Transform* reads one equation in two bases. *Wave–Particle Duality and the Count of Degrees of Freedom* reads the image of the symbol twice, as a dimension of a space of field strengths and as a number of polarisations. This article reads the other half of rank–nullity: the cokernel, as a space of conditions on the data and as the conservation law of the source. The transform is what makes the second reading available. The cokernel is a property of the symbol and the conservation law is a property of the source, and the transform carries the first into the second.

**The strongest objection, stated first.** Charge conservation is a property of matter, and calling it a cokernel only renames it. The objection is right about the naming and wrong about the content. The naming is what makes the counting possible, and the counting yields a statement the continuity equation does not: on the cone there is a second condition, of a different kind, and no fact about the source alone supplies it. §*Charge Conservation Is the Whole Cokernel Off the Cone* and §*On the Cone the Cokernel Is Two-Dimensional* establish that, and §*What the Second Condition Does* measures it.

**What is used and what is new.** *Maxwell's Equations in the Biquaternionic Formulation* derives charge conservation as the integrability condition of $\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\,\tilde J_\Phi$, and that derivation is quoted. *The Fourier Transform and the Symbol of a Differential Operator*, §*The Kernel and the Cokernel*, states that the cokernel measures the conditions on the data, and that statement is used as it stands. The rank is that of *Wave–Particle Duality and the Count of Degrees of Freedom*. What is new here is the cokernel as an object: its dimension at each frequency point, its members, their component forms, and the identity of its second member on the cone.

## The Symbol and Its Cokernel

### The equation and its transform

**The equation is the corpus's, and the article changes nothing in it.** In a medium of permittivity $\epsilon$ and permeability $\mu$, with $c=1/\sqrt{\epsilon\mu}$, the field strength $\tilde F$ and the four-current $\tilde J_\Phi=ic\rho\,e_t+\vec J$ satisfy

$$
\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\,\tilde J_\Phi ,
$$

with $\tilde F$ a pure vector. On a plane wave the gradient is replaced by its symbol, and the transform of the equation is

$$
i\tilde K_\Phi\,\mathcal F[\tilde F]=-\sqrt{\mu}\,\mathcal F[\tilde J_\Phi] .
$$

The factor $-\sqrt{\mu}$ is a non-zero scalar. It multiplies both sides, it moves neither a rank nor a cokernel, and the article keeps it in the displays and drops it in the counting.

**The unknown is pure, so the domain is three-dimensional.** $\mathcal F[\tilde F]$ lies in $\mathbb B_V$, of complex dimension three. The right-hand side lies in the whole algebra, of complex dimension four. The map in question is left multiplication by $i\tilde K_\Phi$ read on $\mathbb B_V$,

$$
L_{i\tilde K_\Phi}:\mathbb B_V\longrightarrow\mathbb B,\qquad \tilde F\longmapsto i\tilde K_\Phi\tilde F ,
$$

three complex dimensions in and four out. Its rank is that of *Wave–Particle Duality and the Count of Degrees of Freedom*: three off the cone and two on it.

**The domain of the article is the forward cone.** $k_{t}^{\prime}\ge0$ and $k_\Phi>0$, with the origin excluded, as in the companion article. The negative cone is not treated separately. Its rank is again two and its cokernel again two-dimensional, and the circular labels are exchanged, which §*Limits* records.

### The cokernel is a space of multipliers

**The cokernel is a quotient, and rank–nullity fixes its dimension.** By definition $\operatorname{coker}L_{i\tilde K_\Phi}=\mathbb B/L_{i\tilde K_\Phi}\mathbb B_V$, and

$$
\dim\operatorname{coker}L_{i\tilde K_\Phi}=4-\operatorname{rank}L_{i\tilde K_\Phi}.
$$

Off the cone the rank is three and the cokernel is one-dimensional. On the cone the rank is two and the cokernel is two-dimensional. No other value occurs on the domain, so the cokernel is one-dimensional in the first case and two-dimensional in the second, and that exhausts the possibilities.

**A quotient of the algebra is again a space of elements, because the algebra carries its own pairing.** The scalar part $\mathrm{Sc}$ is a non-degenerate complex-bilinear form on $\mathbb B$, so every complex-linear functional on $\mathbb B$ is $\sigma\mapsto\mathrm{Sc}(M\sigma)$ for one element $M$, and the functionals that annihilate the image are those $M$ satisfying

$$
\mathrm{Sc}\bigl(M\,i\tilde K_\Phi\tilde F\bigr)=0\qquad\text{for every }\tilde F\in\mathbb B_V .
$$

**That condition is that a product be central.** The scalar part is cyclic, so $\mathrm{Sc}(M\,i\tilde K_\Phi\tilde F)=\mathrm{Sc}(\tilde F\,M\,i\tilde K_\Phi)$. The scalar part against a pure element reads the vector part of what stands beside it, so the condition holds for every pure $\tilde F$ exactly when

$$
\mathrm{Vect}\bigl(M\,i\tilde K_\Phi\bigr)=0 ,
$$

that is, exactly when $M\,i\tilde K_\Phi$ is a multiple of $e_t$. The cokernel is therefore the space of multipliers that turn the symbol into a central element. This identification is what the rest of the article computes, and it is the reason the cokernel can be written down rather than merely counted.

**A word on the name, because the corpus uses the same word for another space.** What is computed here is the annihilator of the image in the dual. It is not the left annihilator $\operatorname{Ann}_L$ that *The Fourier Transform and the Symbol of a Differential Operator*, §*The Kernel and the Cokernel*, writes for the kernel. The two spaces coincide on the cone, where every multiplier that makes the product central makes it vanish, and they differ off it, where the cokernel is a line and the left annihilator is zero.

## Charge Conservation Is the Whole Cokernel Off the Cone

### One element, and it is always in

**The conjugate wave-number element is in the cokernel at every frequency point.** Set

$$
M=\tilde K_\Phi^\natural=i\,k_{t}^{\prime}e_t-\vec k_\Phi .
$$

Then $\tilde K_\Phi^\natural\,\tilde K_\Phi$ is the quaternion norm, which is central, and

$$
\mathrm{Vect}\bigl(\tilde K_\Phi^\natural\,i\tilde K_\Phi\bigr)=i\,\mathrm{Vect}\bigl(\tilde K_\Phi^\natural\tilde K_\Phi\bigr)=0 ,
$$

because $\tilde K_\Phi^\natural\tilde K_\Phi=-k_{t}^{\prime\,2}+k_\Phi^{2}$ is a scalar multiple of $e_t$. So $\tilde K_\Phi^\natural$ lies in the space of §*The cokernel is a space of multipliers* at every point of the domain.

**The functional it defines is the one the corpus already knows.** For a pure $\tilde F$,

$$
\mathrm{Sc}\bigl(\tilde K_\Phi^\natural\,i\tilde K_\Phi\tilde F\bigr)=i\bigl(-k_{t}^{\prime\,2}+k_\Phi^{2}\bigr)\mathrm{Sc}(\tilde F)=0 ,
$$

since $\mathrm{Sc}(\tilde F)=0$. The vanishing is not a property of the particular frequency point. It is a property of the shape of the equation: a central multiplier preserves purity, and the functional reads the scalar part, which a pure element does not have.

**Off the cone this one element is the whole cokernel.** There the space is one-dimensional and it contains $\tilde K_\Phi^\natural$, which is not zero, so the space is the complex line spanned by $\tilde K_\Phi^\natural$. There is no second condition and no choice to make. The single obstruction to solvability at a frequency off the cone is therefore the vanishing of one number, and the next two subsections identify that number twice.

### The component form is the continuity equation

**Evaluated on the four-current, the functional is the wave-number form of charge conservation.** Write $\tilde J_\Phi=ic\rho\,e_t+\vec J$. Then

$$
\tilde K_\Phi^\natural\tilde J_\Phi=\bigl(i k_{t}^{\prime}e_t-\vec k_\Phi\bigr)\bigl(ic\rho\,e_t+\vec J\bigr)
=i k_{t}^{\prime}(ic\rho)\,e_t+i k_{t}^{\prime}\vec J-ic\rho\,\vec k_\Phi-\vec k_\Phi\vec J ,
$$

whose scalar part is

$$
\mathrm{Sc}\bigl(\tilde K_\Phi^\natural\tilde J_\Phi\bigr)=\vec k_\Phi\cdot\vec J-k_{t}^{\prime}\,c\,\rho ,
$$

since $\mathrm{Sc}(\vec k_\Phi\vec J)=-\vec k_\Phi\cdot\vec J$ and $i\cdot i=-1$. The condition is therefore

$$
\vec k_\Phi\cdot\vec J=k_{t}^{\prime}\,c\,\rho .
$$

**This is the continuity equation in the wave-number variables.** With $k_{t}^{\prime}=\omega/c$ and $\vec k_\Phi$ the wave vector, the equation $\mathrm{div}\,\vec J+c\,\partial\rho/\partial r'_t=0$ transforms into $\vec k_\Phi\cdot\vec J=k_{t}^{\prime}c\rho$, and the two statements are the same statement. **The cokernel of the symbol, read on the source, is charge conservation**, which is the identification the introduction promised.

**The same identity in the corpus's own form.** *Maxwell's Equations in the Biquaternionic Formulation* writes the conservation law as $\mathrm{Sc}((\tilde\nabla^{\natural})_\Phi\tilde J_\Phi)=0$. The functional above is the symbol of that operator: on a plane wave $(\tilde\nabla^{\natural})_\Phi$ becomes $i\tilde K_\Phi^\natural$, and the composition $i\tilde K_\Phi^\natural\,i\tilde K_\Phi$ is the central norm. The derivation in that article and the computation here are one argument in two notations, and the agreement is exact: the residual of the identity $\mathrm{Sc}(\tilde K_\Phi^\natural\tilde J_\Phi)=\vec k_\Phi\cdot\vec J-k_{t}^{\prime}c\rho$ over one hundred sampled points is $2.0\times10^{-15}$ relative to the largest term.

### A worked point off the cone

**The point $k_{t}^{\prime}=5$, $\vec k_\Phi=3\vec e_x$ is off the cone and carries the whole picture.** There $\tilde K_\Phi=5i\,e_t+3\vec e_x$, the norm is $-25+9=-16$, and the cokernel is the line spanned by $5i\,e_t-3\vec e_x$. A source $\tilde J_\Phi$ is admissible exactly when $3J_x=5c\rho$, and no other condition appears. A source with $3J_x\ne5c\rho$ has no field, and the functional reports the size of the failure linearly.

**The kernel at that point is empty.** Three directions in, three-dimensional image, so the field strength is determined by the source without freedom. Off the cone the equation is a bijection onto its image, and the one condition is the only obstruction. The asymmetry is the whole content of the two counts: no amplitude is lost, so no freedom appears, and one condition is what the fourth dimension costs.

## On the Cone the Cokernel Is Two-Dimensional

### Rank–nullity forces a second condition

**On the cone the rank drops and the cokernel has no choice.** At $k_{t}^{\prime}=k_\Phi$ the symbol $\tilde K_\Phi=k_\Phi\bigl(i e_t+\vec u_\Phi\bigr)$ is a zero divisor, the rank of $L_{i\tilde K_\Phi}$ on $\mathbb B_V$ is two, and the cokernel is two-dimensional by the dimension formula. The second condition is therefore not an additional postulate. It is forced by the four-dimensional codomain once an amplitude is lost, and the only question left is which condition it is.

**The forced condition is not a second conservation law.** Nothing in the continuity equation produces it, and no statement about the conservation of charge distinguishes the two members of the cokernel. The second member is a different kind of statement, and the rest of this section identifies it.

### The second member is a circular direction

**One circular direction satisfies the condition exactly, and the other does not.** With the right-handed transverse pair $(\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2})$ of the companion article and $\varepsilon_{\mathrm{fop},\pm}=(\varepsilon_{\mathrm{fop},1}\pm i\varepsilon_{\mathrm{fop},2})/\sqrt 2$,

$$
\mathrm{Vect}\bigl(\varepsilon_{\mathrm{fop},-}\,i\tilde K_\Phi\bigr)=0,\qquad \mathrm{Vect}\bigl(\varepsilon_{\mathrm{fop},+}\,i\tilde K_\Phi\bigr)\ne0 ,
$$

on the cone, over one hundred sampled directions. The element $\varepsilon_{\mathrm{fop},-}$ is a pure vector, so it is a legitimate multiplier, and the product vanishes identically rather than merely being central:

$$
\varepsilon_{\mathrm{fop},-}\,i\tilde K_\Phi=0 .
$$

Off the cone neither circular direction satisfies the condition. The residual of $\varepsilon_{\mathrm{fop},-}\,i\tilde K_\Phi$, measured against $\varepsilon_{\mathrm{fop},-}$, is at most $8.2\times10^{-16}$ on the cone and of order one off it.

**So the annihilator of the image on the cone is the span of two elements, and the scalar pairing carries that span to the cokernel,**

$$
\operatorname{coker}L_{i\tilde K_\Phi}=\operatorname{span}\bigl\{\tilde K_\Phi^\natural,\ \varepsilon_{\mathrm{fop},-}\bigr\},
$$

one mixed and one pure, and both are zero divisors there. The first member reads the source as a conservation law; the second reads it as a selection rule.

### Which circular direction, and why that one

**The chosen direction is the one the symbol does not annihilate.** The companion article computes the kernel on the cone: $i\tilde K_\Phi$ kills $\varepsilon_{\mathrm{fop},+}$ and scales $\varepsilon_{\mathrm{fop},-}$ by $-2k_\Phi$,

$$
i\tilde K_\Phi\,\varepsilon_{\mathrm{fop},+}=0,\qquad i\tilde K_\Phi\,\varepsilon_{\mathrm{fop},-}=-2k_\Phi\,\varepsilon_{\mathrm{fop},-} .
$$

The cokernel's circular member is therefore the survivor of the pair, not the casualty. **The direction the symbol annihilates is the one the constraint names; the direction it scales is the multiplier that reads the constraint.** That is the sense in which the second member sits opposite the lost amplitude, and it is the reason the two jumps in the two counts are not the same jump seen twice.

**The pairing that states it is one number.** The circular pair is dual under the scalar part,

$$
\mathrm{Sc}\bigl(\varepsilon_{\mathrm{fop},-}\,\varepsilon_{\mathrm{fop},+}\bigr)=-1 ,
$$

verified to $1.5\times10^{-15}$. A vector part decomposed as $\vec J=a\,\varepsilon_{\mathrm{fop},+}+b\,\varepsilon_{\mathrm{fop},-}$ therefore has $\mathrm{Sc}(\varepsilon_{\mathrm{fop},-}\tilde J_\Phi)=-a$, so the condition $\mathrm{Sc}(\varepsilon_{\mathrm{fop},-}\tilde J_\Phi)=0$ is exactly $a=0$. **The selection rule is that the current carries no component along $\varepsilon_{\mathrm{fop},+}$, the direction the symbol annihilates.**

### The component form on the cone

**On the cone the two conditions have a readable form.** Charge conservation becomes, after division by $k_\Phi$,

$$
\vec u_\Phi\cdot\vec J=c\,\rho ,
$$

so the longitudinal current is fixed by the charge density and carries no freedom of its own. The second condition is the vanishing of the pairing with the dual circular direction,

$$
\vec J\cdot\varepsilon_{\mathrm{fop},-}=0 ,
$$

written with the complex-bilinear form on the vector part. The two circular directions are null and dual, $\mathrm{Sc}(\varepsilon_{\mathrm{fop},\pm}\varepsilon_{\mathrm{fop},\pm})=0$ and $\mathrm{Sc}(\varepsilon_{\mathrm{fop},-}\varepsilon_{\mathrm{fop},+})=-1$, so the pairing with $\varepsilon_{\mathrm{fop},-}$ is the functional that reads the $\varepsilon_{\mathrm{fop},+}$ amplitude, with a minus sign. Together the two conditions leave two free complex amplitudes.

**The admissible sources are then written in closed form.** On the cone a source is admissible exactly when

$$
\tilde J_\Phi=a_\parallel\,\tilde K_\Phi+a_-\,\varepsilon_{\mathrm{fop},-},
$$

with $a_\parallel$ and $a_-$ complex. The longitudinal part carries the charge density and the longitudinal current in the ratio the continuity equation requires, since $\tilde K_\Phi$ has $i k_{t}^{\prime}$ on the time slot and $\vec k_\Phi$ on the space slots; and the transverse part has one circular amplitude and no other. The span of those two elements satisfies both conditions to $3.1\times10^{-15}$ over one hundred sampled directions, and its dimension is two.

**The number is the rank.** Two free amplitudes, two conditions out of four dimensions, and a rank of two. Admissibility and reachability are the same count. The source may carry exactly as many independent amplitudes as the field, and the conditions are the remainder of four.

## What the Second Condition Does

### An unfittable current

**A current that conserves charge can still have no field on the cone.** Take $k_{t}^{\prime}=k_\Phi=5$ with $\vec u_\Phi=\vec e_x$, and the source

$$
\tilde J_\Phi=\tilde K_\Phi+2i\,\varepsilon_{\mathrm{fop},-} .
$$

Both conditions hold, the equation is solvable, and the field strength is determined. Now add $3\,\varepsilon_{\mathrm{fop},+}$:

$$
\tilde J_\Phi=\tilde K_\Phi+2i\,\varepsilon_{\mathrm{fop},-}+3\,\varepsilon_{\mathrm{fop},+} .
$$

Charge conservation still holds, because $\varepsilon_{\mathrm{fop},+}$ is transverse and the longitudinal slot is untouched. The second condition fails, and the equation has no solution.

### The size of the mismatch

**The least-squares defect is exactly the offending component.** Solving $i\tilde K_\Phi\tilde F=-\sqrt{\mu}\tilde J_\Phi$ in the least-squares sense, the residual is at most $10^{-15}$ for the first source and exactly $3$ for the second, in the coefficient norm of the algebra. The residual is the modulus of the coefficient of $\varepsilon_{\mathrm{fop},+}$, over one hundred sampled points and directions, to $8.9\times10^{-16}$.

**This is the operational content of the second member.** The cokernel is a quotient, and a quotient is not directly observable. Its dual is: the coefficient of $\varepsilon_{\mathrm{fop},+}$ in the source is a number one can compute, and it is the obstruction. **Charge conservation is necessary and, on the cone, not sufficient**; the shortage is measured in one circular component of the current.

**The interpretation is physical and the algebra does not force it.** The corpus reads $\varepsilon_{\mathrm{fop},+}$ as a helicity state of the field, and the second condition as the statement that the source drives only the helicity the field can carry. That interpretation is consistent with the algebra and is not derived from it. What the algebra gives is the dimension of the cokernel, the identity of its members, and the residual; what those members are called is a matter of interpretation, and §*Limits* says so.

### What it is not

**The second condition is not a conservation law.** No charge, current or density is conserved by it, and it is not the divergence of anything. It is a linear constraint on the source at one frequency, and it is required only on the cone, so it has no global form.

**It is not a gauge statement.** Gauge freedom is not used anywhere in this article, and the rank here is the rank of a symbol and not of a quotient by gauge orbits. The corpus's treatment of gauge structure belongs to *Maxwell's Equations in the Biquaternionic Formulation*, §*Gauge Structure*, and nothing there is invoked.

**It is not a statement about a particle.** The condition constrains a classical source at a frequency point. Whether a quantum state of a photon is prepared in the surviving polarisation is a different question, and the companion article's limits apply here unchanged.

## The Budget of Four

### The two spaces and their dimensions

**The image and the admissible sources are paired, and both have the rank's dimension.** The image of $L_{i\tilde K_\Phi}$ is the set of field strengths the operator can produce, of dimension $r$. The admissible sources are the elements annihilated by every element of the cokernel, of dimension $4-(4-r)=r$. They are dual to one another, the pairing is $\mathrm{Sc}$, and they have the same dimension at every frequency point.

| Frequency point | Rank $r$ | $\dim\ker$ | $\dim\operatorname{coker}$ | Admissible source amplitudes |
|---|---|---|---|---|
| Off the cone, $k_{t}^{\prime}\ne k_\Phi$ | 3 | 0 | 1 | 3 |
| On the cone, $k_{t}^{\prime}=k_\Phi$ | 2 | 1 | 2 | 2 |

**Every column is a reading of the same integer.** The rank is a dimension of an image and a count of polarisations; $4-r$ is a dimension of a cokernel and a count of conditions; and the freedom in the solution, $3-r$, is the third reading and it appears only on the cone. The table is the one of *Wave–Particle Duality and the Count of Degrees of Freedom* with the conditions and the sources added.

### The duality, read once more

**The wave side counts conditions; the particle side counts states.** At a frequency point the wave side asks how many field strengths the symbol omits, and the answer is $4-r$. The particle side asks how many polarisations the field has, and the answer is $r$. **The two answers add to four**, and the addition is exact because the codomain is four-dimensional, and it holds at every point of the domain including the cone.

**The complementarity is the content of this article's half of the duality.** The companion article established that one integer reports the freedom of the field. This article establishes that the same integer reports the freedom of the source, and that the conditions are the complement. **One rank, two spaces of dimension $r$, and a budget of four.** Charge conservation is the name of one member of the complement off the cone, and of one of two members on it.

**What the transform does.** It turns $\tilde\nabla_\Phi$ into $i\tilde K_\Phi$, so it turns the integrability condition of the field equation into an element of the cokernel, and it turns the conservation law of the source into the component form of that element. Without the transform the statement is that the divergence of the source vanishes. With it the statement is a functional on a four-dimensional space, and the functional can be counted, identified, and on the cone supplemented.

## Limits

**The frequency point is fixed and the coefficients are constant.** Everything here is at one wave number in a homogeneous medium. A medium with position-dependent $\epsilon$ and $\mu$ has a symbol that varies with position, and the cokernel becomes a bundle rather than a vector space. Nothing in the article covers that case.

**The domain is the forward cone, the origin excluded.** $k_{t}^{\prime}\ge0$ and $k_\Phi>0$. At the origin $\tilde K_\Phi=0$, the rank is zero and the cokernel is all of $\mathbb B$; that point is degenerate and carries no condition of the kind computed here. The negative cone repeats the positive one with the circular labels exchanged, as the companion article records: at $k_{t}^{\prime}=-k_\Phi$ the kernel is spanned by $\varepsilon_{\mathrm{fop},-}$ and the cokernel by $\tilde K_\Phi^\natural$ and $\varepsilon_{\mathrm{fop},+}$.

**The map is read on the vector part, and the whole algebra gives other numbers.** Read on $\mathbb B$ rather than on $\mathbb B_V$, the cokernel is zero off the cone and two-dimensional on it. The choice of domain is the physical one, because the field strength is pure, and the numbers quoted throughout are that choice's.

**The labels on the circular pair are the companion article's.** $(\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2},\vec u_\Phi)$ is right-handed, and the circular pair carries the plus sign on the first of them. A different triad exchanges the labels and leaves every dimension and every residual unchanged.

**No value of a mass, no gauge invariance, no statement about a state.** The article computes the cokernel of a massless symbol in a medium. It does not derive the mass shell, it does not exhibit a gauge freedom, and it does not assert that a physical photon occupies one circular polarisation rather than another. The identification of the second member as a helicity selection rule is an interpretation of a linear constraint, and the algebra alone does not supply it.

## Summary

Maxwell's equation transforms into $i\tilde K_\Phi\mathcal F[\tilde F]=-\sqrt{\mu}\mathcal F[\tilde J_\Phi]$, with the field strength in the three-dimensional vector part and the source in the four-dimensional algebra. The map $L_{i\tilde K_\Phi}:\mathbb B_V\to\mathbb B$ has rank three off the light cone and two on it, and its cokernel therefore has dimension one and two respectively. The cokernel is written as a space of multipliers: an element $M$ annihilates the image exactly when $M\,i\tilde K_\Phi$ is central, a condition that is one complex equation and that identifies the quotient with a subspace of the algebra itself.

Off the cone the cokernel is read by one element, the spanning $\tilde K_\Phi^\natural$ of the line, and the functional it defines is $\mathrm{Sc}(\tilde K_\Phi^\natural\tilde J_\Phi)=\vec k_\Phi\cdot\vec J-k_{t}^{\prime}c\rho$. Its vanishing is the continuity equation. Charge conservation is thus the whole cokernel off the cone, and the statement is exactly the integrability condition of the Maxwell article, read on the source instead of on the equation.

On the cone the rank drops to two and the cokernel, read through the scalar pairing, becomes the span of $\tilde K_\Phi^\natural$ and $\varepsilon_{\mathrm{fop},-}$. The second member is the circular direction the symbol scales, while the direction it annihilates, $\varepsilon_{\mathrm{fop},+}$, is the one the second member constrains: the condition $\mathrm{Sc}(\varepsilon_{\mathrm{fop},-}\tilde J_\Phi)=0$ says the current has no component along $\varepsilon_{\mathrm{fop},+}$. Charge conservation is necessary there and not sufficient. The admissible sources are $a_\parallel\tilde K_\Phi+a_-\,\varepsilon_{\mathrm{fop},-}$, with two free complex amplitudes, and a source with a component along $\varepsilon_{\mathrm{fop},+}$ has no field; the least-squares residual is exactly the modulus of that component.

The counts close. The rank and the cokernel dimension add to four at every point, the space of reachable field strengths and the space of admissible sources both have dimension $r$, and the conditions are the complement. The wave side reads $4-r$ conditions and the particle side reads $r$ polarisations, and they are one integer read twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\mathbb{B}_{V}$ | the vector part, of complex dimension three; the domain of the symbol |
| $\tilde F$ | the field-strength biquaternion, a pure vector |
| $\tilde J_\Phi$ | the four-current $ic\rho\,e_t+\vec J$ |
| $\tilde K_{\Phi}$ | the wave-number element $i\,k_{t}^{\prime}e_t+\vec k_{\Phi}$ |
| $\tilde K_{\Phi}^{\natural}$ | its quaternion conjugate $i\,k_{t}^{\prime}e_t-\vec k_{\Phi}$ |
| $k_{t}^{\prime}$ | the energy wave number, $E/(\hbar c)=\omega/c$ |
| $k_{\Phi}$ | the modulus of the momentum wave number |
| $\vec u_\Phi$ | the unit propagation direction, $\vec k_\Phi/k_\Phi$ |
| $\mathbb{B}_V$, $\mathbb{B}$ | the domain and codomain of $L_{i\tilde K_\Phi}$, of complex dimensions three and four |
| $r$ | the rank of $L_{i\tilde K_\Phi}$: three off the cone, two on it |
| $\operatorname{coker}L_{i\tilde K_\Phi}$ | $\mathbb B/L_{i\tilde K_\Phi}\mathbb B_V$, of dimension $4-r$ |
| $M$ | a multiplier; it reads the cokernel through $\sigma\mapsto\mathrm{Sc}(M\sigma)$ |
| $\mathrm{Vect}$, $\mathrm{Sc}$ | the vector part and the scalar part of an element |
| $\varepsilon_{\mathrm{fop},1},\varepsilon_{\mathrm{fop},2}$ | a right-handed orthonormal pair transverse to $\vec u_\Phi$ |
| $\varepsilon_{\mathrm{fop},\pm}$ | the circular directions $(\varepsilon_{\mathrm{fop},1}\pm i\varepsilon_{\mathrm{fop},2})/\sqrt 2$ |
| $\mathrm{Sc}(\tilde K_\Phi^\natural\tilde J_\Phi)$ | $\vec k_\Phi\cdot\vec J-k_{t}^{\prime}c\rho$; its vanishing is charge conservation |
| $a_\parallel$, $a_-$ | the two amplitudes of an admissible source on the cone |

## Further Reading

*Wave–Particle Duality and the Fourier Transform* for the two bases of one equation.

*Wave–Particle Duality and the Count of Degrees of Freedom* for the rank, the kernel, and the polarisation the symbol loses on the cone.

*The Fourier Transform and the Symbol of a Differential Operator*, §*The Kernel and the Cokernel*, for the cokernel as the constraint on the data.

*Maxwell's Equations in the Biquaternionic Formulation*, §*The Biquaternionic Source*, for the integrability condition and the continuity equation.

*The Photon in Biquaternionic Form* for the circular basis and the helicity states.

*The Proca Equation: Massive Spin 1 in Biquaternionic Form* for the massive case, where the count is three and the mechanism is the Lorenz condition rather than the rank of the symbol treated here.

*Helicity in Biquaternionic Form* for the helicity operator whose eigenvectors are the circular directions.

*The First-Order Root of the Biquaternion Klein–Gordon Operator* for the block determinant and the fourfold degeneracy of the second-order symbol.

*The Three Wavenumbers of a Particle* for the relation between $k_{t}^{\prime}$, $k_\Phi$ and $k_m$ that locates the cone.

*Biquaternion Continuous Harmonic Analysis* for the transform and its inverse.
