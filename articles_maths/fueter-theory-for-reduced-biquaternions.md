# __Fueter Theory for Reduced Biquaternions__

## Introduction

This article examines the Fueter programme for the reduced biquaternion algebra: the search for a first-order algebra-valued operator whose square is the Laplacian, the class of functions it defines, the harmonicity and the mean value property, the Fueter construction from holomorphic functions of one complex variable, the axial and slice approach, and the power series. The outcome is a genuine obstruction: because the algebra is **commutative**, the units $1,i,j,ij$ do not anticommute, the operator $D=\sum_\mu e_\mu\partial/\partial Q_\mu$ does not square to a scalar operator, and no algebra-valued first-order operator squares to the Laplacian on this algebra. What replaces the Fueter construction is the pair of the two complex Cauchy–Riemann operators of the two idempotent factors, studied in *Reduced Biquaternion Regular Functions* and *Reduced Biquaternion Integration*. The treatment is purely mathematical.

Throughout the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$, and $\breve Q=Q_{+}\Pi_++Q_{-}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$, so $(ij)^{2}=-1$; the four real coordinates are $q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown}$. The Euclidean Laplacian is $\Delta=\partial^2/\partial q_{\blacktriangle}^2+\partial^2/\partial q'^2_{\blacktriangle}+\partial^2/\partial q_{\blacktriangledown}^2+\partial^2/\partial q'^2_{\blacktriangledown}$.

## The Fueter Operator and Its Square

**Definition.** The **Fueter operator**, or **Cauchy–Riemann–Fueter operator**, of the algebra is
$$
D=\partial/\partial q_{\blacktriangle}+i\,\partial/\partial q'_{\blacktriangle}+j\,\partial/\partial q_{\blacktriangledown}+ij\,\partial/\partial q'_{\blacktriangledown} ,
$$
acting on the left, with its image acting by left multiplication.

**Theorem (the square is not scalar).** The square of the operator is
$$
D^{2}=\Box+2i\,\partial^2/\partial q_{\blacktriangle}\partial q'_{\blacktriangle}+2j\,\partial^2/\partial q_{\blacktriangle}\partial q_{\blacktriangledown}+2ij\,\partial^2/\partial q_{\blacktriangle}\partial q'_{\blacktriangledown}+2ij\,\partial^2/\partial q'_{\blacktriangle}\partial q_{\blacktriangledown}-2j\,\partial^2/\partial q'_{\blacktriangle}\partial q'_{\blacktriangledown}+2i\,\partial^2/\partial q_{\blacktriangledown}\partial q'_{\blacktriangledown} ,
$$
where $\Box=\partial^2/\partial q_{\blacktriangle}^2-\partial^2/\partial q'^2_{\blacktriangle}+\partial^2/\partial q_{\blacktriangledown}^2-\partial^2/\partial q'^2_{\blacktriangledown}$ is the second-order operator of signature $(2,2)$; the six cross terms do **not** vanish. Consequently $D^{2}$ is not a scalar operator and $D$ is **not** a Dirac operator.

*Proof.* Expanding $D^{2}=\sum_{\mu,\nu}e_{\mu}e_{\nu}\partial^2/\partial Q_\mu\partial Q_\nu$ over the four units, the diagonal terms give $\partial^2/\partial q_{\blacktriangle}^2+i^{2}\partial^2/\partial q'^2_{\blacktriangle}+j^{2}\partial^2/\partial q_{\blacktriangledown}^2+(ij)^{2}\partial^2/\partial q'^2_{\blacktriangledown}=\Box$; each off-diagonal pair contributes $e_{\mu} e_{\nu}+e_{\nu} e_{\mu}=2e_{\mu} e_{\nu}=2e_{\nu} e_{\mu}$, which is non-zero because the algebra is commutative and the units satisfy $e_{\mu} e_{\nu}\neq0$; explicitly $i\cdot j=ij$, $i\cdot ij=-j$, $j\cdot ij=i$, and the six products are the displayed ones.

