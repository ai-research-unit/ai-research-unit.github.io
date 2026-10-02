
# __The Hermitian Index Theorem and the Signature Operator__

## Introduction

A Hermitian holomorphic vector bundle over a compact complex manifold carries a canonical connection and a first-order operator, the **Dolbeault operator** $\bar\partial_E$, whose index is the holomorphic Euler characteristic. The **Hermitian index theorem** computes this index as a characteristic number: $\chi(X,E)=\int_X\operatorname{ch}(E)\operatorname{td}(TX)$, the Chern character of the bundle paired with the Todd class of the manifold, which is the Riemann–Roch theorem of Hirzebruch. The theorem is the complex-member of the index family, and it interpolates continuously into the **signature operator**: the complexified exterior algebra splits by $(p,q)$-type, the Dolbeault operators of the bundles $\Omega^p$ assemble into a single operator whose index is the **$\chi_y$-genus**, and the specialisation $y=1$ of that genus is the $L$-class, so the index of the signature operator is recovered as the value $y=1$ of the holomorphic index.

The article develops the Hermitian bundle and its Chern character, the Dolbeault operator and its index, the Hermitian index theorem and its classical cases, the $\chi_y$-genus that interpolates between the Todd genus, the signature and the Euler characteristic, and the identification of the value $y=1$ with the signature operator's index. The signature operator is that of *The Signature Operator*; the Dolbeault cohomology and the Hodge decomposition of a Kähler manifold are those of *Hermitian Metrics and the Hodge Theory*; and the characteristic classes and the general index theorem are those of *Characteristic Classes* and *The Atiyah–Singer Index Theorem and K-Theory*.

The prerequisites are *Hermitian Vector Bundles and the Chern Connection* and *Chern Classes of a Hermitian Bundle* for the Hermitian connection and the Chern–Weil construction; *Characteristic Classes* for the Chern and Pontryagin classes, the Chern character and the Todd class; *The Atiyah–Singer Index Theorem and K-Theory* for the general index theorem and the symbol; *Hermitian Metrics and the Hodge Theory* and *The Hodge Laplacian* for the Dolbeault complex, the Kähler identity and the Hodge decomposition; and *The Signature Operator* and *Polarised Hodge Structures and the Hodge–Riemann Relations* for the signature, the $L$-genus and the Hodge index theorem. The Hermitian metric is a chosen form, and the whole construction is the geometry of that choice. No physics is invoked.

## Hermitian Bundles and the Chern Character

**Definition.** Let $X$ be a compact complex manifold of dimension $n$ and let $E\to X$ be a holomorphic vector bundle of rank $r$. A **Hermitian metric** on $E$ is a smooth family of Hermitian inner products on the fibres; a **Hermitian holomorphic bundle** is a holomorphic bundle with a Hermitian metric, and the metric determines the **Chern connection**, the unique connection of type $(1,0)$ that is compatible with the metric and with the holomorphic structure.

**Theorem (Chern–Weil).** The curvature $F$ of the Chern connection is a $(1,1)$-form with values in $\operatorname{End}(E)$, and the **Chern classes**

$$
c_k(E)=\frac{1}{(2\pi i)^k}\Bigl[\operatorname{tr}\Bigl(\bigwedge\nolimits^{k}F\Bigr)\Bigr],\qquad
c(E)=\det\Bigl(I+\frac{F}{2\pi i}\Bigr),
$$

are closed forms whose de Rham classes are independent of the Hermitian metric; they are the Chern classes of $E$, and the **Chern character**

$$
\operatorname{ch}(E)=\operatorname{tr}\exp\Bigl(\frac{F}{2\pi i}\Bigr)
=r+c_1(E)+\tfrac12\bigl(c_1^{2}-2c_2\bigr)(E)+\cdots
$$

is the corresponding additive characteristic class. The classes of the tangent bundle $TX$ are graded by the bidegree, the **Todd class** is

$$
\operatorname{td}(TX)=\prod_{j=1}^{n}\frac{x_j}{1-e^{-x_j}}
$$

in the Chern roots $x_j$ of $T^{1,0}X$, and the **Euler class** is $e(TX)=c_n(T^{1,0}X)$. The construction of the Chern connection, the Chern–Weil forms and the Todd class is that of *Hermitian Vector Bundles and the Chern Connection*, *Chern Classes of a Hermitian Bundle* and *Characteristic Classes*; the multiplicativity of the Chern character, $\operatorname{ch}(E\oplus F)=\operatorname{ch}(E)+\operatorname{ch}(F)$ and $\operatorname{ch}(E\otimes F)=\operatorname{ch}(E)\operatorname{ch}(F)$, is the property used below.

## The Dolbeault Operator

**Definition.** Let $E$ be a Hermitian holomorphic bundle. The **Dolbeault complex** is