**Corollary (the obstruction is commutativity).** The cancellation of the cross terms in the quaternion and biquaternion cases uses the anticommutation $e_{\mu} e_{\nu}+e_{\nu} e_{\mu}=0$ for $\mu\neq\nu$; in a commutative algebra the anticommutation fails identically, so no algebra-valued first-order operator of the form $\sum_{\mu}e_{\mu}\partial/\partial Q_\mu$ has a scalar square. The Fueter operator of the reduced biquaternion algebra therefore cannot be the square root of the Laplacian, and the classical Fueter theory does not transfer.

*Proof.* The cross-term coefficient is $e_{\mu}e_{\nu}+e_{\nu}e_{\mu}=2e_{\mu}e_{\nu}$ in a commutative algebra, which vanishes only if the product does, and the four units multiply among themselves without any vanishing product; the obstruction is exactly the failure of anticommutativity.

## The Reduced Dirac Operator

**Definition.** The **reduced Dirac operator** and its conjugate are the two-factor operators
$$
\mathcal{D}=\Pi_+\partial/\partial\bar Q_{+}+\Pi_-\partial/\partial\bar Q_{-},\qquad
\bar{\mathcal{D}}=\Pi_+\partial/\partial Q_{+}+\Pi_-\partial/\partial Q_{-},
$$
with the Wirtinger derivatives of the two idempotent coordinates.

**Theorem (the two-factor factorization).** The operator $\mathcal{D}$ acts coefficientwise, $\mathcal{D}=\Pi_+\partial/\partial\bar Q_{+}+\Pi_-\partial/\partial\bar Q_{-}$ on a function $g_{1}\Pi_++g_{2}\Pi_-$, and the scalar reading of its square is the Laplacian,
$$
\boxed{\;
8\,\mathrm{scal}\bigl(\mathcal{D}\bar{\mathcal{D}}\bigr)=\Delta,\qquad \Delta=8\bigl(\partial^2/\partial Q_{+}\partial\bar Q_{+}+\partial^2/\partial Q_{-}\partial\bar Q_{-}\bigr)
\;},
$$
where the scalar reading replaces the two idempotents by $1$ and adds the two components. In each idempotent coordinate the operator is the ordinary complex Cauchy–Riemann operator, so $\mathcal{D}$ is the square root of the Laplacian in each factor.

*Proof.* The operators act coefficientwise and commute; the product is $\mathcal{D}\bar{\mathcal{D}}=\Pi_+\partial^2/\partial Q_{+}\partial\bar Q_{+}+\Pi_-\partial^2/\partial Q_{-}\partial\bar Q_{-}$, whose two components add to the sum $\partial^2/\partial Q_{+}\partial\bar Q_{+}+\partial^2/\partial Q_{-}\partial\bar Q_{-}=\Delta/8$; in the first coordinate $\partial/\partial\bar Q_{+}$ is the complex Cauchy–Riemann operator, whose conjugate product is the two-dimensional Laplacian, and symmetrically in the second.

**Corollary (what replaces the Fueter operator).** The Dirac operator of the reduced biquaternion theory is the pair of the two complex Cauchy–Riemann operators, one per idempotent factor; it is not a single algebra-valued first-order operator, and the two-dimensional square-root property holds factor by factor. This is the honest replacement of the operator $D$ of the preceding section.

*Proof.* The pair acts coefficientwise and each member squares, in its own two real variables, to the Laplacian of that factor; the algebra being a product, the square root exists on each factor and not on the algebra as a single operator.

## Fueter-Regular Functions

**Definition.** A differentiable $f$ is **Fueter-regular** when $\mathcal{D}f=0$. Because the algebra is commutative, the left and the right conditions coincide, $\mathcal{D}f=f\mathcal{D}$.