$$
0\longrightarrow\Omega^{0,0}(X,E)\xrightarrow{\ \bar\partial_E\ }\Omega^{0,1}(X,E)\xrightarrow{\ \bar\partial_E\ }\cdots\xrightarrow{\ \bar\partial_E\ }\Omega^{0,n}(X,E)\longrightarrow0,
$$

where $\Omega^{0,q}(X,E)=\Gamma(\Lambda^{0,q}T^{*}X\otimes E)$ and $\bar\partial_E$ is the $(0,1)$-part of the Chern connection; the **Dolbeault operator** of $E$ is the sum

$$
\bar\partial_E+\bar\partial_E^{*}:\Omega^{0,\bullet}(X,E)\longrightarrow\Omega^{0,\bullet}(X,E),
$$

a formally self-adjoint elliptic operator whose square is the Dolbeault Laplacian.

**Theorem (Dolbeault).** The cohomology of the complex is the sheaf cohomology of the holomorphic bundle,

$$
H^{q}\bigl(\Omega^{0,\bullet}(X,E)\bigr)\cong H^{q}(X,E),
$$

and the index of the Dolbeault operator is the **holomorphic Euler characteristic**

$$
\operatorname{ind}(\bar\partial_E+\bar\partial_E^{*})=\sum_{q=0}^{n}(-1)^{q}\dim H^{q}(X,E)=\chi(X,E) .
$$

**Proof.** The Dolbeault theorem is the $(0,q)$-form version of the de Rham theorem, and the two operators $\bar\partial_E$ and $\bar\partial_E^{*}$ are formal adjoints with respect to the Hermitian structures, so the harmonic representatives of the cohomology are the kernel of the operator and the index is the alternating sum of the cohomology dimensions. The elliptic regularity that upgrades the formal argument to a theorem is that of Part III; the statement is the Dolbeault theorem and the Hodge decomposition for the $\bar\partial$-operator, of *Hermitian Metrics and the Hodge Theory*. $\square$

## The Hermitian Index Theorem

**Theorem (Hirzebruch–Riemann–Roch).** Let $X$ be a compact complex manifold and let $E$ be a Hermitian holomorphic bundle of rank $r$. Then

$$
\chi(X,E)=\int_{X}\operatorname{ch}(E)\,\operatorname{td}(TX),
$$

the Chern character of $E$ paired with the Todd class of the tangent bundle; in the Chern roots $x_j$ of $T^{1,0}X$ this is

$$
\chi(X,E)=\int_{X}\Bigl(\sum_{k}\operatorname{ch}_k(E)\Bigr)\prod_{j=1}^{n}\frac{x_j}{1-e^{-x_j}} .
$$

**Proof sketch.** The symbol of the Dolbeault operator is the $(0,q)$-part of the Clifford multiplication by $\xi$; its class in $K$-theory is the difference $[\Lambda^{0,\bullet}T^{*}X]\otimes[E]$, whose Chern character is $\operatorname{ch}(E)\operatorname{td}(TX)$ by the splitting principle and the multiplicativity of $\operatorname{ch}$; the Atiyah–Singer theorem then computes the index as the integral of the Chern character against the Todd class. The general theorem is in *The Atiyah–Singer Index Theorem and K-Theory*, and the Chern–Weil forms are those of *Chern Classes of a Hermitian Bundle*. $\square$

**Corollary (the classical cases).** For a compact Riemann surface $X$ of genus $g$ and a line bundle $L$ the theorem gives

$$
\chi(X,L)=\deg L+1-g,
$$

the Riemann–Roch theorem for curves, since $\operatorname{td}(TX)=1+(1-g)x$ and $\operatorname{ch}(L)=1+\deg L\cdot x$. For $E=\mathcal{O}_X$ the theorem gives $\chi(X,\mathcal{O}_X)=\int_X\operatorname{td}(TX)$, the Todd genus, and for a projective space $\chi(\mathbb{CP}^{n},\mathcal{O})=1$.

**Corollary (Serre duality).** The theorem applied to $E$ and to $E^{*}\otimes K_X$ gives

$$
\chi(X,E)=(-1)^{n}\chi(X,E^{*}\otimes K_X),
$$

the Euler-characteristic form of Serre duality, with $K_X=\Lambda^{n}T^{1,0*}X$ the canonical bundle; the individual dimensions are paired by $H^{q}(X,E)^{\vee}\cong H^{n-q}(X,E^{*}\otimes K_X)$.

## The $\chi_y$-Genus and the Signature

The Dolbeault indices of the bundles $\Omega^{p}=\Lambda^{p}T^{1,0*}X$ assemble into a single genus, and its specialisations include the signature.

**Definition.** The **$\chi_y$-genus** of a compact complex manifold $X$ is