**Theorem (the regularity class).** A $C^{1}$ function $f=g_{1}\Pi_++g_{2}\Pi_-$ is Fueter-regular if and only if
$$
\boxed{\;
\partial/\partial\bar Q_{+}\,g_{1}=0,\qquad\partial/\partial\bar Q_{-}\,g_{2}=0
\;},
$$
the pair of complex Cauchy–Riemann systems; the reduced-analytic class is $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ with $G_{1},G_{2}$ holomorphic in one complex variable. This is exactly the regular class of *Reduced Biquaternion Regular Functions*, and the two notions agree.

*Proof.* The operator $\mathcal{D}$ acts coefficientwise, so the equation is the pair of complex equations; the reduced-analytic class is characterised in the reference article by the difference-quotient condition, and its functions are precisely the $C^{1}$ solutions with the coordinate separation.

**Corollary (no one-sided obstruction).** In the biquaternion case the left-regular and the right-regular functions differ, the algebra being non-commutative; here they coincide and the regularity class is a two-sided module, commutative in the algebra of functions.

*Proof.* Commutativity makes the two first-order conditions identical and makes the product of two regular functions regular.

## Harmonicity and the Mean Value Property

**Theorem (reduced-analytic functions are harmonic).** Every reduced-analytic function $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ satisfies $\Delta f=0$ and is real-analytic; it satisfies the mean value property over the Euclidean balls and, being harmonic in the ordinary sense in four real variables, enjoys the maximum principle and Liouville's theorem for bounded functions. A general Fueter-regular function of the weaker class $\mathcal{D}f=0$ need not be harmonic: the function $f=\lvert Q_{-}\rvert^{2}\Pi_+$ is Fueter-regular, $\partial/\partial\bar Q_{+}\,\lvert Q_{-}\rvert^{2}=0$, but $\Delta f=8\Pi_+\neq0$, because $\lvert Q_{-}\rvert^{2}$ depends on $\bar Q_{-}$ in a way the single equation $\partial/\partial\bar Q_{+}\,g_{1}=0$ does not see.

*Proof.* For $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ one has $\Delta f=8\partial^2/\partial Q_{+}\partial\bar Q_{+}\,G_{1}\Pi_++8\partial^2/\partial Q_{-}\partial\bar Q_{-}\,G_{2}\Pi_-$, and each term vanishes because $\partial/\partial\bar Q_{+}\,G_{1}=0$ and $\partial/\partial\bar Q_{-}\,G_{2}=0$; harmonicity gives the mean value property, the maximum principle and Liouville's theorem in the definite four-dimensional space.

**The converse fails.** The first real coordinate $f=q_{\blacktriangle}$ is harmonic but not reduced-analytic, since $\partial/\partial\bar Q_{+}\,q_{\blacktriangle}=\tfrac14\neq0$, so the reduced-analytic class is a proper subclass of the harmonic functions.

**Corollary (the contrast with the indefinite case).** The failure of the elliptic tools in the split biquaternion case occurs on the indefinite subspaces, where the second-order operator is a wave operator; on the reduced biquaternion algebra the Laplacian is the ordinary Euclidean one, so the tools are available. The definite generator $i$ and the definite product $ij$ supply the elliptic part; the split generator $j$ alone would make the operator indefinite.

*Proof.* On the subspace annihilated by the definite directions only the operator reduces to a wave operator; on the whole algebra the second-order operator is the Euclidean Laplacian, and the classical elliptic theory applies.

## The Fueter Construction

**Theorem (the construction in the reduced case).** Let $G$ be a holomorphic function of one complex variable. Then the induced function
$$
\boxed{\;
F(\breve Q)=G(Q_{+})\,\Pi_++G(Q_{-})\,\Pi_-
\;}
$$
is Fueter-regular, and conversely every reduced-analytic function is induced from a pair of holomorphic functions. The construction is therefore the **identity** in each idempotent coordinate: the passage from the one-variable holomorphic function to the regular function of the algebra requires no power of the Laplacian, because the algebra is a product of two complex planes and the two-factor calculus is already holomorphic.

*Proof.* Each coordinate of $F$ is a holomorphic function of its own complex variable, hence annihilated by the corresponding Cauchy–Riemann operator, and the operator acts coefficientwise; the converse is the characterisation of the reduced-analytic class.