$$
\chi_y(X)=\sum_{p=0}^{n}\chi(X,\Omega^{p})\,y^{p}=\sum_{p,q}(-1)^{q}h^{p,q}(X)\,y^{p},
$$

the generating function of the Dolbeault Euler characteristics, a polynomial in $y$ whose coefficients are the $\chi(X,\Omega^p)$. Its values at the ends of the interval are

$$
\chi_0(X)=\chi(X,\mathcal{O}_X)=\text{the Todd genus},\qquad
\chi_{-1}(X)=\chi(X)=\text{the Euler characteristic},
$$

and its value at $y=1$ is the signature.

**Theorem (Hirzebruch).** The $\chi_y$-genus is the characteristic number

$$
\chi_y(X)=\int_{X}\prod_{j=1}^{n}\frac{x_j\bigl(1+y\,e^{-x_j(1+y)}\bigr)}{1-e^{-x_j(1+y)}} ,
$$

and its value at $y=1$ is the $L$-genus,

$$
\chi_1(X)=\int_{X}\prod_{j=1}^{n}x_j\coth x_j=\int_{X}L(TX)=\sigma(X),
$$

the signature of $X$; its value at $y=0$ is the Todd genus $\int\prod\frac{x_j}{1-e^{-x_j}}$ and its value at $y=-1$ is the Euler characteristic $\int\prod x_j$.

**Proof sketch.** The genus $\sum_p\chi(\Omega^p)y^p$ is multiplicative for products and additive for the twisted Dolbeault complexes, so it is a genus with a power series determined by its values on the projective spaces; evaluating the resulting product at $y=1$ gives $\frac{x(1+e^{-2x})}{1-e^{-2x}}=x\coth x$, whose product is the $L$-class of *The Signature Operator*, and at $y=0$ the Todd factor; at $y=-1$ the limit is the Euler factor $\prod x_j$. Since the $\chi_y$-genus is independent of the description, the value $y=1$ is the signature by the Hodge index theorem, $\sigma=\sum_{p,q}(-1)^{p}h^{p,q}=\sum_p\chi(\Omega^p)$ of *Polarised Hodge Structures and the Hodge–Riemann Relations*. $\square$

**Corollary (the signature operator and the Chern character).** The complexified exterior algebra splits as $\Lambda^{k}T^{*}_{\mathbb{C}}X=\bigoplus_{p+q=k}\Lambda^{p,q}T^{*}X$, and the signature operator of the underlying real manifold, restricted to this splitting, is the operator whose index is the $y=1$ value of the $\chi_y$-genus; equivalently, the index of the signature operator is

$$
\sigma(X)=\int_{X}\operatorname{ch}\bigl(\textstyle\bigoplus_{p}\Lambda^{p}T^{1,0*}X\bigr)\Bigr|_{y=1}\ ,
$$

the Chern character of the total Dolbeault bundle of the complexification evaluated at $y=1$. This is the sense in which the **Hermitian index theorem contains the signature theorem**: the complex structure organizes the real signature operator into a holomorphic family of Dolbeault operators, and the Chern character of the family, read at the right value of $y$, is the $L$-class. The signature operator itself, its chirality and its index are those of *The Signature Operator*.

## Examples

**Example (the projective space).** For $\mathbb{CP}^{n}$ the Hodge numbers are $h^{p,p}=1$ and the rest zero, so
$$
\chi_y(\mathbb{CP}^{n})=\sum_{p=0}^{n}(-1)^{p}y^{p}
=\frac{1-(-y)^{n+1}}{1+y},
$$
and $\chi_1=1$ for $n$ even and $0$ for $n$ odd, while $\chi_{-1}=\chi(\mathbb{CP}^{n})=n+1$; the signature of a complex projective space of even complex dimension is $1$, in agreement with *The Signature Operator*. The Todd genus is $\chi_0=1$.

**Example (a curve).** For a compact Riemann surface of genus $g$ the Hodge numbers are $h^{0,0}=h^{1,1}=1$ and $h^{0,1}=h^{1,0}=g$, so
$$
\chi_y=(1-g)+(g-1)y ,
$$
with $\chi_1=0$ — the signature of a surface is zero — and $\chi_{-1}=2-2g=\chi$. The Riemann–Roch theorem $\chi(X,L)=\deg L+1-g$ is the twisted form.

**Example (a $K3$ surface).** For a $K3$ surface $h^{0,0}=h^{2,2}=1$, $h^{2,0}=h^{0,2}=1$ and $h^{1,1}=20$, so
$$
\chi_y=2-20y+2y^{2},\qquad \chi_1=2-20+2=-16=\sigma(K3),
$$
and $\chi_{-1}=2+20+2=24=\chi(K3)$, the Euler characteristic; the two values are the signature and the Euler characteristic computed in *The Signature Operator* and *The Hodge Laplacian*.