**Corollary (why the construction degenerates).** In the quaternion and biquaternion cases the Fueter construction must apply a power of the Laplacian, $\Delta^{(n-1)/2}$ in odd dimension $n$, because the slice variable encodes only one complex direction and the regularity conditions of the remaining directions are not automatic. In the reduced biquaternion case the two directions of each factor are exactly the two directions of one complex variable, so no surplus direction remains and the construction needs no correction.

*Proof.* The slice variable of the classical construction is one complex coordinate $q_{0}+Iq_{1}$ inside a space of dimension $n$, and the remaining $n-2$ directions must be supplied by the Laplacian power; here the two directions of the factor exhaust the two-dimensional complex plane, and there is no surplus.

## The Axial and Slice Approach

**Definition.** For a root of minus one $w\in\{\pm i,\pm ij\}$ the **slice** is the complex line
$$
S_{w}=\{\alpha+\beta w:\alpha,\beta\in\mathbb{R}\},
$$
a copy of the complex plane inside the algebra, and a function is **slice-regular** when its restriction to every slice is a holomorphic function of the complex variable $z=\alpha+i\beta$.

**Theorem (the slices and their regularity).** Each slice $S_{w}$ is a copy of $\mathbb{C}$, generated by $\mathbf{1}$ and $w$ with $w^{2}=-1$, and the two model slices are the complex line $S_{i}=\mathbb{R}\{1,i\}$ and the definite plane $S_{ij}=\mathbb{R}\{1,ij\}$; the slice $S_{j}$ generated by $j$ is **not** a copy of $\mathbb{C}$, since $j^{2}=+1$. On $S_{i}$ one has $Q_{\blacktriangledown}=0$ and $Q_{+}=Q_{-}=z$, so the restriction of a reduced-analytic function is holomorphic in $z=\alpha+i\beta$; on $S_{ij}$ one has $Q_{+}=z$ and $Q_{-}=\bar z$, so the restriction is holomorphic in its $\Pi_+$-component and antiholomorphic in its $\Pi_-$-component, harmonic but not holomorphic.

*Proof.* The subalgebra generated by $w$ with $w^{2}=-1$ is the complex plane, and $j$ generates the split complex plane, not a field, so no complex slice structure is available there. On $S_{i}$ the point is $\breve Q=\alpha+\beta i$, with $Q_{\blacktriangle}=\alpha+\beta i$ and $Q_{\blacktriangledown}=0$, hence $Q_{+}=Q_{-}=Q_{\blacktriangle}=z$ and each component $G_{1}(Q_{+}),G_{2}(Q_{-})$ is holomorphic in $z$. On $S_{ij}$ the point is $\breve Q=\alpha+\beta(ij)$, with $Q_{\blacktriangle}=\alpha$ real and $Q_{\blacktriangledown}=\beta i$ purely imaginary, hence $Q_{+}=\alpha+i\beta=z$ and $Q_{-}=\alpha-i\beta=\bar z$, so $G_{1}(Q_{+})=G_{1}(z)$ is holomorphic while $G_{2}(Q_{-})=G_{2}(\bar z)$ is antiholomorphic.

**Corollary (the slice variable and the two factors).** For $w=i$ the slice is the complex line on which $Q_{\blacktriangledown}=0$ and $Q_{+}=Q_{-}=Q_{\blacktriangle}$; for $w=ij$ it is the plane on which $Q_{\blacktriangle}$ is real and $Q_{\blacktriangledown}$ is purely imaginary, with $Q_{+}=z$ and $Q_{-}=\bar z$. The first carries the holomorphic restriction; on the second only the $\Pi_+$-component is holomorphic, so the axial picture of the Fueter class is available only on the complex line $\mathbb{R}\{1,i\}$.