**Example (the Riemann–Roch theorem for surfaces).** For a compact complex surface and a line bundle $L$ the Hermitian index theorem gives
$$
\chi(X,L)=\frac{L\cdot(L-K_X)}{2}+\chi(X,\mathcal{O}_X),
$$
the Riemann–Roch theorem for surfaces, with $\chi(X,\mathcal{O}_X)=(c_1^{2}+c_2)/12$ evaluated on the fundamental class; the Noether formula expresses $\chi(X,\mathcal{O}_X)$ through the Chern numbers, and the formula is the two-dimensional case of the Hermitian index theorem against the Riemann–Roch theorem for curves.

## Summary

A **Hermitian holomorphic bundle** carries the Chern connection, whose Chern classes and **Chern character** are the Chern–Weil forms $\operatorname{ch}(E)=\operatorname{tr}\exp(F/2\pi i)$, and a compact complex manifold carries the **Todd class** $\operatorname{td}(TX)=\prod x_j/(1-e^{-x_j})$. The **Dolbeault operator** $\bar\partial_E+\bar\partial_E^{*}$ of a bundle is elliptic and self-adjoint with index the holomorphic Euler characteristic $\chi(X,E)=\sum(-1)^{q}\dim H^{q}(X,E)$, and the **Hermitian index theorem** of Hirzebruch–Riemann–Roch computes it,
$$
\chi(X,E)=\int_X\operatorname{ch}(E)\operatorname{td}(TX),
$$
with the classical consequences $\chi(X,L)=\deg L+1-g$ for a curve and the surface formula $\chi(X,L)=\tfrac12 L\cdot(L-K_X)+\chi(X,\mathcal{O}_X)$. The Dolbeault indices of the bundles $\Omega^p$ assemble into the **$\chi_y$-genus** $\chi_y=\sum_p\chi(\Omega^p)y^p$, whose characteristic-number form has values $\chi_0=$ Todd genus, $\chi_1=\int L=\sigma$, the **signature**, and $\chi_{-1}=\chi$, the Euler characteristic. The signature operator of the underlying real manifold is the operator whose index is the value $y=1$, so the Hermitian index theorem contains the signature theorem: the complex structure organizes the real operator into a holomorphic family, and the Chern character of the family at $y=1$ is the $L$-class. The examples $\mathbb{CP}^{n}$, the curves and the $K3$ surface check the two ends of the interpolation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E\to X$ | Hermitian holomorphic bundle of rank $r$ over a compact complex $n$-manifold |
| $F$, $c_k(E)$, $\operatorname{ch}(E)$ | Curvature of the Chern connection, Chern classes, Chern character |
| $\operatorname{td}(TX)=\prod x_j/(1-e^{-x_j})$ | Todd class; $x_j$ the Chern roots of $T^{1,0}X$ |
| $K_X=\Lambda^{n}T^{1,0*}X$ | Canonical bundle |
| $\bar\partial_E$, $\bar\partial_E^{*}$ | Dolbeault operator and its adjoint |
| $\chi(X,E)=\sum(-1)^q\dim H^q(X,E)$ | Holomorphic Euler characteristic |
| $\chi(X,E)=\int\operatorname{ch}(E)\operatorname{td}(TX)$ | Hirzebruch–Riemann–Roch |
| $\chi_y=\sum_p\chi(\Omega^p)y^p$ | Hirzebruch $\chi_y$-genus |
| $\chi_0,\chi_1,\chi_{-1}$ | Todd genus, signature, Euler characteristic |
| $\chi_1=\int\prod x_j\coth x_j=\int L=\sigma$ | Signature as the value $y=1$ |

## Further Reading

- Friedrich Hirzebruch, *Topological Methods in Algebraic Geometry*, Classics in Mathematics (Springer, 1995), for the Riemann–Roch theorem, the $\chi_y$-genus and the signature theorem.
- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Dolbeault theorem, the Chern classes and the Hodge numbers.
- Shiing-Shen Chern, *Complex Manifolds without Potential Theory* (Springer, 2nd ed. 1979), for the Chern connection, the Chern–Weil theory and the characteristic classes.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I, III," *Annals of Mathematics* **87** (1968), 484–530 and 546–604, for the index theorem and the symbol of the Dolbeault operator.
- Raymond O. Wells, *Differential Analysis on Complex Manifolds*, Graduate Texts in Mathematics 65 (Springer, 3rd ed. 2008), for the Dolbeault complex and the Hodge theory of complex manifolds.
- Kunihiko Kodaira, *Complex Manifolds and Deformation of Complex Structures* (Springer, 1986), for the holomorphic Euler characteristic and the deformation theory.