*Proof.* The coordinates of $\breve Q=\alpha+\beta i$ are $Q_{\blacktriangle}=\alpha+\beta i$, $Q_{\blacktriangledown}=0$, so $Q_{+}=Q_{-}=Q_{\blacktriangle}=z$; those of $\breve Q=\alpha+\beta(ij)$ are $Q_{\blacktriangle}=\alpha$, $Q_{\blacktriangledown}=\beta i$, so $Q_{+}=\alpha+i\beta=z$ and $Q_{-}=\alpha-i\beta=\bar z$, and $G_{2}(\bar z)$ is antiholomorphic in $z$.

## Power Series Representations

**Theorem (the induced and the monogenic series).** A power series $\sum_{n\ge0}c_{n}\breve Q^{n}$ with complex coefficients converges on the set where both $\lvert Q_{+}\rvert$ and $\lvert Q_{-}\rvert$ lie within the radius, and its sum is Fueter-regular with $\breve Q^{n}=Q_{+}^{n}\Pi_++Q_{-}^{n}\Pi_-$; the induced series of a pair of holomorphic functions is the sum of the two coordinate series, and the monogenic Taylor expansion about a point recollects the regular class.

*Proof.* The series converges in each coordinate within the common radius and acts coefficientwise; the powers are read in the coordinates, and the resulting function is reduced-analytic, hence regular, by the characterisation of the class.

**Corollary (the two series classes agree).** The induced series and the reduced-analytic series are the same class, unlike the biquaternion case, where the slice-regular series and the induced monogenic series are distinct and the Fueter construction passes from the first to the second. Here the construction is the identity and the two classes coincide.

*Proof.* The induced series is $G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ with $G_{1},G_{2}$ given by their Taylor series, which is exactly the reduced-analytic class; there is no surplus direction, so no distinct slice class appears.

## The Reduced Biquaternionic Case

**The algebra.** The reduced biquaternion algebra is $\mathbb{C}\times\mathbb{C}$, commutative, with two generating directions $i$ and $j$, of which $i$ is definite and $j$ split; the two idempotent coordinates $Q_{+},Q_{-}$ are the two independent complex variables.

**What survives of the Fueter theory.** The mean value property, the harmonicity and the real-analyticity of the reduced-analytic functions survive; the Fueter construction survives as the identity in each coordinate; the slice and axial approach survives on the complex line $S_{i}=\mathbb{R}\{1,i\}$, on which the restriction is holomorphic, and degenerates on the definite slice $S_{ij}=\mathbb{R}\{1,ij\}$, on which the restriction is the holomorphic–antiholomorphic pair $G_{1}(z)\Pi_++G_{2}(\bar z)\Pi_-$ and is harmonic but not holomorphic.

**What fails.** The algebra-valued Dirac operator fails to exist, because the units do not anticommute; the single Cauchy kernel of the four-dimensional theory is replaced by the pair of one-variable kernels, the singular set being a union of two complex lines rather than a point or a hypersurface; and there is no distinct slice-regular class to be converted into the regular class.

## Relation to the Biquaternion and Split-Quaternion Theories

The biquaternion and quaternion theories rest on the anticommutation of the units, which makes $\tilde{\nabla}=\sum_\mu e_\mu\partial/\partial Q_\mu$ a square root of the Laplacian and produces the Fueter construction with the Laplacian power $\Delta^{(n-1)/2}$ in odd dimension; the split biquaternion theory keeps the quaternion units in each of its two halves and inherits the same structure half by half. The reduced biquaternion theory removes the anticommutation: the units commute, the single operator splits, and the Fueter theory reduces to the pair of the complex one-variable theories. The structural difference is exactly the passage from a Clifford algebra with anticommuting generators to the commutative algebra $\mathrm{Cl}_{1,0}\otimes\mathrm{Cl}_{0,1}$, whose generators $i$ and $j$ commute.

## Summary

The Fueter operator $D=\partial/\partial q_{\blacktriangle}+i\partial/\partial q'_{\blacktriangle}+j\partial/\partial q_{\blacktriangledown}+ij\partial/\partial q'_{\blacktriangledown}$ of the reduced biquaternion algebra does not square to a scalar operator: its square is the signature-$(2,2)$ operator $\Box$ plus six non-zero cross terms, because the four units commute and do not anticommute, and no algebra-valued first-order operator squares to the Laplacian on this algebra. What replaces it is the reduced Dirac operator $\mathcal{D}=\Pi_+\partial/\partial\bar Q_{+}+\Pi_-\partial/\partial\bar Q_{-}$, whose two idempotent components are the complex Cauchy–Riemann operators of the two factors and whose scalar reading of the square is the Laplacian, $8\,\mathrm{scal}(\mathcal{D}\bar{\mathcal{D}})=\Delta$. The Fueter-regular functions are the solutions $\mathcal{D}f=0$, the pair of complex Cauchy–Riemann conditions $\partial/\partial\bar Q_{+}\,g_{1}=0$, $\partial/\partial\bar Q_{-}\,g_{2}=0$; the reduced-analytic functions $f=G_{1}(Q_{+})\Pi_++G_{2}(Q_{-})\Pi_-$ are the narrower class in which neither component depends on the other coordinate, and every such function is harmonic, real-analytic and satisfies the mean value property, the maximum principle and Liouville's theorem, since the Laplacian here is the ordinary Euclidean one and the elliptic tools are available. The Fueter construction is the identity in each idempotent coordinate, with no Laplacian power, because the two directions of each factor already exhaust one complex variable and no surplus direction remains; the slice approach survives on the definite slice $S_{i}=\mathbb{R}\{1,i\}$, where the restriction is holomorphic, while on the definite slice $S_{ij}=\mathbb{R}\{1,ij\}$ the coordinates are $z$ and $\bar z$ and the restriction is harmonic but not holomorphic, and the slice $S_{j}$ is not a complex slice. The power series converge coordinatewise and the induced and the regular series coincide. Against the quaternion, biquaternion and split biquaternion theories, whose anticommuting units make the Fueter operator a square root of the Laplacian, the reduced biquaternion case has no single Dirac operator and its Fueter theory is the pair of the complex one-variable theories.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D=\partial/\partial q_{\blacktriangle}+i\partial/\partial q'_{\blacktriangle}+j\partial/\partial q_{\blacktriangledown}+ij\partial/\partial q'_{\blacktriangledown}$ | Fueter operator, square not scalar |
| $\Box=\partial^2/\partial q_{\blacktriangle}^2-\partial^2/\partial q'^2_{\blacktriangle}+\partial^2/\partial q_{\blacktriangledown}^2-\partial^2/\partial q'^2_{\blacktriangledown}$ | Signature-$(2,2)$ second-order operator |
| $\mathcal{D}=\Pi_+\partial/\partial\bar Q_{+}+\Pi_-\partial/\partial\bar Q_{-}$ | Reduced Dirac operator |
| $\bar{\mathcal{D}}=\Pi_+\partial/\partial Q_{+}+\Pi_-\partial/\partial Q_{-}$ | Conjugate operator |
| $8\,\mathrm{scal}(\mathcal{D}\bar{\mathcal{D}})=\Delta$ | The two-factor factorization |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | Idempotent coordinates |
| $S_{w}=\{\alpha+\beta w\}$ | Slice, a copy of $\mathbb{C}$ for $w^{2}=-1$ |
| $F(\breve Q)=G(Q_{+})\Pi_++G(Q_{-})\Pi_-$ | Induced regular function |

## Further Reading

- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* 7 (1934), for the construction of regular functions from holomorphic data.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for the monogenic functions and the square root of the Laplacian.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Fueter–Sce construction and the slice approach.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the anticommutation of the generators and the failure of the square root in the commutative case.
- M. Elena Luna-Elizarrarás, Michael Shapiro, Daniele C. Struppa and Adrian Vajiac, *Bicomplex Holomorphic Functions* (Birkhäuser, 2015), for the two-factor calculus that replaces the Fueter theory in the commutative algebra.
